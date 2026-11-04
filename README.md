# Shortest Superstring: How Good Is Greedy?

Implementation for the project proposal (`Shortest-Superstring-Research-Proposal.pptx`).
It contains the maximum-overlap greedy algorithm with configurable tie-breaking,
an exact subset-DP solver, synthetic instance generators, instances
transcribed from the literature, and benchmarking scripts. Pure Python 3.10+,
no dependencies.

```python
from scs import greedy, dp_exact, greedy_outcomes, Priority

S = ["AABA", "ABAA", "BAB"]                 # slide 5
greedy(S).superstring                       # 'AABAABAB'  (8)
dp_exact(S).superstring                     # 'BABAABA'   (7, optimal)
greedy(S, "lex").length                     # tie rules: first|last|lex|revlex|random:<seed>|short-frag|long-frag
greedy(S, lambda cands, state: max(cands))  # or any function choosing among tied (u, v) edges
greedy_outcomes(S).lengths                  # every length reachable by some tie choice -> [8]
```

## Quick start

```bash
python3 -m unittest discover -s tests -t .      # tests (~2 s)
python3 scripts/demo.py                          # tour: slides, tie rules, Chukhin et al., Shibata

# data (already generated in data/; rerun to regenerate identically)
python3 scripts/generate_instances.py --tier tiny --tier small --tier large
python3 scripts/import_literature.py

# experiments
python3 scripts/run_benchmark.py data/synthetic --tier small --out results/small
python3 scripts/run_benchmark.py data/literature --out results/literature --random-ties 100 --explore-max-n 12
python3 scripts/run_benchmark.py data/synthetic --tier large --out results/large --dp-max-n 0 --explore-max-n 0
python3 scripts/summarize_results.py results/small results/large
python3 scripts/summarize_results.py results/literature --by-instance
python3 scripts/bench_scaling.py --out results/scaling
python3 scripts/search_worst_case.py --k 3 --alphabet ABC --max-size 6 --out results/search_k3_abc
```

## What is measured (slide 12)

| measure | where |
|---|---|
| G / OPT, compression ratio (L−G)/(L−OPT) | `runs.csv` (`ratio`, `compression_ratio`), summarised per batch and n |
| optimality rate | `optimal` column / `optimal rate` in `summary.md` |
| runtime | `time_s` per run; `bench_scaling.py` for scaling with n |
| tie sensitivity | fixed rules vs seeded random ties vs *all* tie choices (`greedy_outcomes`) |
| DP correctness | DP vs brute-force enumeration of all orderings on n ≤ 7–8 |

OPT comes from subset DP (n ≤ 16 by default), or, for equal-length inputs,
from an Eulerian-trail certificate that meets the |S|+k−1 lower bound. The
certificate gives exact OPT for the large literature constructions and for
the k-mer family.

## Data

* `data/synthetic/<family>/<variant>/<tier>_nNNNN.json`: random, sampled-fragment
  and repetitive (periodic / cyclic-spectrum / k-mer) instances. Tiers: tiny
  (n=3..8), small (n=4..16) and large (n=50..2000). Every instance stores its
  seed. `manifest.json` lists all parameters and seeds (master seed 20261105).
* `data/literature/*.json`: the slide examples; Tarhio & Ukkonen (1988) Ex. 7;
  Chukhin, Kulikov, Mihajlin, Smal (arXiv:2608.20018) for k = 3, 6, 7, 8, 10;
  Shibata (arXiv:2609.01365), the 9/4 counterexample family, with greedy
  > 2·OPT reproduced at k=10, t ≥ 10; and the Kulikov et al. repository
  examples. Each file stores the reported OPT and greedy length, the paper's
  tie choices (`tie_priority`), and our verified values.

See `AGENTS.md` for design notes, conventions and gotchas.
