# Benchmark summary: `results/real_large`

39 instances, 585 solver runs.

## Solution quality and runtime

Ratio basis `G/OPT` uses an exact optimum (DP or certificate).  `G/|H| (lower bound)` uses a known common superstring H >= OPT, so it is a certified lower bound on G/OPT; these rows are reported separately.

| group | n | basis | algo | inst | mean ratio | max ratio | min compr. ratio | optimal rate | mean time (s) |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| real/phix_err098007_exact | cov10 (n≈571) | G/\|H\| (lower bound) | greedy[first] | 3 | 0.9394 | 0.9485 | - | - | 0.01519 |
| real/phix_err098007_exact | cov10 (n≈571) | G/\|H\| (lower bound) | greedy[last] | 3 | 0.9393 | 0.9483 | - | - | 0.01512 |
| real/phix_err098007_exact | cov10 (n≈571) | G/\|H\| (lower bound) | greedy[lex] | 3 | 0.9393 | 0.9483 | - | - | 0.01433 |
| real/phix_err098007_exact | cov10 (n≈571) | G/\|H\| (lower bound) | greedy[random] | 3 | 0.9393 | 0.9485 | - | - | 0.01467 |
| real/phix_err098007_exact | cov10 (n≈571) | G/\|H\| (lower bound) | greedy[revlex] | 3 | 0.9393 | 0.9483 | - | - | 0.01445 |
| real/phix_err098007_exact | cov10 (n≈571) | G/\|H\| (lower bound) | overlap_graph | 3 | - | - | - | - | 0.01999 |
| real/phix_err098007_exact | cov20 (n≈951) | G/\|H\| (lower bound) | greedy[first] | 3 | 0.9778 | 0.9809 | - | - | 0.04793 |
| real/phix_err098007_exact | cov20 (n≈951) | G/\|H\| (lower bound) | greedy[last] | 3 | 0.9778 | 0.9809 | - | - | 0.04133 |
| real/phix_err098007_exact | cov20 (n≈951) | G/\|H\| (lower bound) | greedy[lex] | 3 | 0.9778 | 0.9809 | - | - | 0.04112 |
| real/phix_err098007_exact | cov20 (n≈951) | G/\|H\| (lower bound) | greedy[random] | 3 | 0.9778 | 0.9809 | - | - | 0.04338 |
| real/phix_err098007_exact | cov20 (n≈951) | G/\|H\| (lower bound) | greedy[revlex] | 3 | 0.9778 | 0.9809 | - | - | 0.04166 |
| real/phix_err098007_exact | cov20 (n≈951) | G/\|H\| (lower bound) | overlap_graph | 3 | - | - | - | - | 0.03868 |
| real/phix_err098007_exact | cov5 (n≈314) | G/\|H\| (lower bound) | greedy[first] | 3 | 0.8385 | 0.8922 | - | - | 0.00456 |
| real/phix_err098007_exact | cov5 (n≈314) | G/\|H\| (lower bound) | greedy[last] | 3 | 0.8385 | 0.8922 | - | - | 0.00429 |
| real/phix_err098007_exact | cov5 (n≈314) | G/\|H\| (lower bound) | greedy[lex] | 3 | 0.8385 | 0.8922 | - | - | 0.00430 |
| real/phix_err098007_exact | cov5 (n≈314) | G/\|H\| (lower bound) | greedy[random] | 3 | 0.8384 | 0.8922 | - | - | 0.00448 |
| real/phix_err098007_exact | cov5 (n≈314) | G/\|H\| (lower bound) | greedy[revlex] | 3 | 0.8384 | 0.8920 | - | - | 0.00439 |
| real/phix_err098007_exact | cov5 (n≈314) | G/\|H\| (lower bound) | overlap_graph | 3 | - | - | - | - | 0.00863 |
| real/phix_err098007_exact | cov50 (n≈1668) | G/\|H\| (lower bound) | greedy[first] | 3 | 0.9827 | 0.9848 | - | - | 0.14631 |
| real/phix_err098007_exact | cov50 (n≈1668) | G/\|H\| (lower bound) | greedy[last] | 3 | 0.9827 | 0.9848 | - | - | 0.13163 |
| real/phix_err098007_exact | cov50 (n≈1668) | G/\|H\| (lower bound) | greedy[lex] | 3 | 0.9827 | 0.9848 | - | - | 0.13289 |
| real/phix_err098007_exact | cov50 (n≈1668) | G/\|H\| (lower bound) | greedy[random] | 3 | 0.9827 | 0.9848 | - | - | 0.13402 |
| real/phix_err098007_exact | cov50 (n≈1668) | G/\|H\| (lower bound) | greedy[revlex] | 3 | 0.9828 | 0.9848 | - | - | 0.13386 |
| real/phix_err098007_exact | cov50 (n≈1668) | G/\|H\| (lower bound) | overlap_graph | 3 | - | - | - | - | 0.08032 |
| real/phix_err098007_exact | covall (n≈3050) | G/\|H\| (lower bound) | greedy[first] | 1 | 0.9852 | 0.9852 | - | - | 0.47075 |
| real/phix_err098007_exact | covall (n≈3050) | G/\|H\| (lower bound) | greedy[last] | 1 | 0.9852 | 0.9852 | - | - | 0.43641 |
| real/phix_err098007_exact | covall (n≈3050) | G/\|H\| (lower bound) | greedy[lex] | 1 | 0.9852 | 0.9852 | - | - | 0.44129 |
| real/phix_err098007_exact | covall (n≈3050) | G/\|H\| (lower bound) | greedy[random] | 1 | 0.9852 | 0.9852 | - | - | 0.44047 |
| real/phix_err098007_exact | covall (n≈3050) | G/\|H\| (lower bound) | greedy[revlex] | 1 | 0.9852 | 0.9852 | - | - | 0.43925 |
| real/phix_err098007_exact | covall (n≈3050) | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.22615 |
| real/phix_err098007_raw | n1000 (n≈903) | no OPT | greedy[first] | 3 | - | - | - | - | 0.04019 |
| real/phix_err098007_raw | n1000 (n≈903) | no OPT | greedy[last] | 3 | - | - | - | - | 0.03509 |
| real/phix_err098007_raw | n1000 (n≈903) | no OPT | greedy[lex] | 3 | - | - | - | - | 0.03451 |
| real/phix_err098007_raw | n1000 (n≈903) | no OPT | greedy[random] | 3 | - | - | - | - | 0.03643 |
| real/phix_err098007_raw | n1000 (n≈903) | no OPT | greedy[revlex] | 3 | - | - | - | - | 0.03584 |
| real/phix_err098007_raw | n1000 (n≈903) | no OPT | overlap_graph | 3 | - | - | - | - | 0.03045 |
| real/phix_err098007_raw | n2000 (n≈1681) | no OPT | greedy[first] | 3 | - | - | - | - | 0.14036 |
| real/phix_err098007_raw | n2000 (n≈1681) | no OPT | greedy[last] | 3 | - | - | - | - | 0.12720 |
| real/phix_err098007_raw | n2000 (n≈1681) | no OPT | greedy[lex] | 3 | - | - | - | - | 0.12710 |
| real/phix_err098007_raw | n2000 (n≈1681) | no OPT | greedy[random] | 3 | - | - | - | - | 0.13113 |
| real/phix_err098007_raw | n2000 (n≈1681) | no OPT | greedy[revlex] | 3 | - | - | - | - | 0.12804 |
| real/phix_err098007_raw | n2000 (n≈1681) | no OPT | overlap_graph | 3 | - | - | - | - | 0.07237 |
| real/phix_err098007_raw | n500 (n≈472) | no OPT | greedy[first] | 3 | - | - | - | - | 0.00960 |
| real/phix_err098007_raw | n500 (n≈472) | no OPT | greedy[last] | 3 | - | - | - | - | 0.00923 |
| real/phix_err098007_raw | n500 (n≈472) | no OPT | greedy[lex] | 3 | - | - | - | - | 0.00919 |
| real/phix_err098007_raw | n500 (n≈472) | no OPT | greedy[random] | 3 | - | - | - | - | 0.00960 |
| real/phix_err098007_raw | n500 (n≈472) | no OPT | greedy[revlex] | 3 | - | - | - | - | 0.00933 |
| real/phix_err098007_raw | n500 (n≈472) | no OPT | overlap_graph | 3 | - | - | - | - | 0.01397 |
| real/sim_lambda_errfree | len100_cov10 (n≈4594) | G/\|H\| (lower bound) | greedy[first] | 1 | 1.0000 | 1 | - | - | 0.60291 |
| real/sim_lambda_errfree | len100_cov10 (n≈4594) | G/\|H\| (lower bound) | greedy[last] | 1 | 1.0000 | 1 | - | - | 0.54982 |
| real/sim_lambda_errfree | len100_cov10 (n≈4594) | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.55319 |
| real/sim_lambda_errfree | len100_cov10 (n≈4594) | G/\|H\| (lower bound) | greedy[random] | 1 | 1.0000 | 1 | - | - | 0.55815 |
| real/sim_lambda_errfree | len100_cov10 (n≈4594) | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.0000 | 1 | - | - | 0.55707 |
| real/sim_lambda_errfree | len100_cov10 (n≈4594) | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 14.82790 |
| real/sim_lambda_errfree | len100_cov5 (n≈2362) | G/\|H\| (lower bound) | greedy[first] | 1 | 0.9892 | 0.9892 | - | - | 0.24460 |
| real/sim_lambda_errfree | len100_cov5 (n≈2362) | G/\|H\| (lower bound) | greedy[last] | 1 | 0.9892 | 0.9892 | - | - | 0.23408 |
| real/sim_lambda_errfree | len100_cov5 (n≈2362) | G/\|H\| (lower bound) | greedy[lex] | 1 | 0.9892 | 0.9892 | - | - | 0.23391 |
| real/sim_lambda_errfree | len100_cov5 (n≈2362) | G/\|H\| (lower bound) | greedy[random] | 1 | 0.9892 | 0.9892 | - | - | 0.23794 |
| real/sim_lambda_errfree | len100_cov5 (n≈2362) | G/\|H\| (lower bound) | greedy[revlex] | 1 | 0.9892 | 0.9892 | - | - | 0.23456 |
| real/sim_lambda_errfree | len100_cov5 (n≈2362) | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.14080 |
| real/sim_phix_err1pct | len100_cov10 (n≈534) | no OPT | greedy[first] | 2 | - | - | - | - | 0.01232 |
| real/sim_phix_err1pct | len100_cov10 (n≈534) | no OPT | greedy[last] | 2 | - | - | - | - | 0.01202 |
| real/sim_phix_err1pct | len100_cov10 (n≈534) | no OPT | greedy[lex] | 2 | - | - | - | - | 0.01419 |
| real/sim_phix_err1pct | len100_cov10 (n≈534) | no OPT | greedy[random] | 2 | - | - | - | - | 0.01229 |
| real/sim_phix_err1pct | len100_cov10 (n≈534) | no OPT | greedy[revlex] | 2 | - | - | - | - | 0.01205 |
| real/sim_phix_err1pct | len100_cov10 (n≈534) | no OPT | overlap_graph | 2 | - | - | - | - | 0.01938 |
| real/sim_phix_errfree | len100_cov10 (n≈514) | G/\|H\| (lower bound) | greedy[first] | 2 | 0.9883 | 0.9916 | - | - | 0.00642 |
| real/sim_phix_errfree | len100_cov10 (n≈514) | G/\|H\| (lower bound) | greedy[last] | 2 | 0.9883 | 0.9916 | - | - | 0.00570 |
| real/sim_phix_errfree | len100_cov10 (n≈514) | G/\|H\| (lower bound) | greedy[lex] | 2 | 0.9883 | 0.9916 | - | - | 0.00824 |
| real/sim_phix_errfree | len100_cov10 (n≈514) | G/\|H\| (lower bound) | greedy[random] | 2 | 0.9883 | 0.9916 | - | - | 0.00599 |
| real/sim_phix_errfree | len100_cov10 (n≈514) | G/\|H\| (lower bound) | greedy[revlex] | 2 | 0.9883 | 0.9916 | - | - | 0.00590 |
| real/sim_phix_errfree | len100_cov10 (n≈514) | G/\|H\| (lower bound) | overlap_graph | 2 | - | - | - | - | 0.01871 |
| real/sim_phix_errfree | len100_cov20 (n≈968) | G/\|H\| (lower bound) | greedy[first] | 2 | 0.9960 | 0.9974 | - | - | 0.02825 |
| real/sim_phix_errfree | len100_cov20 (n≈968) | G/\|H\| (lower bound) | greedy[last] | 2 | 0.9960 | 0.9974 | - | - | 0.02121 |
| real/sim_phix_errfree | len100_cov20 (n≈968) | G/\|H\| (lower bound) | greedy[lex] | 2 | 0.9960 | 0.9974 | - | - | 0.02180 |
| real/sim_phix_errfree | len100_cov20 (n≈968) | G/\|H\| (lower bound) | greedy[random] | 2 | 0.9960 | 0.9974 | - | - | 0.02196 |
| real/sim_phix_errfree | len100_cov20 (n≈968) | G/\|H\| (lower bound) | greedy[revlex] | 2 | 0.9960 | 0.9974 | - | - | 0.02116 |
| real/sim_phix_errfree | len100_cov20 (n≈968) | G/\|H\| (lower bound) | overlap_graph | 2 | - | - | - | - | 0.04408 |
| real/sim_phix_errfree | len100_cov5 (n≈264) | G/\|H\| (lower bound) | greedy[first] | 2 | 0.9819 | 0.9875 | - | - | 0.00261 |
| real/sim_phix_errfree | len100_cov5 (n≈264) | G/\|H\| (lower bound) | greedy[last] | 2 | 0.9819 | 0.9875 | - | - | 0.00223 |
| real/sim_phix_errfree | len100_cov5 (n≈264) | G/\|H\| (lower bound) | greedy[lex] | 2 | 0.9819 | 0.9875 | - | - | 0.00224 |
| real/sim_phix_errfree | len100_cov5 (n≈264) | G/\|H\| (lower bound) | greedy[random] | 2 | 0.9819 | 0.9875 | - | - | 0.00235 |
| real/sim_phix_errfree | len100_cov5 (n≈264) | G/\|H\| (lower bound) | greedy[revlex] | 2 | 0.9819 | 0.9875 | - | - | 0.00232 |
| real/sim_phix_errfree | len100_cov5 (n≈264) | G/\|H\| (lower bound) | overlap_graph | 2 | - | - | - | - | 0.00842 |
| real/sim_phix_errfree | len100_cov50 (n≈2104) | G/\|H\| (lower bound) | greedy[first] | 1 | 0.9971 | 0.9971 | - | - | 0.12684 |
| real/sim_phix_errfree | len100_cov50 (n≈2104) | G/\|H\| (lower bound) | greedy[last] | 1 | 0.9971 | 0.9971 | - | - | 0.10739 |
| real/sim_phix_errfree | len100_cov50 (n≈2104) | G/\|H\| (lower bound) | greedy[lex] | 1 | 0.9971 | 0.9971 | - | - | 0.11063 |
| real/sim_phix_errfree | len100_cov50 (n≈2104) | G/\|H\| (lower bound) | greedy[random] | 1 | 0.9971 | 0.9971 | - | - | 0.11157 |
| real/sim_phix_errfree | len100_cov50 (n≈2104) | G/\|H\| (lower bound) | greedy[revlex] | 1 | 0.9971 | 0.9971 | - | - | 0.11024 |
| real/sim_phix_errfree | len100_cov50 (n≈2104) | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.13885 |
| real/sim_phix_errfree | len50_cov10 (n≈966) | G/\|H\| (lower bound) | greedy[first] | 2 | 0.9916 | 0.9930 | - | - | 0.02334 |
| real/sim_phix_errfree | len50_cov10 (n≈966) | G/\|H\| (lower bound) | greedy[last] | 2 | 0.9916 | 0.9930 | - | - | 0.02032 |
| real/sim_phix_errfree | len50_cov10 (n≈966) | G/\|H\| (lower bound) | greedy[lex] | 2 | 0.9916 | 0.9930 | - | - | 0.02087 |
| real/sim_phix_errfree | len50_cov10 (n≈966) | G/\|H\| (lower bound) | greedy[random] | 2 | 0.9916 | 0.9930 | - | - | 0.02115 |
| real/sim_phix_errfree | len50_cov10 (n≈966) | G/\|H\| (lower bound) | greedy[revlex] | 2 | 0.9916 | 0.9930 | - | - | 0.02167 |
| real/sim_phix_errfree | len50_cov10 (n≈966) | G/\|H\| (lower bound) | overlap_graph | 2 | - | - | - | - | 0.02442 |
| real/sim_sars2_errfree | len100_cov10 (n≈2846) | G/\|H\| (lower bound) | greedy[first] | 2 | 1.0000 | 1 | - | - | 0.24006 |
| real/sim_sars2_errfree | len100_cov10 (n≈2846) | G/\|H\| (lower bound) | greedy[last] | 2 | 1.0000 | 1 | - | - | 0.21083 |
| real/sim_sars2_errfree | len100_cov10 (n≈2846) | G/\|H\| (lower bound) | greedy[lex] | 2 | 1.0000 | 1 | - | - | 0.20573 |
| real/sim_sars2_errfree | len100_cov10 (n≈2846) | G/\|H\| (lower bound) | greedy[random] | 2 | 1.0000 | 1 | - | - | 0.20806 |
| real/sim_sars2_errfree | len100_cov10 (n≈2846) | G/\|H\| (lower bound) | greedy[revlex] | 2 | 1.0000 | 1 | - | - | 0.20953 |
| real/sim_sars2_errfree | len100_cov10 (n≈2846) | G/\|H\| (lower bound) | overlap_graph | 2 | - | - | - | - | 0.23645 |
| real/sim_sars2_errfree | len100_cov5 (n≈1458) | G/\|H\| (lower bound) | greedy[first] | 2 | 0.9916 | 0.9930 | - | - | 0.10472 |
| real/sim_sars2_errfree | len100_cov5 (n≈1458) | G/\|H\| (lower bound) | greedy[last] | 2 | 0.9916 | 0.9930 | - | - | 0.09677 |
| real/sim_sars2_errfree | len100_cov5 (n≈1458) | G/\|H\| (lower bound) | greedy[lex] | 2 | 0.9917 | 0.9930 | - | - | 0.09736 |
| real/sim_sars2_errfree | len100_cov5 (n≈1458) | G/\|H\| (lower bound) | greedy[random] | 2 | 0.9917 | 0.9930 | - | - | 0.09948 |
| real/sim_sars2_errfree | len100_cov5 (n≈1458) | G/\|H\| (lower bound) | greedy[revlex] | 2 | 0.9916 | 0.9930 | - | - | 0.09618 |
| real/sim_sars2_errfree | len100_cov5 (n≈1458) | G/\|H\| (lower bound) | overlap_graph | 2 | - | - | - | - | 0.07616 |

