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


def md(text: str) -> str:
    """Escape pipes inside markdown table cells."""
    return str(text).replace("|", "\\|")


def size_key(row, by_instance: bool):
    """Group size: n, or the batch parameter (e.g. ``cov10``) when n varies within a batch."""
    batch = row.get("batch") or ""
    tail = batch.split("@", 1)[1] if "@" in batch else ""
    param = tail.split("/", 1)[1] if "/" in tail else ""
    if by_instance or not param or param.startswith("n="):
        return (0, int(row["n"]))
    return (1, param)


def size_label(key, rows) -> str:
    if key[0] == 0:
        return str(key[1])
    ns = [int(r["n"]) for r in rows]
    return f"{key[1]} (n≈{round(sum(ns) / len(ns))})"


def basis_of(row) -> str:
    """Ratios against an exact OPT and against a known superstring (lower bounds) are kept apart."""
    kind = row.get("ref_kind")
    if kind == "upper_bound":
        return "G/|H| (lower bound)"
    if kind == "exact" or (kind is None and row.get("opt")):   # older CSVs have no ref_kind column
        return "G/OPT"
    return "no OPT"


def summarize(results: Path, by_instance: bool) -> None:
    with open(results / "runs.csv", newline="", encoding="utf-8") as fh:
        runs = list(csv.DictReader(fh))
    with open(results / "instances.csv", newline="", encoding="utf-8") as fh:
        insts = list(csv.DictReader(fh))

    run_groups = defaultdict(list)
    for r in runs:
        label = r["algo"] if r["algo"] != "greedy" else f"greedy[{r['rule']}]"
        run_groups[(group_of(r, by_instance), size_key(r, by_instance), basis_of(r), label)].append(r)
    run_rows = []
    for (g, n, basis, label), rows in sorted(run_groups.items()):
        ratios = [num(r["ratio"]) for r in rows]
        opt_flags = [num(r["optimal"]) for r in rows]
        times = [num(r["time_s"]) for r in rows]
        run_rows.append({
            "group": g, "n": size_label(n, rows), "basis": basis, "algo": label, "runs": len(rows),
            "instances": len({r["instance"] for r in rows}),
            "mean_ratio": mean(ratios), "max_ratio": mx(ratios),
            "min_compression_ratio": mn(num(r["compression_ratio"]) for r in rows),
            "optimal_rate": mean(opt_flags), "mean_time_s": mean(times), "max_time_s": mx(times),
        })

    tie_groups = defaultdict(list)
    for r in insts:
        tie_groups[(group_of(r, by_instance), size_key(r, by_instance), basis_of(r))].append(r)
    tie_rows = []
    for (g, n, basis), rows in sorted(tie_groups.items()):
        tie_rows.append({
            "group": g, "n": size_label(n, rows), "basis": basis, "instances": len(rows),
            "opt_methods": ",".join(sorted({r["opt_method"] for r in rows})),
            "tie_sensitive_frac": mean(num(r["tie_sensitive"]) for r in rows),
            "mean_random_distinct": mean(num(r["random_distinct"]) for r in rows),
            "mean_random_optimal_frac": mean(num(r["random_optimal_frac"]) for r in rows),
            "mean_tie_steps_first": mean(num(r["tie_steps_first"]) for r in rows),
            "mean_ratio_first": mean(num(r["ratio_first"]) for r in rows),
            "max_ratio_observed": mx(num(r["ratio_worst_observed"]) for r in rows),
            "max_ratio_explored": mx(num(r["ratio_worst_explored"]) for r in rows),
            "mean_g_over_reference": mean(num(r.get("g_first_over_reference")) for r in rows),
            "reconstructs_frac": mean(num(r.get("first_reconstructs_upper")) for r in rows),
            "misjoin_free_frac": mean(num(r.get("first_misjoin_free")) for r in rows),
        })

    # Prescribed (paper) execution vs fixed / random tie rules, per instance.
    paper_rows = []
    for r in insts:
        if num(r.get("greedy_paper")) is None:
            continue
        paper_rows.append({
            "instance": r["instance"], "n": int(r["n"]), "basis": basis_of(r), "ref": num(r["ref"]),
            "opt": num(r["opt"]), "opt_upper": num(r.get("opt_upper")), "greedy_paper": num(r["greedy_paper"]),
            "ratio_paper": num(r["ratio_paper"]), "ratio_first": num(r["ratio_first"]),
            "ratio_random_mean": num(r.get("ratio_random_mean")), "ratio_random_max": num(r.get("ratio_random_max")),
            # Did some random-tie run reach the paper's (bad) length?
            "random_hits_paper": int(r["ratio_random_max"] == r["ratio_paper"]) if r.get("ratio_random_max") else None,
        })

    for name, rows in (("summary_runs.csv", run_rows), ("summary_ties.csv", tie_rows),
                       ("summary_paper.csv", paper_rows)):
        if rows:
            with open(results / name, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, list(rows[0]))
                w.writeheader()
                w.writerows({k: f(v, 6) if isinstance(v, float) else v for k, v in row.items()} for row in rows)

    lines = [f"# Benchmark summary: `{results}`", "",
             f"{len(insts)} instances, {len(runs)} solver runs.", "",
             "## Solution quality and runtime", "",
             "Ratio basis `G/OPT` uses an exact optimum (DP or certificate).  `G/|H| (lower bound)` uses a "
             "known common superstring H >= OPT, so it is a certified lower bound on G/OPT; these rows are "
             "reported separately.", "",
             "| group | n | basis | algo | inst | mean ratio | max ratio | min compr. ratio | optimal rate | mean time (s) |",
             "|---|---:|---|---|---:|---:|---:|---:|---:|---:|"]
    for r in run_rows:
        lines.append(f"| {r['group']} | {r['n']} | {md(r['basis'])} | {r['algo']} | {r['instances']} | {f(r['mean_ratio'])} | "
                     f"{f(r['max_ratio'])} | {f(r['min_compression_ratio'])} | {f(r['optimal_rate'], 3)} | "
                     f"{f(r['mean_time_s'], 5)} |")
    lines += ["", "## Tie sensitivity", "",
              "| group | n | basis | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | "
              "mean tie steps | mean ratio (first) | max ratio observed | max ratio all ties |",
              "|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|"]
    for r in tie_rows:
        lines.append(f"| {r['group']} | {r['n']} | {md(r['basis'])} | {r['instances']} | {r['opt_methods']} | "
                     f"{f(r['tie_sensitive_frac'], 3)} | {f(r['mean_random_distinct'], 2)} | "
                     f"{f(r['mean_random_optimal_frac'], 3)} | {f(r['mean_tie_steps_first'], 1)} | "
                     f"{f(r['mean_ratio_first'])} | {f(r['max_ratio_observed'])} | {f(r['max_ratio_explored'])} |")
    asm_rows = [r for r in tie_rows if r["mean_g_over_reference"] is not None or r["reconstructs_frac"] is not None]
    if asm_rows:
        lines += ["", "## Assembly metrics (genome instances, rule `first`)", "",
                  "G / genome length is descriptive, not a bound.  *Reconstructs*: the output equals the "
                  "reference stretch H.  *Misjoin-free*: the output is a contiguous piece of H.  Both are computed "
                  "only for gapless error-free reads, where H is the true genome stretch.", "",
                  "| group | n | basis | inst | mean G/genome | reconstructs | misjoin-free | mean ratio (first) |",
                  "|---|---:|---|---:|---:|---:|---:|---:|"]
        for r in asm_rows:
            lines.append(f"| {r['group']} | {r['n']} | {md(r['basis'])} | {r['instances']} | "
                         f"{f(r['mean_g_over_reference'])} | {f(r['reconstructs_frac'], 3)} | "
                         f"{f(r['misjoin_free_frac'], 3)} | {f(r['mean_ratio_first'])} |")
    if paper_rows:
        lines += ["", "## Prescribed (paper) execution vs tie rules", "",
                  "| instance | n | basis | ref | OPT | \\|H\\| | G (paper) | ratio paper | ratio first | "
                  "ratio random mean | ratio random max | random reaches paper |",
                  "|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for r in sorted(paper_rows, key=lambda r: (r["basis"], r["instance"])):
            lines.append(f"| {r['instance']} | {r['n']} | {md(r['basis'])} | {f(r['ref'])} | {f(r['opt'])} | "
                         f"{f(r['opt_upper'])} | {f(r['greedy_paper'])} | {f(r['ratio_paper'])} | "
                         f"{f(r['ratio_first'])} | {f(r['ratio_random_mean'])} | {f(r['ratio_random_max'])} | "
                         f"{f(r['random_hits_paper'])} |")
    (results / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {results}/summary.md, summary_runs.csv, summary_ties.csv, summary_paper.csv")


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
