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
python3 scripts/run_benchmark.py data/literature --out results/literature --random-ties 100 --explore-max-n 12 --dp-max-n 20
python3 scripts/experiment_12_5.py --out results/greedy125          # the 12/5 lower bound (paper §5.5)
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
  **the 12/5 construction** of Chukhin, Gajjala, Harviainen, Kulikov, Mihajlin,
  Shibata, Smal, "The Greedy Superstring Conjecture Is False"
  (arXiv:2609.01365v2, Theorem 4.1), stored for r ≤ 20; Shibata's earlier
  9/4 family (arXiv:2609.01365v1); and the Kulikov et al. repository examples.
  Each file stores the reported OPT (or, for the 12/5 family, the explicit
  superstring H ≥ OPT), the reported greedy length, the paper's tie choices
  (`tie_priority`), and our verified values.

## Real-world data: genome sequencing

Shortest superstring is the classic model of *de novo* genome assembly. `data/real/` turns
public sequencing data into SCS instances:

* **Reference genomes** from NCBI RefSeq: phiX174 (NC_001422.1, 5,386 bp, circular),
  SARS-CoV-2 (NC_045512.2, 29,903 bp) and lambda phage (NC_001416.1, 48,502 bp).
* **Real Illumina reads** of phiX174 from ENA run ERR098007 (23,332 reads of ~76 bp). The raw
  FASTQ is downloaded and MD5-checked by `scripts/fetch_real_data.py` and is not tracked by git.

`scripts/generate_real_instances.py` builds instance batches from these:

* **Real reads, exact and oriented:** real reads that match the genome exactly (about 50%),
  with reverse-strand reads flipped.
* **Real reads, raw:** the reads as sequenced, with errors and both strands.
* **Simulated reads:** error-free reads from all three genomes, and phiX174 reads with 1%
  errors.

Small windows (n ≤ 16) get the exact optimum. Whole-genome instances use the genome stretch
as a certified bound and report assembly metrics: does greedy rebuild the genome, and does it
join reads incorrectly?

```bash
python3 scripts/fetch_real_data.py          # needs network; verifies checksums
python3 scripts/generate_real_instances.py
python3 scripts/run_benchmark.py data/real/instances --tier small --out results/real_small
python3 scripts/run_benchmark.py data/real/instances --tier large --out results/real_large --dp-max-n 0 --explore-max-n 0 --random-ties 10 --trace-max-n 0
```

On error-free reads greedy matches OPT on every small window. With full coverage it rebuilds
all three genomes exactly. Sequencing errors and mixed strands break the SCS model: raw reads
give an output 3.6–11.4× the genome length. Pure SCS also ignores reverse complements and read
quality, which is why real assemblers are not SCS solvers.

## The 12/5 lower bound

`scripts/experiment_12_5.py` generates the Theorem 4.1 family for any r (P = r²
by default, also P = r − 1), replays the paper's greedy execution, and compares
it with fixed rules, seeded random ties and shuffled-input-order `first`. It
uses the exact DP for r ≤ 4. For larger r it reports the certified lower
bound G/|H| ≤ G/OPT, kept separate from exact ratios (`ref_kind` column).

| r | P | n | \|H\| (≥ OPT) | G (paper execution) | G/\|H\| |
|---:|---:|---:|---:|---:|---:|
| 4 | 16 | 20 | 893 (OPT 890) | 1702 | 1.906 (G/OPT 1.912) |
| 10 | 100 | 50 | 8291 | 17785 | 2.145 |
| 20 | 400 | 100 | 52781 | 119070 | **2.256 > 9/4** |
| 50 | 2500 | 250 | 703451 | 1643925 | **2.337 > 7/3** |
| 100 | 10⁴ | 500 | 5311901 | 12575350 | 2.367 |

The ratio tends to 12/5 = 2.4 as r → ∞. Random tie-breaking stays near 1.4.

See `AGENTS.md` for design notes, conventions and gotchas.
