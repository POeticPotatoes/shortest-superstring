# AGENTS.md: working notes for this repository

Project: **"Shortest Superstring: How Good Is Greedy?"**, a student research
project. The proposal is in `Shortest-Superstring-Research-Proposal.pptx` and
the talk is in `Shortest-Superstring-Speaker-Script.docx`. `prompt.md` holds the
original implementation brief. The project compares maximum-overlap greedy
with exact answers (subset DP) on synthetic and literature instances. It
measures G/OPT, how often greedy is optimal, runtime and tie sensitivity, and
saves inputs and seeds so every run can be reproduced.

## Hard rules

* **Never commit** (the user manages git; do not stage, commit or change branches).
* **Never modify files outside this directory.** Scratch output from tests goes to
  `tests/_tmp*` (auto-deleted), not `/tmp`.
* **Standard library only.** No numpy, pytest or matplotlib are installed, and the
  code must run with plain `python3` (>= 3.10; developed on 3.14).
* Do not edit the `.pptx` / `.docx` / `prompt.md` inputs.
* Keep `data/` reproducible: if you change a generator, seed derivation or the
  random tie hash, bump `GENERATOR_VERSION` in `scs/generators.py`, regenerate
  `data/synthetic`, and re-run the affected benchmarks. A test pins
  `derive_seed` (see `tests/test_generators.py`).

## Layout

```
scs/                     library (import as `scs`)
  core.py                overlap, merge, preprocess, overlap_graph (sparse; prefix or anchored), superstring_from_order
  tiebreak.py            tie-break rules (static key vs dynamic choose), make_tiebreaker("first"|"random:7"|...)
  greedy.py              greedy (fast, edge formulation), greedy_naive (literal merges), greedy_outcomes (all ties)
  exact.py               dp_exact (subset DP), brute_force_exact, kspectrum_certificate, optimal_length
  generators.py          random_strings, sampled_fragments, repetitive_strings(periodic|cyclic|kmer), derive_seed
  constructions.py       slides + literature instances (Tarhio-Ukkonen, Chukhin et al., Shibata v1 9/4,
                         greedy_12_5 = arXiv:2609.01365v2 Thm 4.1, Kulikov repo)
  instance_io.py         JSON batch/instance formats, load_instances(files|dirs|.txt)
  realdata.py            FASTA/FASTQ parsing, reverse complement, read simulation, exact-read orientation, windows
scripts/                 CLI tools (run from repo root: `python3 scripts/<name>.py`)
  generate_instances.py  synthetic data -> data/synthetic/<family>/<variant>/<tier>_nNNNN.json + manifest.json
  fetch_real_data.py     download + verify NCBI genomes and ENA reads -> data/real/{reference,raw}, sources.json
  generate_real_instances.py  real-data instances -> data/real/instances/<variant>/<tier>_<param>.json
  import_literature.py   writes + verifies data/literature/*.json (+ index.json)
  run_benchmark.py       greedy vs exact -> runs.csv, instances.csv, meta.json
  experiment_12_5.py     12/5 family generated on the fly: paper execution vs tie rules, DP for r<=4, G/|H|
  summarize_results.py   -> summary.md, summary_runs.csv, summary_ties.csv, summary_paper.csv
  bench_scaling.py       runtime vs n for greedy and DP (generates instances on the fly from seeds)
  search_worst_case.py   exhaustive/random search of small k-SCS instances for the worst greedy ratio
  demo.py                guided tour (also the usage example)
tests/                   unittest suite (~70 tests, ~3 s)
data/literature/         transcribed paper instances with reported + verified values
data/synthetic/          generated batches (tiers tiny/small/large) + manifest.json with all seeds
data/real/               reference/ (3 RefSeq genomes, tracked), raw/ (ENA reads, git-ignored), sources.json,
                         instances/ (derived SCS instances, tracked, ~6 MB)
results/                 benchmark outputs (regenerable; baseline runs are in here)
```

## Commands

