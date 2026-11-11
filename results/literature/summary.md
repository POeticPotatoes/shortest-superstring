# Benchmark summary: `results/literature`

54 instances, 5839 solver runs.

## Solution quality and runtime

Ratio basis `G/OPT` uses an exact optimum (DP or certificate).  `G/|H| (lower bound)` uses a known common superstring H >= OPT, so it is a certified lower bound on G/OPT; these rows are reported separately.

| group | n | basis | algo | inst | mean ratio | max ratio | min compr. ratio | optimal rate | mean time (s) |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| chukhin_k10_t1 | 17 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| chukhin_k10_t1 | 17 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.63965 |
| chukhin_k10_t1 | 17 | G/OPT | greedy[first] | 1 | 1.1154 | 1.1154 | 0.9792 | 0.000 | 0.00007 |
| chukhin_k10_t1 | 17 | G/OPT | greedy[last] | 1 | 1.1154 | 1.1154 | 0.9792 | 0.000 | 0.00004 |
| chukhin_k10_t1 | 17 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k10_t1 | 17 | G/OPT | greedy[paper] | 1 | 1.3077 | 1.3077 | 0.9444 | 0.000 | 0.00006 |
| chukhin_k10_t1 | 17 | G/OPT | greedy[random] | 1 | 1.1131 | 1.3077 | 0.9444 | 0.500 | 0.00004 |
| chukhin_k10_t1 | 17 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| chukhin_k10_t1 | 17 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00005 |
| chukhin_k3_t1 | 5 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00007 |
| chukhin_k3_t1 | 5 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| chukhin_k3_t1 | 5 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| chukhin_k3_t1 | 5 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k3_t1 | 5 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| chukhin_k3_t1 | 5 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| chukhin_k3_t1 | 5 | G/OPT | greedy[paper] | 1 | 1.2857 | 1.2857 | 0.7500 | 0.000 | 0.00002 |
| chukhin_k3_t1 | 5 | G/OPT | greedy[random] | 1 | 1.0943 | 1.2857 | 0.7500 | 0.590 | 0.00001 |
| chukhin_k3_t1 | 5 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| chukhin_k3_t1 | 5 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00023 |
| chukhin_k3_t1 | 5 | G/OPT | greedy_worst_tie | 1 | 1.2857 | 1.2857 | 0.7500 | 0.000 | 0.00023 |
| chukhin_k3_t1 | 5 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00000 |
| chukhin_k3_t10 | 50 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| chukhin_k3_t10 | 50 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00010 |
| chukhin_k3_t10 | 50 | G/OPT | greedy[last] | 1 | 1.3461 | 1.3461 | 0.8163 | 0.000 | 0.00015 |
| chukhin_k3_t10 | 50 | G/OPT | greedy[lex] | 1 | 1.3461 | 1.3461 | 0.8163 | 0.000 | 0.00016 |
| chukhin_k3_t10 | 50 | G/OPT | greedy[paper] | 1 | 1.7308 | 1.7308 | 0.6122 | 0.000 | 0.00031 |
| chukhin_k3_t10 | 50 | G/OPT | greedy[random] | 1 | 1.1948 | 1.3269 | 0.8265 | 0.000 | 0.00019 |
| chukhin_k3_t10 | 50 | G/OPT | greedy[revlex] | 1 | 1.3846 | 1.3846 | 0.7959 | 0.000 | 0.00017 |
| chukhin_k3_t10 | 50 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00005 |
| chukhin_k3_t2 | 10 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k3_t2 | 10 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00218 |
| chukhin_k3_t2 | 10 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k3_t2 | 10 | G/OPT | greedy[last] | 1 | 1.1667 | 1.1667 | 0.8889 | 0.000 | 0.00002 |
| chukhin_k3_t2 | 10 | G/OPT | greedy[lex] | 1 | 1.1667 | 1.1667 | 0.8889 | 0.000 | 0.00002 |
| chukhin_k3_t2 | 10 | G/OPT | greedy[paper] | 1 | 1.5000 | 1.5000 | 0.6667 | 0.000 | 0.00003 |
| chukhin_k3_t2 | 10 | G/OPT | greedy[random] | 1 | 1.1950 | 1.5000 | 0.6667 | 0.060 | 0.00002 |
| chukhin_k3_t2 | 10 | G/OPT | greedy[revlex] | 1 | 1.3333 | 1.3333 | 0.7778 | 0.000 | 0.00002 |
| chukhin_k3_t2 | 10 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.02915 |
| chukhin_k3_t2 | 10 | G/OPT | greedy_worst_tie | 1 | 1.5000 | 1.5000 | 0.6667 | 0.000 | 0.02915 |
| chukhin_k3_t2 | 10 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00001 |
| chukhin_k3_t20 | 100 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00010 |
| chukhin_k3_t20 | 100 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00039 |
| chukhin_k3_t20 | 100 | G/OPT | greedy[last] | 1 | 1.3725 | 1.3725 | 0.8081 | 0.000 | 0.00054 |
| chukhin_k3_t20 | 100 | G/OPT | greedy[lex] | 1 | 1.2745 | 1.2745 | 0.8586 | 0.000 | 0.00051 |
| chukhin_k3_t20 | 100 | G/OPT | greedy[paper] | 1 | 1.7647 | 1.7647 | 0.6061 | 0.000 | 0.00110 |
| chukhin_k3_t20 | 100 | G/OPT | greedy[random] | 1 | 1.1900 | 1.2843 | 0.8535 | 0.000 | 0.00065 |
| chukhin_k3_t20 | 100 | G/OPT | greedy[revlex] | 1 | 1.3823 | 1.3823 | 0.8030 | 0.000 | 0.00058 |
| chukhin_k3_t20 | 100 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00012 |
| chukhin_k3_t3 | 15 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k3_t3 | 15 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.13042 |
| chukhin_k3_t3 | 15 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| chukhin_k3_t3 | 15 | G/OPT | greedy[last] | 1 | 1.2353 | 1.2353 | 0.8571 | 0.000 | 0.00003 |
| chukhin_k3_t3 | 15 | G/OPT | greedy[lex] | 1 | 1.2353 | 1.2353 | 0.8571 | 0.000 | 0.00003 |
| chukhin_k3_t3 | 15 | G/OPT | greedy[paper] | 1 | 1.5882 | 1.5882 | 0.6429 | 0.000 | 0.00005 |
| chukhin_k3_t3 | 15 | G/OPT | greedy[random] | 1 | 1.1876 | 1.4118 | 0.7500 | 0.070 | 0.00004 |
| chukhin_k3_t3 | 15 | G/OPT | greedy[revlex] | 1 | 1.3529 | 1.3529 | 0.7857 | 0.000 | 0.00004 |
| chukhin_k3_t3 | 15 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00001 |
| chukhin_k3_t5 | 25 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k3_t5 | 25 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| chukhin_k3_t5 | 25 | G/OPT | greedy[last] | 1 | 1.2963 | 1.2963 | 0.8333 | 0.000 | 0.00006 |
| chukhin_k3_t5 | 25 | G/OPT | greedy[lex] | 1 | 1.2963 | 1.2963 | 0.8333 | 0.000 | 0.00006 |
| chukhin_k3_t5 | 25 | G/OPT | greedy[paper] | 1 | 1.6667 | 1.6667 | 0.6250 | 0.000 | 0.00009 |
| chukhin_k3_t5 | 25 | G/OPT | greedy[random] | 1 | 1.1959 | 1.4444 | 0.7500 | 0.020 | 0.00007 |
| chukhin_k3_t5 | 25 | G/OPT | greedy[revlex] | 1 | 1.3704 | 1.3704 | 0.7917 | 0.000 | 0.00006 |
| chukhin_k3_t5 | 25 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00002 |
| chukhin_k6_t1 | 9 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k6_t1 | 9 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00097 |
| chukhin_k6_t1 | 9 | G/OPT | greedy[first] | 1 | 1.2143 | 1.2143 | 0.9250 | 0.000 | 0.00003 |
| chukhin_k6_t1 | 9 | G/OPT | greedy[last] | 1 | 1.2143 | 1.2143 | 0.9250 | 0.000 | 0.00002 |
| chukhin_k6_t1 | 9 | G/OPT | greedy[lex] | 1 | 1.2143 | 1.2143 | 0.9250 | 0.000 | 0.00002 |
| chukhin_k6_t1 | 9 | G/OPT | greedy[paper] | 1 | 1.2857 | 1.2857 | 0.9000 | 0.000 | 0.00002 |
| chukhin_k6_t1 | 9 | G/OPT | greedy[random] | 1 | 1.0864 | 1.2857 | 0.9000 | 0.530 | 0.00002 |
| chukhin_k6_t1 | 9 | G/OPT | greedy[revlex] | 1 | 1.0714 | 1.0714 | 0.9750 | 0.000 | 0.00002 |
| chukhin_k6_t1 | 9 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00551 |
| chukhin_k6_t1 | 9 | G/OPT | greedy_worst_tie | 1 | 1.2857 | 1.2857 | 0.9000 | 0.000 | 0.00551 |
| chukhin_k6_t1 | 9 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00001 |
| chukhin_k6_t10 | 90 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00008 |
| chukhin_k6_t10 | 90 | G/OPT | greedy[first] | 1 | 1.3158 | 1.3158 | 0.9326 | 0.000 | 0.00045 |
| chukhin_k6_t10 | 90 | G/OPT | greedy[last] | 1 | 1.7895 | 1.7895 | 0.8315 | 0.000 | 0.00055 |
| chukhin_k6_t10 | 90 | G/OPT | greedy[lex] | 1 | 1.6947 | 1.6947 | 0.8517 | 0.000 | 0.00055 |
| chukhin_k6_t10 | 90 | G/OPT | greedy[paper] | 1 | 1.8947 | 1.8947 | 0.8090 | 0.000 | 0.00060 |
| chukhin_k6_t10 | 90 | G/OPT | greedy[random] | 1 | 1.2796 | 1.4632 | 0.9011 | 0.000 | 0.00057 |
| chukhin_k6_t10 | 90 | G/OPT | greedy[revlex] | 1 | 1.3158 | 1.3158 | 0.9326 | 0.000 | 0.00044 |
| chukhin_k6_t10 | 90 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00019 |
| chukhin_k6_t2 | 18 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| chukhin_k6_t2 | 18 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 1.42887 |
| chukhin_k6_t2 | 18 | G/OPT | greedy[first] | 1 | 1.2609 | 1.2609 | 0.9294 | 0.000 | 0.00006 |
| chukhin_k6_t2 | 18 | G/OPT | greedy[last] | 1 | 1.4783 | 1.4783 | 0.8706 | 0.000 | 0.00005 |
| chukhin_k6_t2 | 18 | G/OPT | greedy[lex] | 1 | 1.4348 | 1.4348 | 0.8824 | 0.000 | 0.00004 |
| chukhin_k6_t2 | 18 | G/OPT | greedy[paper] | 1 | 1.5652 | 1.5652 | 0.8471 | 0.000 | 0.00005 |
| chukhin_k6_t2 | 18 | G/OPT | greedy[random] | 1 | 1.2100 | 1.5217 | 0.8588 | 0.090 | 0.00005 |
| chukhin_k6_t2 | 18 | G/OPT | greedy[revlex] | 1 | 1.2609 | 1.2609 | 0.9294 | 0.000 | 0.00004 |
| chukhin_k6_t2 | 18 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00004 |
| chukhin_k6_t3 | 27 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k6_t3 | 27 | G/OPT | greedy[first] | 1 | 1.2812 | 1.2812 | 0.9308 | 0.000 | 0.00007 |
| chukhin_k6_t3 | 27 | G/OPT | greedy[last] | 1 | 1.5938 | 1.5938 | 0.8538 | 0.000 | 0.00008 |
| chukhin_k6_t3 | 27 | G/OPT | greedy[lex] | 1 | 1.5312 | 1.5312 | 0.8692 | 0.000 | 0.00010 |
| chukhin_k6_t3 | 27 | G/OPT | greedy[paper] | 1 | 1.6875 | 1.6875 | 0.8308 | 0.000 | 0.00009 |
| chukhin_k6_t3 | 27 | G/OPT | greedy[random] | 1 | 1.2450 | 1.5000 | 0.8769 | 0.040 | 0.00008 |
| chukhin_k6_t3 | 27 | G/OPT | greedy[revlex] | 1 | 1.2812 | 1.2812 | 0.9308 | 0.000 | 0.00007 |
| chukhin_k6_t3 | 27 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00005 |
| chukhin_k6_t5 | 45 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| chukhin_k6_t5 | 45 | G/OPT | greedy[first] | 1 | 1.3000 | 1.3000 | 0.9318 | 0.000 | 0.00014 |
| chukhin_k6_t5 | 45 | G/OPT | greedy[last] | 1 | 1.7000 | 1.7000 | 0.8409 | 0.000 | 0.00016 |
| chukhin_k6_t5 | 45 | G/OPT | greedy[lex] | 1 | 1.6200 | 1.6200 | 0.8591 | 0.000 | 0.00016 |
| chukhin_k6_t5 | 45 | G/OPT | greedy[paper] | 1 | 1.8000 | 1.8000 | 0.8182 | 0.000 | 0.00018 |
| chukhin_k6_t5 | 45 | G/OPT | greedy[random] | 1 | 1.2702 | 1.5400 | 0.8773 | 0.020 | 0.00018 |
| chukhin_k6_t5 | 45 | G/OPT | greedy[revlex] | 1 | 1.3000 | 1.3000 | 0.9318 | 0.000 | 0.00014 |
| chukhin_k6_t5 | 45 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00009 |
| chukhin_k7_t1 | 11 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k7_t1 | 11 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00514 |
| chukhin_k7_t1 | 11 | G/OPT | greedy[first] | 1 | 1.1765 | 1.1765 | 0.9500 | 0.000 | 0.00003 |
| chukhin_k7_t1 | 11 | G/OPT | greedy[last] | 1 | 1.1765 | 1.1765 | 0.9500 | 0.000 | 0.00002 |
| chukhin_k7_t1 | 11 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k7_t1 | 11 | G/OPT | greedy[paper] | 1 | 1.2941 | 1.2941 | 0.9167 | 0.000 | 0.00003 |
| chukhin_k7_t1 | 11 | G/OPT | greedy[random] | 1 | 1.1176 | 1.2941 | 0.9167 | 0.430 | 0.00002 |
| chukhin_k7_t1 | 11 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k7_t1 | 11 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.02847 |
| chukhin_k7_t1 | 11 | G/OPT | greedy_worst_tie | 1 | 1.2941 | 1.2941 | 0.9167 | 0.000 | 0.02847 |
| chukhin_k7_t1 | 11 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00002 |
| chukhin_k8_t1 | 13 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k8_t1 | 13 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.02668 |
| chukhin_k8_t1 | 13 | G/OPT | greedy[first] | 1 | 1.1500 | 1.1500 | 0.9643 | 0.000 | 0.00004 |
| chukhin_k8_t1 | 13 | G/OPT | greedy[last] | 1 | 1.1500 | 1.1500 | 0.9643 | 0.000 | 0.00003 |
| chukhin_k8_t1 | 13 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k8_t1 | 13 | G/OPT | greedy[paper] | 1 | 1.3000 | 1.3000 | 0.9286 | 0.000 | 0.00004 |
| chukhin_k8_t1 | 13 | G/OPT | greedy[random] | 1 | 1.0965 | 1.3000 | 0.9286 | 0.510 | 0.00003 |
| chukhin_k8_t1 | 13 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k8_t1 | 13 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00003 |
| chukhin_k8_t2 | 26 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k8_t2 | 26 | G/OPT | greedy[first] | 1 | 1.3333 | 1.3333 | 0.9371 | 0.000 | 0.00007 |
| chukhin_k8_t2 | 26 | G/OPT | greedy[last] | 1 | 1.3939 | 1.3939 | 0.9257 | 0.000 | 0.00007 |
| chukhin_k8_t2 | 26 | G/OPT | greedy[lex] | 1 | 1.3939 | 1.3939 | 0.9257 | 0.000 | 0.00007 |
| chukhin_k8_t2 | 26 | G/OPT | greedy[paper] | 1 | 1.5758 | 1.5758 | 0.8914 | 0.000 | 0.00008 |
| chukhin_k8_t2 | 26 | G/OPT | greedy[random] | 1 | 1.2330 | 1.5151 | 0.9029 | 0.080 | 0.00007 |
| chukhin_k8_t2 | 26 | G/OPT | greedy[revlex] | 1 | 1.5151 | 1.5151 | 0.9029 | 0.000 | 0.00008 |
| chukhin_k8_t2 | 26 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00006 |
| chukhin_k8_t5 | 65 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| chukhin_k8_t5 | 65 | G/OPT | greedy[first] | 1 | 1.4861 | 1.4861 | 0.9219 | 0.000 | 0.00025 |
| chukhin_k8_t5 | 65 | G/OPT | greedy[last] | 1 | 1.5972 | 1.5972 | 0.9040 | 0.000 | 0.00029 |
| chukhin_k8_t5 | 65 | G/OPT | greedy[lex] | 1 | 1.5972 | 1.5972 | 0.9040 | 0.000 | 0.00029 |
| chukhin_k8_t5 | 65 | G/OPT | greedy[paper] | 1 | 1.8056 | 1.8056 | 0.8705 | 0.000 | 0.00031 |
| chukhin_k8_t5 | 65 | G/OPT | greedy[random] | 1 | 1.2525 | 1.5417 | 0.9129 | 0.010 | 0.00029 |
| chukhin_k8_t5 | 65 | G/OPT | greedy[revlex] | 1 | 1.7361 | 1.7361 | 0.8817 | 0.000 | 0.00030 |
| chukhin_k8_t5 | 65 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00016 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.1451 | 2.1451 | - | - | 0.00046 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[last] | 1 | 2.0581 | 2.0581 | - | - | 0.00041 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.4577 | 1.4577 | - | - | 0.00040 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.1451 | 2.1451 | - | - | 0.00048 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3912 | 1.6809 | - | - | 0.00041 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5156 | 1.5156 | - | - | 0.00039 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.02297 |
| greedy125_r1_P0 | 5 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00011 |
| greedy125_r1_P0 | 5 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00010 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[first] | 1 | 1.2979 | 1.2979 | 0.8158 | 0.000 | 0.00002 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[paper] | 1 | 1.2979 | 1.2979 | 0.8158 | 0.000 | 0.00002 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[random] | 1 | 1.0985 | 1.2979 | 0.8158 | 0.550 | 0.00001 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| greedy125_r1_P0 | 5 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00026 |
| greedy125_r1_P0 | 5 | G/OPT | greedy_worst_tie | 1 | 1.2979 | 1.2979 | 0.8158 | 0.000 | 0.00026 |
| greedy125_r1_P0 | 5 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00003 |
| greedy125_r1_P1 | 5 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00012 |
| greedy125_r1_P1 | 5 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00011 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[first] | 1 | 1.3036 | 1.3036 | 0.8211 | 0.000 | 0.00002 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[last] | 1 | 1.1964 | 1.1964 | 0.8842 | 0.000 | 0.00001 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[paper] | 1 | 1.3036 | 1.3036 | 0.8211 | 0.000 | 0.00002 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[random] | 1 | 1.1170 | 1.3036 | 0.8211 | 0.550 | 0.00001 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| greedy125_r1_P1 | 5 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00013 |
| greedy125_r1_P1 | 5 | G/OPT | greedy_worst_tie | 1 | 1.3036 | 1.3036 | 0.8211 | 0.000 | 0.00013 |
| greedy125_r1_P1 | 5 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00003 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.2559 | 2.2559 | - | - | 0.00164 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[last] | 1 | 2.2097 | 2.2097 | - | - | 0.00155 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.5284 | 1.5284 | - | - | 0.00154 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.2559 | 2.2559 | - | - | 0.00190 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3995 | 1.6810 | - | - | 0.00159 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5580 | 1.5580 | - | - | 0.00151 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.04369 |
| greedy125_r2_P1 | 10 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00240 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[first] | 1 | 1.6313 | 1.6313 | 0.7278 | 0.000 | 0.00004 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[last] | 1 | 1.3188 | 1.3188 | 0.8625 | 0.000 | 0.00003 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[paper] | 1 | 1.6313 | 1.6313 | 0.7278 | 0.000 | 0.00004 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[random] | 1 | 1.2309 | 1.6000 | 0.7412 | 0.200 | 0.00003 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[revlex] | 1 | 1.2437 | 1.2437 | 0.8949 | 0.000 | 0.00003 |
| greedy125_r2_P1 | 10 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00207 |
| greedy125_r2_P1 | 10 | G/OPT | greedy_worst_tie | 1 | 1.6313 | 1.6313 | 0.7278 | 0.000 | 0.00207 |
| greedy125_r2_P1 | 10 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00012 |
| greedy125_r2_P4 | 10 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00264 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[first] | 1 | 1.6485 | 1.6485 | 0.7364 | 0.000 | 0.00004 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[last] | 1 | 1.3267 | 1.3267 | 0.8672 | 0.000 | 0.00003 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[paper] | 1 | 1.6485 | 1.6485 | 0.7364 | 0.000 | 0.00004 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[random] | 1 | 1.2344 | 1.6485 | 0.7364 | 0.130 | 0.00003 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[revlex] | 1 | 1.2376 | 1.2376 | 0.9034 | 0.000 | 0.00003 |
| greedy125_r2_P4 | 10 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00098 |
| greedy125_r2_P4 | 10 | G/OPT | greedy_worst_tie | 1 | 1.6485 | 1.6485 | 0.7364 | 0.000 | 0.00098 |
| greedy125_r2_P4 | 10 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00015 |
| greedy125_r3_P2 | 15 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.14558 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[first] | 1 | 1.7804 | 1.7804 | 0.7035 | 0.000 | 0.00008 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[last] | 1 | 1.5519 | 1.5519 | 0.7903 | 0.000 | 0.00006 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[lex] | 1 | 1.1335 | 1.1335 | 0.9493 | 0.000 | 0.00005 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[paper] | 1 | 1.7804 | 1.7804 | 0.7035 | 0.000 | 0.00007 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[random] | 1 | 1.3058 | 1.6825 | 0.7407 | 0.040 | 0.00005 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[revlex] | 1 | 1.3531 | 1.3531 | 0.8658 | 0.000 | 0.00005 |
| greedy125_r3_P2 | 15 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00028 |
| greedy125_r3_P9 | 15 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.14386 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[first] | 1 | 1.8128 | 1.8128 | 0.7154 | 0.000 | 0.00008 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[last] | 1 | 1.5745 | 1.5745 | 0.7988 | 0.000 | 0.00006 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[lex] | 1 | 1.1702 | 1.1702 | 0.9404 | 0.000 | 0.00005 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[paper] | 1 | 1.8128 | 1.8128 | 0.7154 | 0.000 | 0.00007 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[random] | 1 | 1.2987 | 1.6532 | 0.7712 | 0.060 | 0.00005 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[revlex] | 1 | 1.3425 | 1.3425 | 0.8800 | 0.000 | 0.00006 |
| greedy125_r3_P9 | 15 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00042 |
| greedy125_r4_P16 | 20 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 7.60851 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[first] | 1 | 1.9124 | 1.9124 | 0.7066 | 0.000 | 0.00011 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[last] | 1 | 1.7225 | 1.7225 | 0.7677 | 0.000 | 0.00009 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[lex] | 1 | 1.2663 | 1.2663 | 0.9144 | 0.000 | 0.00008 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[paper] | 1 | 1.9124 | 1.9124 | 0.7066 | 0.000 | 0.00010 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[random] | 1 | 1.3432 | 1.6809 | 0.7811 | 0.000 | 0.00008 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[revlex] | 1 | 1.4011 | 1.4011 | 0.8710 | 0.000 | 0.00008 |
| greedy125_r4_P16 | 20 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00089 |
| greedy125_r4_P3 | 20 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 7.55860 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[first] | 1 | 1.8651 | 1.8651 | 0.6921 | 0.000 | 0.00011 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[last] | 1 | 1.6851 | 1.6851 | 0.7562 | 0.000 | 0.00008 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[lex] | 1 | 1.2422 | 1.2422 | 0.9138 | 0.000 | 0.00007 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[paper] | 1 | 1.8651 | 1.8651 | 0.6921 | 0.000 | 0.00010 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[random] | 1 | 1.3446 | 1.7422 | 0.7358 | 0.000 | 0.00008 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[revlex] | 1 | 1.4152 | 1.4152 | 0.8522 | 0.000 | 0.00008 |
| greedy125_r4_P3 | 20 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00050 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.0264 | 2.0264 | - | - | 0.00018 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.8910 | 1.8910 | - | - | 0.00016 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.3674 | 1.3674 | - | - | 0.00014 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.0264 | 2.0264 | - | - | 0.00018 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3580 | 1.6222 | - | - | 0.00016 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.4608 | 1.4608 | - | - | 0.00015 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.00302 |
| kulikov_collapsing_cex | 5 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00009 |
| kulikov_collapsing_cex | 5 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00009 |
| kulikov_collapsing_cex | 5 | G/OPT | greedy[first] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00002 |
| kulikov_collapsing_cex | 5 | G/OPT | greedy[last] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00001 |
| kulikov_collapsing_cex | 5 | G/OPT | greedy[lex] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00001 |
| kulikov_collapsing_cex | 5 | G/OPT | greedy[random] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00001 |
| kulikov_collapsing_cex | 5 | G/OPT | greedy[revlex] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00002 |
| kulikov_collapsing_cex | 5 | G/OPT | greedy_best_tie | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00006 |
| kulikov_collapsing_cex | 5 | G/OPT | greedy_worst_tie | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00006 |
| kulikov_collapsing_cex | 5 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00002 |
| kulikov_readme_example | 6 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00031 |
| kulikov_readme_example | 6 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00009 |
| kulikov_readme_example | 6 | G/OPT | greedy[first] | 1 | 1.1667 | 1.1667 | 0.7500 | 0.000 | 0.00002 |
| kulikov_readme_example | 6 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| kulikov_readme_example | 6 | G/OPT | greedy[lex] | 1 | 1.1667 | 1.1667 | 0.7500 | 0.000 | 0.00001 |
| kulikov_readme_example | 6 | G/OPT | greedy[random] | 1 | 1.1067 | 1.2500 | 0.6250 | 0.200 | 0.00001 |
| kulikov_readme_example | 6 | G/OPT | greedy[revlex] | 1 | 1.1667 | 1.1667 | 0.7500 | 0.000 | 0.00002 |
| kulikov_readme_example | 6 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00018 |
| kulikov_readme_example | 6 | G/OPT | greedy_worst_tie | 1 | 1.2500 | 1.2500 | 0.6250 | 0.000 | 0.00018 |
| kulikov_readme_example | 6 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00000 |
| shibata_k10_t1 | 22 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| shibata_k10_t1 | 22 | G/OPT | greedy[first] | 1 | 1.1613 | 1.1613 | 0.9735 | 0.000 | 0.00006 |
| shibata_k10_t1 | 22 | G/OPT | greedy[last] | 1 | 1.3226 | 1.3226 | 0.9471 | 0.000 | 0.00006 |
| shibata_k10_t1 | 22 | G/OPT | greedy[lex] | 1 | 1.1613 | 1.1613 | 0.9735 | 0.000 | 0.00005 |
| shibata_k10_t1 | 22 | G/OPT | greedy[paper] | 1 | 1.5161 | 1.5161 | 0.9153 | 0.000 | 0.00007 |
| shibata_k10_t1 | 22 | G/OPT | greedy[random] | 1 | 1.1719 | 1.4516 | 0.9259 | 0.220 | 0.00006 |
| shibata_k10_t1 | 22 | G/OPT | greedy[revlex] | 1 | 1.1613 | 1.1613 | 0.9735 | 0.000 | 0.00006 |
| shibata_k10_t1 | 22 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00006 |
| shibata_k10_t10 | 220 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00018 |
| shibata_k10_t10 | 220 | G/OPT | greedy[first] | 1 | 1.4934 | 1.4934 | 0.9427 | 0.000 | 0.00289 |
| shibata_k10_t10 | 220 | G/OPT | greedy[last] | 1 | 1.7118 | 1.7118 | 0.9173 | 0.000 | 0.00262 |
| shibata_k10_t10 | 220 | G/OPT | greedy[lex] | 1 | 1.5720 | 1.5720 | 0.9335 | 0.000 | 0.00324 |
| shibata_k10_t10 | 220 | G/OPT | greedy[paper] | 1 | 2.0131 | 2.0131 | 0.8823 | 0.000 | 0.00352 |
| shibata_k10_t10 | 220 | G/OPT | greedy[random] | 1 | 1.3330 | 1.4629 | 0.9462 | 0.000 | 0.00338 |
| shibata_k10_t10 | 220 | G/OPT | greedy[revlex] | 1 | 1.4934 | 1.4934 | 0.9427 | 0.000 | 0.00269 |
| shibata_k10_t10 | 220 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00105 |
| shibata_k10_t2 | 44 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| shibata_k10_t2 | 44 | G/OPT | greedy[first] | 1 | 1.3208 | 1.3208 | 0.9561 | 0.000 | 0.00017 |
| shibata_k10_t2 | 44 | G/OPT | greedy[last] | 1 | 1.5094 | 1.5094 | 0.9302 | 0.000 | 0.00016 |
| shibata_k10_t2 | 44 | G/OPT | greedy[lex] | 1 | 1.3585 | 1.3585 | 0.9509 | 0.000 | 0.00018 |
| shibata_k10_t2 | 44 | G/OPT | greedy[paper] | 1 | 1.7547 | 1.7547 | 0.8966 | 0.000 | 0.00020 |
| shibata_k10_t2 | 44 | G/OPT | greedy[random] | 1 | 1.2506 | 1.5094 | 0.9302 | 0.030 | 0.00017 |
| shibata_k10_t2 | 44 | G/OPT | greedy[revlex] | 1 | 1.3208 | 1.3208 | 0.9561 | 0.000 | 0.00016 |
| shibata_k10_t2 | 44 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00012 |
| shibata_k10_t20 | 440 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00041 |
| shibata_k10_t20 | 440 | G/OPT | greedy[first] | 1 | 1.5189 | 1.5189 | 0.9410 | 0.000 | 0.01090 |
| shibata_k10_t20 | 440 | G/OPT | greedy[last] | 1 | 1.7416 | 1.7416 | 0.9157 | 0.000 | 0.01019 |
| shibata_k10_t20 | 440 | G/OPT | greedy[lex] | 1 | 1.5613 | 1.5613 | 0.9362 | 0.000 | 0.01272 |
| shibata_k10_t20 | 440 | G/OPT | greedy[paper] | 1 | 2.0512 | 2.0512 | 0.8805 | 0.000 | 0.01315 |
| shibata_k10_t20 | 440 | G/OPT | greedy[random] | 1 | 1.3264 | 1.4343 | 0.9506 | 0.000 | 0.01344 |
| shibata_k10_t20 | 440 | G/OPT | greedy[revlex] | 1 | 1.6949 | 1.6949 | 0.9210 | 0.000 | 0.01309 |
| shibata_k10_t20 | 440 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00342 |
| shibata_k10_t3 | 66 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00007 |
| shibata_k10_t3 | 66 | G/OPT | greedy[first] | 1 | 1.3867 | 1.3867 | 0.9504 | 0.000 | 0.00033 |
| shibata_k10_t3 | 66 | G/OPT | greedy[last] | 1 | 1.5867 | 1.5867 | 0.9248 | 0.000 | 0.00031 |
| shibata_k10_t3 | 66 | G/OPT | greedy[lex] | 1 | 1.4400 | 1.4400 | 0.9436 | 0.000 | 0.00036 |
| shibata_k10_t3 | 66 | G/OPT | greedy[paper] | 1 | 1.8533 | 1.8533 | 0.8906 | 0.000 | 0.00039 |
| shibata_k10_t3 | 66 | G/OPT | greedy[random] | 1 | 1.3124 | 1.5733 | 0.9265 | 0.020 | 0.00035 |
| shibata_k10_t3 | 66 | G/OPT | greedy[revlex] | 1 | 1.3867 | 1.3867 | 0.9504 | 0.000 | 0.00032 |
| shibata_k10_t3 | 66 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00023 |
| shibata_k10_t5 | 110 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00010 |
| shibata_k10_t5 | 110 | G/OPT | greedy[first] | 1 | 1.4454 | 1.4454 | 0.9460 | 0.000 | 0.00084 |
| shibata_k10_t5 | 110 | G/OPT | greedy[last] | 1 | 1.6555 | 1.6555 | 0.9205 | 0.000 | 0.00076 |
| shibata_k10_t5 | 110 | G/OPT | greedy[lex] | 1 | 1.5126 | 1.5126 | 0.9378 | 0.000 | 0.00090 |
| shibata_k10_t5 | 110 | G/OPT | greedy[paper] | 1 | 1.9412 | 1.9412 | 0.8858 | 0.000 | 0.00097 |
| shibata_k10_t5 | 110 | G/OPT | greedy[random] | 1 | 1.3258 | 1.5378 | 0.9348 | 0.000 | 0.00090 |
| shibata_k10_t5 | 110 | G/OPT | greedy[revlex] | 1 | 1.4454 | 1.4454 | 0.9460 | 0.000 | 0.00078 |
| shibata_k10_t5 | 110 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00040 |
| shibata_k10_t50 | 1100 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00119 |
| shibata_k10_t50 | 1100 | G/OPT | greedy[first] | 1 | 1.5347 | 1.5347 | 0.9400 | 0.000 | 0.07942 |
| shibata_k10_t50 | 1100 | G/OPT | greedy[last] | 1 | 1.7601 | 1.7601 | 0.9148 | 0.000 | 0.07112 |
| shibata_k10_t50 | 1100 | G/OPT | greedy[lex] | 1 | 1.5518 | 1.5518 | 0.9381 | 0.000 | 0.08782 |
| shibata_k10_t50 | 1100 | G/OPT | greedy[paper] | 1 | 2.0748 | 2.0748 | 0.8795 | 0.000 | 0.08806 |
| shibata_k10_t50 | 1100 | G/OPT | greedy[random] | 1 | 1.3242 | 1.4112 | 0.9539 | 0.000 | 0.09032 |
| shibata_k10_t50 | 1100 | G/OPT | greedy[revlex] | 1 | 1.8224 | 1.8224 | 0.9078 | 0.000 | 0.08967 |
| shibata_k10_t50 | 1100 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.01967 |
| shibata_k12_t1 | 26 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| shibata_k12_t1 | 26 | G/OPT | greedy[first] | 1 | 1.1622 | 1.1622 | 0.9782 | 0.000 | 0.00008 |
| shibata_k12_t1 | 26 | G/OPT | greedy[last] | 1 | 1.3243 | 1.3243 | 0.9564 | 0.000 | 0.00007 |
| shibata_k12_t1 | 26 | G/OPT | greedy[lex] | 1 | 1.1622 | 1.1622 | 0.9782 | 0.000 | 0.00007 |
| shibata_k12_t1 | 26 | G/OPT | greedy[paper] | 1 | 1.5135 | 1.5135 | 0.9309 | 0.000 | 0.00010 |
| shibata_k12_t1 | 26 | G/OPT | greedy[random] | 1 | 1.1654 | 1.4324 | 0.9418 | 0.280 | 0.00007 |
| shibata_k12_t1 | 26 | G/OPT | greedy[revlex] | 1 | 1.1622 | 1.1622 | 0.9782 | 0.000 | 0.00007 |
| shibata_k12_t1 | 26 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00008 |
| shibata_k12_t20 | 520 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00051 |
| shibata_k12_t20 | 520 | G/OPT | greedy[first] | 1 | 1.5122 | 1.5122 | 0.9524 | 0.000 | 0.01747 |
| shibata_k12_t20 | 520 | G/OPT | greedy[last] | 1 | 1.7382 | 1.7382 | 0.9313 | 0.000 | 0.01453 |
| shibata_k12_t20 | 520 | G/OPT | greedy[lex] | 1 | 1.5499 | 1.5499 | 0.9489 | 0.000 | 0.02064 |
| shibata_k12_t20 | 520 | G/OPT | greedy[paper] | 1 | 2.0734 | 2.0734 | 0.9002 | 0.000 | 0.02121 |
| shibata_k12_t20 | 520 | G/OPT | greedy[random] | 1 | 1.3343 | 1.4934 | 0.9541 | 0.000 | 0.02087 |
| shibata_k12_t20 | 520 | G/OPT | greedy[revlex] | 1 | 1.6629 | 1.6629 | 0.9383 | 0.000 | 0.02049 |
| shibata_k12_t20 | 520 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00547 |
| shibata_k12_t5 | 130 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00011 |
| shibata_k12_t5 | 130 | G/OPT | greedy[first] | 1 | 1.4397 | 1.4397 | 0.9563 | 0.000 | 0.00108 |
| shibata_k12_t5 | 130 | G/OPT | greedy[last] | 1 | 1.6525 | 1.6525 | 0.9352 | 0.000 | 0.00100 |
| shibata_k12_t5 | 130 | G/OPT | greedy[lex] | 1 | 1.4965 | 1.4965 | 0.9507 | 0.000 | 0.00137 |
| shibata_k12_t5 | 130 | G/OPT | greedy[paper] | 1 | 1.9574 | 1.9574 | 0.9049 | 0.000 | 0.00136 |
| shibata_k12_t5 | 130 | G/OPT | greedy[random] | 1 | 1.3233 | 1.5319 | 0.9471 | 0.000 | 0.00136 |
| shibata_k12_t5 | 130 | G/OPT | greedy[revlex] | 1 | 1.4397 | 1.4397 | 0.9563 | 0.000 | 0.00102 |
| shibata_k12_t5 | 130 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00060 |
| shibata_k16_t1 | 34 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| shibata_k16_t1 | 34 | G/OPT | greedy[first] | 1 | 1.1633 | 1.1633 | 0.9838 | 0.000 | 0.00012 |
| shibata_k16_t1 | 34 | G/OPT | greedy[last] | 1 | 1.3265 | 1.3265 | 0.9677 | 0.000 | 0.00011 |
| shibata_k16_t1 | 34 | G/OPT | greedy[lex] | 1 | 1.1633 | 1.1633 | 0.9838 | 0.000 | 0.00011 |
| shibata_k16_t1 | 34 | G/OPT | greedy[paper] | 1 | 1.5102 | 1.5102 | 0.9495 | 0.000 | 0.00016 |
| shibata_k16_t1 | 34 | G/OPT | greedy[random] | 1 | 1.1735 | 1.4490 | 0.9556 | 0.180 | 0.00012 |
| shibata_k16_t1 | 34 | G/OPT | greedy[revlex] | 1 | 1.1633 | 1.1633 | 0.9838 | 0.000 | 0.00012 |
| shibata_k16_t1 | 34 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00015 |
| shibata_k16_t20 | 680 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00068 |
| shibata_k16_t20 | 680 | G/OPT | greedy[first] | 1 | 1.5036 | 1.5036 | 0.9656 | 0.000 | 0.03131 |
| shibata_k16_t20 | 680 | G/OPT | greedy[last] | 1 | 1.7338 | 1.7338 | 0.9499 | 0.000 | 0.02753 |
| shibata_k16_t20 | 680 | G/OPT | greedy[lex] | 1 | 1.5583 | 1.5583 | 0.9619 | 0.000 | 0.04257 |
| shibata_k16_t20 | 680 | G/OPT | greedy[paper] | 1 | 2.1022 | 2.1022 | 0.9248 | 0.000 | 0.04268 |
| shibata_k16_t20 | 680 | G/OPT | greedy[random] | 1 | 1.3427 | 1.5093 | 0.9652 | 0.000 | 0.04277 |
| shibata_k16_t20 | 680 | G/OPT | greedy[revlex] | 1 | 1.6734 | 1.6734 | 0.9540 | 0.000 | 0.04279 |
| shibata_k16_t20 | 680 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.01117 |
| shibata_k16_t5 | 170 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00015 |
| shibata_k16_t5 | 170 | G/OPT | greedy[first] | 1 | 1.4324 | 1.4324 | 0.9684 | 0.000 | 0.00190 |
| shibata_k16_t5 | 170 | G/OPT | greedy[last] | 1 | 1.6486 | 1.6486 | 0.9527 | 0.000 | 0.00176 |
| shibata_k16_t5 | 170 | G/OPT | greedy[lex] | 1 | 1.5189 | 1.5189 | 0.9621 | 0.000 | 0.00253 |
| shibata_k16_t5 | 170 | G/OPT | greedy[paper] | 1 | 1.9784 | 1.9784 | 0.9286 | 0.000 | 0.00254 |
| shibata_k16_t5 | 170 | G/OPT | greedy[random] | 1 | 1.3304 | 1.5351 | 0.9609 | 0.000 | 0.00246 |
| shibata_k16_t5 | 170 | G/OPT | greedy[revlex] | 1 | 1.4324 | 1.4324 | 0.9684 | 0.000 | 0.00172 |
| shibata_k16_t5 | 170 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00108 |
| shibata_k20_t1 | 42 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| shibata_k20_t1 | 42 | G/OPT | greedy[first] | 1 | 1.1639 | 1.1639 | 0.9872 | 0.000 | 0.00018 |
| shibata_k20_t1 | 42 | G/OPT | greedy[last] | 1 | 1.3279 | 1.3279 | 0.9743 | 0.000 | 0.00016 |
| shibata_k20_t1 | 42 | G/OPT | greedy[lex] | 1 | 1.1639 | 1.1639 | 0.9872 | 0.000 | 0.00016 |
| shibata_k20_t1 | 42 | G/OPT | greedy[paper] | 1 | 1.5082 | 1.5082 | 0.9602 | 0.000 | 0.00023 |
| shibata_k20_t1 | 42 | G/OPT | greedy[random] | 1 | 1.1470 | 1.4426 | 0.9653 | 0.260 | 0.00016 |
| shibata_k20_t1 | 42 | G/OPT | greedy[revlex] | 1 | 1.1639 | 1.1639 | 0.9872 | 0.000 | 0.00017 |
| shibata_k20_t1 | 42 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00022 |
| shibata_k20_t20 | 840 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00087 |
| shibata_k20_t20 | 840 | G/OPT | greedy[first] | 1 | 1.4983 | 1.4983 | 0.9732 | 0.000 | 0.05351 |
| shibata_k20_t20 | 840 | G/OPT | greedy[last] | 1 | 1.7311 | 1.7311 | 0.9606 | 0.000 | 0.04581 |
| shibata_k20_t20 | 840 | G/OPT | greedy[lex] | 1 | 1.5635 | 1.5635 | 0.9696 | 0.000 | 0.07253 |
| shibata_k20_t20 | 840 | G/OPT | greedy[paper] | 1 | 2.1199 | 2.1199 | 0.9397 | 0.000 | 0.07536 |
| shibata_k20_t20 | 840 | G/OPT | greedy[random] | 1 | 1.3561 | 1.5052 | 0.9728 | 0.000 | 0.07543 |
| shibata_k20_t20 | 840 | G/OPT | greedy[revlex] | 1 | 1.6799 | 1.6799 | 0.9634 | 0.000 | 0.07269 |
| shibata_k20_t20 | 840 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.02112 |
| shibata_k20_t5 | 210 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00018 |
| shibata_k20_t5 | 210 | G/OPT | greedy[first] | 1 | 1.4280 | 1.4280 | 0.9753 | 0.000 | 0.00309 |
| shibata_k20_t5 | 210 | G/OPT | greedy[last] | 1 | 1.6463 | 1.6463 | 0.9627 | 0.000 | 0.00274 |
| shibata_k20_t5 | 210 | G/OPT | greedy[lex] | 1 | 1.5328 | 1.5328 | 0.9693 | 0.000 | 0.00412 |
| shibata_k20_t5 | 210 | G/OPT | greedy[paper] | 1 | 1.9913 | 1.9913 | 0.9428 | 0.000 | 0.00430 |
| shibata_k20_t5 | 210 | G/OPT | greedy[random] | 1 | 1.3525 | 1.5371 | 0.9690 | 0.000 | 0.00413 |
| shibata_k20_t5 | 210 | G/OPT | greedy[revlex] | 1 | 1.4280 | 1.4280 | 0.9753 | 0.000 | 0.00265 |
| shibata_k20_t5 | 210 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00188 |
| slides_attac | 3 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| slides_attac | 3 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | G/OPT | greedy[random] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| slides_attac | 3 | G/OPT | greedy_worst_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| slides_attac | 3 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00000 |
| slides_greedy_fail | 3 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_greedy_fail | 3 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| slides_greedy_fail | 3 | G/OPT | greedy[first] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | G/OPT | greedy[last] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | G/OPT | greedy[lex] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | G/OPT | greedy[paper] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | G/OPT | greedy[random] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | G/OPT | greedy[revlex] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | G/OPT | greedy_best_tie | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00003 |
| slides_greedy_fail | 3 | G/OPT | greedy_worst_tie | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00003 |
| slides_greedy_fail | 3 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00000 |
| slides_preprocess | 3 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| slides_preprocess | 3 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | G/OPT | greedy[random] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| slides_preprocess | 3 | G/OPT | greedy_worst_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| slides_preprocess | 3 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00000 |
| tu88_ex7_h1 | 3 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h1 | 3 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | G/OPT | greedy[lex] | 1 | 1.2500 | 1.2500 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h1 | 3 | G/OPT | greedy[paper] | 1 | 1.2500 | 1.2500 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h1 | 3 | G/OPT | greedy[random] | 1 | 1.0775 | 1.2500 | 0.5000 | 0.690 | 0.00001 |
| tu88_ex7_h1 | 3 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| tu88_ex7_h1 | 3 | G/OPT | greedy_worst_tie | 1 | 1.2500 | 1.2500 | 0.5000 | 0.000 | 0.00004 |
| tu88_ex7_h1 | 3 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00000 |
| tu88_ex7_h10 | 3 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h10 | 3 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h10 | 3 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h10 | 3 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h10 | 3 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h10 | 3 | G/OPT | greedy[lex] | 1 | 1.7692 | 1.7692 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h10 | 3 | G/OPT | greedy[paper] | 1 | 1.7692 | 1.7692 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h10 | 3 | G/OPT | greedy[random] | 1 | 1.2462 | 1.7692 | 0.5000 | 0.680 | 0.00001 |
| tu88_ex7_h10 | 3 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h10 | 3 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| tu88_ex7_h10 | 3 | G/OPT | greedy_worst_tie | 1 | 1.7692 | 1.7692 | 0.5000 | 0.000 | 0.00004 |
| tu88_ex7_h10 | 3 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00001 |
| tu88_ex7_h2 | 3 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h2 | 3 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h2 | 3 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h2 | 3 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h2 | 3 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h2 | 3 | G/OPT | greedy[lex] | 1 | 1.4000 | 1.4000 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h2 | 3 | G/OPT | greedy[paper] | 1 | 1.4000 | 1.4000 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h2 | 3 | G/OPT | greedy[random] | 1 | 1.1520 | 1.4000 | 0.5000 | 0.620 | 0.00001 |
| tu88_ex7_h2 | 3 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h2 | 3 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h2 | 3 | G/OPT | greedy_worst_tie | 1 | 1.4000 | 1.4000 | 0.5000 | 0.000 | 0.00003 |
| tu88_ex7_h2 | 3 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00000 |
| tu88_ex7_h20 | 3 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h20 | 3 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h20 | 3 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| tu88_ex7_h20 | 3 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h20 | 3 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h20 | 3 | G/OPT | greedy[lex] | 1 | 1.8696 | 1.8696 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h20 | 3 | G/OPT | greedy[paper] | 1 | 1.8696 | 1.8696 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h20 | 3 | G/OPT | greedy[random] | 1 | 1.3130 | 1.8696 | 0.5000 | 0.640 | 0.00001 |
| tu88_ex7_h20 | 3 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h20 | 3 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| tu88_ex7_h20 | 3 | G/OPT | greedy_worst_tie | 1 | 1.8696 | 1.8696 | 0.5000 | 0.000 | 0.00006 |
| tu88_ex7_h20 | 3 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00001 |
| tu88_ex7_h3 | 3 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h3 | 3 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | G/OPT | greedy[lex] | 1 | 1.5000 | 1.5000 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h3 | 3 | G/OPT | greedy[paper] | 1 | 1.5000 | 1.5000 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h3 | 3 | G/OPT | greedy[random] | 1 | 1.1800 | 1.5000 | 0.5000 | 0.640 | 0.00001 |
| tu88_ex7_h3 | 3 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| tu88_ex7_h3 | 3 | G/OPT | greedy_worst_tie | 1 | 1.5000 | 1.5000 | 0.5000 | 0.000 | 0.00004 |
| tu88_ex7_h3 | 3 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00000 |
| tu88_ex7_h5 | 3 | G/OPT | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h5 | 3 | G/OPT | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h5 | 3 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h5 | 3 | G/OPT | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h5 | 3 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h5 | 3 | G/OPT | greedy[lex] | 1 | 1.6250 | 1.6250 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h5 | 3 | G/OPT | greedy[paper] | 1 | 1.6250 | 1.6250 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h5 | 3 | G/OPT | greedy[random] | 1 | 1.2000 | 1.6250 | 0.5000 | 0.680 | 0.00001 |
| tu88_ex7_h5 | 3 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h5 | 3 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| tu88_ex7_h5 | 3 | G/OPT | greedy_worst_tie | 1 | 1.6250 | 1.6250 | 0.5000 | 0.000 | 0.00004 |
| tu88_ex7_h5 | 3 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00000 |