## Tie sensitivity

| group | n | basis | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | mean tie steps | mean ratio (first) | max ratio observed | max ratio all ties |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| real/phix_err098007_exact | cov10 (n≈571) | G/\|H\| (lower bound) | 3 | none | 1.000 | 2.67 | - | - | 0.9394 | 0.9485 | - |
| real/phix_err098007_exact | cov20 (n≈951) | G/\|H\| (lower bound) | 3 | none | 0.333 | 1.33 | - | - | 0.9778 | 0.9809 | - |
| real/phix_err098007_exact | cov5 (n≈314) | G/\|H\| (lower bound) | 3 | none | 0.333 | 1.33 | - | - | 0.8385 | 0.8922 | - |
| real/phix_err098007_exact | cov50 (n≈1668) | G/\|H\| (lower bound) | 3 | none | 0.333 | 1.33 | - | - | 0.9827 | 0.9848 | - |
| real/phix_err098007_exact | covall (n≈3050) | G/\|H\| (lower bound) | 1 | none | 0.000 | 1.00 | - | - | 0.9852 | 0.9852 | - |
| real/phix_err098007_raw | n1000 (n≈903) | no OPT | 3 | none | 0.333 | 1.33 | - | - | - | - | - |
| real/phix_err098007_raw | n2000 (n≈1681) | no OPT | 3 | none | 1.000 | 2.00 | - | - | - | - | - |
| real/phix_err098007_raw | n500 (n≈472) | no OPT | 3 | none | 0.667 | 2.33 | - | - | - | - | - |
| real/sim_lambda_errfree | len100_cov10 (n≈4594) | G/\|H\| (lower bound) | 1 | none | 0.000 | 1.00 | - | - | 1.0000 | 1 | - |
| real/sim_lambda_errfree | len100_cov5 (n≈2362) | G/\|H\| (lower bound) | 1 | none | 0.000 | 1.00 | - | - | 0.9892 | 0.9892 | - |
| real/sim_phix_err1pct | len100_cov10 (n≈534) | no OPT | 2 | none | 1.000 | 1.50 | - | - | - | - | - |
| real/sim_phix_errfree | len100_cov10 (n≈514) | G/\|H\| (lower bound) | 2 | none | 0.000 | 1.00 | - | - | 0.9883 | 0.9916 | - |
| real/sim_phix_errfree | len100_cov20 (n≈968) | G/\|H\| (lower bound) | 2 | none | 0.000 | 1.00 | - | - | 0.9960 | 0.9974 | - |
| real/sim_phix_errfree | len100_cov5 (n≈264) | G/\|H\| (lower bound) | 2 | none | 0.000 | 1.00 | - | - | 0.9819 | 0.9875 | - |
| real/sim_phix_errfree | len100_cov50 (n≈2104) | G/\|H\| (lower bound) | 1 | none | 0.000 | 1.00 | - | - | 0.9971 | 0.9971 | - |
| real/sim_phix_errfree | len50_cov10 (n≈966) | G/\|H\| (lower bound) | 2 | none | 0.000 | 1.00 | - | - | 0.9916 | 0.9930 | - |
| real/sim_sars2_errfree | len100_cov10 (n≈2846) | G/\|H\| (lower bound) | 2 | none | 0.000 | 1.00 | - | - | 1.0000 | 1 | - |
| real/sim_sars2_errfree | len100_cov5 (n≈1458) | G/\|H\| (lower bound) | 2 | none | 1.000 | 2.50 | - | - | 0.9916 | 0.9930 | - |