```bash
python3 -m unittest discover -s tests -t .           # all tests (run from repo root)
python3 scripts/demo.py                               # sanity tour
python3 scripts/generate_instances.py --list          # variants/tiers
python3 scripts/generate_instances.py                 # small + large tiers (default master seed 20261105)
python3 scripts/generate_instances.py --tier tiny     # n=3..8, 30 per size (brute-force validation)
python3 scripts/import_literature.py                  # rebuild + verify data/literature (~25 s; DP up to n=20)
python3 scripts/run_benchmark.py data/synthetic --tier small --out results/small
python3 scripts/run_benchmark.py data/synthetic --tier tiny --out results/tiny --bf-check-max-n 8 --explore-max-n 8
python3 scripts/run_benchmark.py data/literature --out results/literature --random-ties 100 --explore-max-n 12 --dp-max-n 20
python3 scripts/experiment_12_5.py --family adapted --out results/greedy125_adapted   # report §4.4 family S_n (~20 s)
python3 scripts/experiment_12_5.py --family adapted --out results/greedy125_adapted_big --n 70,100 --random-ties 5 --shuffle-orders 5
python3 scripts/experiment_12_5.py --out results/greedy125           # the paper's (r, P) family (~30 s)
python3 scripts/experiment_12_5.py --out results/greedy125_big --r 70,100 --small-p-r "" --random-ties 5 --shuffle-orders 5
python3 scripts/run_benchmark.py data/synthetic --tier large --out results/large --dp-max-n 0 --explore-max-n 0
python3 scripts/summarize_results.py results/small    # add --by-instance for literature
python3 scripts/fetch_real_data.py                    # network: genomes (NCBI) + ERR098007 reads (ENA), verified
python3 scripts/generate_real_instances.py            # ~3 s; deterministic (master seed 20261111)
python3 scripts/run_benchmark.py data/real/instances --tier small --out results/real_small
python3 scripts/run_benchmark.py data/real/instances --tier large --out results/real_large --dp-max-n 0 --explore-max-n 0 --random-ties 10 --trace-max-n 0
python3 scripts/bench_scaling.py --out results/scaling
python3 scripts/search_worst_case.py --k 3 --alphabet ABC --max-size 5 --out results/search_k3
```

`run_benchmark.py` filters: `--tier`, `--family`, `--max-n`, `--limit`. Rules:
`--rules first,last,lex,revlex` plus `--random-ties R` seeded runs. Literature
instances also get the `paper` rule (their `tie_priority`).

**Ratio basis (`ref`, `ref_kind`).** Ratios divide by `ref`. That is the exact
OPT (`ref_kind=exact`: DP, certificate or a reported OPT) when available.
Otherwise it is the length of a known common superstring (`known.opt_upper`, e.g.
H of the 12/5 construction; `ref_kind=upper_bound`), making the ratio a certified
*lower bound* G/|H| ≤ G/OPT. `summarize_results.py` keeps the two bases in
separate rows ("G/OPT" vs "G/|H| (lower bound)"). This follows the
team's paper draft (§5.5): never mix them. `compression_ratio` and `optimal`
are filled only for exact references.

## Key conventions and semantics (read before changing algorithms)

* **Strings are Python `str`; one character = one symbol.** Constructions that
  need many symbols (Shibata's `b_i`, Chukhin's `X_i`, `Y_j`) use digits, Greek,
  Latin Extended and Cyrillic characters (`constructions.fresh_symbols`). JSON
  is written with `ensure_ascii=False`. NUL (`\x00`) is reserved.
* **Preprocessing** (`core.preprocess`) removes duplicates and contained strings.
  It **keeps first-occurrence order**, and all indices (`u`, `v`, `order`,
  `merges`) refer to the reduced list (`result.strings`). Every solver
  preprocesses by default. Pass `preprocess=False` only with already-reduced input.
* **Overlap** `ov(u, v)` = longest suffix of u that is a prefix of v.
  `overlap_graph` is sparse (`list[dict]`, zero overlaps omitted). It has two
  methods, which tests check agree: `prefix` hashes every proper prefix
  (fast for many short strings, memory ~Σℓ²/2), and `anchored` checks each pair
  with C-level `str.find` on the anchor "first run of v + next char". `auto`
  switches at `PREFIX_INDEX_LIMIT`. The 12/5 gap words (ℓ up to ~60k) need
  `anchored`. Pass a precomputed `graph=` to `greedy` when running many rules.
