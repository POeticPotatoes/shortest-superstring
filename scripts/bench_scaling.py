#!/usr/bin/env python3
"""Runtime scaling of greedy and subset DP as n grows.

Instances are generated on the fly from recorded seeds
(``derive_seed(master_seed, family, n, rep)``), so no data files are needed.
Writes ``scaling.csv`` and ``meta.json`` to ``--out`` and prints a table.
Timings are best-of ``--repeats``.

* DP: n in ``--dp-sizes`` (default 4..18).  Its cost is O(n^2 2^n) and does
  not depend on the instance family.
* Greedy: n in ``--greedy-sizes`` (default 100..5000), timed separately for
  building the overlap graph and for the merge loop under each rule in
  ``--rules``.

    python scripts/bench_scaling.py --out results/scaling
    python scripts/bench_scaling.py --out results/scaling_quick --dp-sizes 4,8,12 --greedy-sizes 100,500 --reps 2
"""

from __future__ import annotations

import argparse
import csv
import json
import time
from pathlib import Path

import _common  # noqa: F401
from scs import dp_exact, greedy, overlap_graph, preprocess, total_length
from scs.generators import derive_seed, generate
from scs.instance_io import environment_info

FAMILIES = {
    "random": lambda n: {"length": (8, 15), "alphabet": "ACGT"},
    "sampled": lambda n: {"source_length": max(4 * n, 40), "fragment_length": (12, 25), "alphabet": "ACGT"},
    "repetitive": lambda n: {"mode": "periodic", "motif_length": (2, 4), "mutation_rate": 0.08,
                             "fragment_length": (12, 24), "source_length": 8 * n, "alphabet": "ACGT"},
}


def best_time(fn, repeats):
    best, out = float("inf"), None
    for _ in range(repeats):
        t0 = time.perf_counter()
        out = fn()
        best = min(best, time.perf_counter() - t0)
    return out, best


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--families", default=",".join(FAMILIES))
    ap.add_argument("--dp-sizes", default="4,6,8,10,12,14,16,18")
    ap.add_argument("--greedy-sizes", default="100,200,500,1000,2000,5000")
    ap.add_argument("--rules", default="first,random:0,lex")
    ap.add_argument("--reps", type=int, default=3, help="instances per (family, n)")
    ap.add_argument("--repeats", type=int, default=3, help="timing repeats per measurement")
    ap.add_argument("--master-seed", type=int, default=20261105)
    args = ap.parse_args(argv)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rows = []
    families = args.families.split(",")
    rules = [r for r in args.rules.split(",") if r]

    def instance(family, n, rep):
        seed = derive_seed(args.master_seed, "scaling", family, n, rep)
        inst = generate(family, seed, n=n, **FAMILIES[family](n))
        return seed, preprocess(inst["strings"])

    for n in [int(x) for x in args.dp_sizes.split(",") if x]:
        for rep in range(args.reps):
            family = families[rep % len(families)]
            seed, S = instance(family, n, rep)
            res, t = best_time(lambda: dp_exact(S, preprocess=False, max_n=max(n, 20)), 1 if n >= 16 else args.repeats)
            rows.append({"algo": "dp", "rule": "", "family": family, "n": n, "L": total_length(S), "rep": rep,
                         "seed": seed, "length": res.length, "time_s": t})
            print(f"dp      {family:10s} n={n:5d} rep={rep} {t:9.4f}s")

    for n in [int(x) for x in args.greedy_sizes.split(",") if x]:
        for family in families:
            for rep in range(args.reps):
                seed, S = instance(family, n, rep)
                g, tg = best_time(lambda: overlap_graph(S), args.repeats)
                rows.append({"algo": "overlap_graph", "rule": "", "family": family, "n": n, "L": total_length(S),
                             "rep": rep, "seed": seed, "length": "", "time_s": tg, "edges": sum(map(len, g))})
                for rule in rules:
                    res, t = best_time(lambda: greedy(S, rule, preprocess=False, graph=g), args.repeats)
                    rows.append({"algo": "greedy", "rule": rule, "family": family, "n": n, "L": total_length(S),
                                 "rep": rep, "seed": seed, "length": res.length, "time_s": t,
                                 "edges": sum(map(len, g))})
                print(f"greedy  {family:10s} n={n:5d} rep={rep} graph={tg:.3f}s "
                      f"merge[{rules[0] if rules else '-'}]={rows[-len(rules)]['time_s'] if rules else 0:.3f}s")

    fields = ["algo", "rule", "family", "n", "L", "rep", "seed", "length", "time_s", "edges"]
    with open(out / "scaling.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fields)
        w.writeheader()
        w.writerows(rows)
    (out / "meta.json").write_text(json.dumps({**environment_info(), "args": vars(args),
                                               "seed_scheme": "derive_seed(master_seed, 'scaling', family, n, rep)"},
                                              indent=1) + "\n")

    # Median time per (algo, rule, n) across families/reps.
    agg: dict = {}
    for r in rows:
        agg.setdefault((r["algo"], r["rule"], r["n"]), []).append(r["time_s"])
    print("\nalgo           rule        n     median_s")
    for (algo, rule, n), ts in sorted(agg.items(), key=lambda x: (x[0][0], x[0][1], x[0][2])):
        ts = sorted(ts)
        print(f"{algo:14s} {rule:10s} {n:5d} {ts[len(ts) // 2]:10.4f}")
    print(f"-> {out}/scaling.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