## Tie sensitivity

| group | n | basis | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | mean tie steps | mean ratio (first) | max ratio observed | max ratio all ties |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| chukhin_k10_t1 | 17 | G/OPT | 1 | dp | 1.000 | 9.00 | 0.500 | 15.0 | 1.1154 | 1.3077 | - |
| chukhin_k3_t1 | 5 | G/OPT | 1 | dp | 1.000 | 3.00 | 0.590 | 4.0 | 1.0000 | 1.2857 | 1.2857 |
| chukhin_k3_t10 | 50 | G/OPT | 1 | certificate | 1.000 | 14.00 | 0.000 | 49.0 | 1.0000 | 1.7308 | - |
| chukhin_k3_t2 | 10 | G/OPT | 1 | dp | 1.000 | 6.00 | 0.060 | 9.0 | 1.0000 | 1.5000 | 1.5000 |
| chukhin_k3_t20 | 100 | G/OPT | 1 | certificate | 1.000 | 18.00 | 0.000 | 99.0 | 1.0000 | 1.7647 | - |
| chukhin_k3_t3 | 15 | G/OPT | 1 | dp | 1.000 | 8.00 | 0.070 | 14.0 | 1.0000 | 1.5882 | - |
| chukhin_k3_t5 | 25 | G/OPT | 1 | certificate | 1.000 | 12.00 | 0.020 | 24.0 | 1.0000 | 1.6667 | - |
| chukhin_k6_t1 | 9 | G/OPT | 1 | dp | 1.000 | 5.00 | 0.530 | 8.0 | 1.2143 | 1.2857 | 1.2857 |
| chukhin_k6_t10 | 90 | G/OPT | 1 | certificate | 1.000 | 31.00 | 0.000 | 89.0 | 1.3158 | 1.8947 | - |
| chukhin_k6_t2 | 18 | G/OPT | 1 | dp | 1.000 | 12.00 | 0.090 | 17.0 | 1.2609 | 1.5652 | - |
| chukhin_k6_t3 | 27 | G/OPT | 1 | certificate | 1.000 | 17.00 | 0.040 | 26.0 | 1.2812 | 1.6875 | - |
| chukhin_k6_t5 | 45 | G/OPT | 1 | certificate | 1.000 | 24.00 | 0.020 | 44.0 | 1.3000 | 1.8000 | - |
| chukhin_k7_t1 | 11 | G/OPT | 1 | dp | 1.000 | 6.00 | 0.430 | 9.0 | 1.1765 | 1.2941 | 1.2941 |
| chukhin_k8_t1 | 13 | G/OPT | 1 | dp | 1.000 | 7.00 | 0.510 | 11.0 | 1.1500 | 1.3000 | - |
| chukhin_k8_t2 | 26 | G/OPT | 1 | certificate | 1.000 | 17.00 | 0.080 | 24.0 | 1.3333 | 1.5758 | - |
| chukhin_k8_t5 | 65 | G/OPT | 1 | certificate | 1.000 | 30.00 | 0.010 | 63.0 | 1.4861 | 1.8056 | - |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | 1 | none | 1.000 | 93.00 | - | 39.0 | 2.1451 | 2.1451 | - |
| greedy125_r1_P0 | 5 | G/OPT | 1 | dp | 1.000 | 6.00 | 0.550 | 4.0 | 1.2979 | 1.2979 | 1.2979 |
| greedy125_r1_P1 | 5 | G/OPT | 1 | dp | 1.000 | 5.00 | 0.550 | 3.0 | 1.3036 | 1.3036 | 1.3036 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | 1 | none | 1.000 | 100.00 | - | 79.0 | 2.2559 | 2.2559 | - |
| greedy125_r2_P1 | 10 | G/OPT | 1 | dp | 1.000 | 17.00 | 0.200 | 8.0 | 1.6313 | 1.6313 | 1.6313 |
| greedy125_r2_P4 | 10 | G/OPT | 1 | dp | 1.000 | 15.00 | 0.130 | 7.0 | 1.6485 | 1.6485 | 1.6485 |
| greedy125_r3_P2 | 15 | G/OPT | 1 | dp | 1.000 | 41.00 | 0.040 | 12.0 | 1.7804 | 1.7804 | - |
| greedy125_r3_P9 | 15 | G/OPT | 1 | dp | 1.000 | 38.00 | 0.060 | 11.0 | 1.8128 | 1.8128 | - |
| greedy125_r4_P16 | 20 | G/OPT | 1 | dp | 1.000 | 66.00 | 0.000 | 15.0 | 1.9124 | 1.9124 | - |
| greedy125_r4_P3 | 20 | G/OPT | 1 | dp | 1.000 | 65.00 | 0.000 | 16.0 | 1.8651 | 1.8651 | - |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | 1 | none | 1.000 | 85.00 | - | 23.0 | 2.0264 | 2.0264 | - |
| kulikov_collapsing_cex | 5 | G/OPT | 1 | dp | 0.000 | 1.00 | 0.000 | 0.0 | 1.3243 | 1.3243 | 1.3243 |
| kulikov_readme_example | 6 | G/OPT | 1 | dp | 1.000 | 4.00 | 0.200 | 5.0 | 1.1667 | 1.2500 | 1.2500 |
| shibata_k10_t1 | 22 | G/OPT | 1 | certificate | 1.000 | 15.00 | 0.220 | 20.0 | 1.1613 | 1.5161 | - |
| shibata_k10_t10 | 220 | G/OPT | 1 | certificate | 1.000 | 51.00 | 0.000 | 219.0 | 1.4934 | 2.0131 | - |
| shibata_k10_t2 | 44 | G/OPT | 1 | certificate | 1.000 | 26.00 | 0.030 | 43.0 | 1.3208 | 1.7547 | - |
| shibata_k10_t20 | 440 | G/OPT | 1 | certificate | 1.000 | 63.00 | 0.000 | - | 1.5189 | 2.0512 | - |
| shibata_k10_t3 | 66 | G/OPT | 1 | certificate | 1.000 | 33.00 | 0.020 | 65.0 | 1.3867 | 1.8533 | - |
| shibata_k10_t5 | 110 | G/OPT | 1 | certificate | 1.000 | 42.00 | 0.000 | 109.0 | 1.4454 | 1.9412 | - |
| shibata_k10_t50 | 1100 | G/OPT | 1 | certificate | 1.000 | 74.00 | 0.000 | - | 1.5347 | 2.0748 | - |
| shibata_k12_t1 | 26 | G/OPT | 1 | certificate | 1.000 | 17.00 | 0.280 | 24.0 | 1.1622 | 1.5135 | - |
| shibata_k12_t20 | 520 | G/OPT | 1 | certificate | 1.000 | 62.00 | 0.000 | - | 1.5122 | 2.0734 | - |
| shibata_k12_t5 | 130 | G/OPT | 1 | certificate | 1.000 | 37.00 | 0.000 | 129.0 | 1.4397 | 1.9574 | - |
| shibata_k16_t1 | 34 | G/OPT | 1 | certificate | 1.000 | 22.00 | 0.180 | 32.0 | 1.1633 | 1.5102 | - |
| shibata_k16_t20 | 680 | G/OPT | 1 | certificate | 1.000 | 72.00 | 0.000 | - | 1.5036 | 2.1022 | - |
| shibata_k16_t5 | 170 | G/OPT | 1 | certificate | 1.000 | 50.00 | 0.000 | 169.0 | 1.4324 | 1.9784 | - |
| shibata_k20_t1 | 42 | G/OPT | 1 | certificate | 1.000 | 24.00 | 0.260 | 40.0 | 1.1639 | 1.5082 | - |
| shibata_k20_t20 | 840 | G/OPT | 1 | certificate | 1.000 | 72.00 | 0.000 | - | 1.4983 | 2.1199 | - |
| shibata_k20_t5 | 210 | G/OPT | 1 | certificate | 1.000 | 56.00 | 0.000 | 209.0 | 1.4280 | 1.9913 | - |
| slides_attac | 3 | G/OPT | 1 | dp | 0.000 | 1.00 | 1.000 | 1.0 | 1.0000 | 1 | 1 |
| slides_greedy_fail | 3 | G/OPT | 1 | dp | 0.000 | 1.00 | 0.000 | 1.0 | 1.1429 | 1.1429 | 1.1429 |
| slides_preprocess | 3 | G/OPT | 1 | dp | 0.000 | 1.00 | 1.000 | 1.0 | 1.0000 | 1 | 1 |
| tu88_ex7_h1 | 3 | G/OPT | 1 | dp | 1.000 | 2.00 | 0.690 | 2.0 | 1.0000 | 1.2500 | 1.2500 |
| tu88_ex7_h10 | 3 | G/OPT | 1 | dp | 1.000 | 2.00 | 0.680 | 1.0 | 1.0000 | 1.7692 | 1.7692 |
| tu88_ex7_h2 | 3 | G/OPT | 1 | dp | 1.000 | 2.00 | 0.620 | 1.0 | 1.0000 | 1.4000 | 1.4000 |
| tu88_ex7_h20 | 3 | G/OPT | 1 | dp | 1.000 | 2.00 | 0.640 | 1.0 | 1.0000 | 1.8696 | 1.8696 |
| tu88_ex7_h3 | 3 | G/OPT | 1 | dp | 1.000 | 2.00 | 0.640 | 1.0 | 1.0000 | 1.5000 | 1.5000 |
| tu88_ex7_h5 | 3 | G/OPT | 1 | dp | 1.000 | 2.00 | 0.680 | 1.0 | 1.0000 | 1.6250 | 1.6250 |

