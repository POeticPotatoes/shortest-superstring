# Benchmark summary: `results/greedy125`

16 instances, 1232 solver runs.

## Solution quality and runtime

Ratio basis `G/OPT` uses an exact optimum (DP or certificate).  `G/|H| (lower bound)` uses a known common superstring H >= OPT, so it is a certified lower bound on G/OPT; these rows are reported separately.

| group | n | basis | algo | inst | mean ratio | max ratio | min compr. ratio | optimal rate | mean time (s) |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.3781 | 1.5995 | - | - | 0.00046 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.1451 | 2.1451 | - | - | 0.00042 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[last] | 1 | 2.0581 | 2.0581 | - | - | 0.00040 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.4577 | 1.4577 | - | - | 0.00040 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.1451 | 2.1451 | - | - | 0.00045 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.4071 | 1.5553 | - | - | 0.00040 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5156 | 1.5156 | - | - | 0.00038 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.01683 |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.3975 | 1.5550 | - | - | 0.00101 |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.2162 | 2.2162 | - | - | 0.00091 |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | greedy[last] | 1 | 2.1559 | 2.1559 | - | - | 0.00088 |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.5046 | 1.5046 | - | - | 0.00083 |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.2162 | 2.2162 | - | - | 0.00099 |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3972 | 1.6062 | - | - | 0.00087 |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5438 | 1.5438 | - | - | 0.00083 |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.01152 |
| greedy125_r1_P0 | 5 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00012 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[first@shuffled] | 1 | 1.0915 | 1.2979 | 0.8158 | 0.650 | 0.00002 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[first] | 1 | 1.2979 | 1.2979 | 0.8158 | 0.000 | 0.00004 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[last] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[paper] | 1 | 1.2979 | 1.2979 | 0.8158 | 0.000 | 0.00002 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[random] | 1 | 1.0996 | 1.2979 | 0.8158 | 0.540 | 0.00001 |
| greedy125_r1_P0 | 5 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| greedy125_r1_P0 | 5 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00028 |
| greedy125_r1_P0 | 5 | G/OPT | greedy_worst_tie | 1 | 1.2979 | 1.2979 | 0.8158 | 0.000 | 0.00028 |
| greedy125_r1_P0 | 5 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00003 |
| greedy125_r1_P1 | 5 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00011 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[first@shuffled] | 1 | 1.1071 | 1.3036 | 0.8211 | 0.600 | 0.00002 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[first] | 1 | 1.3036 | 1.3036 | 0.8211 | 0.000 | 0.00002 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[last] | 1 | 1.1964 | 1.1964 | 0.8842 | 0.000 | 0.00002 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[paper] | 1 | 1.3036 | 1.3036 | 0.8211 | 0.000 | 0.00002 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[random] | 1 | 1.1464 | 1.3036 | 0.8211 | 0.440 | 0.00001 |
| greedy125_r1_P1 | 5 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| greedy125_r1_P1 | 5 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00014 |
| greedy125_r1_P1 | 5 | G/OPT | greedy_worst_tie | 1 | 1.3036 | 1.3036 | 0.8211 | 0.000 | 0.00014 |
| greedy125_r1_P1 | 5 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00003 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.4165 | 1.5794 | - | - | 0.00180 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.2559 | 2.2559 | - | - | 0.00164 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[last] | 1 | 2.2097 | 2.2097 | - | - | 0.00161 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.5284 | 1.5284 | - | - | 0.00147 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.2559 | 2.2559 | - | - | 0.00177 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.4031 | 1.6810 | - | - | 0.00156 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5580 | 1.5580 | - | - | 0.00147 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.04327 |
| greedy125_r2_P1 | 10 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00385 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[first@shuffled] | 1 | 1.2122 | 1.4250 | 0.8167 | 0.150 | 0.00004 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[first] | 1 | 1.6313 | 1.6313 | 0.7278 | 0.000 | 0.00005 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[last] | 1 | 1.3188 | 1.3188 | 0.8625 | 0.000 | 0.00003 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[paper] | 1 | 1.6313 | 1.6313 | 0.7278 | 0.000 | 0.00004 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[random] | 1 | 1.2341 | 1.5625 | 0.7574 | 0.180 | 0.00003 |
| greedy125_r2_P1 | 10 | G/OPT | greedy[revlex] | 1 | 1.2437 | 1.2437 | 0.8949 | 0.000 | 0.00003 |
| greedy125_r2_P1 | 10 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00214 |
| greedy125_r2_P1 | 10 | G/OPT | greedy_worst_tie | 1 | 1.6313 | 1.6313 | 0.7278 | 0.000 | 0.00214 |
| greedy125_r2_P1 | 10 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00011 |
| greedy125_r2_P4 | 10 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00271 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[first@shuffled] | 1 | 1.2658 | 1.5644 | 0.7706 | 0.100 | 0.00004 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[first] | 1 | 1.6485 | 1.6485 | 0.7364 | 0.000 | 0.00004 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[last] | 1 | 1.3267 | 1.3267 | 0.8672 | 0.000 | 0.00004 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[paper] | 1 | 1.6485 | 1.6485 | 0.7364 | 0.000 | 0.00008 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[random] | 1 | 1.2316 | 1.4356 | 0.8229 | 0.120 | 0.00003 |
| greedy125_r2_P4 | 10 | G/OPT | greedy[revlex] | 1 | 1.2376 | 1.2376 | 0.9034 | 0.000 | 0.00007 |
| greedy125_r2_P4 | 10 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00099 |
| greedy125_r2_P4 | 10 | G/OPT | greedy_worst_tie | 1 | 1.6485 | 1.6485 | 0.7364 | 0.000 | 0.00099 |
| greedy125_r2_P4 | 10 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00015 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.4239 | 1.5325 | - | - | 0.00403 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.2992 | 2.2992 | - | - | 0.00385 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | greedy[last] | 1 | 2.2676 | 2.2676 | - | - | 0.00347 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.5523 | 1.5523 | - | - | 0.00329 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.2992 | 2.2992 | - | - | 0.00392 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3957 | 1.5379 | - | - | 0.00350 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5721 | 1.5721 | - | - | 0.00324 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.32835 |
| greedy125_r3_P2 | 15 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.14383 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[first@shuffled] | 1 | 1.2607 | 1.5460 | 0.7926 | 0.100 | 0.00006 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[first] | 1 | 1.7804 | 1.7804 | 0.7035 | 0.000 | 0.00008 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[last] | 1 | 1.5519 | 1.5519 | 0.7903 | 0.000 | 0.00006 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[lex] | 1 | 1.1335 | 1.1335 | 0.9493 | 0.000 | 0.00005 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[paper] | 1 | 1.7804 | 1.7804 | 0.7035 | 0.000 | 0.00006 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[random] | 1 | 1.3316 | 1.5816 | 0.7790 | 0.020 | 0.00006 |
| greedy125_r3_P2 | 15 | G/OPT | greedy[revlex] | 1 | 1.3531 | 1.3531 | 0.8658 | 0.000 | 0.00005 |
| greedy125_r3_P2 | 15 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00028 |
| greedy125_r3_P9 | 15 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.14299 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[first@shuffled] | 1 | 1.2479 | 1.4851 | 0.8301 | 0.150 | 0.00006 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[first] | 1 | 1.8128 | 1.8128 | 0.7154 | 0.000 | 0.00008 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[last] | 1 | 1.5745 | 1.5745 | 0.7988 | 0.000 | 0.00006 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[lex] | 1 | 1.1702 | 1.1702 | 0.9404 | 0.000 | 0.00005 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[paper] | 1 | 1.8128 | 1.8128 | 0.7154 | 0.000 | 0.00007 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[random] | 1 | 1.2994 | 1.5894 | 0.7936 | 0.080 | 0.00005 |
| greedy125_r3_P9 | 15 | G/OPT | greedy[revlex] | 1 | 1.3425 | 1.3425 | 0.8800 | 0.000 | 0.00005 |
| greedy125_r3_P9 | 15 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00040 |
| greedy125_r4_P16 | 20 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 7.58133 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[first@shuffled] | 1 | 1.3715 | 1.6483 | 0.7915 | 0.000 | 0.00010 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[first] | 1 | 1.9124 | 1.9124 | 0.7066 | 0.000 | 0.00011 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[last] | 1 | 1.7225 | 1.7225 | 0.7677 | 0.000 | 0.00009 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[lex] | 1 | 1.2663 | 1.2663 | 0.9144 | 0.000 | 0.00008 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[paper] | 1 | 1.9124 | 1.9124 | 0.7066 | 0.000 | 0.00010 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[random] | 1 | 1.3602 | 1.6685 | 0.7850 | 0.000 | 0.00009 |
| greedy125_r4_P16 | 20 | G/OPT | greedy[revlex] | 1 | 1.4011 | 1.4011 | 0.8710 | 0.000 | 0.00008 |
| greedy125_r4_P16 | 20 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00092 |
| greedy125_r4_P3 | 20 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 7.58132 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[first@shuffled] | 1 | 1.3201 | 1.5606 | 0.8005 | 0.000 | 0.00010 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[first] | 1 | 1.8651 | 1.8651 | 0.6921 | 0.000 | 0.00011 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[last] | 1 | 1.6851 | 1.6851 | 0.7562 | 0.000 | 0.00008 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[lex] | 1 | 1.2422 | 1.2422 | 0.9138 | 0.000 | 0.00007 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[paper] | 1 | 1.8651 | 1.8651 | 0.6921 | 0.000 | 0.00014 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[random] | 1 | 1.3287 | 1.7422 | 0.7358 | 0.000 | 0.00008 |
| greedy125_r4_P3 | 20 | G/OPT | greedy[revlex] | 1 | 1.4152 | 1.4152 | 0.8522 | 0.000 | 0.00008 |
| greedy125_r4_P3 | 20 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00058 |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.3958 | 1.4770 | - | - | 0.01109 |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.3369 | 2.3369 | - | - | 0.01057 |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | greedy[last] | 1 | 2.3176 | 2.3176 | - | - | 0.01035 |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.5714 | 1.5714 | - | - | 0.01087 |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.3369 | 2.3369 | - | - | 0.01141 |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.4183 | 1.5711 | - | - | 0.01043 |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5834 | 1.5834 | - | - | 0.00953 |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 2.34053 |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.3532 | 1.6558 | - | - | 0.00013 |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | greedy[first] | 1 | 1.9753 | 1.9753 | - | - | 0.00013 |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.8175 | 1.8175 | - | - | 0.00012 |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.3242 | 1.3242 | - | - | 0.00011 |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | greedy[paper] | 1 | 1.9753 | 1.9753 | - | - | 0.00013 |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3379 | 1.7086 | - | - | 0.00012 |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.4345 | 1.4345 | - | - | 0.00011 |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.00167 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.3652 | 1.4751 | - | - | 0.00018 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.0264 | 2.0264 | - | - | 0.00017 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.8910 | 1.8910 | - | - | 0.00016 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.3674 | 1.3674 | - | - | 0.00014 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.0264 | 2.0264 | - | - | 0.00018 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3400 | 1.6222 | - | - | 0.00016 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.4608 | 1.4608 | - | - | 0.00015 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.00302 |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.4013 | 1.6012 | - | - | 0.00032 |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.0975 | 2.0975 | - | - | 0.00028 |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.9917 | 1.9917 | - | - | 0.00027 |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.4232 | 1.4232 | - | - | 0.00024 |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.0975 | 2.0975 | - | - | 0.00030 |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3866 | 1.5934 | - | - | 0.00026 |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.4948 | 1.4948 | - | - | 0.00025 |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.00759 |

