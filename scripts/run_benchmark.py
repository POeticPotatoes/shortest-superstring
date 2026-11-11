#!/usr/bin/env python3
"""Benchmark greedy against exact solutions (slide 12 measurements).

For each instance it records:

* **OPT**: from subset DP when ``n <= --dp-max-n``, else from a k-spectrum
  certificate, else from a value reported in the literature (``known.opt``).
  Ratios use the reference ``ref``: the exact OPT when one is available
  (``ref_kind=exact``).  Otherwise it is the length of a known common superstring
  (``known.opt_upper``, e.g. H of the 12/5 construction; ``ref_kind=upper_bound``),
  in which case the ratio is a certified *lower bound* G/|H| <= G/OPT.
  When both DP and a certificate exist, they are cross-checked.  Brute force
  cross-checks the DP when ``n <= --bf-check-max-n``.
* **Greedy** under each fixed tie rule (``--rules``), under the paper's
  execution (``paper``) for literature instances with ``tie_priority``, and
  under ``--random-ties`` seeded random tie rules.
* **All tie outcomes** (best and worst greedy) when ``n <= --explore-max-n``.
* G/OPT, compression ratio (L-G)/(L-OPT), optimality and runtime per run.

Outputs, under ``--out``:

``runs.csv``
    One row per solver run (long format).
``instances.csv``
    One row per instance (summary).
``meta.json``
    Arguments, environment and seeds, so the run can be repeated.

Examples::

    python scripts/run_benchmark.py data/synthetic --tier small --out results/small
    python scripts/run_benchmark.py data/literature --out results/literature --random-ties 100
    python scripts/run_benchmark.py data/synthetic --tier large --dp-max-n 0 --out results/large
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from pathlib import Path

import _common  # noqa: F401
from scs import ExplorationBudgetExceeded, Priority, brute_force_exact, dp_exact, greedy, greedy_outcomes, \
    is_superstring, kspectrum_certificate, overlap_graph, preprocess, total_length
from scs.generators import derive_seed
from scs.instance_io import environment_info, load_instances

RUN_FIELDS = ["instance", "family", "batch", "n", "L", "opt", "opt_method", "ref", "ref_kind", "algo", "rule",
              "tie_seed",
              "length", "time_s", "ratio", "compression_ratio", "optimal"]
INSTANCE_FIELDS = ["instance", "family", "batch", "path", "seed", "n_raw", "n", "L", "max_len", "alphabet",
                   "opt", "opt_method", "opt_upper", "ref", "ref_kind", "dp_time_s", "greedy_first", "greedy_min_observed", "greedy_max_observed",
                   "random_distinct", "random_optimal_frac", "explore_min", "explore_max", "explore_distinct",
                   "explore_states", "tie_steps_first", "ratio_first", "ratio_worst_observed", "ratio_worst_explored",
                   "tie_sensitive", "known_greedy_bad", "greedy_paper", "ratio_paper", "ratio_random_mean",
                   "ratio_random_max", "ratio_worst_vs_upper", "g_first_over_reference",
                   "first_reconstructs_upper", "first_misjoin_free"]


def timed(fn, repeats: int = 1):
    best, out = float("inf"), None
    for _ in range(max(1, repeats)):
        t0 = time.perf_counter()
        out = fn()
        best = min(best, time.perf_counter() - t0)
    return out, best


def ratio(g, opt):
    return None if not opt or g is None else g / opt


def compression_ratio(g, opt, L):
    if opt is None or g is None:
        return None
    return 1.0 if L == opt else (L - g) / (L - opt)


def tier_of(inst: dict) -> str | None:
    batch = inst.get("batch") or ""
    return batch.split("@", 1)[1].split("/", 1)[0] if "@" in batch else None


def benchmark_instance(inst: dict, args) -> tuple[list[dict], dict]:
    S = inst["strings"]
    reduced = preprocess(S)
    n, L = len(reduced), total_length(reduced)
    iid = inst.get("id") or Path(inst["path"]).stem
    base = {"instance": iid, "family": inst.get("family"), "batch": inst.get("batch") or "", "n": n, "L": L}
    runs: list[dict] = []
    summary = {**base, "path": inst.get("path"), "seed": inst.get("seed"), "n_raw": len(S),
               "max_len": max(map(len, reduced), default=0), "alphabet": len(set("".join(reduced))),
               "known_greedy_bad": (inst.get("known") or {}).get("greedy_bad")}

    # ---- OPT
    opt, method, dp_time = None, "none", None
    if n <= args.dp_max_n:
        res, dp_time = timed(lambda: dp_exact(reduced, preprocess=False, max_n=args.dp_max_n))
        if not is_superstring(res.superstring, reduced):
            raise AssertionError(f"{iid}: DP output is not a superstring")
        opt, method = res.length, "dp"
        runs.append({**base, "algo": "dp", "rule": "", "tie_seed": "", "length": res.length, "time_s": dp_time})
        if n <= args.bf_check_max_n:
            bf, bf_time = timed(lambda: brute_force_exact(reduced, preprocess=False))
            if bf.length != opt:
                raise AssertionError(f"{iid}: DP {opt} != brute force {bf.length}")
            runs.append({**base, "algo": "bruteforce", "rule": "", "tie_seed": "", "length": bf.length,
                         "time_s": bf_time})
    cert, cert_time = timed(lambda: kspectrum_certificate(reduced))
    if cert is not None:
        if opt is not None and opt != len(cert):
            raise AssertionError(f"{iid}: DP {opt} != certificate {len(cert)}")
        if opt is None:
            opt, method = len(cert), "certificate"
        runs.append({**base, "algo": "certificate", "rule": "", "tie_seed": "", "length": len(cert),
                     "time_s": cert_time})
    known = inst.get("known") or {}
    if opt is None and known.get("opt") is not None:
        opt, method = known["opt"], "known"
    # A known common superstring (e.g. H in the 12/5 construction) bounds OPT from above,
    # so G/|H| <= G/OPT is a certified *lower* bound on the ratio.  Such ratios are
    # tagged ref_kind=upper_bound and never mixed with exact ratios.
    upper = known.get("opt_upper")
    if inst.get("upper_superstring") is not None:
        if not is_superstring(inst["upper_superstring"], reduced):
            raise AssertionError(f"{iid}: stored upper_superstring is not a superstring")
        upper = len(inst["upper_superstring"]) if upper is None else upper
    if opt is not None and upper is not None and upper < opt:
        raise AssertionError(f"{iid}: upper bound {upper} < OPT {opt}")
    ref, ref_kind = (opt, "exact") if opt is not None else (upper, "upper_bound" if upper is not None else "")
    summary.update(opt=opt, opt_method=method, dp_time_s=dp_time, opt_upper=upper, ref=ref, ref_kind=ref_kind)
    base.update(opt=opt, opt_method=method, ref=ref, ref_kind=ref_kind)
    for r in runs:
        r.update(opt=opt, opt_method=method, ref=ref, ref_kind=ref_kind)

    # ---- greedy runs (time_s excludes the shared overlap-graph build, recorded as algo=overlap_graph)
    graph, graph_time = timed(lambda: overlap_graph(reduced))
    runs.append({**base, "algo": "overlap_graph", "rule": "", "tie_seed": "", "length": "", "time_s": graph_time})

    def run_greedy(rule_name, tie, tie_seed=""):
        res, t = timed(lambda: greedy(reduced, tie, preprocess=False, graph=graph), args.timing_repeats)
        if not is_superstring(res.superstring, reduced):
            raise AssertionError(f"{iid}: greedy({rule_name}) output is not a superstring")
        runs.append({**base, "algo": "greedy", "rule": rule_name, "tie_seed": tie_seed, "length": res.length,
                     "time_s": t})
        return res

    lengths = []
    first = None
    first_sup = None
    for rule in args.rules:
        res = run_greedy(rule, rule)
        first_sup = first_sup if first_sup is not None else res.superstring
        lengths.append(res.length)
        first = first if first is not None else res.length
    paper_len = None
    if inst.get("tie_priority"):
        paper_len = run_greedy("paper", Priority(inst["tie_priority"])).length
        lengths.append(paper_len)
    rand_lengths = []
    for r in range(args.random_ties):
        seed = derive_seed(args.tie_seed, iid, r)
        rand_lengths.append(run_greedy("random", f"random:{seed}", seed).length)
    lengths += rand_lengths

    if n <= args.trace_max_n and args.rules:
        traced = greedy(reduced, args.rules[0], preprocess=False, trace=True, graph=graph)
        summary["tie_steps_first"] = traced.tie_steps

    # ---- all tie outcomes
    if n <= args.explore_max_n:
        try:
            ex, t = timed(lambda: greedy_outcomes(reduced, preprocess=False, max_states=args.explore_max_states))
            summary.update(explore_min=ex.min_length, explore_max=ex.max_length,
                           explore_distinct=len(ex.lengths), explore_states=ex.states,
                           ratio_worst_explored=ratio(ex.max_length, ref))
            for algo, length in (("greedy_best_tie", ex.min_length), ("greedy_worst_tie", ex.max_length)):
                runs.append({**base, "algo": algo, "rule": "explore", "tie_seed": "", "length": length, "time_s": t})
        except ExplorationBudgetExceeded:
            summary["explore_states"] = f">{args.explore_max_states}"

    for r in runs:
        if not isinstance(r["length"], int):
            continue
        r["ratio"] = ratio(r["length"], ref)
        r["compression_ratio"] = compression_ratio(r["length"], opt, L)
        r["optimal"] = None if opt is None else int(r["length"] == opt)

    summary.update(
        greedy_first=first,
        greedy_min_observed=min(lengths) if lengths else None,
        greedy_max_observed=max(lengths) if lengths else None,
        random_distinct=len(set(rand_lengths)) if rand_lengths else None,
        random_optimal_frac=(sum(x == opt for x in rand_lengths) / len(rand_lengths)) if rand_lengths and opt else None,
        ratio_first=ratio(first, ref),
        ratio_worst_observed=ratio(max(lengths), ref) if lengths else None,
        ratio_paper=ratio(paper_len, ref),
        ratio_random_mean=ratio(sum(rand_lengths) / len(rand_lengths), ref) if rand_lengths else None,
        ratio_random_max=ratio(max(rand_lengths), ref) if rand_lengths else None,
        greedy_paper=paper_len,
        ratio_worst_vs_upper=ratio(max(lengths), upper) if lengths else None,
    )
    # Assembly-style metrics (genome instances): G / genome length is descriptive only.  For gapless
    # error-free reads the stored superstring is the true genome stretch.  "Misjoin-free" then means the
    # greedy output is a contiguous piece of it, and "reconstructs" means it equals it exactly.
    if inst.get("reference_length") and first is not None:
        summary["g_first_over_reference"] = first / inst["reference_length"]
    if inst.get("gapless") and inst.get("upper_superstring") is not None and first_sup is not None:
        circle = inst.get("circular_reference")
        if circle:
            # A circular genome has no start, so the output may be any rotation.  Compare with the circle.
            misjoin_free = first_sup in circle * 3
            summary["first_reconstructs_upper"] = int(misjoin_free and len(first_sup) >= len(circle))
        else:
            misjoin_free = first_sup in inst["upper_superstring"]
            summary["first_reconstructs_upper"] = int(first_sup == inst["upper_superstring"])
        summary["first_misjoin_free"] = int(misjoin_free)
    lo = min([x for x in (summary["greedy_min_observed"], summary.get("explore_min")) if x is not None], default=None)
    hi = max([x for x in (summary["greedy_max_observed"], summary.get("explore_max")) if x is not None], default=None)
    summary["tie_sensitive"] = None if lo is None else int(lo != hi)
    return runs, summary


def fmt(v):
    return f"{v:.6g}" if isinstance(v, float) else ("" if v is None else v)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", help="instance files or directories")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--tier", action="append", help="only batches of this generation tier (tiny/small/large)")
    ap.add_argument("--family", action="append", help="only instances of this family")
    ap.add_argument("--max-n", type=int, help="skip instances with more strings after preprocessing")
    ap.add_argument("--limit", type=int, help="stop after this many instances")
    ap.add_argument("--rules", default="first,last,lex,revlex",
                    help="comma-separated fixed tie rules (see scs.tiebreak); empty for none")
    ap.add_argument("--random-ties", type=int, default=20, help="random-tie greedy runs per instance")
    ap.add_argument("--tie-seed", type=int, default=0, help="base seed for random tie runs")
    ap.add_argument("--dp-max-n", type=int, default=16, help="run subset DP up to this n")
    ap.add_argument("--bf-check-max-n", type=int, default=7, help="cross-check DP by brute force up to this n")
    ap.add_argument("--explore-max-n", type=int, default=10, help="enumerate all tie outcomes up to this n")
    ap.add_argument("--explore-max-states", type=int, default=50_000)
    ap.add_argument("--trace-max-n", type=int, default=300, help="count tie steps of the first rule up to this n")
    ap.add_argument("--timing-repeats", type=int, default=1, help="repeat greedy timings, keep the best")
    args = ap.parse_args(argv)
    args.rules = [r for r in args.rules.split(",") if r]

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    meta = {**environment_info(), "args": vars(args), "random_tie_seed_scheme": "derive_seed(tie_seed, instance_id, r)"}
    t_start = time.perf_counter()
    count = 0
    with open(out / "runs.csv", "w", newline="", encoding="utf-8") as fr, \
            open(out / "instances.csv", "w", newline="", encoding="utf-8") as fi:
        wr = csv.DictWriter(fr, RUN_FIELDS, extrasaction="ignore")
        wi = csv.DictWriter(fi, INSTANCE_FIELDS, extrasaction="ignore")
        wr.writeheader()
        wi.writeheader()
        for inst in load_instances(*args.inputs):
            if args.tier and tier_of(inst) not in args.tier:
                continue
            if args.family and inst.get("family") not in args.family:
                continue
            if args.max_n is not None and len(preprocess(inst["strings"])) > args.max_n:
                continue
            t0 = time.perf_counter()
            runs, summary = benchmark_instance(inst, args)
            wr.writerows({k: fmt(v) for k, v in r.items()} for r in runs)
            wi.writerow({k: fmt(v) for k, v in summary.items()})
            fr.flush()
            fi.flush()
            count += 1
            print(f"[{count}] {summary['instance']}: n={summary['n']} OPT={summary['opt']} ({summary['opt_method']}) "
                  f"G_first={summary['greedy_first']} G_range=[{summary['greedy_min_observed']},"
                  f"{summary['greedy_max_observed']}] {time.perf_counter() - t0:.2f}s", file=sys.stderr)
            if args.limit and count >= args.limit:
                break
    meta.update(instances=count, elapsed_s=time.perf_counter() - t_start)
    (out / "meta.json").write_text(json.dumps(meta, indent=1) + "\n", encoding="utf-8")
    print(f"{count} instances -> {out}/runs.csv, instances.csv, meta.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
