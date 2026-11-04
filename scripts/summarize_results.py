#!/usr/bin/env python3
"""Aggregate ``run_benchmark.py`` output into tables.

Reads ``runs.csv`` and ``instances.csv`` from each results directory and
writes ``summary.md``, ``summary_runs.csv`` and ``summary_ties.csv`` there.

* **Per (group, n, algo/rule)**: instance count, mean/max G/OPT, minimum
  compression ratio, optimality rate, mean/max runtime.
* **Tie sensitivity per (group, n)**: share of instances where different tie
  choices give different lengths, mean number of distinct lengths across
  random ties, mean share of random-tie runs that are optimal, and mean
  number of steps with tied candidates.

``group`` is the batch variant (for example ``repetitive/periodic``), or the
instance id for literature instances.

    python scripts/summarize_results.py results/small [results/literature ...] [--by-instance]
"""

from __future__ import annotations

import argparse
import csv
import statistics
from collections import defaultdict
from pathlib import Path


def num(x):
    if x in ("", None):
        return None
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return None


def group_of(row, by_instance: bool) -> str:
    if by_instance or not row.get("batch"):
        return row["instance"]
    return row["batch"].split("@", 1)[0]


def mean(xs):
    xs = [x for x in xs if x is not None]
    return statistics.fmean(xs) if xs else None


def mx(xs):
    xs = [x for x in xs if x is not None]
    return max(xs) if xs else None


def mn(xs):
    xs = [x for x in xs if x is not None]
    return min(xs) if xs else None


def f(x, nd=4):
    if x is None:
        return "-"
    return f"{x:.{nd}f}" if isinstance(x, float) else str(x)


def summarize(results: Path, by_instance: bool) -> None:
    with open(results / "runs.csv", newline="", encoding="utf-8") as fh:
        runs = list(csv.DictReader(fh))
    with open(results / "instances.csv", newline="", encoding="utf-8") as fh:
        insts = list(csv.DictReader(fh))

    run_groups = defaultdict(list)
    for r in runs:
        label = r["algo"] if r["algo"] != "greedy" else f"greedy[{r['rule']}]"
        run_groups[(group_of(r, by_instance), int(r["n"]), label)].append(r)
    run_rows = []
    for (g, n, label), rows in sorted(run_groups.items()):
        ratios = [num(r["ratio"]) for r in rows]
        opt_flags = [num(r["optimal"]) for r in rows]
        times = [num(r["time_s"]) for r in rows]
        run_rows.append({
            "group": g, "n": n, "algo": label, "runs": len(rows),
            "instances": len({r["instance"] for r in rows}),
            "mean_ratio": mean(ratios), "max_ratio": mx(ratios),
            "min_compression_ratio": mn(num(r["compression_ratio"]) for r in rows),
            "optimal_rate": mean(opt_flags), "mean_time_s": mean(times), "max_time_s": mx(times),
        })

    tie_groups = defaultdict(list)
    for r in insts:
        tie_groups[(group_of(r, by_instance), int(r["n"]))].append(r)
    tie_rows = []
    for (g, n), rows in sorted(tie_groups.items()):
        tie_rows.append({
            "group": g, "n": n, "instances": len(rows),
            "opt_methods": ",".join(sorted({r["opt_method"] for r in rows})),
            "tie_sensitive_frac": mean(num(r["tie_sensitive"]) for r in rows),
            "mean_random_distinct": mean(num(r["random_distinct"]) for r in rows),
            "mean_random_optimal_frac": mean(num(r["random_optimal_frac"]) for r in rows),
            "mean_tie_steps_first": mean(num(r["tie_steps_first"]) for r in rows),
            "mean_ratio_first": mean(num(r["ratio_first"]) for r in rows),
            "max_ratio_observed": mx(num(r["ratio_worst_observed"]) for r in rows),
            "max_ratio_explored": mx(num(r["ratio_worst_explored"]) for r in rows),
        })

    for name, rows in (("summary_runs.csv", run_rows), ("summary_ties.csv", tie_rows)):
        if rows:
            with open(results / name, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, list(rows[0]))
                w.writeheader()
                w.writerows({k: f(v, 6) if isinstance(v, float) else v for k, v in row.items()} for row in rows)

    lines = [f"# Benchmark summary: `{results}`", "",
             f"{len(insts)} instances, {len(runs)} solver runs.", "",
             "## Solution quality and runtime", "",
             "| group | n | algo | inst | mean G/OPT | max G/OPT | min compr. ratio | optimal rate | mean time (s) |",
             "|---|---:|---|---:|---:|---:|---:|---:|---:|"]
    for r in run_rows:
        lines.append(f"| {r['group']} | {r['n']} | {r['algo']} | {r['instances']} | {f(r['mean_ratio'])} | "
                     f"{f(r['max_ratio'])} | {f(r['min_compression_ratio'])} | {f(r['optimal_rate'], 3)} | "
                     f"{f(r['mean_time_s'], 5)} |")
    lines += ["", "## Tie sensitivity", "",
              "| group | n | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | "
              "mean tie steps | mean G/OPT (first) | max G/OPT observed | max G/OPT all ties |",
              "|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|"]
    for r in tie_rows:
        lines.append(f"| {r['group']} | {r['n']} | {r['instances']} | {r['opt_methods']} | "
                     f"{f(r['tie_sensitive_frac'], 3)} | {f(r['mean_random_distinct'], 2)} | "
                     f"{f(r['mean_random_optimal_frac'], 3)} | {f(r['mean_tie_steps_first'], 1)} | "
                     f"{f(r['mean_ratio_first'])} | {f(r['max_ratio_observed'])} | {f(r['max_ratio_explored'])} |")
    (results / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {results}/summary.md, summary_runs.csv, summary_ties.csv")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("results", nargs="+", type=Path)
    ap.add_argument("--by-instance", action="store_true", help="one group per instance instead of per batch")
    args = ap.parse_args(argv)
    for res in args.results:
        summarize(res, args.by_instance)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
