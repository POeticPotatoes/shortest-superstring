"""Shortest common superstring: greedy vs exact (project code).

Quick start::

    from scs import greedy, dp_exact
    greedy(["AABA", "ABAA", "BAB"]).superstring    # 'AABAABAB' (length 8)
    dp_exact(["AABA", "ABAA", "BAB"]).superstring  # length 7
"""

from .core import is_superstring, merge, overlap, overlap_graph, overlap_matrix, preprocess, \
    superstring_from_order, total_length
from .exact import brute_force_exact, dp_exact, equal_length_lower_bound, kspectrum_certificate, optimal_length
from .greedy import ExplorationBudgetExceeded, GreedyResult, GreedyState, greedy, greedy_naive, greedy_outcomes
from .tiebreak import Priority, RandomTie, TieBreaker, make_tiebreaker

__all__ = [
    "brute_force_exact", "dp_exact", "equal_length_lower_bound", "ExplorationBudgetExceeded", "greedy",
    "greedy_naive", "greedy_outcomes", "GreedyResult", "GreedyState", "is_superstring", "kspectrum_certificate",
    "make_tiebreaker", "merge", "optimal_length", "overlap", "overlap_graph", "overlap_matrix", "preprocess",
    "Priority", "RandomTie", "superstring_from_order", "TieBreaker", "total_length",
]