* **Greedy is implemented on the overlap graph** (Tarhio–Ukkonen view): merging
  fragment X (last input u) with fragment Y (first input v) is edge `(u, v)`
  and saves `ov(u, v)`. Valid edge: u has no successor, v has no predecessor,
  and v is not the head of u's path. `greedy_naive` (literal string merging) is
  kept as a reference. Tests assert that fast, traced and naive greedy give
  **identical superstrings** for every static rule. Keep it that way.
* **Tie-breakers** choose among *edges* `(u, v)` tied at the current maximum
  overlap.
  * Static rules (`key(u, v)`, smallest wins): `first`, `last`, `lex`, `revlex`,
    `random:<seed>`, `Priority(edge_list, fallback)`. Greedy sorts each overlap
    level once (after dropping already-invalid edges) and scans it. That is
    equivalent to "choose the min-key valid candidate each step", because an
    invalid edge never becomes valid again.
  * Dynamic rules (`choose(candidates, state)`): `short-frag`, `long-frag`, or
    any callable `f(candidates, state) -> (u, v)`. `GreedyState` offers
    `ov`, `fragment(x)`, `fragment_length(x)`, `heads()`, `path(h)`, `merges`.
  * `random:<seed>` uses a stateless splitmix64 hash of `(seed, u, v)`, so it
    does not depend on call order or Python version. It is a uniformly random
    choice among tied candidates (a test checks the 1/3 rate on TU Example 7).
  * `first` / `last` depend on input order. Generators shuffle output so
    that the order never spells the source (cyclic/kmer used to leak the
    optimal order). Literature instances keep the order they were transcribed in.
  * `Priority` cannot force a non-maximum merge. Greedy only reorders ties, so
    replaying a paper's execution also checks that it is a valid greedy run.
  * `trace=True` records the number of candidates per merge (`result.tie_steps`).
  * At overlap 0 with more than 2M fragment pairs, static rules concatenate by
    index (`zero_level_shortcut=True`). The length is unaffected.
* **`greedy_outcomes`** enumerates all tie choices (memoised on the
  successor array, and it stops branching once the max overlap is 0). It is
  exponential: use n ≤ ~12 or set `max_states`. It raises
  `ExplorationBudgetExceeded` when the budget runs out.
* **Exact**: `dp_exact` stores max overlap per `(mask, last)` with the inner
  max done via `map(add, ...)`. Measured: n=16 ≈ 0.3 s, n=18 ≈ 1.5 s, n=20
  ≈ 7 s and 250 MB. Default `max_n=20`, and the benchmark default is
  `--dp-max-n 16`. `brute_force_exact` is for n ≤ 8 only.
  `kspectrum_certificate`: for equal-length-k inputs, OPT ≥ |S|+k−1, and an
  Eulerian trail in the (k−1)-mer graph meets that bound. This is how OPT is
  known exactly for large literature/kmer instances.
* **Metrics**: ratio = G/OPT; compression ratio = (L−G)/(L−OPT); L = total
  length after preprocessing. The ½-compression theorem (L−G ≥ (L−OPT)/2 for
  every greedy run) and G ≤ 3·OPT (Chukhin et al. preprint) are asserted in
  tests and counted by `search_worst_case.py`.

## Data and reproducibility

* Batch JSON (`scs-batch/1`): `master_seed`, generator params, python/platform,
  command line, and per-instance `seed`, `strings`, `source` (sampled/periodic/kmer),
  `n_reduced`, `total_length`. Instance seed =
  `derive_seed(master_seed, variant, n, index)` (sha256-based, stable).
  `data/synthetic/manifest.json` lists every batch with all seeds.
  Regenerate one instance with `scs.generators.generate(family, seed, n=n, **params)`.
* Tiers: `tiny` n=3..8 ×30, `small` n=4..16 ×20 (exact DP), `large`
  n=50..2000 ×5 (greedy only; OPT certified for kmer variants only).
* Variants: random (DNA, binary), sampled (DNA source 4n, binary source 3n),
  repetitive periodic (mutated tandem repeats), cyclic (unions of cyclic
  k-spectra, the structure of all recent bad-greedy constructions), kmer
  (de Bruijn self-avoiding walk, so OPT = |source|).
