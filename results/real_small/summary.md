# Benchmark summary: `results/real_small`

600 instances, 16300 solver runs.

## Solution quality and runtime

Ratio basis `G/OPT` uses an exact optimum (DP or certificate).  `G/|H| (lower bound)` uses a known common superstring H >= OPT, so it is a certified lower bound on G/OPT; these rows are reported separately.

| group | n | basis | algo | inst | mean ratio | max ratio | min compr. ratio | optimal rate | mean time (s) |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00049 |
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00036 |
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00013 |
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00013 |
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00009 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00067 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00018 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00018 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00013 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00282 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00024 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00024 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00017 |
| real/phix_err098007_exact | n12 (n≈12) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01263 |
| real/phix_err098007_exact | n12 (n≈12) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/phix_err098007_exact | n12 (n≈12) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n12 (n≈12) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n12 (n≈12) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n12 (n≈12) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n12 (n≈12) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00019 |
| real/phix_err098007_exact | n14 (n≈14) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.06454 |
| real/phix_err098007_exact | n14 (n≈14) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| real/phix_err098007_exact | n14 (n≈14) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n14 (n≈14) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n14 (n≈14) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/phix_err098007_exact | n14 (n≈14) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/phix_err098007_exact | n14 (n≈14) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00023 |
| real/phix_err098007_exact | n16 (n≈16) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.32507 |
| real/phix_err098007_exact | n16 (n≈16) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| real/phix_err098007_exact | n16 (n≈16) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/phix_err098007_exact | n16 (n≈16) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/phix_err098007_exact | n16 (n≈16) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/phix_err098007_exact | n16 (n≈16) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/phix_err098007_exact | n16 (n≈16) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00027 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00054 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00033 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00016 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00016 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00012 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00075 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00021 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00021 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00016 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00276 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00027 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00027 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00020 |
| real/sim_lambda_errfree | n12 (n≈12) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01303 |
| real/sim_lambda_errfree | n12 (n≈12) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_lambda_errfree | n12 (n≈12) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_lambda_errfree | n12 (n≈12) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_lambda_errfree | n12 (n≈12) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_lambda_errfree | n12 (n≈12) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_lambda_errfree | n12 (n≈12) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00025 |
| real/sim_lambda_errfree | n14 (n≈14) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.06455 |
| real/sim_lambda_errfree | n14 (n≈14) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| real/sim_lambda_errfree | n14 (n≈14) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_lambda_errfree | n14 (n≈14) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_lambda_errfree | n14 (n≈14) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_lambda_errfree | n14 (n≈14) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_lambda_errfree | n14 (n≈14) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00030 |
| real/sim_lambda_errfree | n16 (n≈16) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.32958 |
| real/sim_lambda_errfree | n16 (n≈16) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| real/sim_lambda_errfree | n16 (n≈16) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_lambda_errfree | n16 (n≈16) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_lambda_errfree | n16 (n≈16) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_lambda_errfree | n16 (n≈16) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_lambda_errfree | n16 (n≈16) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00036 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00055 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00033 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | greedy[first] | 20 | 1.0004 | 1.0044 | 0.9600 | 0.850 | 0.00002 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | greedy[last] | 20 | 1.0003 | 1.0027 | 0.9600 | 0.850 | 0.00001 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | greedy[lex] | 20 | 1.0006 | 1.0044 | 0.9600 | 0.750 | 0.00001 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | greedy[random] | 20 | 1.0004 | 1.0044 | 0.7500 | 0.848 | 0.00001 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | greedy[revlex] | 20 | 1.0002 | 1.0027 | 0.9600 | 0.900 | 0.00002 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00018 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | greedy_worst_tie | 20 | 1.0008 | 1.0044 | 0.7500 | 0.650 | 0.00018 |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00012 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00074 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | greedy[first] | 20 | 1.0002 | 1.0029 | 0.9500 | 0.900 | 0.00003 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | greedy[last] | 20 | 1.0004 | 1.0028 | 0.9500 | 0.800 | 0.00002 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | greedy[lex] | 20 | 1.0001 | 1.0014 | 0.9500 | 0.900 | 0.00002 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | greedy[random] | 20 | 1.0003 | 1.0029 | 0.9500 | 0.833 | 0.00002 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | greedy[revlex] | 20 | 1.0004 | 1.0029 | 0.9500 | 0.850 | 0.00002 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | greedy_best_tie | 20 | 1.0001 | 1.0014 | 0.9500 | 0.900 | 0.00029 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | greedy_worst_tie | 20 | 1.0005 | 1.0029 | 0.9500 | 0.750 | 0.00029 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00016 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00276 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | greedy[first] | 20 | 1.0003 | 1.0041 | 0.9853 | 0.850 | 0.00003 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | greedy[last] | 20 | 1.0004 | 1.0041 | 0.9853 | 0.850 | 0.00002 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | greedy[lex] | 20 | 1.0004 | 1.0041 | 0.9853 | 0.800 | 0.00002 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | greedy[random] | 20 | 1.0004 | 1.0041 | 0.9853 | 0.845 | 0.00003 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | greedy[revlex] | 20 | 1.0003 | 1.0041 | 0.9889 | 0.900 | 0.00003 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | greedy_best_tie | 20 | 1.0002 | 1.0041 | 0.9889 | 0.950 | 0.00033 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | greedy_worst_tie | 20 | 1.0006 | 1.0041 | 0.9853 | 0.650 | 0.00033 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00020 |
| real/sim_phix_err1pct | n12 (n≈12) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01236 |
| real/sim_phix_err1pct | n12 (n≈12) | G/OPT | greedy[first] | 20 | 1.0003 | 1.0014 | 0.9930 | 0.750 | 0.00004 |
| real/sim_phix_err1pct | n12 (n≈12) | G/OPT | greedy[last] | 20 | 1.0003 | 1.0014 | 0.9930 | 0.700 | 0.00003 |
| real/sim_phix_err1pct | n12 (n≈12) | G/OPT | greedy[lex] | 20 | 1.0003 | 1.0014 | 0.9930 | 0.750 | 0.00003 |
| real/sim_phix_err1pct | n12 (n≈12) | G/OPT | greedy[random] | 20 | 1.0003 | 1.0019 | 0.9859 | 0.728 | 0.00003 |
| real/sim_phix_err1pct | n12 (n≈12) | G/OPT | greedy[revlex] | 20 | 1.0003 | 1.0014 | 0.9930 | 0.700 | 0.00003 |
| real/sim_phix_err1pct | n12 (n≈12) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00025 |
| real/sim_phix_err1pct | n14 (n≈14) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.06143 |
| real/sim_phix_err1pct | n14 (n≈14) | G/OPT | greedy[first] | 20 | 1.0003 | 1.0019 | 0.9933 | 0.700 | 0.00006 |
| real/sim_phix_err1pct | n14 (n≈14) | G/OPT | greedy[last] | 20 | 1.0002 | 1.0011 | 0.9933 | 0.750 | 0.00004 |
| real/sim_phix_err1pct | n14 (n≈14) | G/OPT | greedy[lex] | 20 | 1.0004 | 1.0022 | 0.9933 | 0.650 | 0.00003 |
| real/sim_phix_err1pct | n14 (n≈14) | G/OPT | greedy[random] | 20 | 1.0004 | 1.0022 | 0.9933 | 0.705 | 0.00004 |
| real/sim_phix_err1pct | n14 (n≈14) | G/OPT | greedy[revlex] | 20 | 1.0003 | 1.0020 | 0.9933 | 0.750 | 0.00004 |
| real/sim_phix_err1pct | n14 (n≈14) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00030 |
| real/sim_phix_err1pct | n16 (n≈16) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.30034 |
| real/sim_phix_err1pct | n16 (n≈16) | G/OPT | greedy[first] | 20 | 1.0002 | 1.0020 | 0.9944 | 0.850 | 0.00006 |
| real/sim_phix_err1pct | n16 (n≈16) | G/OPT | greedy[last] | 20 | 1.0001 | 1.0009 | 0.9963 | 0.900 | 0.00004 |
| real/sim_phix_err1pct | n16 (n≈16) | G/OPT | greedy[lex] | 20 | 1.0003 | 1.0030 | 0.9968 | 0.850 | 0.00004 |
| real/sim_phix_err1pct | n16 (n≈16) | G/OPT | greedy[random] | 20 | 1.0002 | 1.0030 | 0.9927 | 0.868 | 0.00004 |
| real/sim_phix_err1pct | n16 (n≈16) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1.0008 | 0.9963 | 0.950 | 0.00004 |
| real/sim_phix_err1pct | n16 (n≈16) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00035 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00054 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00033 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00016 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00016 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00012 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00074 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00021 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00021 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00016 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00275 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00027 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00027 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00020 |
| real/sim_phix_errfree | n12 (n≈12) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01298 |
| real/sim_phix_errfree | n12 (n≈12) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_phix_errfree | n12 (n≈12) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_phix_errfree | n12 (n≈12) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_phix_errfree | n12 (n≈12) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_phix_errfree | n12 (n≈12) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_phix_errfree | n12 (n≈12) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00025 |
| real/sim_phix_errfree | n14 (n≈14) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.06460 |
| real/sim_phix_errfree | n14 (n≈14) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| real/sim_phix_errfree | n14 (n≈14) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_phix_errfree | n14 (n≈14) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_phix_errfree | n14 (n≈14) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_phix_errfree | n14 (n≈14) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_phix_errfree | n14 (n≈14) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00030 |
| real/sim_phix_errfree | n16 (n≈16) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.32420 |
| real/sim_phix_errfree | n16 (n≈16) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| real/sim_phix_errfree | n16 (n≈16) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_phix_errfree | n16 (n≈16) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_phix_errfree | n16 (n≈16) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_phix_errfree | n16 (n≈16) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_phix_errfree | n16 (n≈16) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00037 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00054 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00032 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00015 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00015 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00011 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00074 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00021 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00021 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00016 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00276 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00027 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00027 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00020 |
| real/sim_sars2_errfree | n12 (n≈12) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01289 |
| real/sim_sars2_errfree | n12 (n≈12) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_sars2_errfree | n12 (n≈12) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_sars2_errfree | n12 (n≈12) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| real/sim_sars2_errfree | n12 (n≈12) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_sars2_errfree | n12 (n≈12) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_sars2_errfree | n12 (n≈12) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00025 |
| real/sim_sars2_errfree | n14 (n≈14) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.06429 |
| real/sim_sars2_errfree | n14 (n≈14) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| real/sim_sars2_errfree | n14 (n≈14) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_sars2_errfree | n14 (n≈14) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_sars2_errfree | n14 (n≈14) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_sars2_errfree | n14 (n≈14) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| real/sim_sars2_errfree | n14 (n≈14) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00030 |
| real/sim_sars2_errfree | n16 (n≈16) | G/OPT | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.32627 |
| real/sim_sars2_errfree | n16 (n≈16) | G/OPT | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| real/sim_sars2_errfree | n16 (n≈16) | G/OPT | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_sars2_errfree | n16 (n≈16) | G/OPT | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_sars2_errfree | n16 (n≈16) | G/OPT | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_sars2_errfree | n16 (n≈16) | G/OPT | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| real/sim_sars2_errfree | n16 (n≈16) | G/OPT | overlap_graph | 20 | - | - | - | - | 0.00035 |

