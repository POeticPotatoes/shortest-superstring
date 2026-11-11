#!/usr/bin/env python3
"""Build SCS instances from real sequencing data (run ``fetch_real_data.py`` first).

Writes batches to ``data/real/instances/<variant>/<tier>_<param>.json`` and a
``manifest.json`` with every seed.  Each instance seed is
``derive_seed(master_seed, variant, tier, param, index)``.  Variants:

``phix_err098007_exact``
    Real Illumina reads (ENA ERR098007) that occur *exactly* in the phiX174
    genome (NC_001422.1, circular), with reverse-strand reads flipped to the
    forward strand.  This is a reference-guided filter (about 50% of reads pass).
    The covered stretch of the genome is stored as ``upper_superstring`` (>= OPT).
``phix_err098007_raw``
    Real reads as sequenced, after dropping reads with ``N``: both strands, with
    sequencing errors.  Here no reference bound on OPT exists, so ratios are only
    available where subset DP runs.  ``g_over_reference`` (G / genome length) is
    descriptive only.
``sim_<genome>_errfree``
    Error-free forward-strand reads simulated from the phiX174, SARS-CoV-2 and lambda
    reference genomes.  The covered stretch of the genome is ``upper_superstring``.
``sim_phix_err1pct``
    Simulated phiX174 reads with 1% substitution errors (no reference bound).

Tiers: ``small`` (n = 6..16 reads from one genome window, so exact DP applies)
and ``large`` (whole genome at a given coverage; greedy only, with G/|H| from the
reference stretch where it is a valid superstring).

    python scripts/generate_real_instances.py [--count 20] [--master-seed 20261111]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import _common  # noqa: F401
from scs.core import is_superstring, preprocess, total_length
from scs.generators import derive_seed
from scs.instance_io import environment_info, save_batch
from scs.realdata import orient_exact_reads, read_fasta, read_fastq, simulate_reads, window_subset

ROOT = _common.ROOT
REAL = ROOT / "data" / "real"
SMALL_SIZES = [6, 8, 10, 12, 14, 16]
SIM_GENOMES = {"phix": "NC_001422.1", "sars2": "NC_045512.2", "lambda": "NC_001416.1"}
SIM_LARGE = {  # genome -> list of (read_length, coverage, replicates)
    "phix": [(100, 5, 2), (100, 10, 2), (100, 20, 2), (100, 50, 1), (50, 10, 2)],
    "sars2": [(100, 5, 2), (100, 10, 2)],
    "lambda": [(100, 5, 1), (100, 10, 1)],
}


def load_sources() -> dict:
    path = REAL / "sources.json"
    if not path.exists():
        raise SystemExit("data/real/sources.json missing: run scripts/fetch_real_data.py first")
    return json.loads(path.read_text())


def genome_of(sources: dict, acc: str) -> tuple[str, dict]:
    info = sources["genomes"][acc]
    (_, seq), = read_fasta(ROOT / info["path"])
    return seq, info


def finish(inst: dict, variant: str, idx: int, upper: str | None) -> dict:
    # Identical reads are dropped (preprocessing would remove them anyway); keep the first start of each.
    S, starts = [], []
    seen = set()
    for j, r in enumerate(inst["strings"]):
        if r not in seen:
            seen.add(r)
            S.append(r)
            if "starts" in inst:
                starts.append(inst["starts"][j])
    inst["duplicates_removed"] = len(inst["strings"]) - len(S)
    inst["strings"] = S
    if "starts" in inst:
        inst["starts"] = starts
    reduced = preprocess(S)
    inst.update(id=f"real_{variant}_{inst['tier']}_{inst['param']}_{idx:03d}", index=idx, family="real",
                n_reduced=len(reduced), total_length=total_length(reduced))
    if inst["tier"] != "large":
        inst.pop("reference_length", None)  # G / genome length only makes sense for whole-genome instances
        inst.pop("circular_reference", None)
    if upper is not None and inst.get("starts"):
        # Gapless: sorted by position, every read overlaps the furthest end so far.  Only then is the
        # genome stretch a sensible "true assembly" to compare greedy's output with.
        spans = sorted((st, st + len(r)) for st, r in zip(inst["starts"], S))
        end, gapless = spans[0][1], True
        for a, b in spans[1:]:
            if a >= end:
                gapless = False
                break
            end = max(end, b)
        inst["gapless"] = gapless
    if upper is not None:
        assert is_superstring(upper, reduced), inst["id"]
        inst["upper_superstring"] = upper
        inst["known"] = {"opt": None, "greedy_bad": None, "opt_upper": len(upper)}
    return inst


class Writer:
    def __init__(self, out: Path, master_seed: int):
        self.out, self.master_seed = out, master_seed
        self.manifest: dict = {"batches": {}}

    def batch(self, variant: str, tier: str, param: str, params: dict, instances: list[dict], source: dict):
        rel = Path(variant) / f"{tier}_{param}.json"
        save_batch(self.out / rel, name=f"real/{variant}@{tier}/{param}", family="real", params=params,
                   master_seed=self.master_seed, instances=instances,
                   extra={"tier": tier, "variant": f"real/{variant}", "source": source,
                          "seed_scheme": "derive_seed(master_seed, variant, tier, param, index)"})
        self.manifest["batches"][str(rel)] = {"variant": variant, "tier": tier, "param": param, "params": params,
                                              "count": len(instances), "seeds": [i["seed"] for i in instances]}
        print(f"  wrote {rel} ({len(instances)} instances, n_reduced "
              f"{min(i['n_reduced'] for i in instances)}..{max(i['n_reduced'] for i in instances)})")

    def seed(self, *parts) -> int:
        return derive_seed(self.master_seed, *parts)


def real_read_variants(w: Writer, sources: dict, count: int) -> None:
    run = sources["reads"]["ERR098007"]
    genome, ginfo = genome_of(sources, run["reference"])
    reads = [s for _, s in read_fastq(ROOT / run["path"])]
    src = {"run": "ERR098007", "study": run["study_accession"], "fastq_md5": run["fastq_md5"],
           "instrument": run["instrument_model"], "reference": run["reference"], "circular": ginfo["circular"]}
    ex = orient_exact_reads(reads, genome, ginfo["circular"])
    print(f"ERR098007: {ex['stats']}")
    src_exact = {**src, "filter": "exact match to reference, reverse-strand reads flipped", "stats": ex["stats"]}
    text = ex["text"]

    v = "phix_err098007_exact"
    for n in SMALL_SIZES:
        insts = []
        for idx in range(count):
            seed = w.seed(v, "small", n, idx)
            sub = window_subset(ex["reads"], ex["starts"], text, n, window=4 * 76, seed=seed)
            insts.append(finish({"tier": "small", "param": f"n{n:02d}", "seed": seed, "strings": sub["reads"],
                                 "starts": sub["starts"], "reference": run["reference"],
                                 "reference_length": len(genome)}, v, idx, sub["covered"]))
        w.batch(v, "small", f"n{n:02d}", {"n": n, "window": 4 * 76}, insts, src_exact)
    import random
    for cov in (5, 10, 20, 50, "all"):
        reps = 1 if cov == "all" else 3
        insts = []
        for idx in range(reps):
            seed = w.seed(v, "large", cov, idx)
            if cov == "all":
                chosen = list(range(len(ex["reads"])))
            else:
                k = min(len(ex["reads"]), round(cov * len(genome) / 76))
                chosen = sorted(random.Random(seed).sample(range(len(ex["reads"])), k))
            S = [ex["reads"][i] for i in chosen]
            st = [ex["starts"][i] for i in chosen]
            lo, hi = min(st), max(s + len(r) for s, r in zip(st, S))
            insts.append(finish({"tier": "large", "param": f"cov{cov}", "seed": seed, "strings": S, "starts": st,
                                 "reference": run["reference"], "reference_length": len(genome),
                                 "circular_reference": genome}, v, idx, text[lo:hi]))
        w.batch(v, "large", f"cov{cov}", {"coverage": cov, "read_length": 76}, insts, src_exact)

    v = "phix_err098007_raw"
    clean = [r for r in reads if not r.strip("ACGT")]
    src_raw = {**src, "filter": "reads containing N removed; both strands; sequencing errors kept",
               "reads_after_filter": len(clean)}
    for n in (500, 1000, 2000):
        insts = []
        for idx in range(3):
            seed = w.seed(v, "large", n, idx)
            S = random.Random(seed).sample(clean, n)
            insts.append(finish({"tier": "large", "param": f"n{n}", "seed": seed, "strings": S,
                                 "reference": run["reference"], "reference_length": len(genome)}, v, idx, None))
        w.batch(v, "large", f"n{n}", {"n": n}, insts, src_raw)


def simulated_variants(w: Writer, sources: dict, count: int) -> None:
    for gname, acc in SIM_GENOMES.items():
        genome, ginfo = genome_of(sources, acc)
        circ = ginfo["circular"]
        src = {"reference": acc, "title": ginfo["title"], "circular": circ, "strand": "forward only",
               "errors": "none"}
        v = f"sim_{gname}_errfree"
        for n in SMALL_SIZES:
            insts = []
            for idx in range(count):
                seed = w.seed(v, "small", n, idx)
                pool = simulate_reads(genome, read_length=100, coverage=30, circular=circ, seed=seed)
                text = genome + genome[:99] if circ else genome
                sub = window_subset(pool["reads"], pool["starts"], text, n, window=400, seed=seed + 1)
                insts.append(finish({"tier": "small", "param": f"n{n:02d}", "seed": seed, "strings": sub["reads"],
                                     "starts": sub["starts"], "reference": acc, "reference_length": len(genome)},
                                    v, idx, sub["covered"]))
            w.batch(v, "small", f"n{n:02d}", {"n": n, "read_length": 100, "window": 400}, insts, src)
        for read_len, cov, reps in SIM_LARGE[gname]:
            insts = []
            param = f"len{read_len}_cov{cov}"
            for idx in range(reps):
                seed = w.seed(v, "large", param, idx)
                sim = simulate_reads(genome, read_length=read_len, coverage=cov, circular=circ, seed=seed)
                extra = {"circular_reference": genome} if circ else {}
                insts.append(finish({"tier": "large", "param": param, "seed": seed, "strings": sim["reads"],
                                     "starts": sim["starts"], "reference": acc, "reference_length": len(genome),
                                     **extra}, v, idx, sim["covered"]))
            w.batch(v, "large", param, {"read_length": read_len, "coverage": cov}, insts, src)

    genome, ginfo = genome_of(sources, "NC_001422.1")
    v = "sim_phix_err1pct"
    src = {"reference": "NC_001422.1", "circular": True, "strand": "forward only", "errors": "1% substitutions"}
    for n in SMALL_SIZES:
        insts = []
        for idx in range(count):
            seed = w.seed(v, "small", n, idx)
            pool = simulate_reads(genome, read_length=100, coverage=30, circular=True, error_rate=0.01, seed=seed)
            text = genome + genome[:99]
            sub = window_subset(pool["reads"], pool["starts"], text, n, window=400, seed=seed + 1)
            insts.append(finish({"tier": "small", "param": f"n{n:02d}", "seed": seed, "strings": sub["reads"],
                                 "starts": sub["starts"], "reference": "NC_001422.1",
                                 "reference_length": len(genome)}, v, idx, None))
        w.batch(v, "small", f"n{n:02d}", {"n": n, "read_length": 100, "window": 400, "error_rate": 0.01}, insts, src)
    insts = []
    for idx in range(2):
        seed = w.seed(v, "large", "len100_cov10", idx)
        sim = simulate_reads(genome, read_length=100, coverage=10, circular=True, error_rate=0.01, seed=seed)
        insts.append(finish({"tier": "large", "param": "len100_cov10", "seed": seed, "strings": sim["reads"],
                             "starts": sim["starts"], "reference": "NC_001422.1", "reference_length": len(genome)},
                            v, idx, None))
    w.batch(v, "large", "len100_cov10", {"read_length": 100, "coverage": 10, "error_rate": 0.01}, insts, src)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(REAL / "instances"))
    ap.add_argument("--count", type=int, default=20, help="instances per small-tier size")
    ap.add_argument("--master-seed", type=int, default=20261111)
    ap.add_argument("--skip-reads", action="store_true", help="only simulated variants (no ERR098007 needed)")
    args = ap.parse_args(argv)

    sources = load_sources()
    w = Writer(Path(args.out), args.master_seed)
    if not args.skip_reads:
        real_read_variants(w, sources, args.count)
    simulated_variants(w, sources, args.count)
    w.manifest.update(environment_info(), sources={k: {a: {kk: vv for kk, vv in info.items() if kk in
                                                           ("accession", "run_accession", "sha256", "fastq_md5",
                                                            "url", "length", "read_count")}
                                                       for a, info in sources[k].items()}
                                                   for k in ("genomes", "reads")})
    (Path(args.out) / "manifest.json").write_text(json.dumps(w.manifest, indent=1) + "\n", encoding="utf-8")
    print(f"manifest: {Path(args.out) / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