## Tie sensitivity

| group | n | basis | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | mean tie steps | mean ratio (first) | max ratio observed | max ratio all ties |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | 1 | none | 1.000 | 49.00 | - | - | 2.1451 | 2.1451 | - |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | 1 | none | 1.000 | 50.00 | - | - | 2.2162 | 2.2162 | - |
| greedy125_r1_P0 | 5 | G/OPT | 1 | dp | 1.000 | 6.00 | 0.540 | - | 1.2979 | 1.2979 | 1.2979 |
| greedy125_r1_P1 | 5 | G/OPT | 1 | dp | 1.000 | 5.00 | 0.440 | - | 1.3036 | 1.3036 | 1.3036 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | 1 | none | 1.000 | 50.00 | - | - | 2.2559 | 2.2559 | - |
| greedy125_r2_P1 | 10 | G/OPT | 1 | dp | 1.000 | 15.00 | 0.180 | - | 1.6313 | 1.6313 | 1.6313 |
| greedy125_r2_P4 | 10 | G/OPT | 1 | dp | 1.000 | 13.00 | 0.120 | - | 1.6485 | 1.6485 | 1.6485 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | 1 | none | 1.000 | 50.00 | - | - | 2.2992 | 2.2992 | - |
| greedy125_r3_P2 | 15 | G/OPT | 1 | dp | 1.000 | 29.00 | 0.020 | - | 1.7804 | 1.7804 | - |
| greedy125_r3_P9 | 15 | G/OPT | 1 | dp | 1.000 | 28.00 | 0.080 | - | 1.8128 | 1.8128 | - |
| greedy125_r4_P16 | 20 | G/OPT | 1 | dp | 1.000 | 40.00 | 0.000 | - | 1.9124 | 1.9124 | - |
| greedy125_r4_P3 | 20 | G/OPT | 1 | dp | 1.000 | 41.00 | 0.000 | - | 1.8651 | 1.8651 | - |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | 1 | none | 1.000 | 50.00 | - | - | 2.3369 | 2.3369 | - |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | 1 | none | 1.000 | 44.00 | - | - | 1.9753 | 1.9753 | - |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | 1 | none | 1.000 | 48.00 | - | - | 2.0264 | 2.0264 | - |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | 1 | none | 1.000 | 49.00 | - | - | 2.0975 | 2.0975 | - |

