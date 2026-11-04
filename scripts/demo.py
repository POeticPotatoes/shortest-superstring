#!/usr/bin/env python3
"""A tour of the library, using the examples from the slides and papers.

    python scripts/demo.py
"""

import _common  # noqa: F401
from scs import (Priority, dp_exact, greedy, greedy_outcomes, kspectrum_certificate, make_tiebreaker, overlap,
                 preprocess)
from scs.constructions import chukhin_k, shibata, tarhio_ukkonen_example7
from scs.generators import random_strings, repetitive_strings, sampled_fragments


def section(title):
    print(f"\n=== {title} ===")


section("Slides 1-3: overlaps and preprocessing")
print("ov(ATT, TTA) =", overlap("ATT", "TTA"), "  ov(TTA, ATT) =", overlap("TTA", "ATT"))
print("preprocess([ATT, TT, TTA, ATT, TAC]) =", preprocess(["ATT", "TT", "TTA", "ATT", "TAC"]))
print("greedy:", greedy(["ATT", "TTA", "TAC"]).superstring, " DP:", dp_exact(["ATT", "TTA", "TAC"]).superstring)

section("Slide 5: greedy can fail")
S = ["AABA", "ABAA", "BAB"]
g, opt = greedy(S), dp_exact(S)
print(f"greedy {g.superstring} ({g.length})  merges(u, v, overlap)={g.merges}")
print(f"OPT    {opt.superstring} ({opt.length})  ratio {g.length / opt.length:.3f}")

section("Tie-breaking rules on Tarhio-Ukkonen Example 7 {ab^h, b^(h+1), b^h a}, h = 4")
inst = tarhio_ukkonen_example7(4)
for rule in ["first", "last", "lex", "revlex", "short-frag", "long-frag", "random:1", "random:2"]:
    r = greedy(inst["strings"], rule, trace=True)
    print(f"  {rule:10s} -> {r.superstring:14s} length {r.length}  (tie steps: {r.tie_steps})")
ex = greedy_outcomes(inst["strings"])
print(f"  all tie choices give lengths {ex.lengths}; OPT = {dp_exact(inst['strings']).length}")


def prefer_longest_string(candidates, state):
    """A custom dynamic rule: merge the pair whose strings are longest."""
    return max(candidates, key=lambda e: (len(state.strings[e[0]]) + len(state.strings[e[1]]), e))


print("  custom callable rule ->", greedy(inst["strings"], prefer_longest_string).superstring)
print("  paper's tie choice   ->", greedy(inst["strings"], Priority(inst["tie_priority"])).superstring)
print("  make_tiebreaker('random:5') =", make_tiebreaker("random:5"))

section("Chukhin et al. 2026: k = 6, t = 1 (OPT 14, greedy may give 18)")
inst = chukhin_k(6, 1)
r = greedy(inst["strings"], Priority(inst["tie_priority"]))
print("strings:", inst["strings"])
print("paper execution:", r.superstring, r.length, "  OPT certificate:", kspectrum_certificate(inst["strings"]))
print("all tie outcomes:", greedy_outcomes(inst["strings"]).lengths)

section("Shibata 2026: greedy > 2 OPT (k = 10, t = 10)")
inst = shibata(10, 10)
r = greedy(inst["strings"], Priority(inst["tie_priority"]))
cert = kspectrum_certificate(inst["strings"])
print(f"n = {len(inst['strings'])}, greedy (paper ties) = {r.length}, OPT = {len(cert)}, ratio = {r.length / len(cert):.4f}")
print(f"greedy with 'first' ties = {greedy(inst['strings'], 'first').length}")

section("Generators (seeded, reproducible)")
for inst in [random_strings(6, (4, 8), "AB", seed=1), sampled_fragments(6, 30, (5, 9), "ACGT", seed=2),
             repetitive_strings(6, "periodic", seed=3), repetitive_strings(6, "cyclic", k=5, alphabet="AB", seed=4),
             repetitive_strings(6, "kmer", k=5, seed=5)]:
    S = inst["strings"]
    print(f"  {inst['family']:10s} {inst['params'].get('mode', ''):8s} seed={inst['seed']} {S} "
          f"greedy={greedy(S).length} OPT={dp_exact(S).length}")