## Tie sensitivity

| group | n | basis | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | mean tie steps | mean ratio (first) | max ratio observed | max ratio all ties |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.2 | 1.0000 | 1 | 1 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.8 | 1.0000 | 1 | 1 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 1.1 | 1.0000 | 1 | 1 |
| real/phix_err098007_exact | n12 (n≈12) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 1.9 | 1.0000 | 1 | - |
| real/phix_err098007_exact | n14 (n≈14) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 2.9 | 1.0000 | 1 | - |
| real/phix_err098007_exact | n16 (n≈16) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 4.2 | 1.0000 | 1 | - |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.3 | 1.0000 | 1 | 1 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.5 | 1.0000 | 1 | 1 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.8 | 1.0000 | 1 | 1 |
| real/sim_lambda_errfree | n12 (n≈12) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 1.3 | 1.0000 | 1 | - |
| real/sim_lambda_errfree | n14 (n≈14) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 1.2 | 1.0000 | 1 | - |
| real/sim_lambda_errfree | n16 (n≈16) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 2.1 | 1.0000 | 1 | - |
| real/sim_phix_err1pct | n06 (n≈6) | G/OPT | 20 | dp | 0.350 | 1.35 | 0.847 | 1.9 | 1.0004 | 1.0044 | 1.0044 |
| real/sim_phix_err1pct | n08 (n≈8) | G/OPT | 20 | dp | 0.200 | 1.20 | 0.832 | 2.4 | 1.0002 | 1.0029 | 1.0029 |
| real/sim_phix_err1pct | n10 (n≈10) | G/OPT | 20 | dp | 0.300 | 1.30 | 0.845 | 3.2 | 1.0003 | 1.0041 | 1.0041 |
| real/sim_phix_err1pct | n12 (n≈12) | G/OPT | 20 | dp | 0.350 | 1.40 | 0.728 | 3.9 | 1.0003 | 1.0019 | - |
| real/sim_phix_err1pct | n14 (n≈14) | G/OPT | 20 | dp | 0.500 | 1.65 | 0.705 | 4.4 | 1.0003 | 1.0022 | - |
| real/sim_phix_err1pct | n16 (n≈16) | G/OPT | 20 | dp | 0.350 | 1.45 | 0.868 | 5.7 | 1.0002 | 1.0030 | - |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.2 | 1.0000 | 1 | 1 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.4 | 1.0000 | 1 | 1 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.8 | 1.0000 | 1 | 1 |
| real/sim_phix_errfree | n12 (n≈12) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 1.2 | 1.0000 | 1 | - |
| real/sim_phix_errfree | n14 (n≈14) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 1.9 | 1.0000 | 1 | - |
| real/sim_phix_errfree | n16 (n≈16) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 1.7 | 1.0000 | 1 | - |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.2 | 1.0000 | 1 | 1 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.3 | 1.0000 | 1 | 1 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 0.6 | 1.0000 | 1 | 1 |
| real/sim_sars2_errfree | n12 (n≈12) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 1.4 | 1.0000 | 1 | - |
| real/sim_sars2_errfree | n14 (n≈14) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 1.9 | 1.0000 | 1 | - |
| real/sim_sars2_errfree | n16 (n≈16) | G/OPT | 20 | dp | 0.000 | 1.00 | 1.000 | 2.6 | 1.0000 | 1 | - |

