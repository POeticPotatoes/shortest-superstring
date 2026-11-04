"""Tie-breaking rules for maximum-overlap greedy.

Greedy is implemented on the overlap graph (see :mod:`scs.greedy`): every
merge of two current fragments ``X`` and ``Y`` corresponds to the edge
``(u, v)`` where ``u`` is the last input string of ``X`` and ``v`` is the first
input string of ``Y``.  A tie-breaker therefore chooses among *edges*
``(u, v)`` of the reduced input, where ``u`` and ``v`` are indices into
:attr:`GreedyState.strings`.

Two kinds of rules exist:

* **Static** rules define ``key(u, v)``; among the tied candidates the edge
  with the smallest key is chosen.  Because candidates only ever become
  invalid, greedy can sort each overlap level once and scan it, which makes
  static rules fast (``O(E log E)``).
* **Dynamic** rules define ``choose(candidates, state)`` and see the full
  greedy state (current fragments etc.).  They are re-evaluated at every
  step, which is slower but arbitrarily flexible.

Use :func:`make_tiebreaker` to build a rule from a short spec string such as
``"first"``, ``"lex"`` or ``"random:42"``.
"""

from __future__ import annotations

import random
from typing import TYPE_CHECKING, Callable, Iterable, Sequence

if TYPE_CHECKING:
    from .greedy import GreedyState

Edge = tuple[int, int]


class TieBreaker:
    """Base class.  Subclasses override :meth:`key` (static) or :meth:`choose` (dynamic)."""

    name = "base"
    dynamic = False

    def bind(self, strings: Sequence[str]) -> None:
        """Called once per greedy run with the reduced input strings."""
        self.strings = strings

    def key(self, u: int, v: int):
        raise NotImplementedError

    def choose(self, candidates: list[Edge], state: "GreedyState") -> Edge:
        return min(candidates, key=lambda e: self.key(*e))

    def __repr__(self) -> str:
        return f"<TieBreaker {self.name}>"


class FirstIndex(TieBreaker):
    """Smallest ``(u, v)`` in input order (the 'scan the matrix row by row' rule)."""

    name = "first"

    def key(self, u, v):
        return (u, v)


class LastIndex(TieBreaker):
    """Largest ``(u, v)`` in input order."""

    name = "last"

    def key(self, u, v):
        return (-u, -v)


class Lexicographic(TieBreaker):
    """Lexicographically smallest ``(strings[u], strings[v])``.

    Independent of the input order, so it is invariant under shuffling.
    """

    name = "lex"

    def key(self, u, v):
        return (self.strings[u], self.strings[v])


class ReverseLexicographic(TieBreaker):
    """Lexicographically largest pair; usually explores a different execution than ``lex``."""

    name = "revlex"

    def bind(self, strings):
        super().bind(strings)
        order = sorted(range(len(strings)), key=lambda i: strings[i], reverse=True)
        self._rank = {i: r for r, i in enumerate(order)}

    def key(self, u, v):
        return (self._rank[u], self._rank[v])


_MASK64 = (1 << 64) - 1


def _splitmix64(x: int) -> int:
    x = (x + 0x9E3779B97F4A7C15) & _MASK64
    x = ((x ^ (x >> 30)) * 0xBF58476D1CE4E5B9) & _MASK64
    x = ((x ^ (x >> 27)) * 0x94D049BB133111EB) & _MASK64
    return x ^ (x >> 31)


class RandomTie(TieBreaker):
    """Uniformly random choice among the tied candidates, reproducible from ``seed``.

    Each edge gets a pseudo-random key ``splitmix64(seed, u, v)``.  The key does
    not depend on call order or Python version, so the fast, traced and naive
    greedy implementations make identical choices for the same seed.  Scanning
    edges in this random order and taking the first one still valid gives a
    uniformly random valid candidate at every step, because the edges not yet
    examined stay in exchangeable random order.
    """

    name = "random"

    def __init__(self, seed: int | None = None):
        if seed is None:
            seed = random.getrandbits(63)
        self.seed = seed

    def bind(self, strings):
        super().bind(strings)
        self._n = len(strings) + 1
        self._base = _splitmix64(self.seed & _MASK64)

    def key(self, u, v):
        return _splitmix64(self._base ^ (u * self._n + v))

    def __repr__(self):
        return f"<TieBreaker random seed={self.seed}>"