## Assembly metrics (genome instances, rule `first`)

G / genome length is descriptive, not a bound.  *Reconstructs*: the output equals the reference stretch H.  *Misjoin-free*: the output is a contiguous piece of H.  Both are computed only for gapless error-free reads, where H is the true genome stretch.

| group | n | basis | inst | mean G/genome | reconstructs | misjoin-free | mean ratio (first) |
|---|---:|---|---:|---:|---:|---:|---:|
| real/phix_err098007_exact | cov10 (n≈571) | G/\|H\| (lower bound) | 3 | 0.9449 | - | - | 0.9394 |
| real/phix_err098007_exact | cov20 (n≈951) | G/\|H\| (lower bound) | 3 | 0.9822 | - | - | 0.9778 |
| real/phix_err098007_exact | cov5 (n≈314) | G/\|H\| (lower bound) | 3 | 0.8399 | - | - | 0.8385 |
| real/phix_err098007_exact | cov50 (n≈1668) | G/\|H\| (lower bound) | 3 | 0.9943 | - | - | 0.9827 |
| real/phix_err098007_exact | covall (n≈3050) | G/\|H\| (lower bound) | 1 | 0.9981 | - | - | 0.9852 |
| real/phix_err098007_raw | n1000 (n≈903) | no OPT | 3 | 6.2234 | - | - | - |
| real/phix_err098007_raw | n2000 (n≈1681) | no OPT | 3 | 11.3970 | - | - | - |
| real/phix_err098007_raw | n500 (n≈472) | no OPT | 3 | 3.5789 | - | - | - |
| real/sim_lambda_errfree | len100_cov10 (n≈4594) | G/\|H\| (lower bound) | 1 | 0.9999 | 1.000 | 1.000 | 1.0000 |
| real/sim_lambda_errfree | len100_cov5 (n≈2362) | G/\|H\| (lower bound) | 1 | 0.9878 | - | - | 0.9892 |
| real/sim_phix_err1pct | len100_cov10 (n≈534) | no OPT | 2 | 5.9169 | - | - | - |
| real/sim_phix_errfree | len100_cov10 (n≈514) | G/\|H\| (lower bound) | 2 | 1.0041 | 1.000 | 1.000 | 0.9883 |
| real/sim_phix_errfree | len100_cov20 (n≈968) | G/\|H\| (lower bound) | 2 | 1.0126 | 1.000 | 1.000 | 0.9960 |
| real/sim_phix_errfree | len100_cov5 (n≈264) | G/\|H\| (lower bound) | 2 | 0.9967 | 1.000 | 1.000 | 0.9819 |
| real/sim_phix_errfree | len100_cov50 (n≈2104) | G/\|H\| (lower bound) | 1 | 1.0152 | 1.000 | 1.000 | 0.9971 |
| real/sim_phix_errfree | len50_cov10 (n≈966) | G/\|H\| (lower bound) | 2 | 1.0004 | 1.000 | 1.000 | 0.9916 |
| real/sim_sars2_errfree | len100_cov10 (n≈2846) | G/\|H\| (lower bound) | 2 | 0.9993 | 1.000 | 1.000 | 1.0000 |
| real/sim_sars2_errfree | len100_cov5 (n≈1458) | G/\|H\| (lower bound) | 2 | 0.9906 | - | - | 0.9916 |
