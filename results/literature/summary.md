# Benchmark summary: `results/literature`

43 instances, 4653 solver runs.

## Solution quality and runtime

| group | n | algo | inst | mean G/OPT | max G/OPT | min compr. ratio | optimal rate | mean time (s) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| chukhin_k10_t1 | 17 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k10_t1 | 17 | greedy[first] | 1 | 1.1154 | 1.1154 | 0.9792 | 0.000 | 0.00006 |
| chukhin_k10_t1 | 17 | greedy[last] | 1 | 1.1154 | 1.1154 | 0.9792 | 0.000 | 0.00004 |
| chukhin_k10_t1 | 17 | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k10_t1 | 17 | greedy[paper] | 1 | 1.3077 | 1.3077 | 0.9444 | 0.000 | 0.00006 |
| chukhin_k10_t1 | 17 | greedy[random] | 1 | 1.1131 | 1.3077 | 0.9444 | 0.500 | 0.00004 |
| chukhin_k10_t1 | 17 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k10_t1 | 17 | overlap_graph | 1 | - | - | - | - | 0.00005 |
| chukhin_k3_t1 | 5 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| chukhin_k3_t1 | 5 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| chukhin_k3_t1 | 5 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| chukhin_k3_t1 | 5 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k3_t1 | 5 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| chukhin_k3_t1 | 5 | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| chukhin_k3_t1 | 5 | greedy[paper] | 1 | 1.2857 | 1.2857 | 0.7500 | 0.000 | 0.00002 |
| chukhin_k3_t1 | 5 | greedy[random] | 1 | 1.0943 | 1.2857 | 0.7500 | 0.590 | 0.00001 |
| chukhin_k3_t1 | 5 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| chukhin_k3_t1 | 5 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00023 |
| chukhin_k3_t1 | 5 | greedy_worst_tie | 1 | 1.2857 | 1.2857 | 0.7500 | 0.000 | 0.00023 |
| chukhin_k3_t1 | 5 | overlap_graph | 1 | - | - | - | - | 0.00000 |
| chukhin_k3_t10 | 50 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| chukhin_k3_t10 | 50 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00158 |
| chukhin_k3_t10 | 50 | greedy[last] | 1 | 1.3461 | 1.3461 | 0.8163 | 0.000 | 0.00016 |
| chukhin_k3_t10 | 50 | greedy[lex] | 1 | 1.3461 | 1.3461 | 0.8163 | 0.000 | 0.00016 |
| chukhin_k3_t10 | 50 | greedy[paper] | 1 | 1.7308 | 1.7308 | 0.6122 | 0.000 | 0.00029 |
| chukhin_k3_t10 | 50 | greedy[random] | 1 | 1.1948 | 1.3269 | 0.8265 | 0.000 | 0.00019 |
| chukhin_k3_t10 | 50 | greedy[revlex] | 1 | 1.3846 | 1.3846 | 0.7959 | 0.000 | 0.00018 |
| chukhin_k3_t10 | 50 | overlap_graph | 1 | - | - | - | - | 0.00005 |
| chukhin_k3_t2 | 10 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k3_t2 | 10 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00225 |
| chukhin_k3_t2 | 10 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k3_t2 | 10 | greedy[last] | 1 | 1.1667 | 1.1667 | 0.8889 | 0.000 | 0.00002 |
| chukhin_k3_t2 | 10 | greedy[lex] | 1 | 1.1667 | 1.1667 | 0.8889 | 0.000 | 0.00002 |
| chukhin_k3_t2 | 10 | greedy[paper] | 1 | 1.5000 | 1.5000 | 0.6667 | 0.000 | 0.00003 |
| chukhin_k3_t2 | 10 | greedy[random] | 1 | 1.1950 | 1.5000 | 0.6667 | 0.060 | 0.00002 |
| chukhin_k3_t2 | 10 | greedy[revlex] | 1 | 1.3333 | 1.3333 | 0.7778 | 0.000 | 0.00002 |
| chukhin_k3_t2 | 10 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.02870 |
| chukhin_k3_t2 | 10 | greedy_worst_tie | 1 | 1.5000 | 1.5000 | 0.6667 | 0.000 | 0.02870 |
| chukhin_k3_t2 | 10 | overlap_graph | 1 | - | - | - | - | 0.00001 |
| chukhin_k3_t20 | 100 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00009 |
| chukhin_k3_t20 | 100 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00035 |
| chukhin_k3_t20 | 100 | greedy[last] | 1 | 1.3725 | 1.3725 | 0.8081 | 0.000 | 0.00051 |
| chukhin_k3_t20 | 100 | greedy[lex] | 1 | 1.2745 | 1.2745 | 0.8586 | 0.000 | 0.00049 |
| chukhin_k3_t20 | 100 | greedy[paper] | 1 | 1.7647 | 1.7647 | 0.6061 | 0.000 | 0.00213 |
| chukhin_k3_t20 | 100 | greedy[random] | 1 | 1.1900 | 1.2843 | 0.8535 | 0.000 | 0.00063 |
| chukhin_k3_t20 | 100 | greedy[revlex] | 1 | 1.3823 | 1.3823 | 0.8030 | 0.000 | 0.00055 |
| chukhin_k3_t20 | 100 | overlap_graph | 1 | - | - | - | - | 0.00010 |
| chukhin_k3_t3 | 15 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k3_t3 | 15 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.12962 |
| chukhin_k3_t3 | 15 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| chukhin_k3_t3 | 15 | greedy[last] | 1 | 1.2353 | 1.2353 | 0.8571 | 0.000 | 0.00004 |
| chukhin_k3_t3 | 15 | greedy[lex] | 1 | 1.2353 | 1.2353 | 0.8571 | 0.000 | 0.00003 |
| chukhin_k3_t3 | 15 | greedy[paper] | 1 | 1.5882 | 1.5882 | 0.6429 | 0.000 | 0.00005 |
| chukhin_k3_t3 | 15 | greedy[random] | 1 | 1.1876 | 1.4118 | 0.7500 | 0.070 | 0.00004 |
| chukhin_k3_t3 | 15 | greedy[revlex] | 1 | 1.3529 | 1.3529 | 0.7857 | 0.000 | 0.00004 |
| chukhin_k3_t3 | 15 | overlap_graph | 1 | - | - | - | - | 0.00001 |
| chukhin_k3_t5 | 25 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k3_t5 | 25 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| chukhin_k3_t5 | 25 | greedy[last] | 1 | 1.2963 | 1.2963 | 0.8333 | 0.000 | 0.00006 |
| chukhin_k3_t5 | 25 | greedy[lex] | 1 | 1.2963 | 1.2963 | 0.8333 | 0.000 | 0.00006 |
| chukhin_k3_t5 | 25 | greedy[paper] | 1 | 1.6667 | 1.6667 | 0.6250 | 0.000 | 0.00009 |
| chukhin_k3_t5 | 25 | greedy[random] | 1 | 1.1959 | 1.4444 | 0.7500 | 0.020 | 0.00007 |
| chukhin_k3_t5 | 25 | greedy[revlex] | 1 | 1.3704 | 1.3704 | 0.7917 | 0.000 | 0.00006 |
| chukhin_k3_t5 | 25 | overlap_graph | 1 | - | - | - | - | 0.00002 |
| chukhin_k6_t1 | 9 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k6_t1 | 9 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00116 |
| chukhin_k6_t1 | 9 | greedy[first] | 1 | 1.2143 | 1.2143 | 0.9250 | 0.000 | 0.00004 |
| chukhin_k6_t1 | 9 | greedy[last] | 1 | 1.2143 | 1.2143 | 0.9250 | 0.000 | 0.00002 |
| chukhin_k6_t1 | 9 | greedy[lex] | 1 | 1.2143 | 1.2143 | 0.9250 | 0.000 | 0.00002 |
| chukhin_k6_t1 | 9 | greedy[paper] | 1 | 1.2857 | 1.2857 | 0.9000 | 0.000 | 0.00003 |
| chukhin_k6_t1 | 9 | greedy[random] | 1 | 1.0864 | 1.2857 | 0.9000 | 0.530 | 0.00002 |
| chukhin_k6_t1 | 9 | greedy[revlex] | 1 | 1.0714 | 1.0714 | 0.9750 | 0.000 | 0.00002 |
| chukhin_k6_t1 | 9 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00580 |
| chukhin_k6_t1 | 9 | greedy_worst_tie | 1 | 1.2857 | 1.2857 | 0.9000 | 0.000 | 0.00580 |
| chukhin_k6_t1 | 9 | overlap_graph | 1 | - | - | - | - | 0.00001 |
| chukhin_k6_t10 | 90 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00008 |
| chukhin_k6_t10 | 90 | greedy[first] | 1 | 1.3158 | 1.3158 | 0.9326 | 0.000 | 0.00048 |
| chukhin_k6_t10 | 90 | greedy[last] | 1 | 1.7895 | 1.7895 | 0.8315 | 0.000 | 0.00056 |
| chukhin_k6_t10 | 90 | greedy[lex] | 1 | 1.6947 | 1.6947 | 0.8517 | 0.000 | 0.00056 |
| chukhin_k6_t10 | 90 | greedy[paper] | 1 | 1.8947 | 1.8947 | 0.8090 | 0.000 | 0.00062 |
| chukhin_k6_t10 | 90 | greedy[random] | 1 | 1.2796 | 1.4632 | 0.9011 | 0.000 | 0.00060 |
| chukhin_k6_t10 | 90 | greedy[revlex] | 1 | 1.3158 | 1.3158 | 0.9326 | 0.000 | 0.00045 |
| chukhin_k6_t10 | 90 | overlap_graph | 1 | - | - | - | - | 0.00020 |
| chukhin_k6_t2 | 18 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k6_t2 | 18 | greedy[first] | 1 | 1.2609 | 1.2609 | 0.9294 | 0.000 | 0.00005 |
| chukhin_k6_t2 | 18 | greedy[last] | 1 | 1.4783 | 1.4783 | 0.8706 | 0.000 | 0.00005 |
| chukhin_k6_t2 | 18 | greedy[lex] | 1 | 1.4348 | 1.4348 | 0.8824 | 0.000 | 0.00004 |
| chukhin_k6_t2 | 18 | greedy[paper] | 1 | 1.5652 | 1.5652 | 0.8471 | 0.000 | 0.00006 |
| chukhin_k6_t2 | 18 | greedy[random] | 1 | 1.2100 | 1.5217 | 0.8588 | 0.090 | 0.00005 |
| chukhin_k6_t2 | 18 | greedy[revlex] | 1 | 1.2609 | 1.2609 | 0.9294 | 0.000 | 0.00004 |
| chukhin_k6_t2 | 18 | overlap_graph | 1 | - | - | - | - | 0.00003 |
| chukhin_k6_t3 | 27 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k6_t3 | 27 | greedy[first] | 1 | 1.2812 | 1.2812 | 0.9308 | 0.000 | 0.00008 |
| chukhin_k6_t3 | 27 | greedy[last] | 1 | 1.5938 | 1.5938 | 0.8538 | 0.000 | 0.00008 |
| chukhin_k6_t3 | 27 | greedy[lex] | 1 | 1.5312 | 1.5312 | 0.8692 | 0.000 | 0.00008 |
| chukhin_k6_t3 | 27 | greedy[paper] | 1 | 1.6875 | 1.6875 | 0.8308 | 0.000 | 0.00009 |
| chukhin_k6_t3 | 27 | greedy[random] | 1 | 1.2450 | 1.5000 | 0.8769 | 0.040 | 0.00008 |
| chukhin_k6_t3 | 27 | greedy[revlex] | 1 | 1.2812 | 1.2812 | 0.9308 | 0.000 | 0.00007 |
| chukhin_k6_t3 | 27 | overlap_graph | 1 | - | - | - | - | 0.00004 |
| chukhin_k6_t5 | 45 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| chukhin_k6_t5 | 45 | greedy[first] | 1 | 1.3000 | 1.3000 | 0.9318 | 0.000 | 0.00015 |
| chukhin_k6_t5 | 45 | greedy[last] | 1 | 1.7000 | 1.7000 | 0.8409 | 0.000 | 0.00017 |
| chukhin_k6_t5 | 45 | greedy[lex] | 1 | 1.6200 | 1.6200 | 0.8591 | 0.000 | 0.00017 |
| chukhin_k6_t5 | 45 | greedy[paper] | 1 | 1.8000 | 1.8000 | 0.8182 | 0.000 | 0.00019 |
| chukhin_k6_t5 | 45 | greedy[random] | 1 | 1.2702 | 1.5400 | 0.8773 | 0.020 | 0.00018 |
| chukhin_k6_t5 | 45 | greedy[revlex] | 1 | 1.3000 | 1.3000 | 0.9318 | 0.000 | 0.00015 |
| chukhin_k6_t5 | 45 | overlap_graph | 1 | - | - | - | - | 0.00008 |
| chukhin_k7_t1 | 11 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k7_t1 | 11 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00518 |
| chukhin_k7_t1 | 11 | greedy[first] | 1 | 1.1765 | 1.1765 | 0.9500 | 0.000 | 0.00003 |
| chukhin_k7_t1 | 11 | greedy[last] | 1 | 1.1765 | 1.1765 | 0.9500 | 0.000 | 0.00003 |
| chukhin_k7_t1 | 11 | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k7_t1 | 11 | greedy[paper] | 1 | 1.2941 | 1.2941 | 0.9167 | 0.000 | 0.00003 |
| chukhin_k7_t1 | 11 | greedy[random] | 1 | 1.1176 | 1.2941 | 0.9167 | 0.430 | 0.00002 |
| chukhin_k7_t1 | 11 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k7_t1 | 11 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.02767 |
| chukhin_k7_t1 | 11 | greedy_worst_tie | 1 | 1.2941 | 1.2941 | 0.9167 | 0.000 | 0.02767 |
| chukhin_k7_t1 | 11 | overlap_graph | 1 | - | - | - | - | 0.00002 |
| chukhin_k8_t1 | 13 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k8_t1 | 13 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.02721 |
| chukhin_k8_t1 | 13 | greedy[first] | 1 | 1.1500 | 1.1500 | 0.9643 | 0.000 | 0.00004 |
| chukhin_k8_t1 | 13 | greedy[last] | 1 | 1.1500 | 1.1500 | 0.9643 | 0.000 | 0.00003 |
| chukhin_k8_t1 | 13 | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k8_t1 | 13 | greedy[paper] | 1 | 1.3000 | 1.3000 | 0.9286 | 0.000 | 0.00004 |
| chukhin_k8_t1 | 13 | greedy[random] | 1 | 1.0965 | 1.3000 | 0.9286 | 0.510 | 0.00003 |
| chukhin_k8_t1 | 13 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| chukhin_k8_t1 | 13 | overlap_graph | 1 | - | - | - | - | 0.00003 |
| chukhin_k8_t2 | 26 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| chukhin_k8_t2 | 26 | greedy[first] | 1 | 1.3333 | 1.3333 | 0.9371 | 0.000 | 0.00007 |
| chukhin_k8_t2 | 26 | greedy[last] | 1 | 1.3939 | 1.3939 | 0.9257 | 0.000 | 0.00007 |
| chukhin_k8_t2 | 26 | greedy[lex] | 1 | 1.3939 | 1.3939 | 0.9257 | 0.000 | 0.00007 |
| chukhin_k8_t2 | 26 | greedy[paper] | 1 | 1.5758 | 1.5758 | 0.8914 | 0.000 | 0.00008 |
| chukhin_k8_t2 | 26 | greedy[random] | 1 | 1.2330 | 1.5151 | 0.9029 | 0.080 | 0.00007 |
| chukhin_k8_t2 | 26 | greedy[revlex] | 1 | 1.5151 | 1.5151 | 0.9029 | 0.000 | 0.00008 |
| chukhin_k8_t2 | 26 | overlap_graph | 1 | - | - | - | - | 0.00005 |
| chukhin_k8_t5 | 65 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| chukhin_k8_t5 | 65 | greedy[first] | 1 | 1.4861 | 1.4861 | 0.9219 | 0.000 | 0.00025 |
| chukhin_k8_t5 | 65 | greedy[last] | 1 | 1.5972 | 1.5972 | 0.9040 | 0.000 | 0.00028 |
| chukhin_k8_t5 | 65 | greedy[lex] | 1 | 1.5972 | 1.5972 | 0.9040 | 0.000 | 0.00028 |
| chukhin_k8_t5 | 65 | greedy[paper] | 1 | 1.8056 | 1.8056 | 0.8705 | 0.000 | 0.00031 |
| chukhin_k8_t5 | 65 | greedy[random] | 1 | 1.2525 | 1.5417 | 0.9129 | 0.010 | 0.00029 |
| chukhin_k8_t5 | 65 | greedy[revlex] | 1 | 1.7361 | 1.7361 | 0.8817 | 0.000 | 0.00030 |
| chukhin_k8_t5 | 65 | overlap_graph | 1 | - | - | - | - | 0.00015 |
| kulikov_collapsing_cex | 5 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00009 |
| kulikov_collapsing_cex | 5 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00008 |
| kulikov_collapsing_cex | 5 | greedy[first] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00002 |
| kulikov_collapsing_cex | 5 | greedy[last] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00002 |
| kulikov_collapsing_cex | 5 | greedy[lex] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00001 |
| kulikov_collapsing_cex | 5 | greedy[random] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00001 |
| kulikov_collapsing_cex | 5 | greedy[revlex] | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00001 |
| kulikov_collapsing_cex | 5 | greedy_best_tie | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00006 |
| kulikov_collapsing_cex | 5 | greedy_worst_tie | 1 | 1.3243 | 1.3243 | 0.7692 | 0.000 | 0.00006 |
| kulikov_collapsing_cex | 5 | overlap_graph | 1 | - | - | - | - | 0.00002 |
| kulikov_readme_example | 6 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00031 |
| kulikov_readme_example | 6 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00009 |
| kulikov_readme_example | 6 | greedy[first] | 1 | 1.1667 | 1.1667 | 0.7500 | 0.000 | 0.00002 |
| kulikov_readme_example | 6 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| kulikov_readme_example | 6 | greedy[lex] | 1 | 1.1667 | 1.1667 | 0.7500 | 0.000 | 0.00001 |
| kulikov_readme_example | 6 | greedy[random] | 1 | 1.1067 | 1.2500 | 0.6250 | 0.200 | 0.00001 |
| kulikov_readme_example | 6 | greedy[revlex] | 1 | 1.1667 | 1.1667 | 0.7500 | 0.000 | 0.00002 |
| kulikov_readme_example | 6 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00017 |
| kulikov_readme_example | 6 | greedy_worst_tie | 1 | 1.2500 | 1.2500 | 0.6250 | 0.000 | 0.00017 |
| kulikov_readme_example | 6 | overlap_graph | 1 | - | - | - | - | 0.00000 |
| shibata_k10_t1 | 22 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| shibata_k10_t1 | 22 | greedy[first] | 1 | 1.1613 | 1.1613 | 0.9735 | 0.000 | 0.00006 |
| shibata_k10_t1 | 22 | greedy[last] | 1 | 1.3226 | 1.3226 | 0.9471 | 0.000 | 0.00005 |
| shibata_k10_t1 | 22 | greedy[lex] | 1 | 1.1613 | 1.1613 | 0.9735 | 0.000 | 0.00005 |
| shibata_k10_t1 | 22 | greedy[paper] | 1 | 1.5161 | 1.5161 | 0.9153 | 0.000 | 0.00008 |
| shibata_k10_t1 | 22 | greedy[random] | 1 | 1.1719 | 1.4516 | 0.9259 | 0.220 | 0.00006 |
| shibata_k10_t1 | 22 | greedy[revlex] | 1 | 1.1613 | 1.1613 | 0.9735 | 0.000 | 0.00006 |
| shibata_k10_t1 | 22 | overlap_graph | 1 | - | - | - | - | 0.00006 |
| shibata_k10_t10 | 220 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00018 |
| shibata_k10_t10 | 220 | greedy[first] | 1 | 1.4934 | 1.4934 | 0.9427 | 0.000 | 0.00305 |
| shibata_k10_t10 | 220 | greedy[last] | 1 | 1.7118 | 1.7118 | 0.9173 | 0.000 | 0.00271 |
| shibata_k10_t10 | 220 | greedy[lex] | 1 | 1.5720 | 1.5720 | 0.9335 | 0.000 | 0.00341 |
| shibata_k10_t10 | 220 | greedy[paper] | 1 | 2.0131 | 2.0131 | 0.8823 | 0.000 | 0.00348 |
| shibata_k10_t10 | 220 | greedy[random] | 1 | 1.3330 | 1.4629 | 0.9462 | 0.000 | 0.00343 |
| shibata_k10_t10 | 220 | greedy[revlex] | 1 | 1.4934 | 1.4934 | 0.9427 | 0.000 | 0.00285 |
| shibata_k10_t10 | 220 | overlap_graph | 1 | - | - | - | - | 0.00121 |
| shibata_k10_t2 | 44 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| shibata_k10_t2 | 44 | greedy[first] | 1 | 1.3208 | 1.3208 | 0.9561 | 0.000 | 0.00017 |
| shibata_k10_t2 | 44 | greedy[last] | 1 | 1.5094 | 1.5094 | 0.9302 | 0.000 | 0.00016 |
| shibata_k10_t2 | 44 | greedy[lex] | 1 | 1.3585 | 1.3585 | 0.9509 | 0.000 | 0.00018 |
| shibata_k10_t2 | 44 | greedy[paper] | 1 | 1.7547 | 1.7547 | 0.8966 | 0.000 | 0.00020 |
| shibata_k10_t2 | 44 | greedy[random] | 1 | 1.2506 | 1.5094 | 0.9302 | 0.030 | 0.00017 |
| shibata_k10_t2 | 44 | greedy[revlex] | 1 | 1.3208 | 1.3208 | 0.9561 | 0.000 | 0.00016 |
| shibata_k10_t2 | 44 | overlap_graph | 1 | - | - | - | - | 0.00012 |
| shibata_k10_t20 | 440 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00040 |
| shibata_k10_t20 | 440 | greedy[first] | 1 | 1.5189 | 1.5189 | 0.9410 | 0.000 | 0.01371 |
| shibata_k10_t20 | 440 | greedy[last] | 1 | 1.7416 | 1.7416 | 0.9157 | 0.000 | 0.01075 |
| shibata_k10_t20 | 440 | greedy[lex] | 1 | 1.5613 | 1.5613 | 0.9362 | 0.000 | 0.01306 |
| shibata_k10_t20 | 440 | greedy[paper] | 1 | 2.0512 | 2.0512 | 0.8805 | 0.000 | 0.01385 |
| shibata_k10_t20 | 440 | greedy[random] | 1 | 1.3264 | 1.4343 | 0.9506 | 0.000 | 0.01369 |
| shibata_k10_t20 | 440 | greedy[revlex] | 1 | 1.6949 | 1.6949 | 0.9210 | 0.000 | 0.01331 |
| shibata_k10_t20 | 440 | overlap_graph | 1 | - | - | - | - | 0.00411 |
| shibata_k10_t3 | 66 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| shibata_k10_t3 | 66 | greedy[first] | 1 | 1.3867 | 1.3867 | 0.9504 | 0.000 | 0.00032 |
| shibata_k10_t3 | 66 | greedy[last] | 1 | 1.5867 | 1.5867 | 0.9248 | 0.000 | 0.00031 |
| shibata_k10_t3 | 66 | greedy[lex] | 1 | 1.4400 | 1.4400 | 0.9436 | 0.000 | 0.00038 |
| shibata_k10_t3 | 66 | greedy[paper] | 1 | 1.8533 | 1.8533 | 0.8906 | 0.000 | 0.00038 |
| shibata_k10_t3 | 66 | greedy[random] | 1 | 1.3124 | 1.5733 | 0.9265 | 0.020 | 0.00035 |
| shibata_k10_t3 | 66 | greedy[revlex] | 1 | 1.3867 | 1.3867 | 0.9504 | 0.000 | 0.00032 |
| shibata_k10_t3 | 66 | overlap_graph | 1 | - | - | - | - | 0.00019 |
| shibata_k10_t5 | 110 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00010 |
| shibata_k10_t5 | 110 | greedy[first] | 1 | 1.4454 | 1.4454 | 0.9460 | 0.000 | 0.00257 |
| shibata_k10_t5 | 110 | greedy[last] | 1 | 1.6555 | 1.6555 | 0.9205 | 0.000 | 0.00074 |
| shibata_k10_t5 | 110 | greedy[lex] | 1 | 1.5126 | 1.5126 | 0.9378 | 0.000 | 0.00090 |
| shibata_k10_t5 | 110 | greedy[paper] | 1 | 1.9412 | 1.9412 | 0.8858 | 0.000 | 0.00093 |
| shibata_k10_t5 | 110 | greedy[random] | 1 | 1.3258 | 1.5378 | 0.9348 | 0.000 | 0.00091 |
| shibata_k10_t5 | 110 | greedy[revlex] | 1 | 1.4454 | 1.4454 | 0.9460 | 0.000 | 0.00078 |
| shibata_k10_t5 | 110 | overlap_graph | 1 | - | - | - | - | 0.00038 |
| shibata_k10_t50 | 1100 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00114 |
| shibata_k10_t50 | 1100 | greedy[first] | 1 | 1.5347 | 1.5347 | 0.9400 | 0.000 | 0.07860 |
| shibata_k10_t50 | 1100 | greedy[last] | 1 | 1.7601 | 1.7601 | 0.9148 | 0.000 | 0.07445 |
| shibata_k10_t50 | 1100 | greedy[lex] | 1 | 1.5518 | 1.5518 | 0.9381 | 0.000 | 0.09006 |
| shibata_k10_t50 | 1100 | greedy[paper] | 1 | 2.0748 | 2.0748 | 0.8795 | 0.000 | 0.09183 |
| shibata_k10_t50 | 1100 | greedy[random] | 1 | 1.3242 | 1.4112 | 0.9539 | 0.000 | 0.09362 |
| shibata_k10_t50 | 1100 | greedy[revlex] | 1 | 1.8224 | 1.8224 | 0.9078 | 0.000 | 0.09108 |
| shibata_k10_t50 | 1100 | overlap_graph | 1 | - | - | - | - | 0.02151 |
| shibata_k12_t1 | 26 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| shibata_k12_t1 | 26 | greedy[first] | 1 | 1.1622 | 1.1622 | 0.9782 | 0.000 | 0.00009 |
| shibata_k12_t1 | 26 | greedy[last] | 1 | 1.3243 | 1.3243 | 0.9564 | 0.000 | 0.00007 |
| shibata_k12_t1 | 26 | greedy[lex] | 1 | 1.1622 | 1.1622 | 0.9782 | 0.000 | 0.00007 |
| shibata_k12_t1 | 26 | greedy[paper] | 1 | 1.5135 | 1.5135 | 0.9309 | 0.000 | 0.00010 |
| shibata_k12_t1 | 26 | greedy[random] | 1 | 1.1654 | 1.4324 | 0.9418 | 0.280 | 0.00007 |
| shibata_k12_t1 | 26 | greedy[revlex] | 1 | 1.1622 | 1.1622 | 0.9782 | 0.000 | 0.00008 |
| shibata_k12_t1 | 26 | overlap_graph | 1 | - | - | - | - | 0.00008 |
| shibata_k12_t20 | 520 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00049 |
| shibata_k12_t20 | 520 | greedy[first] | 1 | 1.5122 | 1.5122 | 0.9524 | 0.000 | 0.01748 |
| shibata_k12_t20 | 520 | greedy[last] | 1 | 1.7382 | 1.7382 | 0.9313 | 0.000 | 0.01520 |
| shibata_k12_t20 | 520 | greedy[lex] | 1 | 1.5499 | 1.5499 | 0.9489 | 0.000 | 0.02065 |
| shibata_k12_t20 | 520 | greedy[paper] | 1 | 2.0734 | 2.0734 | 0.9002 | 0.000 | 0.02512 |
| shibata_k12_t20 | 520 | greedy[random] | 1 | 1.3343 | 1.4934 | 0.9541 | 0.000 | 0.02088 |
| shibata_k12_t20 | 520 | greedy[revlex] | 1 | 1.6629 | 1.6629 | 0.9383 | 0.000 | 0.02068 |
| shibata_k12_t20 | 520 | overlap_graph | 1 | - | - | - | - | 0.00584 |
| shibata_k12_t5 | 130 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00011 |
| shibata_k12_t5 | 130 | greedy[first] | 1 | 1.4397 | 1.4397 | 0.9563 | 0.000 | 0.00108 |
| shibata_k12_t5 | 130 | greedy[last] | 1 | 1.6525 | 1.6525 | 0.9352 | 0.000 | 0.00101 |
| shibata_k12_t5 | 130 | greedy[lex] | 1 | 1.4965 | 1.4965 | 0.9507 | 0.000 | 0.00134 |
| shibata_k12_t5 | 130 | greedy[paper] | 1 | 1.9574 | 1.9574 | 0.9049 | 0.000 | 0.00137 |
| shibata_k12_t5 | 130 | greedy[random] | 1 | 1.3233 | 1.5319 | 0.9471 | 0.000 | 0.00135 |
| shibata_k12_t5 | 130 | greedy[revlex] | 1 | 1.4397 | 1.4397 | 0.9563 | 0.000 | 0.00106 |
| shibata_k12_t5 | 130 | overlap_graph | 1 | - | - | - | - | 0.00058 |
| shibata_k16_t1 | 34 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| shibata_k16_t1 | 34 | greedy[first] | 1 | 1.1633 | 1.1633 | 0.9838 | 0.000 | 0.00012 |
| shibata_k16_t1 | 34 | greedy[last] | 1 | 1.3265 | 1.3265 | 0.9677 | 0.000 | 0.00011 |
| shibata_k16_t1 | 34 | greedy[lex] | 1 | 1.1633 | 1.1633 | 0.9838 | 0.000 | 0.00011 |
| shibata_k16_t1 | 34 | greedy[paper] | 1 | 1.5102 | 1.5102 | 0.9495 | 0.000 | 0.00017 |
| shibata_k16_t1 | 34 | greedy[random] | 1 | 1.1735 | 1.4490 | 0.9556 | 0.180 | 0.00012 |
| shibata_k16_t1 | 34 | greedy[revlex] | 1 | 1.1633 | 1.1633 | 0.9838 | 0.000 | 0.00012 |
| shibata_k16_t1 | 34 | overlap_graph | 1 | - | - | - | - | 0.00014 |
| shibata_k16_t20 | 680 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00067 |
| shibata_k16_t20 | 680 | greedy[first] | 1 | 1.5036 | 1.5036 | 0.9656 | 0.000 | 0.03479 |
| shibata_k16_t20 | 680 | greedy[last] | 1 | 1.7338 | 1.7338 | 0.9499 | 0.000 | 0.02803 |
| shibata_k16_t20 | 680 | greedy[lex] | 1 | 1.5583 | 1.5583 | 0.9619 | 0.000 | 0.04113 |
| shibata_k16_t20 | 680 | greedy[paper] | 1 | 2.1022 | 2.1022 | 0.9248 | 0.000 | 0.04289 |
| shibata_k16_t20 | 680 | greedy[random] | 1 | 1.3427 | 1.5093 | 0.9652 | 0.000 | 0.04508 |
| shibata_k16_t20 | 680 | greedy[revlex] | 1 | 1.6734 | 1.6734 | 0.9540 | 0.000 | 0.04255 |
| shibata_k16_t20 | 680 | overlap_graph | 1 | - | - | - | - | 0.01119 |
| shibata_k16_t5 | 170 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00015 |
| shibata_k16_t5 | 170 | greedy[first] | 1 | 1.4324 | 1.4324 | 0.9684 | 0.000 | 0.00200 |
| shibata_k16_t5 | 170 | greedy[last] | 1 | 1.6486 | 1.6486 | 0.9527 | 0.000 | 0.00181 |
| shibata_k16_t5 | 170 | greedy[lex] | 1 | 1.5189 | 1.5189 | 0.9621 | 0.000 | 0.00257 |
| shibata_k16_t5 | 170 | greedy[paper] | 1 | 1.9784 | 1.9784 | 0.9286 | 0.000 | 0.00268 |
| shibata_k16_t5 | 170 | greedy[random] | 1 | 1.3304 | 1.5351 | 0.9609 | 0.000 | 0.00253 |
| shibata_k16_t5 | 170 | greedy[revlex] | 1 | 1.4324 | 1.4324 | 0.9684 | 0.000 | 0.00179 |
| shibata_k16_t5 | 170 | overlap_graph | 1 | - | - | - | - | 0.00108 |
| shibata_k20_t1 | 42 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| shibata_k20_t1 | 42 | greedy[first] | 1 | 1.1639 | 1.1639 | 0.9872 | 0.000 | 0.00018 |
| shibata_k20_t1 | 42 | greedy[last] | 1 | 1.3279 | 1.3279 | 0.9743 | 0.000 | 0.00016 |
| shibata_k20_t1 | 42 | greedy[lex] | 1 | 1.1639 | 1.1639 | 0.9872 | 0.000 | 0.00016 |
| shibata_k20_t1 | 42 | greedy[paper] | 1 | 1.5082 | 1.5082 | 0.9602 | 0.000 | 0.00023 |
| shibata_k20_t1 | 42 | greedy[random] | 1 | 1.1470 | 1.4426 | 0.9653 | 0.260 | 0.00016 |
| shibata_k20_t1 | 42 | greedy[revlex] | 1 | 1.1639 | 1.1639 | 0.9872 | 0.000 | 0.00017 |
| shibata_k20_t1 | 42 | overlap_graph | 1 | - | - | - | - | 0.00022 |
| shibata_k20_t20 | 840 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00087 |
| shibata_k20_t20 | 840 | greedy[first] | 1 | 1.4983 | 1.4983 | 0.9732 | 0.000 | 0.05272 |
| shibata_k20_t20 | 840 | greedy[last] | 1 | 1.7311 | 1.7311 | 0.9606 | 0.000 | 0.04578 |
| shibata_k20_t20 | 840 | greedy[lex] | 1 | 1.5635 | 1.5635 | 0.9696 | 0.000 | 0.07646 |
| shibata_k20_t20 | 840 | greedy[paper] | 1 | 2.1199 | 2.1199 | 0.9397 | 0.000 | 0.07828 |
| shibata_k20_t20 | 840 | greedy[random] | 1 | 1.3561 | 1.5052 | 0.9728 | 0.000 | 0.08342 |
| shibata_k20_t20 | 840 | greedy[revlex] | 1 | 1.6799 | 1.6799 | 0.9634 | 0.000 | 0.07635 |
| shibata_k20_t20 | 840 | overlap_graph | 1 | - | - | - | - | 0.02310 |
| shibata_k20_t5 | 210 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00018 |
| shibata_k20_t5 | 210 | greedy[first] | 1 | 1.4280 | 1.4280 | 0.9753 | 0.000 | 0.00318 |
| shibata_k20_t5 | 210 | greedy[last] | 1 | 1.6463 | 1.6463 | 0.9627 | 0.000 | 0.00272 |
| shibata_k20_t5 | 210 | greedy[lex] | 1 | 1.5328 | 1.5328 | 0.9693 | 0.000 | 0.00428 |
| shibata_k20_t5 | 210 | greedy[paper] | 1 | 1.9913 | 1.9913 | 0.9428 | 0.000 | 0.00427 |
| shibata_k20_t5 | 210 | greedy[random] | 1 | 1.3525 | 1.5371 | 0.9690 | 0.000 | 0.00423 |
| shibata_k20_t5 | 210 | greedy[revlex] | 1 | 1.4280 | 1.4280 | 0.9753 | 0.000 | 0.00279 |
| shibata_k20_t5 | 210 | overlap_graph | 1 | - | - | - | - | 0.00186 |
| slides_attac | 3 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| slides_attac | 3 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | greedy[random] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_attac | 3 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| slides_attac | 3 | greedy_worst_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| slides_attac | 3 | overlap_graph | 1 | - | - | - | - | 0.00000 |
| slides_greedy_fail | 3 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_greedy_fail | 3 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| slides_greedy_fail | 3 | greedy[first] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | greedy[last] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | greedy[lex] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | greedy[paper] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | greedy[random] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | greedy[revlex] | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00001 |
| slides_greedy_fail | 3 | greedy_best_tie | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00002 |
| slides_greedy_fail | 3 | greedy_worst_tie | 1 | 1.1429 | 1.1429 | 0.7500 | 0.000 | 0.00002 |
| slides_greedy_fail | 3 | overlap_graph | 1 | - | - | - | - | 0.00000 |
| slides_preprocess | 3 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| slides_preprocess | 3 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | greedy[random] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| slides_preprocess | 3 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| slides_preprocess | 3 | greedy_worst_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| slides_preprocess | 3 | overlap_graph | 1 | - | - | - | - | 0.00000 |
| tu88_ex7_h1 | 3 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h1 | 3 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | greedy[lex] | 1 | 1.2500 | 1.2500 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h1 | 3 | greedy[paper] | 1 | 1.2500 | 1.2500 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h1 | 3 | greedy[random] | 1 | 1.0775 | 1.2500 | 0.5000 | 0.690 | 0.00001 |
| tu88_ex7_h1 | 3 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h1 | 3 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| tu88_ex7_h1 | 3 | greedy_worst_tie | 1 | 1.2500 | 1.2500 | 0.5000 | 0.000 | 0.00004 |
| tu88_ex7_h1 | 3 | overlap_graph | 1 | - | - | - | - | 0.00000 |
| tu88_ex7_h10 | 3 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h10 | 3 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h10 | 3 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h10 | 3 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h10 | 3 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h10 | 3 | greedy[lex] | 1 | 1.7692 | 1.7692 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h10 | 3 | greedy[paper] | 1 | 1.7692 | 1.7692 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h10 | 3 | greedy[random] | 1 | 1.2462 | 1.7692 | 0.5000 | 0.680 | 0.00001 |
| tu88_ex7_h10 | 3 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h10 | 3 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| tu88_ex7_h10 | 3 | greedy_worst_tie | 1 | 1.7692 | 1.7692 | 0.5000 | 0.000 | 0.00004 |
| tu88_ex7_h10 | 3 | overlap_graph | 1 | - | - | - | - | 0.00001 |
| tu88_ex7_h2 | 3 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h2 | 3 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h2 | 3 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h2 | 3 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h2 | 3 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h2 | 3 | greedy[lex] | 1 | 1.4000 | 1.4000 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h2 | 3 | greedy[paper] | 1 | 1.4000 | 1.4000 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h2 | 3 | greedy[random] | 1 | 1.1520 | 1.4000 | 0.5000 | 0.620 | 0.00001 |
| tu88_ex7_h2 | 3 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h2 | 3 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h2 | 3 | greedy_worst_tie | 1 | 1.4000 | 1.4000 | 0.5000 | 0.000 | 0.00003 |
| tu88_ex7_h2 | 3 | overlap_graph | 1 | - | - | - | - | 0.00000 |
| tu88_ex7_h20 | 3 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h20 | 3 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h20 | 3 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| tu88_ex7_h20 | 3 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h20 | 3 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h20 | 3 | greedy[lex] | 1 | 1.8696 | 1.8696 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h20 | 3 | greedy[paper] | 1 | 1.8696 | 1.8696 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h20 | 3 | greedy[random] | 1 | 1.3130 | 1.8696 | 0.5000 | 0.640 | 0.00001 |
| tu88_ex7_h20 | 3 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h20 | 3 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| tu88_ex7_h20 | 3 | greedy_worst_tie | 1 | 1.8696 | 1.8696 | 0.5000 | 0.000 | 0.00004 |
| tu88_ex7_h20 | 3 | overlap_graph | 1 | - | - | - | - | 0.00001 |
| tu88_ex7_h3 | 3 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h3 | 3 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | greedy[lex] | 1 | 1.5000 | 1.5000 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h3 | 3 | greedy[paper] | 1 | 1.5000 | 1.5000 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h3 | 3 | greedy[random] | 1 | 1.1800 | 1.5000 | 0.5000 | 0.640 | 0.00001 |
| tu88_ex7_h3 | 3 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h3 | 3 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h3 | 3 | greedy_worst_tie | 1 | 1.5000 | 1.5000 | 0.5000 | 0.000 | 0.00003 |
| tu88_ex7_h3 | 3 | overlap_graph | 1 | - | - | - | - | 0.00000 |
| tu88_ex7_h5 | 3 | bruteforce | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h5 | 3 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h5 | 3 | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| tu88_ex7_h5 | 3 | greedy[first] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h5 | 3 | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h5 | 3 | greedy[lex] | 1 | 1.6250 | 1.6250 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h5 | 3 | greedy[paper] | 1 | 1.6250 | 1.6250 | 0.5000 | 0.000 | 0.00001 |
| tu88_ex7_h5 | 3 | greedy[random] | 1 | 1.2000 | 1.6250 | 0.5000 | 0.680 | 0.00001 |
| tu88_ex7_h5 | 3 | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| tu88_ex7_h5 | 3 | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| tu88_ex7_h5 | 3 | greedy_worst_tie | 1 | 1.6250 | 1.6250 | 0.5000 | 0.000 | 0.00003 |
| tu88_ex7_h5 | 3 | overlap_graph | 1 | - | - | - | - | 0.00000 |