## Prescribed (paper) execution vs tie rules

| instance | n | basis | ref | OPT | \|H\| | G (paper) | ratio paper | ratio first | ratio random mean | ratio random max | random reaches paper |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| greedy125_r1_P0 | 5 | G/OPT | 47 | 47 | 47 | 61 | 1.2979 | 1.2979 | 1.0996 | 1.2979 | 1 |
| greedy125_r1_P1 | 5 | G/OPT | 56 | 56 | 56 | 73 | 1.3036 | 1.3036 | 1.1464 | 1.3036 | 1 |
| greedy125_r2_P1 | 10 | G/OPT | 160 | 160 | 161 | 261 | 1.6313 | 1.6313 | 1.2341 | 1.5625 | 0 |
| greedy125_r2_P4 | 10 | G/OPT | 202 | 202 | 203 | 333 | 1.6485 | 1.6485 | 1.2316 | 1.4356 | 0 |
| greedy125_r3_P2 | 15 | G/OPT | 337 | 337 | 339 | 600 | 1.7804 | 1.7804 | 1.3316 | 1.5816 | 0 |
| greedy125_r3_P9 | 15 | G/OPT | 470 | 470 | 472 | 852 | 1.8128 | 1.8128 | 1.2994 | 1.5894 | 0 |
| greedy125_r4_P16 | 20 | G/OPT | 890 | 890 | 893 | 1702 | 1.9124 | 1.9124 | 1.3602 | 1.6685 | 0 |
| greedy125_r4_P3 | 20 | G/OPT | 578 | 578 | 581 | 1078 | 1.8651 | 1.8651 | 1.3287 | 1.7422 | 0 |
| greedy125_r10_P100 | 50 | G/\|H\| (lower bound) | 8291 | - | 8291 | 17785 | 2.1451 | 2.1451 | 1.4071 | 1.5553 | 0 |
| greedy125_r15_P225 | 75 | G/\|H\| (lower bound) | 24136 | - | 24136 | 53490 | 2.2162 | 2.2162 | 1.3972 | 1.6062 | 0 |
| greedy125_r20_P400 | 100 | G/\|H\| (lower bound) | 52781 | - | 52781 | 119070 | 2.2559 | 2.2559 | 1.4031 | 1.6810 | 0 |
| greedy125_r30_P900 | 150 | G/\|H\| (lower bound) | 163471 | - | 163471 | 375855 | 2.2992 | 2.2992 | 1.3957 | 1.5379 | 0 |
| greedy125_r50_P2500 | 250 | G/\|H\| (lower bound) | 703451 | - | 703451 | 1643925 | 2.3369 | 2.3369 | 1.4183 | 1.5711 | 0 |
| greedy125_r5_P25 | 25 | G/\|H\| (lower bound) | 1496 | - | 1496 | 2955 | 1.9753 | 1.9753 | 1.3379 | 1.7086 | 0 |
| greedy125_r6_P36 | 30 | G/\|H\| (lower bound) | 2311 | - | 2311 | 4683 | 2.0264 | 2.0264 | 1.3400 | 1.6222 | 0 |
| greedy125_r8_P64 | 40 | G/\|H\| (lower bound) | 4697 | - | 4697 | 9852 | 2.0975 | 2.0975 | 1.3866 | 1.5934 | 0 |
