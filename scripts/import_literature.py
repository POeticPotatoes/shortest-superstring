#!/usr/bin/env python3
"""Write the literature / slide instances to ``data/literature`` and verify them.

The instances are transcribed in :mod:`scs.constructions` from the papers
cited there.  For each one this script checks:

* the reported OPT, using a k-spectrum certificate or subset DP when ``n`` is
  small enough,
* for constructions that only give a common superstring H (the 12/5 family),
  that H contains every input, that its length matches the paper's formula, and,
  when DP is feasible, how far |H| is from the true OPT,
* that replaying the paper's greedy execution (``tie_priority``) through our
  greedy, which only takes maximum-overlap merges, gives the reported length,
* the full range of greedy outcomes over all tie choices, for small ``n``.

Each JSON file records the results under ``verified``.

    python scripts/import_literature.py [--out data/literature] [--explore-max-n 12]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import _common  # noqa: F401
from scs import ExplorationBudgetExceeded, Priority, dp_exact, greedy, greedy_outcomes, is_superstring, \
    kspectrum_certificate, preprocess, total_length
from scs.constructions import literature_instances
from scs.instance_io import environment_info, save_instance


def verify(inst: dict, dp_max_n: int, explore_max_n: int) -> dict:
    S = inst["strings"]
    reduced = preprocess(S)
    out: dict = {"n": len(reduced), "total_length": total_length(reduced)}
    cert = kspectrum_certificate(S)
    if cert is not None:
        out.update(opt=len(cert), opt_method="certificate", opt_superstring=cert)
    elif len(reduced) <= dp_max_n:
        r = dp_exact(S)
        out.update(opt=r.length, opt_method="dp", opt_superstring=r.superstring)
    known = inst["known"]
    if known.get("opt") is not None and out.get("opt") is not None:
        out["opt_matches_reported"] = known["opt"] == out["opt"]
    if inst.get("upper_superstring") is not None:
        H = inst["upper_superstring"]
        out["upper_is_superstring"] = is_superstring(H, reduced)
        out["upper_matches_reported"] = len(H) == known.get("opt_upper")
        if out.get("opt") is not None:
            out["upper_minus_opt"] = len(H) - out["opt"]
    if inst["tie_priority"]:
        g = greedy(S, Priority(inst["tie_priority"]))
        out.update(greedy_paper=g.length, greedy_paper_superstring=g.superstring)
        if known.get("greedy_bad") is not None:
            out["greedy_matches_reported"] = g.length == known["greedy_bad"]
    out["greedy_first"] = greedy(S, "first").length
    if len(reduced) <= explore_max_n:
        try:
            ex = greedy_outcomes(S, max_states=200_000)
            out.update(greedy_all_lengths=ex.lengths, greedy_states=ex.states,
                       greedy_worst_superstring=ex.max_superstring)
        except ExplorationBudgetExceeded:
            out["greedy_all_lengths"] = "budget exceeded"
    return out


MAX_STORED_SUPERSTRING = 10_000  # longer verification superstrings are dropped to keep data/ small


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="data/literature")
    ap.add_argument("--dp-max-n", type=int, default=20, help="DP for instances without a certificate (n=20 ~ 8 s)")
    ap.add_argument("--explore-max-n", type=int, default=12)
    args = ap.parse_args(argv)

    out = Path(args.out)
    index = []
    ok = True
    for inst in literature_instances():
        v = verify(inst, args.dp_max_n, args.explore_max_n)
        for key in [k for k, x in v.items() if isinstance(x, str) and len(x) > MAX_STORED_SUPERSTRING]:
            v[key] = f"<omitted: {len(v[key])} chars; regenerate with scs.constructions>"
        inst["verified"] = v
        save_instance(out / f"{inst['id']}.json", inst)
        good = all(v.get(k, True) for k in ("opt_matches_reported", "greedy_matches_reported",
                                             "upper_is_superstring", "upper_matches_reported"))
        ok &= good
        ref = v.get("opt") or inst["known"].get("opt_upper")
        basis = "G/OPT" if v.get("opt") else ("G/|H|" if ref else None)
        ratio = (v.get("greedy_paper") or v["greedy_first"]) / ref if ref else None
        index.append({"id": inst["id"], "n": v["n"], "opt": v.get("opt"), "opt_method": v.get("opt_method"),
                      "greedy_bad": inst["known"].get("greedy_bad"), "greedy_paper": v.get("greedy_paper"),
                      "opt_upper": inst["known"].get("opt_upper"), "greedy_first": v["greedy_first"],
                      "ratio_bad": ratio, "ratio_basis": basis, "verified": good,
                      "citation": inst["citation"]})
        print(f"{'OK ' if good else 'BAD'} {inst['id']:26s} n={v['n']:5d} OPT={v.get('opt')!s:>5} "
              f"greedy(paper)={v.get('greedy_paper')!s:>5} greedy(first)={v['greedy_first']:5d} "
              f"{basis or 'ratio'}={ratio if ratio is None else round(ratio, 4)}")
    (out / "index.json").write_text(json.dumps({**environment_info(), "instances": index}, indent=1,
                                               ensure_ascii=False) + "\n", encoding="utf-8")
    print("all reported values reproduced" if ok else "SOME REPORTED VALUES WERE NOT REPRODUCED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