* Benchmark random-tie seeds: `derive_seed(tie_seed, instance_id, r)`, logged in
  `runs.csv`. `meta.json` stores all CLI args and the environment.

## Real-world data (genome sequencing)

SCS is the textbook model of *de novo* genome assembly (reads = strings, genome ≈ superstring).
No public dataset ships ready-made SCS instances, so `data/real/` builds them from public
sequencing data:

| source | what | stored |
|---|---|---|
| NCBI RefSeq NC_001422.1 | phiX174, 5,386 bp, **circular** (the standard Illumina control) | `reference/` |
| NCBI RefSeq NC_045512.2 | SARS-CoV-2 Wuhan-Hu-1, 29,903 bp | `reference/` |
| NCBI RefSeq NC_001416.1 | lambda phage, 48,502 bp (treated as linear) | `reference/` |
| ENA ERR098007 (study PRJEB2910) | real Illumina GA IIx phiX174 reads, 23,332 × ~76 bp, 1.8 MB | `raw/` (git-ignored; MD5-checked) |

Variants (`generate_real_instances.py`). Tiers: `small` = n 6–16 reads from one
window (DP gives exact OPT); `large` = whole genome at a given coverage (greedy only).

* `phix_err098007_exact`: real reads that match the reference **exactly** on either strand
  (11,739 of 23,332; 34 contain N, 11,559 have errors), with reverse-strand reads flipped
  (a reference-guided step). Even with all of them, coverage has **3 gaps** (pos 584–588,
  832–833, 2807–2812): no exact read covers those bases, most likely sites where the sequenced
  strain differs from RefSeq. So the large instances are 4 contigs, not gapless.
* `phix_err098007_raw`: real reads as sequenced (N-reads dropped): both strands plus errors.
  No reference bound on OPT (`basis = no OPT`).
* `sim_{phix,sars2,lambda}_errfree`: forward-strand error-free reads simulated from the
  genomes (lengths 100/50, coverage 5–50).
* `sim_phix_err1pct`: simulated with 1% substitutions (no reference bound).

Conventions: identical reads are dropped at generation (`duplicates_removed`). Error-free
instances store the covered genome stretch as `upper_superstring` (so ratios are G/|H|
lower bounds), `starts` (true positions) and `gapless`. Whole-genome instances also store
`reference_length`, and circular genomes store `circular_reference`. `run_benchmark.py` adds
`g_first_over_reference` (descriptive expansion factor, not a bound) and, for gapless
error-free instances, `first_misjoin_free` (output is a contiguous piece of the genome; for circular
genomes any rotation) and `first_reconstructs_upper` (it is the whole stretch/circle).
SCS ignores reverse complements and quality values, and has no error model. These are the
reasons real assemblers are not SCS solvers. Say so when presenting these results.

## Literature (transcribed in `scs/constructions.py`, verified by `import_literature.py` and tests)

