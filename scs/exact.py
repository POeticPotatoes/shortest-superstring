"""Exact SCS solvers for small instances, plus optimality certificates.

* :func:`dp_exact`: subset dynamic programming (Held–Karp style, slide 11).
  A state is ``(used set, last string)`` and stores the maximum overlap
  collected, which is the same as the shortest length reached.
  ``O(n^2 2^n)`` time and ``O(n 2^n)`` memory after computing overlaps.  The
  pure-Python version takes about 0.3 s at ``n = 16``, 1.5 s at ``n = 18`` and
  7 s / 250 MB at ``n = 20``.  Time grows about 5x per +2 in n.
* :func:`brute_force_exact`: tries every permutation; used to validate the DP
  on tiny inputs (``n <= 8``).
* :func:`kspectrum_certificate`: for inputs whose strings all have length
  ``k``, ``OPT >= |S| + k - 1``.  If the de Bruijn-style graph on
  ``(k-1)``-mers has an Eulerian trail, the trail spells a superstring of
  exactly that length, which certifies OPT without any search.  This
  is how Shibata (2026) and Chukhin et al. (2026) compute OPT for their
  constructions, and it gives exact answers far beyond the DP's reach.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from operator import add
from typing import Sequence

from .core import is_superstring, overlap_matrix, preprocess as _preprocess, superstring_from_order, total_length

NEG = -(1 << 60)
DEFAULT_DP_MAX_N = 20


@dataclass
class ExactResult:
    length: int
    superstring: str
    order: list[int]
    strings: list[str]
    method: str

    @property
    def compression(self) -> int:
        return total_length(self.strings) - self.length


def dp_exact(strings: Sequence[str], *, preprocess: bool = True, max_n: int = DEFAULT_DP_MAX_N) -> ExactResult:
    """Exact shortest superstring by subset DP over (used set, last string)."""
    reduced = _preprocess(strings) if preprocess else list(strings)
    n = len(reduced)
    if n == 0:
        return ExactResult(0, "", [], reduced, "dp")
    if n > max_n:
        raise ValueError(f"subset DP limited to n <= {max_n} (got n = {n}); raise max_n deliberately")
    ov = overlap_matrix(reduced)
    col = [[ov[i][j] for i in range(n)] for j in range(n)]  # col[j][i] = ov(i, j)

    # best[mask][j] = max total overlap of an ordering of `mask` ending in j (NEG if j not in mask).
    full = (1 << n) - 1
    best: list[list[int]] = [[]] * (1 << n)
    best[0] = [NEG] * n
    for mask in range(1, full + 1):
        row = [NEG] * n
        if mask & (mask - 1) == 0:
            row[mask.bit_length() - 1] = 0
        else:
            m = mask
            while m:
                low = m & -m
                m ^= low
                j = low.bit_length() - 1
                row[j] = max(map(add, best[mask ^ low], col[j]))
        best[mask] = row

    final = best[full]
    last = max(range(n), key=lambda j: final[j])
    saved = final[last]

    # Walk back through the table to recover an optimal order.
    order = [last]
    mask = full
    while mask & (mask - 1):
        prev_mask = mask ^ (1 << last)
        prev_row = best[prev_mask]
        target = best[mask][last]
        last = next(i for i in range(n) if prev_row[i] != NEG and prev_row[i] + ov[i][last] == target)
        order.append(last)
        mask = prev_mask
    order.reverse()

    sup = superstring_from_order(reduced, order)
    assert len(sup) == total_length(reduced) - saved
    return ExactResult(len(sup), sup, order, reduced, "dp")


def brute_force_exact(strings: Sequence[str], *, preprocess: bool = True, max_n: int = 9) -> ExactResult:
    """Exact answer by trying every ordering (``O(n! n)``); for validating the DP."""
    reduced = _preprocess(strings) if preprocess else list(strings)
    n = len(reduced)
    if n > max_n:
        raise ValueError(f"brute force limited to n <= {max_n} (got n = {n})")
    if n == 0:
        return ExactResult(0, "", [], reduced, "bruteforce")
    ov = overlap_matrix(reduced)
    best_saved, best_order = -1, list(range(n))
    for perm in itertools.permutations(range(n)):
        saved = sum(ov[a][b] for a, b in zip(perm, perm[1:]))
        if saved > best_saved:
            best_saved, best_order = saved, list(perm)
    sup = superstring_from_order(reduced, best_order)
    return ExactResult(len(sup), sup, best_order, reduced, "bruteforce")


def equal_length_lower_bound(strings: Sequence[str]) -> int | None:
    """``|S| + k - 1`` if all (distinct) strings have length ``k``, else ``None``.

    Each string after the first contributes at least one new character,
    because the overlap of two distinct length-k strings is at most k-1.
    """
    reduced = _preprocess(strings)
    lengths = {len(s) for s in reduced}
    if len(lengths) != 1:
        return None
    return len(reduced) + lengths.pop() - 1


def kspectrum_certificate(strings: Sequence[str]) -> str | None:
    """Superstring of length ``|S| + k - 1`` from an Eulerian trail, if one exists.

    Returns ``None`` if the strings do not all have the same length or the
    ``(k-1)``-mer graph has no Eulerian trail.  When a string is returned, it is
    an optimal superstring, because it meets :func:`equal_length_lower_bound`.
    """
    reduced = _preprocess(strings)
    if not reduced:
        return ""
    k = len(reduced[0])
    if any(len(s) != k for s in reduced):
        return None
    if k == 1:
        return "".join(reduced)
    adj: dict[str, list[str]] = {}
    indeg: dict[str, int] = {}
    for s in reduced:
        a, b = s[:-1], s[1:]
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, [])
        indeg[b] = indeg.get(b, 0) + 1
    start = None
    plus = minus = 0
    for node, outs in adj.items():
        d = len(outs) - indeg.get(node, 0)
        if d == 1:
            plus += 1
            start = node
        elif d == -1:
            minus += 1
        elif d != 0:
            return None
    if (plus, minus) not in ((0, 0), (1, 1)):
        return None
    if start is None:
        start = reduced[0][:-1]
    # Hierholzer's algorithm (iterative).
    ptr = {node: 0 for node in adj}
    stack, trail = [start], []
    while stack:
        node = stack[-1]
        if ptr[node] < len(adj[node]):
            nxt = adj[node][ptr[node]]
            ptr[node] += 1
            stack.append(nxt)
        else:
            trail.append(stack.pop())
    if len(trail) != len(reduced) + 1:
        return None  # graph not connected
    trail.reverse()
    sup = trail[0] + "".join(node[-1] for node in trail[1:])
    assert len(sup) == len(reduced) + k - 1 and is_superstring(sup, reduced)
    return sup


def optimal_length(strings: Sequence[str], *, dp_max_n: int = 16, known: int | None = None) -> tuple[int | None, str]:
    """Best available exact OPT: a k-spectrum certificate, then subset DP, then a supplied value.

    Returns ``(opt, method)`` where method is ``"certificate"``, ``"dp"``,
    ``"known"`` or ``"none"``.
    """
    cert = kspectrum_certificate(strings)
    if cert is not None:
        return len(cert), "certificate"
    reduced = _preprocess(strings)
    if len(reduced) <= dp_max_n:
        return dp_exact(reduced, preprocess=False, max_n=dp_max_n).length, "dp"
    if known is not None:
        return known, "known"
    return None, "none"
