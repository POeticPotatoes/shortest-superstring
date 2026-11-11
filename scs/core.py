"""Core string utilities for the shortest common superstring (SCS) problem.

Conventions used throughout the package
---------------------------------------
* An *instance* is a list of strings.  Each character of a Python ``str`` is
  one alphabet symbol, so constructions that need many symbols (e.g. the
  fresh symbols ``b_1 .. b_t`` of Shibata's construction) map them to distinct
  Unicode characters.
* ``preprocess`` removes duplicates and strings contained in other strings.
  It keeps the first-occurrence order of the survivors, so indices into the
  reduced list are stable and reproducible.
* ``ov(u, v)`` is the length of the longest suffix of ``u`` that is a prefix
  of ``v``.  For a substring-free set and ``u != v`` this is always strictly
  smaller than ``min(len(u), len(v))``.
"""

from __future__ import annotations

from typing import Iterable, Sequence

SEPARATOR = "\x00"


def overlap(a: str, b: str) -> int:
    """Length of the longest suffix of ``a`` that is also a prefix of ``b``.

    Follows the definition used by Shibata (2026): the overlap may be as long
    as ``min(len(a), len(b))``.  For distinct strings of a substring-free set
    it is always a *proper* overlap.
    """
    for k in range(min(len(a), len(b)), 0, -1):
        if a.endswith(b[:k]):
            return k
    return 0


def merge(a: str, b: str, k: int | None = None) -> str:
    """Return ``a ⊙ b``: ``a`` followed by ``b`` without its first ``ov(a, b)`` characters."""
    if k is None:
        k = overlap(a, b)
    return a + b[k:]


def preprocess(strings: Iterable[str]) -> list[str]:
    """Remove duplicate strings and strings contained in another input.

    The shortest superstring is unchanged by this reduction.  Survivors keep
    their first-occurrence order.
    """
    seen: set[str] = set()
    unique: list[str] = []
    for s in strings:
        if SEPARATOR in s:
            raise ValueError("strings must not contain the NUL character")
        if s and s not in seen:
            seen.add(s)
            unique.append(s)

    # Process longest strings first.  Containment is transitive, so it is
    # enough to test each string against the strings already kept.
    by_len = sorted(range(len(unique)), key=lambda i: -len(unique[i]))
    keep = [False] * len(unique)
    kept_text = ""  # NUL-joined kept strings that are strictly longer
    pending: list[str] = []
    current_len = None
    for i in by_len:
        s = unique[i]
        if len(s) != current_len:
            if pending:
                kept_text += SEPARATOR + SEPARATOR.join(pending)
                pending = []
            current_len = len(s)
        if s not in kept_text:
            keep[i] = True
            pending.append(s)
    return [s for i, s in enumerate(unique) if keep[i]]


def is_substring_free(strings: Sequence[str]) -> bool:
    """True if the strings are distinct and none is a substring of another."""
    return len(preprocess(strings)) == len(strings)


def total_length(strings: Iterable[str]) -> int:
    return sum(len(s) for s in strings)


# Above this many prefix characters (sum of len(s)^2 / 2), overlap_graph
# switches from the prefix index to the pairwise anchored search.
PREFIX_INDEX_LIMIT = 20_000_000


def overlap_graph(strings: Sequence[str], method: str = "auto") -> list[dict[int, int]]:
    """Sparse overlap graph: ``g[u][v] = ov(strings[u], strings[v]) > 0`` for ``u != v``.

    Pairs with overlap 0 are omitted.  The strings must be substring-free.

    ``method="prefix"`` indexes every proper prefix in a hash map.  It is fast for
    many short strings but needs about ``sum(len(s)^2) / 2`` characters of memory.
    ``method="anchored"`` checks every ordered pair with C-level string
    searches (see :func:`_anchored_overlap`), which suits long strings such as
    the gap words of the 12/5 construction.  ``"auto"`` picks between them
    using :data:`PREFIX_INDEX_LIMIT`.
    """
    if method == "auto":
        method = "prefix" if sum(len(s) ** 2 for s in strings) // 2 <= PREFIX_INDEX_LIMIT else "anchored"
    if method == "anchored":
        return _overlap_graph_anchored(strings)
    if method != "prefix":
        raise ValueError(f"unknown overlap_graph method {method!r}")
    prefixes: dict[str, list[int]] = {}
    for v, s in enumerate(strings):
        for k in range(1, len(s)):
            prefixes.setdefault(s[:k], []).append(v)

    graph: list[dict[int, int]] = [dict() for _ in strings]
    for u, s in enumerate(strings):
        row = graph[u]
        # Increasing k: later (longer) matches overwrite shorter ones.
        for k in range(1, len(s)):
            for v in prefixes.get(s[-k:], ()):
                if v != u:
                    row[v] = k
    return graph


def _leading_run(s: str) -> int:
    """Length of the run of ``s[0]`` at the start of ``s``."""
    return len(s) - len(s.lstrip(s[0]))


def _trailing_run(s: str, c: str) -> int:
    """Number of trailing copies of ``c`` in ``s``."""
    return len(s) - len(s.rstrip(c))


def _anchored_overlap(u: str, v: str, run: int) -> int:
    """``ov(u, v)`` for distinct, mutually non-contained ``u`` and ``v``.

    ``run`` is the length of the leading run of ``v[0]`` in ``v``.  An overlap
    of length ``k <= run`` is ``v[0] * k``, so it exists iff ``u`` ends with that
    many copies.  A longer overlap must start with the anchor
    ``v[:run + 1]``.  We find its occurrences in ``u`` from the left and take
    the first one where the rest of ``u`` is a prefix of ``v``.  The
    leftmost match gives the longest overlap.
    """
    cap = min(len(u), len(v)) - 1
    best = min(_trailing_run(u, v[0]), run, cap)
    if run >= len(v):
        return best
    anchor = v[:run + 1]
    j = u.find(anchor, 1)
    while j != -1:
        k = len(u) - j
        if k <= cap and u.startswith(v[:k], j):
            return max(best, k)
        j = u.find(anchor, j + 1)
    return best


def _overlap_graph_anchored(strings: Sequence[str]) -> list[dict[int, int]]:
    runs = [_leading_run(s) if s else 0 for s in strings]
    graph: list[dict[int, int]] = [dict() for _ in strings]
    for u, su in enumerate(strings):
        row = graph[u]
        for v, sv in enumerate(strings):
            if v != u:
                k = _anchored_overlap(su, sv, runs[v])
                if k:
                    row[v] = k
    return graph


def overlap_matrix(strings: Sequence[str]) -> list[list[int]]:
    """Dense ``n x n`` overlap matrix (diagonal set to 0)."""
    n = len(strings)
    dense = [[0] * n for _ in range(n)]
    for u, row in enumerate(overlap_graph(strings)):
        for v, k in row.items():
            dense[u][v] = k
    return dense


def superstring_from_order(strings: Sequence[str], order: Sequence[int],
                           graph: Sequence[dict[int, int]] | None = None) -> str:
    """Merge ``strings`` in the given order using maximum overlaps."""
    if not order:
        return ""
    if graph is None:
        graph = overlap_graph(strings)
    parts = [strings[order[0]]]
    for u, v in zip(order, order[1:]):
        parts.append(strings[v][graph[u].get(v, 0):])
    return "".join(parts)


def is_superstring(candidate: str, strings: Iterable[str]) -> bool:
    """True if every string occurs in ``candidate`` as a contiguous substring."""
    return all(s in candidate for s in strings)