| source | instance | reported | status |
|---|---|---|---|
| Slides | ATT/TTA/TAC; AABA/ABAA/BAB | OPT 5; greedy 8 vs OPT 7 | reproduced |
| Tarhio & Ukkonen 1988, Ex. 7 (https://users.aalto.fi/~tarhio/papers/greedy.pdf) | {ab^h, b^(h+1), b^h a} | OPT h+3, greedy 2h+3 | reproduced |
| Chukhin, Kulikov, Mihajlin, Smal, arXiv:2608.20018 | 3-spectrum of AB[X_i A X_i AB]…; CSpec_k of ABAABX_i y, ABX_i y | ρ₃=9/5 (9t vs 5t+2); ρ_k≥2 ((4k−6)t vs (2k−3)t+k−1) | reproduced |
| **Chukhin, Gajjala, Harviainen, Kulikov, Mihajlin, Shibata, Smal, "The Greedy Superstring Conjecture Is False", arXiv:2609.01365v2 (6 Nov 2026), Thm 4.1** | `greedy_12_5(r, P)`: 5r binary gap words X,Y,U,V,Z; P ≥ r−1 (default r²) | \|H\| = 5Pr+27r²+4P+19r+1 ≥ OPT; greedy 12Pr+(115r²+7r)/2; ratio → **12/5** | reproduced r ≤ 100; G/\|H\| > 9/4 from r=20, > 7/3 from r=50 |
| Shibata, arXiv:2609.01365**v1** (now a preliminary version of v2) | S_{k,t} (U_i,V_i,W_i rotations) | OPT t(4s+2)+k−1, greedy t(9s+1)+1, ratio → 9/4 | reproduced; superseded |
| Chukhin et al., arXiv:2609.27921v2 (merged into 2609.01365v2) | upper bound G ≤ 3·OPT (theory only, no instances) | | asserted in tests |
| Kalugin & Nikolaev, SOSA 2024 (doi:10.1137/1.9781611977936.9) | ½-compression proof (theory only) | | asserted in tests |
| Nikolaev, "All instantiations of the greedy algorithm for SCS are equivalent", SPIRE 2021 (arXiv:2102.05579) | (theory) every fixed tie-breaking rule has the same worst-case ratio | | cited in report §2/§4.4/§5.7 to reconcile "random ties never find the bad run" with the worst-case bounds |
| github.com/alexanderskulikov/greedy-superstring-conjecture | README example; collapsing-conjecture counterexample | OPT via DP | included |

"OpenAI paper" (from the Q&A): this is most likely **OpenAI (2026), "A Polynomial-Time
2-Approximation for Shortest Common Superstring"**, an OpenAI Math Release preprint
(github.com/openai/math, result #128, preprint dated 2026-09-24), which arXiv:2609.01365v2
cites. It is a new approximation algorithm for general SCS, not a greedy
result, and it is **not implemented here** (a possible extension: a third solver to compare against
greedy). The greedy lower-bound papers credit AI too. v2 says GPT-5.6 Sol / GPT-6 Astra
found the 9/4, 7/3 and 19/8 constructions, and Claude Opus-5.5 found the 12/5 one. The
experiments derived from that line of work are the equal-length (k-SCS) families,
paper ties vs fixed/random ties, scaling of t / r, and `search_worst_case.py`.

Takeaways from the baseline runs (see `results/*/summary.md`):

* **Real data** (`results/real_small`, `results/real_large`): on error-free windows (real exact
  reads and simulated) greedy = OPT on all 480 small instances. On gapless windows it reproduces
  the true genome stretch, with one exception: lambda n=6 #003, where a spurious 3-base overlap
  beats a true 1-base overlap and even OPT is 2 bases shorter than the genome. This is SCS
  over-collapsing. Whole-genome error-free reads at ≥ 10× coverage: greedy reconstructs phiX174
  (circular), SARS-CoV-2 and lambda exactly. With 1% errors greedy's output is ~5.9× the genome.
  Raw ERR098007 reads give 3.6× (500 reads) to 11.4× (2000 reads) because almost nothing overlaps
  exactly. With 1% errors on small windows G/OPT is still ≤ 1.0044.

* **Report's adapted S_n** (`results/greedy125_adapted*`): every claim verified for n ≤ 100.
  H_n is optimal for n ≤ 5 (DP), and G_n/|H_n| = 2.011 (n=6), 2.274 (n=20), 2.348 (n=50), 2.374 (n=100).
  `lex` always outputs a string of length |H_n|, `revlex` ≤ 1.59, random ≤ 1.80, shuffled `first` 1.11–1.57.
* **12/5 construction** (`results/greedy125`, `results/greedy125_big`). The prescribed
  execution reproduces 12Pr+(115r²+7r)/2 exactly for every tested (r, P). H is a valid
  superstring with the stated length. Certified G/|H| (P=r²): r=6 2.026, r=10 2.145,
  r=20 2.256 (> 9/4), r=50 2.337 (> 7/3), r=100 2.367. Convergence to 12/5 is slow,
  and 19/8 = 2.375 is not passed by r=100. Exact DP (r ≤ 4) shows H is close to optimal
  but not optimal (|H| − OPT = 0–3), e.g. r=4, P=16: OPT 890 vs |H| 893, G/OPT 1.912.
  Random ties reproduce the bad run only for tiny r (r=1, and once in 100 runs at r=2, P=4).
  For r ≥ 3 they never do (mean ≈ 1.40, max ≤ 1.74). The
  order-independent `lex`/`revlex` give ≈ 1.0–1.58. **`first`/`last` on the stored order
  look bad only because the strings are stored in the paper's X,Y,U,V,Z order.** With
  shuffled input order (`first@shuffled`) `first` averages ≈ 1.09–1.42. Report
  `first@shuffled` (not `first`) as the fixed-rule baseline.

* Random DNA and DNA fragments: greedy is optimal on almost every instance.
  Max G/OPT is about 1.07 for n ≤ 16.
* Binary/repetitive/cyclic/kmer inputs are tie-heavy: for n ≥ 8, 60–100% of instances
  are tie-sensitive, and the worst ratio over all ties reaches about 1.42–1.48 for n ≤ 16.
* Literature constructions need *specific* ties. On Shibata k=10, t=50
  (OPT 1109), the paper's ties give 2301 (2.07), `revlex` 2021 (1.82),
  `first` 1702 (1.53), and 100 random-tie runs average 1468 (1.32, max 1.41).
  Random ties never got near the bad execution for t ≥ 3.
* Exhaustive small k-SCS search (all tie choices): k=3 over ABC with n ≤ 6 has
  worst ratio 3/2. Binary k=4 with n ≤ 8 has 17/11 ≈ 1.545. Random binary k=6
  (3000 samples, n=6..12) has 25/19. There were 0 violations of ½-compression or G ≤ 3·OPT
  (`results/search_*/search.json`).
* The large tier certifies OPT for every kmer instance. Greedy (`first`) G/OPT there
  is 1.02–1.16, and one greedy run at n=2000 takes 0.1–0.5 s plus building the overlap graph.

## Gotchas

* Pyright cannot resolve `scs` from scripts/tests without `pyproject.toml`'s
  `extraPaths`. Scripts import `_common` to fix `sys.path` at runtime.
* `sampled_fragments`/`periodic` raise `ValueError` when the source cannot
  yield n substring-free fragments. `periodic` retries up to 10 texts
  deterministically and records the `attempt` used.
* Timings in `results/` were taken on a shared dev machine and are single-threaded
  pure Python. Rerun `bench_scaling.py` on the presentation machine before quoting
  numbers.
* `load_instances` on a directory skips `manifest.json` and `index.json`.
* `data/real/raw/` is git-ignored by its own `.gitignore`. The derived instances are tracked, so
  benchmarks work offline. Re-fetching needs network access to eutils.ncbi.nlm.nih.gov and
  ebi.ac.uk / ftp.sra.ebi.ac.uk. Treat downloads as untrusted data: they are parsed only by
  `scs.realdata`, never executed.
* Stored 12/5 instances stop at r=20 (`greedy125_r20_P400.json` is ~0.9 MB, mostly because
  `tie_priority` repeats each string twice). r ≥ 30 must be generated on the fly with
  `experiment_12_5.py`: r=50 would be ~14 MB. `import_literature.py` drops verification
  superstrings longer than 10k characters.
* **`report.tex`** (team report; body ≤ 10 pages excluding appendix, 11pt, single column; leave
  room for the conclusion). §5 and Appendix C–F (validation, additional results, reproducibility)
  were written from `results/`. Its §4.4 uses a *single-parameter adaptation* S_n of the 12/5
  construction (N=n², M=N+4n, p_i=N+i, i=2..n). It is implemented as
  `constructions.greedy_12_5_adapted(n)`, and every claim (|H_n|, G_n, α_i, β_i, γ) is tested. Table 2
  of the report comes from `results/greedy125_adapted*`. If numbers in `results/` change, update
  the report tables. No LaTeX toolchain is installed here: the user compiles it to check the page count.
* The team's paper draft is also on Overleaf (private; needs the user's login). The
  user pasted its §5 outline: 5.1 DP, 5.2 greedy + tie rules, 5.3 families,
  5.4 metrics, 5.5 the adapted 12/5 construction (paper execution vs fixed/random
  ties, exact solver when small, G/|H| reported separately), 5.6 results, 5.7 discussion.
  Do not edit the paper. Produce results/tables it can use.