## Prescribed (paper) execution vs tie rules

| instance | n | basis | ref | OPT | \|H\| | G (paper) | ratio paper | ratio first | ratio random mean | ratio random max | random reaches paper |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| chukhin_k10_t1 | 17 | G/OPT | 26 | 26 | - | 34 | 1.3077 | 1.1154 | 1.1131 | 1.3077 | 1 |
| chukhin_k3_t1 | 5 | G/OPT | 7 | 7 | - | 9 | 1.2857 | 1 | 1.0943 | 1.2857 | 1 |
| chukhin_k3_t10 | 50 | G/OPT | 52 | 52 | - | 90 | 1.7308 | 1 | 1.1948 | 1.3269 | 0 |
| chukhin_k3_t2 | 10 | G/OPT | 12 | 12 | - | 18 | 1.5000 | 1 | 1.1950 | 1.5000 | 1 |
| chukhin_k3_t20 | 100 | G/OPT | 102 | 102 | - | 180 | 1.7647 | 1 | 1.1900 | 1.2843 | 0 |
| chukhin_k3_t3 | 15 | G/OPT | 17 | 17 | - | 27 | 1.5882 | 1 | 1.1877 | 1.4118 | 0 |
| chukhin_k3_t5 | 25 | G/OPT | 27 | 27 | - | 45 | 1.6667 | 1 | 1.1959 | 1.4444 | 0 |
| chukhin_k6_t1 | 9 | G/OPT | 14 | 14 | - | 18 | 1.2857 | 1.2143 | 1.0864 | 1.2857 | 1 |
| chukhin_k6_t10 | 90 | G/OPT | 95 | 95 | - | 180 | 1.8947 | 1.3158 | 1.2796 | 1.4632 | 0 |
| chukhin_k6_t2 | 18 | G/OPT | 23 | 23 | - | 36 | 1.5652 | 1.2609 | 1.2100 | 1.5217 | 0 |
| chukhin_k6_t3 | 27 | G/OPT | 32 | 32 | - | 54 | 1.6875 | 1.2812 | 1.2450 | 1.5000 | 0 |
| chukhin_k6_t5 | 45 | G/OPT | 50 | 50 | - | 90 | 1.8000 | 1.3000 | 1.2702 | 1.5400 | 0 |
| chukhin_k7_t1 | 11 | G/OPT | 17 | 17 | - | 22 | 1.2941 | 1.1765 | 1.1177 | 1.2941 | 1 |
| chukhin_k8_t1 | 13 | G/OPT | 20 | 20 | - | 26 | 1.3000 | 1.1500 | 1.0965 | 1.3000 | 1 |
| chukhin_k8_t2 | 26 | G/OPT | 33 | 33 | - | 52 | 1.5758 | 1.3333 | 1.2330 | 1.5151 | 0 |
| chukhin_k8_t5 | 65 | G/OPT | 72 | 72 | - | 130 | 1.8056 | 1.4861 | 1.2525 | 1.5417 | 0 |
| greedy125_r1_P0 | 5 | G/OPT | 47 | 47 | 47 | 61 | 1.2979 | 1.2979 | 1.0985 | 1.2979 | 1 |
| greedy125_r1_P1 | 5 | G/OPT | 56 | 56 | 56 | 73 | 1.3036 | 1.3036 | 1.1170 | 1.3036 | 1 |
| greedy125_r2_P1 | 10 | G/OPT | 160 | 160 | 161 | 261 | 1.6313 | 1.6313 | 1.2309 | 1.6000 | 0 |
| greedy125_r2_P4 | 10 | G/OPT | 202 | 202 | 203 | 333 | 1.6485 | 1.6485 | 1.2344 | 1.6485 | 1 |
| greedy125_r3_P2 | 15 | G/OPT | 337 | 337 | 339 | 600 | 1.7804 | 1.7804 | 1.3058 | 1.6825 | 0 |
| greedy125_r3_P9 | 15 | G/OPT | 470 | 470 | 472 | 852 | 1.8128 | 1.8128 | 1.2987 | 1.6532 | 0 |
| greedy125_r4_P16 | 20 | G/OPT | 890 | 890 | 893 | 1702 | 1.9124 | 1.9124 | 1.3432 | 1.6809 | 0 |
| greedy125_r4_P3 | 20 | G/OPT | 578 | 578 | 581 | 1078 | 1.8651 | 1.8651 | 1.3446 | 1.7422 | 0 |
| shibata_k10_t1 | 22 | G/OPT | 31 | 31 | - | 47 | 1.5161 | 1.1613 | 1.1719 | 1.4516 | 0 |
| shibata_k10_t10 | 220 | G/OPT | 229 | 229 | - | 461 | 2.0131 | 1.4934 | 1.3330 | 1.4629 | 0 |
| shibata_k10_t2 | 44 | G/OPT | 53 | 53 | - | 93 | 1.7547 | 1.3208 | 1.2506 | 1.5094 | 0 |
| shibata_k10_t20 | 440 | G/OPT | 449 | 449 | - | 921 | 2.0512 | 1.5189 | 1.3264 | 1.4343 | 0 |
| shibata_k10_t3 | 66 | G/OPT | 75 | 75 | - | 139 | 1.8533 | 1.3867 | 1.3124 | 1.5733 | 0 |
| shibata_k10_t5 | 110 | G/OPT | 119 | 119 | - | 231 | 1.9412 | 1.4454 | 1.3258 | 1.5378 | 0 |
| shibata_k10_t50 | 1100 | G/OPT | 1109 | 1109 | - | 2301 | 2.0748 | 1.5347 | 1.3242 | 1.4112 | 0 |
| shibata_k12_t1 | 26 | G/OPT | 37 | 37 | - | 56 | 1.5135 | 1.1622 | 1.1654 | 1.4324 | 0 |
| shibata_k12_t20 | 520 | G/OPT | 531 | 531 | - | 1101 | 2.0734 | 1.5122 | 1.3343 | 1.4934 | 0 |
| shibata_k12_t5 | 130 | G/OPT | 141 | 141 | - | 276 | 1.9574 | 1.4397 | 1.3233 | 1.5319 | 0 |
| shibata_k16_t1 | 34 | G/OPT | 49 | 49 | - | 74 | 1.5102 | 1.1633 | 1.1735 | 1.4490 | 0 |
| shibata_k16_t20 | 680 | G/OPT | 695 | 695 | - | 1461 | 2.1022 | 1.5036 | 1.3427 | 1.5093 | 0 |
| shibata_k16_t5 | 170 | G/OPT | 185 | 185 | - | 366 | 1.9784 | 1.4324 | 1.3304 | 1.5351 | 0 |
| shibata_k20_t1 | 42 | G/OPT | 61 | 61 | - | 92 | 1.5082 | 1.1639 | 1.1470 | 1.4426 | 0 |
| shibata_k20_t20 | 840 | G/OPT | 859 | 859 | - | 1821 | 2.1199 | 1.4983 | 1.3561 | 1.5052 | 0 |
| shibata_k20_t5 | 210 | G/OPT | 229 | 229 | - | 456 | 1.9913 | 1.4280 | 1.3525 | 1.5371 | 0 |
| slides_greedy_fail | 3 | G/OPT | 7 | 7 | - | 8 | 1.1429 | 1.1429 | 1.1429 | 1.1429 | 1 |
| tu88_ex7_h1 | 3 | G/OPT | 4 | 4 | - | 5 | 1.2500 | 1 | 1.0775 | 1.2500 | 1 |
| tu88_ex7_h10 | 3 | G/OPT | 13 | 13 | - | 23 | 1.7692 | 1 | 1.2462 | 1.7692 | 1 |
| tu88_ex7_h2 | 3 | G/OPT | 5 | 5 | - | 7 | 1.4000 | 1 | 1.1520 | 1.4000 | 1 |
| tu88_ex7_h20 | 3 | G/OPT | 23 | 23 | - | 43 | 1.8696 | 1 | 1.3130 | 1.8696 | 1 |
| tu88_ex7_h3 | 3 | G/OPT | 6 | 6 | - | 9 | 1.5000 | 1 | 1.1800 | 1.5000 | 1 |
| tu88_ex7_h5 | 3 | G/OPT | 8 | 8 | - | 13 | 1.6250 | 1 | 1.2000 | 1.6250 | 1 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | 8291 | - | 8291 | 17785 | 2.1451 | 2.1451 | 1.3912 | 1.6809 | 0 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | 52781 | - | 52781 | 119070 | 2.2559 | 2.2559 | 1.3995 | 1.6810 | 0 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | 2311 | - | 2311 | 4683 | 2.0264 | 2.0264 | 1.3580 | 1.6222 | 0 |
