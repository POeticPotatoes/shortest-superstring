# AGENTS.md: working notes for this repository

Project: **"Shortest Superstring: How Good Is Greedy?"**, a student research
project. The proposal is in `Shortest-Superstring-Research-Proposal.pptx` and
the talk is in `Shortest-Superstring-Speaker-Script.docx`. `prompt.md` holds the
original implementation brief. The project compares maximum-overlap greedy
with exact answers (subset DP) on synthetic and literature instances. It
measures G/OPT, how often greedy is optimal, runtime and tie sensitivity, and
saves inputs and seeds so every run can be reproduced.

## Hard rules

* **Never commit** (the directory is not a git repo; do not `git init` unless asked).
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
  core.py                overlap, merge, preprocess, overlap_graph (sparse), superstring_from_order
  tiebreak.py            tie-break rules (static key vs dynamic choose), make_tiebreaker("first"|"random:7"|...)
  greedy.py              greedy (fast, edge formulation), greedy_naive (literal merges), greedy_outcomes (all ties)
  exact.py               dp_exact (subset DP), brute_force_exact, kspectrum_certificate, optimal_length
  generators.py          random_strings, sampled_fragments, repetitive_strings(periodic|cyclic|kmer), derive_seed
  constructions.py       slides + literature instances (Tarhio-Ukkonen, Chukhin et al., Shibata, Kulikov repo)
  instance_io.py         JSON batch/instance formats, load_instances(files|dirs|.txt)
scripts/                 CLI tools (run from repo root: `python3 scripts/<name>.py`)
  generate_instances.py  synthetic data -> data/synthetic/<family>/<variant>/<tier>_nNNNN.json + manifest.json
  import_literature.py   writes + verifies data/literature/*.json (+ index.json)
  run_benchmark.py       greedy vs exact -> runs.csv, instances.csv, meta.json
  summarize_results.py   -> summary.md, summary_runs.csv, summary_ties.csv
  bench_scaling.py       runtime vs n for greedy and DP (generates instances on the fly from seeds)
  search_worst_case.py   exhaustive/random search of small k-SCS instances for the worst greedy ratio
  demo.py                guided tour (also the usage example)
tests/                   unittest suite (~60 tests, ~2 s)
data/literature/         transcribed paper instances with reported + verified values
data/synthetic/          generated batches (tiers tiny/small/large) + manifest.json with all seeds
results/                 benchmark outputs (regenerable; baseline runs are in here)
```

## Commands

```bash
python3 -m unittest discover -s tests -t .           # all tests (run from repo root)
python3 scripts/demo.py                               # sanity tour
python3 scripts/generate_instances.py --list          # variants/tiers
python3 scripts/generate_instances.py                 # small + large tiers (default master seed 20261105)
python3 scripts/generate_instances.py --tier tiny     # n=3..8, 30 per size (brute-force validation)
python3 scripts/import_literature.py                  # rebuild + verify data/literature
python3 scripts/run_benchmark.py data/synthetic --tier small --out results/small
python3 scripts/run_benchmark.py data/synthetic --tier tiny --out results/tiny --bf-check-max-n 8 --explore-max-n 8
python3 scripts/run_benchmark.py data/literature --out results/literature --random-ties 100 --explore-max-n 12
python3 scripts/run_benchmark.py data/synthetic --tier large --out results/large --dp-max-n 0 --explore-max-n 0
python3 scripts/summarize_results.py results/small    # add --by-instance for literature
python3 scripts/bench_scaling.py --out results/scaling
python3 scripts/search_worst_case.py --k 3 --alphabet ABC --max-size 5 --out results/search_k3
```

`run_benchmark.py` filters: `--tier`, `--family`, `--max-n`, `--limit`. Rules:
`--rules first,last,lex,revlex` plus `--random-ties R` seeded runs. Literature
instances also get the `paper` rule (their `tie_priority`).

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
  `overlap_graph` is sparse (`list[dict]`, zero overlaps omitted).
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

## Literature (transcribed in `scs/constructions.py`, verified by `import_literature.py` and tests)

| source | instance | reported | status |
|---|---|---|---|
| Slides | ATT/TTA/TAC; AABA/ABAA/BAB | OPT 5; greedy 8 vs OPT 7 | reproduced |
| Tarhio & Ukkonen 1988, Ex. 7 (https://users.aalto.fi/~tarhio/papers/greedy.pdf) | {ab^h, b^(h+1), b^h a} | OPT h+3, greedy 2h+3 | reproduced |
| Chukhin, Kulikov, Mihajlin, Smal, arXiv:2608.20018 | 3-spectrum of AB[X_i A X_i AB]…; CSpec_k of ABAABX_i y, ABX_i y | ρ₃=9/5 (9t vs 5t+2); ρ_k≥2 ((4k−6)t vs (2k−3)t+k−1) | reproduced |
| Shibata, arXiv:2609.01365v1 | S_{k,t} (U_i,V_i,W_i rotations) | OPT t(4s+2)+k−1, greedy t(9s+1)+1, >2·OPT from k=10,t=10 (461/229) | reproduced |
| Chukhin et al., arXiv:2609.27921v2 | upper bound G ≤ 3·OPT (theory only, no instances) | | asserted in tests |
| Kalugin & Nikolaev, SOSA 2024 (doi:10.1137/1.9781611977936.9) | ½-compression proof (theory only) | | asserted in tests |
| github.com/alexanderskulikov/greedy-superstring-conjecture | README example; collapsing-conjecture counterexample | OPT via DP | included |

"OpenAI paper" (from the Q&A): no paper published by OpenAI itself was found
(searched Nov 2026). The relevant work is the two 2026 preprints that
credit OpenAI's GPT-5.6 Sol. Shibata says the model first found the 9/4
counterexample, and Chukhin et al. (length-6) used GPT-5.6 Sol Ultra/Pro to find the
constructions. The extra experiments derived from them are equal-length
(k-SCS) instance families, adversarial vs random tie-breaking on those
families, the scaling of t, and the exhaustive small-instance search
(`search_worst_case.py`). Ask the user if a different paper was meant.

Takeaways from the baseline runs (see `results/*/summary.md`):

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