## Assembly metrics (genome instances, rule `first`)

G / genome length is descriptive, not a bound.  *Reconstructs*: the output equals the reference stretch H.  *Misjoin-free*: the output is a contiguous piece of H.  Both are computed only for gapless error-free reads, where H is the true genome stretch.

| group | n | basis | inst | mean G/genome | reconstructs | misjoin-free | mean ratio (first) |
|---|---:|---|---:|---:|---:|---:|---:|
| real/phix_err098007_exact | n06 (n≈6) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/phix_err098007_exact | n08 (n≈8) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/phix_err098007_exact | n10 (n≈10) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/phix_err098007_exact | n12 (n≈12) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/phix_err098007_exact | n14 (n≈14) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/phix_err098007_exact | n16 (n≈16) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_lambda_errfree | n06 (n≈6) | G/OPT | 20 | - | 0.889 | 0.889 | 1.0000 |
| real/sim_lambda_errfree | n08 (n≈8) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_lambda_errfree | n10 (n≈10) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_lambda_errfree | n12 (n≈12) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_lambda_errfree | n14 (n≈14) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_lambda_errfree | n16 (n≈16) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_phix_errfree | n06 (n≈6) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_phix_errfree | n08 (n≈8) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_phix_errfree | n10 (n≈10) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_phix_errfree | n12 (n≈12) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_phix_errfree | n14 (n≈14) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_phix_errfree | n16 (n≈16) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_sars2_errfree | n06 (n≈6) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_sars2_errfree | n08 (n≈8) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_sars2_errfree | n10 (n≈10) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_sars2_errfree | n12 (n≈12) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_sars2_errfree | n14 (n≈14) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
| real/sim_sars2_errfree | n16 (n≈16) | G/OPT | 20 | - | 1.000 | 1.000 | 1.0000 |
