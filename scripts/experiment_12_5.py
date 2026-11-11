#!/usr/bin/env python3
"""Experiment for the 12/5 construction (arXiv:2609.01365v2, Theorem 4.1; paper section 5.5).

For each ``(r, P)`` it generates the instance on the fly (nothing needs to be
stored), then:

* replays the prescribed bad execution of Section 4.4 (rule ``paper``) and checks
  its length against ``12Pr + (115r^2 + 7r)/2``,
* runs greedy with the fixed tie rules and ``--random-ties`` seeded random rules,
  plus ``first`` on ``--shuffle-orders`` seeded shuffles of the input order.  The
  stored X, Y, U, V, Z order steers index-based rules into the bad execution,
  so ``first`` / ``last`` on the stored order are not a fair "fixed rule" baseline,
* checks that H is a common superstring of length ``5Pr + 27r^2 + 4P + 19r + 1``,
* computes the exact OPT with subset DP when ``5r <= --dp-max-n`` (r <= 4 by default).

Ratios use the exact OPT when it is known (``ref_kind=exact``).  Otherwise they
use |H| (``ref_kind=upper_bound``), giving the certified lower bound
G/|H| <= G/OPT.  The two kinds are reported separately in ``summary.md``.

Output in ``--out``: ``runs.csv``, ``instances.csv`` (same columns as
``run_benchmark.py``), ``theorem.csv`` (formula checks per instance), ``meta.json``
and ``summary.md``.

    python scripts/experiment_12_5.py --out results/greedy125
    python scripts/experiment_12_5.py --family adapted --out results/greedy125_adapted   # the report's S_n
    python scripts/experiment_12_5.py --out results/greedy125_big --r 70,100 --small-p-r "" --random-ties 10
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

import _common  # noqa: F401
import run_benchmark as rb
import summarize_results
from scs import greedy, overlap_graph
from scs.constructions import greedy_12_5, greedy_12_5_adapted, greedy_12_5_adapted_formulas, greedy_12_5_formulas
from scs.generators import derive_seed, shuffled
from scs.instance_io import environment_info

THEOREM_FIELDS = ["instance", "r", "P", "n", "H_len", "H_formula", "H_is_superstring", "greedy_paper",
                  "greedy_formula", "opt", "H_minus_opt", "ratio_paper_vs_H", "ratio_paper_vs_opt",
                  "exceeds_9_4", "exceeds_7_3", "exceeds_19_8"]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--family", choices=["paper", "adapted"], default="paper",
                    help="paper: Theorem 4.1 with (r, P); adapted: the team report's single-parameter S_n (Section 4.4)")
    ap.add_argument("--n", default="2,3,4,5,6,8,10,15,20,30,50", help="n values for --family adapted")
    ap.add_argument("--r", default="1,2,3,4,5,6,8,10,15,20,30,50", help="r values with P = r^2")
    ap.add_argument("--small-p-r", default="1,2,3,4", help="r values also run with the minimal P = r - 1")
    ap.add_argument("--rules", default="first,last,lex,revlex")
    ap.add_argument("--random-ties", type=int, default=50)
    ap.add_argument("--shuffle-orders", type=int, default=20,
                    help="also run `first` on this many seeded shuffles of the input order")
    ap.add_argument("--tie-seed", type=int, default=0)
    ap.add_argument("--dp-max-n", type=int, default=20)
    ap.add_argument("--explore-max-n", type=int, default=10)
    ap.add_argument("--explore-max-states", type=int, default=200_000)
    args = ap.parse_args(argv)

    if args.family == "adapted":
        configs = [(n, None) for n in map(int, filter(None, args.n.split(",")))]
    else:
        configs = [(r, r * r) for r in map(int, filter(None, args.r.split(",")))]
        configs += [(r, r - 1) for r in map(int, filter(None, args.small_p_r.split(",")))]
        configs = sorted(set(configs))
    bench_args = argparse.Namespace(rules=[x for x in args.rules.split(",") if x], random_ties=args.random_ties,
                                    tie_seed=args.tie_seed, dp_max_n=args.dp_max_n, bf_check_max_n=0,
                                    explore_max_n=args.explore_max_n, explore_max_states=args.explore_max_states,
                                    trace_max_n=0, timing_repeats=1)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    t_start = time.perf_counter()
    with open(out / "runs.csv", "w", newline="", encoding="utf-8") as fr, \
            open(out / "instances.csv", "w", newline="", encoding="utf-8") as fi, \
            open(out / "theorem.csv", "w", newline="", encoding="utf-8") as ft:
        wr = csv.DictWriter(fr, rb.RUN_FIELDS, extrasaction="ignore")
        wi = csv.DictWriter(fi, rb.INSTANCE_FIELDS, extrasaction="ignore")
        wt = csv.DictWriter(ft, THEOREM_FIELDS)
        for w in (wr, wi, wt):
            w.writeheader()
        for r, P in configs:
            t0 = time.perf_counter()
            if args.family == "adapted":
                inst = greedy_12_5_adapted(r)
                inst["path"] = f"generated:greedy_12_5_adapted(n={r})"
                inst["batch"] = f"greedy125adapted@generated/n={5 * (r - 1)}"
                f = greedy_12_5_adapted_formulas(r)
            else:
                inst = greedy_12_5(r, P)
                inst["path"] = f"generated:greedy_12_5(r={r}, P={P})"
                inst["batch"] = f"greedy125/P={'r^2' if P == r * r else 'r-1'}@generated/n={5 * r}"
                f = greedy_12_5_formulas(r, P)
            runs, summary = rb.benchmark_instance(inst, bench_args)
            # The strings are stored in the paper's X, Y, U, V, Z order, which happens to steer
            # index-based rules (first/last) into the bad execution.  Shuffled orders show
            # what `first` does without that hint.
            base = {k: summary[k] for k in ("instance", "family", "batch", "n", "L", "opt", "opt_method",
                                            "ref", "ref_kind")}
            shuffled_ratios = []
            graph = overlap_graph(inst["strings"])  # substring-free already; permute it per shuffle
            for j in range(args.shuffle_orders):
                seed = derive_seed(args.tie_seed, "shuffle", inst["id"], j)
                t1 = time.perf_counter()
                perm = shuffled(range(len(inst["strings"])), seed)
                pos = {v: a for a, v in enumerate(perm)}
                res = greedy([inst["strings"][v] for v in perm], "first", preprocess=False,
                             graph=[{pos[v]: w for v, w in graph[u].items()} for u in perm])
                ratio = res.length / summary["ref"]
                shuffled_ratios.append(ratio)
                runs.append({**base, "algo": "greedy", "rule": "first@shuffled", "tie_seed": seed,
                             "length": res.length, "time_s": time.perf_counter() - t1, "ratio": ratio,
                             "compression_ratio": rb.compression_ratio(res.length, summary["opt"], summary["L"]),
                             "optimal": None if summary["opt"] is None else int(res.length == summary["opt"])})
            wr.writerows({k: rb.fmt(v) for k, v in row.items()} for row in runs)
            wi.writerow({k: rb.fmt(v) for k, v in summary.items()})

            H = inst["upper_superstring"]
            G = summary["greedy_paper"]
            opt = summary["opt"]
            vs_h = G / len(H)
            wt.writerow({k: rb.fmt(v) for k, v in {
                "instance": inst["id"], "r": r, "P": P, "n": len(inst["strings"]), "H_len": len(H), "H_formula": f["opt_upper"],
                "H_is_superstring": 1, "greedy_paper": G, "greedy_formula": f["greedy_bad"], "opt": opt,
                "H_minus_opt": None if opt is None else len(H) - opt, "ratio_paper_vs_H": vs_h,
                "ratio_paper_vs_opt": None if opt is None else G / opt,
                "exceeds_9_4": int(vs_h > 9 / 4), "exceeds_7_3": int(vs_h > 7 / 3), "exceeds_19_8": int(vs_h > 19 / 8),
            }.items()})
            for fh in (fr, fi, ft):
                fh.flush()
            if G != f["greedy_bad"] or len(H) != f["opt_upper"]:
                print(f"MISMATCH for r={r}, P={P}: G={G} (formula {f['greedy_bad']}), |H|={len(H)} "
                      f"(formula {f['opt_upper']})", file=sys.stderr)
                return 1
            print(f"{'n' if P is None else 'r'}={r:3d} P={P!s:>5} strings={len(inst['strings']):4d} |H|={len(H):8d} OPT={opt!s:>6} G(paper)={G:8d} "
                  f"G/|H|={vs_h:.4f} first={summary['ratio_first']:.4f} random mean/max="
                  f"{summary['ratio_random_mean'] or 0:.4f}/{summary['ratio_random_max'] or 0:.4f} "
                  f"first@shuffled mean={sum(shuffled_ratios) / len(shuffled_ratios) if shuffled_ratios else 0:.4f} "
                  f"[{summary['ref_kind']}] {time.perf_counter() - t0:.1f}s", file=sys.stderr)

    meta = {**environment_info(), "args": vars(args), "configs": configs,
            "random_tie_seed_scheme": "derive_seed(tie_seed, instance_id, r)",
            "shuffle_seed_scheme": "derive_seed(tie_seed, 'shuffle', instance_id, j)",
            "source": ("team report Section 4.4 (scs.constructions.greedy_12_5_adapted)" if args.family == "adapted"
                       else "arXiv:2609.01365v2 Theorem 4.1 (scs.constructions.greedy_12_5)"),
            "elapsed_s": time.perf_counter() - t_start}
    (out / "meta.json").write_text(json.dumps(meta, indent=1) + "\n", encoding="utf-8")
    summarize_results.summarize(out, by_instance=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