## Tie sensitivity

| group | n | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | mean tie steps | mean G/OPT (first) | max G/OPT observed | max G/OPT all ties |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| chukhin_k10_t1 | 17 | 1 | certificate | 1.000 | 9.00 | 0.500 | 15.0 | 1.1154 | 1.3077 | - |
| chukhin_k3_t1 | 5 | 1 | dp | 1.000 | 3.00 | 0.590 | 4.0 | 1.0000 | 1.2857 | 1.2857 |
| chukhin_k3_t10 | 50 | 1 | certificate | 1.000 | 14.00 | 0.000 | 49.0 | 1.0000 | 1.7308 | - |
| chukhin_k3_t2 | 10 | 1 | dp | 1.000 | 6.00 | 0.060 | 9.0 | 1.0000 | 1.5000 | 1.5000 |
| chukhin_k3_t20 | 100 | 1 | certificate | 1.000 | 18.00 | 0.000 | 99.0 | 1.0000 | 1.7647 | - |
| chukhin_k3_t3 | 15 | 1 | dp | 1.000 | 8.00 | 0.070 | 14.0 | 1.0000 | 1.5882 | - |
| chukhin_k3_t5 | 25 | 1 | certificate | 1.000 | 12.00 | 0.020 | 24.0 | 1.0000 | 1.6667 | - |
| chukhin_k6_t1 | 9 | 1 | dp | 1.000 | 5.00 | 0.530 | 8.0 | 1.2143 | 1.2857 | 1.2857 |
| chukhin_k6_t10 | 90 | 1 | certificate | 1.000 | 31.00 | 0.000 | 89.0 | 1.3158 | 1.8947 | - |
| chukhin_k6_t2 | 18 | 1 | certificate | 1.000 | 12.00 | 0.090 | 17.0 | 1.2609 | 1.5652 | - |
| chukhin_k6_t3 | 27 | 1 | certificate | 1.000 | 17.00 | 0.040 | 26.0 | 1.2812 | 1.6875 | - |
| chukhin_k6_t5 | 45 | 1 | certificate | 1.000 | 24.00 | 0.020 | 44.0 | 1.3000 | 1.8000 | - |
| chukhin_k7_t1 | 11 | 1 | dp | 1.000 | 6.00 | 0.430 | 9.0 | 1.1765 | 1.2941 | 1.2941 |
| chukhin_k8_t1 | 13 | 1 | dp | 1.000 | 7.00 | 0.510 | 11.0 | 1.1500 | 1.3000 | - |
| chukhin_k8_t2 | 26 | 1 | certificate | 1.000 | 17.00 | 0.080 | 24.0 | 1.3333 | 1.5758 | - |
| chukhin_k8_t5 | 65 | 1 | certificate | 1.000 | 30.00 | 0.010 | 63.0 | 1.4861 | 1.8056 | - |
| kulikov_collapsing_cex | 5 | 1 | dp | 0.000 | 1.00 | 0.000 | 0.0 | 1.3243 | 1.3243 | 1.3243 |
| kulikov_readme_example | 6 | 1 | dp | 1.000 | 4.00 | 0.200 | 5.0 | 1.1667 | 1.2500 | 1.2500 |
| shibata_k10_t1 | 22 | 1 | certificate | 1.000 | 15.00 | 0.220 | 20.0 | 1.1613 | 1.5161 | - |
| shibata_k10_t10 | 220 | 1 | certificate | 1.000 | 51.00 | 0.000 | 219.0 | 1.4934 | 2.0131 | - |
| shibata_k10_t2 | 44 | 1 | certificate | 1.000 | 26.00 | 0.030 | 43.0 | 1.3208 | 1.7547 | - |
| shibata_k10_t20 | 440 | 1 | certificate | 1.000 | 63.00 | 0.000 | - | 1.5189 | 2.0512 | - |
| shibata_k10_t3 | 66 | 1 | certificate | 1.000 | 33.00 | 0.020 | 65.0 | 1.3867 | 1.8533 | - |
| shibata_k10_t5 | 110 | 1 | certificate | 1.000 | 42.00 | 0.000 | 109.0 | 1.4454 | 1.9412 | - |
| shibata_k10_t50 | 1100 | 1 | certificate | 1.000 | 74.00 | 0.000 | - | 1.5347 | 2.0748 | - |
| shibata_k12_t1 | 26 | 1 | certificate | 1.000 | 17.00 | 0.280 | 24.0 | 1.1622 | 1.5135 | - |
| shibata_k12_t20 | 520 | 1 | certificate | 1.000 | 62.00 | 0.000 | - | 1.5122 | 2.0734 | - |
| shibata_k12_t5 | 130 | 1 | certificate | 1.000 | 37.00 | 0.000 | 129.0 | 1.4397 | 1.9574 | - |
| shibata_k16_t1 | 34 | 1 | certificate | 1.000 | 22.00 | 0.180 | 32.0 | 1.1633 | 1.5102 | - |
| shibata_k16_t20 | 680 | 1 | certificate | 1.000 | 72.00 | 0.000 | - | 1.5036 | 2.1022 | - |
| shibata_k16_t5 | 170 | 1 | certificate | 1.000 | 50.00 | 0.000 | 169.0 | 1.4324 | 1.9784 | - |
| shibata_k20_t1 | 42 | 1 | certificate | 1.000 | 24.00 | 0.260 | 40.0 | 1.1639 | 1.5082 | - |
| shibata_k20_t20 | 840 | 1 | certificate | 1.000 | 72.00 | 0.000 | - | 1.4983 | 2.1199 | - |
| shibata_k20_t5 | 210 | 1 | certificate | 1.000 | 56.00 | 0.000 | 209.0 | 1.4280 | 1.9913 | - |
| slides_attac | 3 | 1 | dp | 0.000 | 1.00 | 1.000 | 1.0 | 1.0000 | 1 | 1 |
| slides_greedy_fail | 3 | 1 | dp | 0.000 | 1.00 | 0.000 | 1.0 | 1.1429 | 1.1429 | 1.1429 |
| slides_preprocess | 3 | 1 | dp | 0.000 | 1.00 | 1.000 | 1.0 | 1.0000 | 1 | 1 |
| tu88_ex7_h1 | 3 | 1 | dp | 1.000 | 2.00 | 0.690 | 2.0 | 1.0000 | 1.2500 | 1.2500 |
| tu88_ex7_h10 | 3 | 1 | dp | 1.000 | 2.00 | 0.680 | 1.0 | 1.0000 | 1.7692 | 1.7692 |
| tu88_ex7_h2 | 3 | 1 | dp | 1.000 | 2.00 | 0.620 | 1.0 | 1.0000 | 1.4000 | 1.4000 |
| tu88_ex7_h20 | 3 | 1 | dp | 1.000 | 2.00 | 0.640 | 1.0 | 1.0000 | 1.8696 | 1.8696 |
| tu88_ex7_h3 | 3 | 1 | dp | 1.000 | 2.00 | 0.640 | 1.0 | 1.0000 | 1.5000 | 1.5000 |
| tu88_ex7_h5 | 3 | 1 | dp | 1.000 | 2.00 | 0.680 | 1.0 | 1.0000 | 1.6250 | 1.6250 |