class Priority(TieBreaker):
    """Prefer an explicit list of edges, given as ``(u_string, v_string)`` pairs.

    Edges earlier in ``preferred`` win.  Ties between non-listed edges are
    resolved by ``fallback``.  This is how the bad executions described in
    the literature (e.g. Shibata 2026) are reproduced: the construction
    supplies the merges the paper performs, and greedy only follows them while
    they are genuinely maximum-overlap choices.
    """

    name = "priority"

    def __init__(self, preferred: Iterable[Sequence[str]], fallback: TieBreaker | None = None):
        self.preferred = [tuple(p) for p in preferred]
        self.fallback = fallback or FirstIndex()

    def bind(self, strings):
        super().bind(strings)
        self.fallback.bind(strings)
        index = {s: i for i, s in enumerate(strings)}
        self._rank: dict[Edge, int] = {}
        for r, (a, b) in enumerate(self.preferred):
            if a in index and b in index:
                self._rank.setdefault((index[a], index[b]), r)

    def key(self, u, v):
        return (self._rank.get((u, v), len(self._rank) + 1), self.fallback.key(u, v))


class CallableTie(TieBreaker):
    """Wrap a user function ``f(candidates, state) -> edge`` as a dynamic rule."""

    dynamic = True

    def __init__(self, func: Callable[[list[Edge], "GreedyState"], Edge], name: str = "custom"):
        self.func = func
        self.name = name

    def choose(self, candidates, state):
        return self.func(candidates, state)


class ShortestFragments(TieBreaker):
    """Dynamic rule: merge the pair whose merged fragment is shortest.

    It is mainly an example of the dynamic interface, though it is a
    plausible heuristic in its own right.  Ties are broken by index.
    """

    name = "short-frag"
    dynamic = True

    def choose(self, candidates, state):
        return min(candidates, key=lambda e: (state.fragment_length(e[0]) + state.fragment_length(e[1]), e))


class LongestFragments(TieBreaker):
    """Dynamic rule: merge the pair whose merged fragment is longest."""

    name = "long-frag"
    dynamic = True

    def choose(self, candidates, state):
        return min(candidates, key=lambda e: (-(state.fragment_length(e[0]) + state.fragment_length(e[1])), e))


NAMED_RULES: dict[str, Callable[[], TieBreaker]] = {
    "first": FirstIndex,
    "last": LastIndex,
    "lex": Lexicographic,
    "revlex": ReverseLexicographic,
    "short-frag": ShortestFragments,
    "long-frag": LongestFragments,
}


def make_tiebreaker(spec: "str | TieBreaker | Callable | None" = None, seed: int | None = None) -> TieBreaker:
    """Build a tie-breaker.

    ``spec`` may be a :class:`TieBreaker`, a callable ``f(candidates, state)``,
    ``None`` (meaning ``"first"``) or one of the strings
    ``first``, ``last``, ``lex``, ``revlex``, ``short-frag``, ``long-frag``,
    ``random`` or ``random:<seed>``.
    """
    if spec is None:
        return FirstIndex()
    if isinstance(spec, TieBreaker):
        return spec
    if callable(spec):
        return CallableTie(spec)
    if spec == "random":
        return RandomTie(seed)
    if spec.startswith("random:"):
        return RandomTie(int(spec.split(":", 1)[1]))
    try:
        return NAMED_RULES[spec]()
    except KeyError:
        raise ValueError(f"unknown tie-break rule {spec!r}; known: {sorted(NAMED_RULES)} or random[:seed]") from None
