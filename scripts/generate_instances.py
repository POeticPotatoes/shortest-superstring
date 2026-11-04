#!/usr/bin/env python3
"""Generate the synthetic benchmark instances.

Writes one batch file per (variant, n) to
``<out>/<family>/<variant>/n<NNNN>.json`` plus ``<out>/manifest.json``, which
lists every batch with its parameters, master seed and per-instance seeds.
Each instance seed is ``derive_seed(master_seed, variant, n, index)``, so
any single instance can be regenerated with ``scs.generators.generate``.

Examples::

    python scripts/generate_instances.py                      # default: small + large tiers
    python scripts/generate_instances.py --tier small --count 50 --master-seed 7
    python scripts/generate_instances.py --tier tiny --out data/synthetic_tiny
    python scripts/generate_instances.py --list               # show variants
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import _common  # noqa: F401
from scs.core import preprocess, total_length
from scs.generators import derive_seed, generate
from scs.instance_io import environment_info, save_batch

DEFAULT_MASTER_SEED = 20261105

# variant name -> (family, function n -> generator params)
SMALL_VARIANTS = {
    "random/dna_l5-12":      ("random", lambda n: {"length": (5, 12), "alphabet": "ACGT"}),
    "random/bin_l4-8":       ("random", lambda n: {"length": (4, 8), "alphabet": "AB"}),
    "sampled/dna_src4n":     ("sampled", lambda n: {"source_length": max(4 * n, 40), "fragment_length": (8, 15), "alphabet": "ACGT"}),
    "sampled/bin_src3n":     ("sampled", lambda n: {"source_length": max(3 * n, 30), "fragment_length": (6, 12), "alphabet": "AB"}),
    "repetitive/periodic":   ("repetitive", lambda n: {"mode": "periodic", "motif_length": (2, 4), "mutation_rate": 0.08,
                                                         "fragment_length": (8, 14), "source_length": 8 * n, "alphabet": "ACGT"}),
    "repetitive/cyclic_k6":  ("repetitive", lambda n: {"mode": "cyclic", "k": 6, "alphabet": "AB"}),
    "repetitive/kmer_k8":    ("repetitive", lambda n: {"mode": "kmer", "k": 8, "motif_length": (3, 5), "mutation_rate": 0.1,
                                                         "alphabet": "ACGT"}),
}

LARGE_VARIANTS = {
    "random/dna_l8-15":      ("random", lambda n: {"length": (8, 15), "alphabet": "ACGT"}),
    "random/bin_l10-16":     ("random", lambda n: {"length": (10, 16), "alphabet": "AB"}),
    "sampled/dna_src4n":     ("sampled", lambda n: {"source_length": 4 * n, "fragment_length": (12, 25), "alphabet": "ACGT"}),
    "repetitive/periodic":   ("repetitive", lambda n: {"mode": "periodic", "motif_length": (2, 4), "mutation_rate": 0.08,
                                                         "fragment_length": (12, 24), "source_length": 8 * n, "alphabet": "ACGT"}),
    "repetitive/cyclic_k8":  ("repetitive", lambda n: {"mode": "cyclic", "k": 8, "alphabet": "ABC"}),
    "repetitive/kmer_k10":   ("repetitive", lambda n: {"mode": "kmer", "k": 10, "motif_length": (3, 6), "mutation_rate": 0.1,
                                                         "alphabet": "ACGT"}),
}

TIERS = {
    # name: (variants, sizes, default count)
    "tiny":  (SMALL_VARIANTS, [3, 4, 5, 6, 7, 8], 30),
    "small": (SMALL_VARIANTS, [4, 6, 8, 10, 12, 14, 16], 20),
    "large": (LARGE_VARIANTS, [50, 100, 200, 500, 1000, 2000], 5),
}


def generate_batch(variant: str, family: str, params: dict, n: int, count: int, master_seed: int) -> list[dict]:
    instances = []
    for idx in range(count):
        seed = derive_seed(master_seed, variant, n, idx)
        inst = generate(family, seed, n=n, **params)
        reduced = preprocess(inst["strings"])
        inst.update(id=f"{variant.replace('/', '_')}_n{n:04d}_{idx:03d}", index=idx,
                    n_reduced=len(reduced), total_length=total_length(reduced))
        instances.append(inst)
    return instances


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="data/synthetic", help="output directory (default: data/synthetic)")
    ap.add_argument("--tier", action="append", choices=sorted(TIERS),
                    help="tier(s) to generate (default: small and large)")
    ap.add_argument("--variants", help="comma-separated subset of variant names")
    ap.add_argument("--sizes", help="comma-separated n values overriding the tier sizes")
    ap.add_argument("--count", type=int, help="instances per (variant, n) overriding the tier default")
    ap.add_argument("--master-seed", type=int, default=DEFAULT_MASTER_SEED)
    ap.add_argument("--list", action="store_true", help="list variants and exit")
    args = ap.parse_args(argv)

    if args.list:
        for tier, (variants, sizes, count) in TIERS.items():
            print(f"[{tier}] sizes={sizes} count={count}")
            for name, (family, fn) in variants.items():
                print(f"  {name:24s} {family:10s} {fn(10)}")
        return 0

    out = Path(args.out)
    tiers = args.tier or ["small", "large"]
    manifest_path = out / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"batches": {}}
    wanted = set(args.variants.split(",")) if args.variants else None

    for tier in tiers:
        variants, sizes, count = TIERS[tier]
        sizes = [int(x) for x in args.sizes.split(",")] if args.sizes else sizes
        count = args.count or count
        for variant, (family, param_fn) in variants.items():
            if wanted and variant not in wanted:
                continue
            for n in sizes:
                params = param_fn(n)
                t0 = time.perf_counter()
                try:
                    instances = generate_batch(variant, family, params, n, count, args.master_seed)
                except ValueError as e:
                    print(f"  skip {variant} n={n}: {e}", file=sys.stderr)
                    continue
                rel = Path(family) / variant.split("/", 1)[1] / f"{tier}_n{n:04d}.json"
                save_batch(out / rel, name=f"{variant}@{tier}/n={n}", family=family, params={**params, "n": n},
                           master_seed=args.master_seed, instances=instances,
                           extra={"tier": tier, "variant": variant,
                                  "seed_scheme": "derive_seed(master_seed, variant, n, index)"})
                manifest["batches"][str(rel)] = {
                    "tier": tier, "variant": variant, "family": family, "n": n, "count": count,
                    "params": params, "master_seed": args.master_seed,
                    "seeds": [i["seed"] for i in instances],
                }
                print(f"  wrote {rel} ({count} instances, {time.perf_counter() - t0:.2f}s)")

    manifest.update(environment_info())
    manifest["generator_script"] = "scripts/generate_instances.py"
    out.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
