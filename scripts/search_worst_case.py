#!/usr/bin/env python3
"""Search small k-SCS instances for the worst greedy ratio over all tie choices.

The recent bad-greedy constructions (Chukhin et al. 2026; Shibata 2026, whose
counterexample was first found by OpenAI's GPT-5.6 Sol) are all
equal-length ("k-SCS") instances, so this script searches that space directly:

* ``--mode exhaustive``: every subset of Sigma^k with size in
  ``[--min-size, --max-size]``, up to relabelling of the alphabet.
* ``--mode random``: ``--samples`` random subsets (seeded), for larger k or
  alphabets.

For every instance it computes OPT (k-spectrum certificate or DP) and the
worst and best greedy outputs over all tie choices.  It also checks two proven
bounds on every greedy execution:

* compression: ``L - G >= (L - OPT) / 2`` (Tarhio–Ukkonen; Kalugin–Nikolaev),
* length: ``G <= 3 * OPT`` (Chukhin et al. 2026, preprint).

Known values to compare against: rho_3 = 9/5 (approached only as the
instance grows), and rho_4 <= 2 (the conjecture holds for length 4).

    python scripts/search_worst_case.py --k 3 --alphabet ABC --max-size 6 --out results/search_k3
    python scripts/search_worst_case.py --k 4 --alphabet AB --max-size 8 --out results/search_k4
    python scripts/search_worst_case.py --k 6 --alphabet AB --mode random --samples 2000 --min-size 6 --max-size 12 --seed 1 --out results/search_k6
"""

from __future__ import annotations

import argparse
import heapq
import itertools
import json
import math
import random
import time
from fractions import Fraction
from pathlib import Path

import _common  # noqa: F401
from scs import ExplorationBudgetExceeded, dp_exact, greedy_outcomes, kspectrum_certificate, total_length
from scs.instance_io import environment_info


def canonical(strings, alphabet):
    """Smallest relabelling of the instance under alphabet permutations."""
    best = None
    for perm in itertools.permutations(alphabet):
        table = str.maketrans(alphabet, "".join(perm))
        form = tuple(sorted(s.translate(table) for s in strings))
        if best is None or form < best:
            best = form
    return best


def evaluate(strings, max_states):
    cert = kspectrum_certificate(strings)
    opt = len(cert) if cert is not None else dp_exact(strings, preprocess=False).length
    ex = greedy_outcomes(strings, preprocess=False, max_states=max_states)
    return opt, ex


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--alphabet", default="AB")
    ap.add_argument("--min-size", type=int, default=2)
    ap.add_argument("--max-size", type=int, default=8)
    ap.add_argument("--mode", choices=["exhaustive", "random"], default="exhaustive")
    ap.add_argument("--samples", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--max-states", type=int, default=100_000)
    ap.add_argument("--max-instances", type=int, default=2_000_000, help="safety cap for exhaustive mode")
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)

    words = ["".join(p) for p in itertools.product(args.alphabet, repeat=args.k)]
    if args.mode == "exhaustive":
        total = sum(math.comb(len(words), r) for r in range(args.min_size, args.max_size + 1))
        if total > args.max_instances:
            raise SystemExit(f"too many subsets ({total}); use --mode random or lower --max-size")

        def gen():
            for r in range(args.min_size, args.max_size + 1):
                yield from itertools.combinations(words, r)
    else:
        rng = random.Random(args.seed)

        def gen():
            for _ in range(args.samples):
                r = rng.randint(args.min_size, min(args.max_size, len(words)))
                yield tuple(rng.sample(words, r))

    seen: set = set()
    top: list = []  # min-heap of (ratio, tiebreak, record)
    stats = {"evaluated": 0, "duplicates": 0, "budget_exceeded": 0, "greedy_suboptimal": 0,
             "tie_sensitive": 0, "compression_bound_violations": 0, "factor3_violations": 0}
    worst = Fraction(1)
    t0 = time.perf_counter()
    for subset in gen():
        key = canonical(subset, args.alphabet)
        if key in seen:
            stats["duplicates"] += 1
            continue
        seen.add(key)
        strings = list(key)
        try:
            opt, ex = evaluate(strings, args.max_states)
        except ExplorationBudgetExceeded:
            stats["budget_exceeded"] += 1
            continue
        stats["evaluated"] += 1
        L = total_length(strings)
        if ex.max_length > opt:
            stats["greedy_suboptimal"] += 1
        if ex.tie_sensitive:
            stats["tie_sensitive"] += 1
        if 2 * (L - ex.max_length) < (L - opt):
            stats["compression_bound_violations"] += 1
        if ex.max_length > 3 * opt:
            stats["factor3_violations"] += 1
        r = Fraction(ex.max_length, opt)
        worst = max(worst, r)
        rec = {"strings": strings, "opt": opt, "greedy_worst": ex.max_length, "greedy_best": ex.min_length,
               "greedy_lengths": ex.lengths, "ratio": float(r), "ratio_exact": str(r),
               "worst_superstring": ex.max_superstring}
        item = (r, -len(strings), stats["evaluated"], rec)
        if len(top) < args.top:
            heapq.heappush(top, item)
        elif item[:3] > top[0][:3]:
            heapq.heapreplace(top, item)

    elapsed = time.perf_counter() - t0
    best = [it[3] for it in sorted(top, key=lambda it: it[:3], reverse=True)]
    report = {**environment_info(), "args": vars(args), "stats": stats, "worst_ratio": float(worst),
              "worst_ratio_exact": str(worst), "elapsed_s": elapsed, "top": best}
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "search.json").write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(stats))
    print(f"worst greedy/OPT over all ties: {worst} = {float(worst):.4f}  ({elapsed:.1f}s)")
    for rec in best[:5]:
        print(f"  {rec['ratio_exact']:>6}  OPT={rec['opt']} G_worst={rec['greedy_worst']}  {rec['strings']}")
    print(f"-> {out}/search.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
