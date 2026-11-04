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


def overlap_graph(strings: Sequence[str]) -> list[dict[int, int]]:
    """Sparse overlap graph: ``g[u][v] = ov(strings[u], strings[v]) > 0`` for ``u != v``.

    Pairs with overlap 0 are omitted.  The strings must be substring-free.
    Runs in time proportional to the total length of the strings times their
    maximum length plus the number of (pair, overlap-length) matches, using a
    hash map from prefixes to string indices.
    """
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
