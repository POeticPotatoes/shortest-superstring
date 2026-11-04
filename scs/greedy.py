"""Maximum-overlap greedy for SCS, with configurable tie-breaking.

The textbook description (slide 4) repeatedly merges the ordered pair of
current strings with the largest overlap.  For a substring-free input this
is equivalent to building Hamiltonian paths in the overlap graph: merging
fragment ``X`` (ending with input ``u``) and fragment ``Y`` (starting with
input ``v``) saves exactly ``ov(u, v)`` characters (Tarhio & Ukkonen 1988).
So greedy repeatedly selects the heaviest edge ``(u, v)`` such that

* ``u`` has no successor yet (it ends a fragment),
* ``v`` has no predecessor yet (it starts a fragment),
* ``v`` is not the first string of ``u``'s fragment (no cycle).

:func:`greedy` implements this edge formulation.  :func:`greedy_naive`
implements the literal "merge strings and recompute overlaps" description and
is kept as a slow reference to cross-check the fast one.  :func:`greedy_outcomes`
explores *every* tie choice on small inputs to give the best and worst
greedy executions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

from .core import overlap, overlap_graph, preprocess as _preprocess, superstring_from_order, total_length
from .tiebreak import Edge, TieBreaker, make_tiebreaker

# At overlap 0 every pair of fragments is a candidate.  Above this many
# candidate pairs, static rules concatenate the remaining fragments in index
# order instead of enumerating every pair.  The length is unaffected, since
# all remaining merges save 0 characters.
ZERO_LEVEL_PAIR_LIMIT = 2_000_000


class GreedyState:
    """The forest of fragments (paths in the overlap graph) during a greedy run.

    Dynamic tie-breakers receive this object.  Useful members are
    ``strings``, ``ov(u, v)``, ``fragment(x)``, ``fragment_length(x)``,
    ``heads()`` and ``merges``.
    """

    def __init__(self, strings: Sequence[str], graph: Sequence[dict[int, int]]):
        n = len(strings)
        self.strings = strings
        self.graph = graph
        self.succ: list[int] = [-1] * n
        self.pred: list[int] = [-1] * n
        # Valid only for tails / heads respectively.
        self.head_of_tail: list[int] = list(range(n))
        self.tail_of_head: list[int] = list(range(n))
        self.frag_len: list[int] = [len(s) for s in strings]  # valid for heads
        self.n_fragments = n
        self.merges: list[tuple[int, int, int]] = []
        self.saved = 0

    def ov(self, u: int, v: int) -> int:
        return self.graph[u].get(v, 0)

    def valid(self, u: int, v: int) -> bool:
        return self.succ[u] < 0 and self.pred[v] < 0 and self.head_of_tail[u] != v

    def add(self, u: int, v: int, w: int) -> None:
        h, t = self.head_of_tail[u], self.tail_of_head[v]
        self.succ[u] = v
        self.pred[v] = u
        self.tail_of_head[h] = t
        self.head_of_tail[t] = h
        self.frag_len[h] += self.frag_len[v] - w
        self.n_fragments -= 1
        self.merges.append((u, v, w))
        self.saved += w

    def head_of(self, x: int) -> int:
        if self.succ[x] < 0:
            return self.head_of_tail[x]
        while self.pred[x] >= 0:
            x = self.pred[x]
        return x

    def heads(self) -> list[int]:
        return [x for x in range(len(self.strings)) if self.pred[x] < 0]

    def path(self, head: int) -> list[int]:
        out = [head]
        while self.succ[out[-1]] >= 0:
            out.append(self.succ[out[-1]])
        return out

    def fragment_length(self, x: int) -> int:
        """Length of the current fragment containing input ``x``."""
        return self.frag_len[self.head_of(x)]

    def fragment(self, x: int) -> str:
        """The current fragment (merged string) containing input ``x``."""
        return superstring_from_order(self.strings, self.path(self.head_of(x)), self.graph)


@dataclass
class GreedyResult:
    superstring: str
    length: int
    strings: list[str]               # reduced (preprocessed) input
    order: list[int]                 # order of reduced inputs in the output
    merges: list[tuple[int, int, int]]  # (u, v, overlap) in the order chosen
    tie_rule: str
    trace: list[dict] | None = None  # per-merge candidate info (trace=True)
    zero_level_shortcut: bool = False

    @property
    def total_input_length(self) -> int:
        return total_length(self.strings)

    @property
    def compression(self) -> int:
        return self.total_input_length - self.length

    @property
    def tie_steps(self) -> int | None:
        """Number of merges that had more than one maximum-overlap candidate (needs ``trace=True``)."""
        if self.trace is None:
            return None
        return sum(1 for t in self.trace if t["candidates"] > 1)


def _levels(graph: Sequence[dict[int, int]]) -> dict[int, list[Edge]]:
    levels: dict[int, list[Edge]] = {}
    for u, row in enumerate(graph):
        for v, w in row.items():
            levels.setdefault(w, []).append((u, v))
    return levels


def greedy(strings: Sequence[str], tie_break: "str | TieBreaker | None" = "first", *,
           seed: int | None = None, preprocess: bool = True, trace: bool = False,
           graph: Sequence[dict[int, int]] | None = None) -> GreedyResult:
    """Run maximum-overlap greedy.

    Parameters
    ----------
    strings:
        Input strings.  Preprocessing removes duplicates and contained
        strings unless ``preprocess=False``, in which case the input must
        already be substring-free.
    tie_break:
        Rule for choosing among maximum-overlap candidates.  See
        :func:`scs.tiebreak.make_tiebreaker`.  Examples: ``"first"``,
        ``"last"``, ``"lex"``, ``"random:7"``, a :class:`~scs.tiebreak.Priority`
        instance, or a function ``f(candidates, state) -> (u, v)``.
    seed:
        Seed for ``tie_break="random"``.
    trace:
        Record, for every merge, the overlap and the number of tied
        candidates.  This evaluates candidates step by step, which is slower.
    graph:
        Precomputed ``overlap_graph`` of the (already preprocessed) input, to
        avoid recomputing it across many runs.  Requires ``preprocess=False``.
    """
    if graph is not None and preprocess:
        raise ValueError("pass graph= together with preprocess=False and the reduced strings")
    reduced = _preprocess(strings) if preprocess else list(strings)
    tb = make_tiebreaker(tie_break, seed)
    tb.bind(reduced)
    graph = overlap_graph(reduced) if graph is None else graph
    state = GreedyState(reduced, graph)
    log: list[dict] | None = [] if trace else None
    stepwise = tb.dynamic or trace

    def run_level(edges: list[Edge], w: int) -> None:
        # Edges that are already invalid stay invalid, so drop them before sorting.
        cands = [e for e in edges if state.valid(*e)]
        if not stepwise:
            cands.sort(key=lambda e: tb.key(*e))
            for u, v in cands:
                if state.valid(u, v):
                    state.add(u, v, w)
            return
        while cands:
            u, v = tb.choose(cands, state)
            if (u, v) not in cands:
                raise ValueError(f"tie-breaker {tb!r} returned non-candidate edge {(u, v)}")
            if log is not None:
                log.append({"u": u, "v": v, "overlap": w, "candidates": len(cands)})
            state.add(u, v, w)
            cands = [e for e in cands if state.valid(*e)]

    for w, edges in sorted(_levels(graph).items(), reverse=True):
        if state.n_fragments == 1:
            break
        run_level(edges, w)

    shortcut = False
    if state.n_fragments > 1:
        # Every remaining valid edge has overlap 0 (it would have been taken earlier otherwise).
        if stepwise:
            while state.n_fragments > 1:
                heads = state.heads()
                cands = [(state.tail_of_head[a], b) for a in heads for b in heads if a != b]
                run_level(cands, 0)
        else:
            heads = state.heads()
            m = len(heads)
            if m * (m - 1) <= ZERO_LEVEL_PAIR_LIMIT:
                run_level([(state.tail_of_head[a], b) for a in heads for b in heads if a != b], 0)
            else:
                shortcut = True
                for a, b in zip(heads, heads[1:]):
                    state.add(state.tail_of_head[a], b, 0)

    order = state.path(state.heads()[0]) if reduced else []
    sup = superstring_from_order(reduced, order, graph)
    assert len(sup) == total_length(reduced) - state.saved
    return GreedyResult(sup, len(sup), reduced, order, state.merges, getattr(tb, "name", "custom"), log, shortcut)


def greedy_naive(strings: Sequence[str], tie_break: "str | TieBreaker | None" = "first", *,
                 seed: int | None = None, preprocess: bool = True) -> GreedyResult:
    """Literal greedy: merge actual strings and recompute all overlaps every step.

    ``O(n^3 * l)`` reference implementation.  Supports static tie-break rules
    only.  Candidates are identified by the edge ``(last input of X, first
    input of Y)``, so for the same rule it makes the same choices as
    :func:`greedy` whenever the two formulations agree.
    """
    reduced = _preprocess(strings) if preprocess else list(strings)
    tb = make_tiebreaker(tie_break, seed)
    if tb.dynamic:
        raise ValueError("greedy_naive supports static tie-break rules only")
    tb.bind(reduced)
    frags = [{"text": s, "head": i, "tail": i, "order": [i]} for i, s in enumerate(reduced)]
    merges = []
    while len(frags) > 1:
        best, cands = -1, []
        for a, X in enumerate(frags):
            for b, Y in enumerate(frags):
                if a == b:
                    continue
                k = overlap(X["text"], Y["text"])
                if k > best:
                    best, cands = k, [(a, b)]
                elif k == best:
                    cands.append((a, b))
        a, b = min(cands, key=lambda ab: tb.key(frags[ab[0]]["tail"], frags[ab[1]]["head"]))
        X, Y = frags[a], frags[b]
        merges.append((X["tail"], Y["head"], best))
        merged = {"text": X["text"] + Y["text"][best:], "head": X["head"], "tail": Y["tail"],
                  "order": X["order"] + Y["order"]}
        frags = [f for i, f in enumerate(frags) if i not in (a, b)] + [merged]
    sup = frags[0]["text"] if frags else ""
    order = frags[0]["order"] if frags else []
    return GreedyResult(sup, len(sup), reduced, order, merges, getattr(tb, "name", "custom"))


class ExplorationBudgetExceeded(RuntimeError):
    pass


@dataclass
class TieExploration:
    """Every output length reachable by some valid greedy execution."""

    lengths: list[int]
    min_length: int
    max_length: int
    min_merges: list[tuple[int, int, int]]
    max_merges: list[tuple[int, int, int]]
    strings: list[str]
    states: int
    min_superstring: str = ""
    max_superstring: str = ""
    complete: bool = True
    extra: dict = field(default_factory=dict)

    @property
    def tie_sensitive(self) -> bool:
        return self.min_length != self.max_length


def greedy_outcomes(strings: Sequence[str], *, preprocess: bool = True,
                    max_states: int = 200_000) -> TieExploration:
    """Explore all tie-breaking choices of greedy (exponential; small inputs only).

    The search memoises on the set of chosen edges and stops branching once
    the maximum overlap is 0, because the remaining merges no longer change
    the length.  Raises :class:`ExplorationBudgetExceeded` after
    ``max_states`` distinct states.
    """
    reduced = _preprocess(strings) if preprocess else list(strings)
    graph = overlap_graph(reduced)
    levels = sorted(_levels(graph).items(), reverse=True)
    L = total_length(reduced)
    # memo[succ-tuple] = (set of achievable remaining savings, argmin edge, argmax edge)
    memo: dict[tuple[int, ...], tuple[frozenset[int], tuple | None, tuple | None]] = {}

    def candidates(st: GreedyState) -> tuple[int, list[Edge]]:
        for w, edges in levels:
            c = [e for e in edges if st.valid(*e)]
            if c:
                return w, c
        return 0, []

    def clone(st: GreedyState) -> GreedyState:
        c = GreedyState.__new__(GreedyState)
        c.strings, c.graph = st.strings, st.graph
        c.succ, c.pred = st.succ[:], st.pred[:]
        c.head_of_tail, c.tail_of_head = st.head_of_tail[:], st.tail_of_head[:]
        c.frag_len, c.n_fragments, c.merges, c.saved = st.frag_len[:], st.n_fragments, [], st.saved
        return c

    def solve(st: GreedyState):
        key = tuple(st.succ)
        hit = memo.get(key)
        if hit is not None:
            return hit
        if len(memo) >= max_states:
            raise ExplorationBudgetExceeded(f"more than {max_states} greedy states")
        w, cands = candidates(st)
        if not cands:
            res = (frozenset([0]), None, None)
        else:
            totals: set[int] = set()
            lo = hi = None
            for (u, v) in cands:
                nxt = clone(st)
                nxt.add(u, v, w)
                sub, _, _ = solve(nxt)
                totals.update(w + s for s in sub)
                smin, smax = w + min(sub), w + max(sub)
                if lo is None or smax > lo[0]:
                    lo = (smax, (u, v, w))      # most saving -> shortest output
                if hi is None or smin < hi[0]:
                    hi = (smin, (u, v, w))      # least saving -> longest output
            res = (frozenset(totals), lo[1], hi[1])
        memo[key] = res
        return res

    root = GreedyState(reduced, graph)
    savings, _, _ = solve(root)

    def follow(pick: int) -> tuple[list[tuple[int, int, int]], str]:
        st = GreedyState(reduced, graph)
        while True:
            entry = memo.get(tuple(st.succ))
            if entry is None or entry[pick] is None:
                break
            st.add(*entry[pick])
        merges = list(st.merges)
        # Join leftover fragments (overlap 0) in index order.
        heads = st.heads()
        for a, b in zip(heads, heads[1:]):
            st.add(st.tail_of_head[a], b, 0)
        order = st.path(st.heads()[0]) if reduced else []
        return merges, superstring_from_order(reduced, order, graph)

    min_merges, min_sup = follow(1)
    max_merges, max_sup = follow(2)
    lengths = sorted(L - s for s in savings)
    return TieExploration(lengths, lengths[0], lengths[-1], min_merges, max_merges, reduced,
                          len(memo), min_sup, max_sup)
