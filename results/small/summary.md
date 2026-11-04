# Benchmark summary: `results/small`

980 instances, 27048 solver runs.

## Solution quality and runtime

| group | n | algo | inst | mean G/OPT | max G/OPT | min compr. ratio | optimal rate | mean time (s) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| random/bin_l4-8 | 4 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| random/bin_l4-8 | 4 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| random/bin_l4-8 | 4 | greedy[first] | 20 | 1.0110 | 1.0833 | 0.8333 | 0.850 | 0.00001 |
| random/bin_l4-8 | 4 | greedy[last] | 20 | 1.0138 | 1.1333 | 0.7143 | 0.850 | 0.00001 |
| random/bin_l4-8 | 4 | greedy[lex] | 20 | 1.0071 | 1.0833 | 0.8333 | 0.900 | 0.00001 |
| random/bin_l4-8 | 4 | greedy[random] | 20 | 1.0120 | 1.1539 | 0.6667 | 0.850 | 0.00001 |
| random/bin_l4-8 | 4 | greedy[revlex] | 20 | 1.0176 | 1.1333 | 0.7143 | 0.800 | 0.00001 |
| random/bin_l4-8 | 4 | greedy_best_tie | 20 | 1.0071 | 1.0833 | 0.8333 | 0.900 | 0.00011 |
| random/bin_l4-8 | 4 | greedy_worst_tie | 20 | 1.0242 | 1.1539 | 0.6667 | 0.750 | 0.00011 |
| random/bin_l4-8 | 4 | overlap_graph | 20 | - | - | - | - | 0.00000 |
| random/bin_l4-8 | 6 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00031 |
| random/bin_l4-8 | 6 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00009 |
| random/bin_l4-8 | 6 | greedy[first] | 20 | 1.0073 | 1.0741 | 0.8889 | 0.850 | 0.00002 |
| random/bin_l4-8 | 6 | greedy[last] | 20 | 1.0085 | 1.0500 | 0.9231 | 0.800 | 0.00001 |
| random/bin_l4-8 | 6 | greedy[lex] | 20 | 1.0059 | 1.0500 | 0.9167 | 0.850 | 0.00001 |
| random/bin_l4-8 | 6 | greedy[random] | 20 | 1.0109 | 1.0769 | 0.8667 | 0.775 | 0.00001 |
| random/bin_l4-8 | 6 | greedy[revlex] | 20 | 1.0106 | 1.0500 | 0.9231 | 0.750 | 0.00001 |
| random/bin_l4-8 | 6 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00008 |
| random/bin_l4-8 | 6 | greedy_worst_tie | 20 | 1.0245 | 1.0769 | 0.8667 | 0.500 | 0.00008 |
| random/bin_l4-8 | 6 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| random/bin_l4-8 | 8 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00042 |
| random/bin_l4-8 | 8 | greedy[first] | 20 | 1.0180 | 1.1600 | 0.8333 | 0.650 | 0.00002 |
| random/bin_l4-8 | 8 | greedy[last] | 20 | 1.0084 | 1.0400 | 0.9524 | 0.750 | 0.00002 |
| random/bin_l4-8 | 8 | greedy[lex] | 20 | 1.0129 | 1.1200 | 0.8750 | 0.750 | 0.00002 |
| random/bin_l4-8 | 8 | greedy[random] | 20 | 1.0158 | 1.1600 | 0.8333 | 0.655 | 0.00002 |
| random/bin_l4-8 | 8 | greedy[revlex] | 20 | 1.0147 | 1.1035 | 0.8800 | 0.700 | 0.00002 |
| random/bin_l4-8 | 8 | greedy_best_tie | 20 | 1.0016 | 1.0323 | 0.9545 | 0.950 | 0.00019 |
| random/bin_l4-8 | 8 | greedy_worst_tie | 20 | 1.0394 | 1.1600 | 0.8333 | 0.300 | 0.00019 |
| random/bin_l4-8 | 8 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| random/bin_l4-8 | 10 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00221 |
| random/bin_l4-8 | 10 | greedy[first] | 20 | 1.0056 | 1.0294 | 0.9655 | 0.800 | 0.00003 |
| random/bin_l4-8 | 10 | greedy[last] | 20 | 1.0101 | 1.0645 | 0.9333 | 0.750 | 0.00002 |
| random/bin_l4-8 | 10 | greedy[lex] | 20 | 1.0099 | 1.0303 | 0.9655 | 0.650 | 0.00002 |
| random/bin_l4-8 | 10 | greedy[random] | 20 | 1.0080 | 1.0732 | 0.9000 | 0.745 | 0.00002 |
| random/bin_l4-8 | 10 | greedy[revlex] | 20 | 1.0111 | 1.0488 | 0.9333 | 0.650 | 0.00002 |
| random/bin_l4-8 | 10 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00063 |
| random/bin_l4-8 | 10 | greedy_worst_tie | 20 | 1.0278 | 1.0976 | 0.8667 | 0.300 | 0.00063 |
| random/bin_l4-8 | 10 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| random/bin_l4-8 | 12 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01146 |
| random/bin_l4-8 | 12 | greedy[first] | 20 | 1.0095 | 1.0540 | 0.9474 | 0.700 | 0.00003 |
| random/bin_l4-8 | 12 | greedy[last] | 20 | 1.0059 | 1.0682 | 0.9333 | 0.850 | 0.00003 |
| random/bin_l4-8 | 12 | greedy[lex] | 20 | 1.0121 | 1.0540 | 0.9474 | 0.650 | 0.00003 |
| random/bin_l4-8 | 12 | greedy[random] | 20 | 1.0138 | 1.1111 | 0.9149 | 0.662 | 0.00003 |
| random/bin_l4-8 | 12 | greedy[revlex] | 20 | 1.0134 | 1.0682 | 0.9333 | 0.650 | 0.00003 |
| random/bin_l4-8 | 12 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| random/bin_l4-8 | 14 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.05804 |
| random/bin_l4-8 | 14 | greedy[first] | 20 | 1.0175 | 1.0851 | 0.9200 | 0.550 | 0.00004 |
| random/bin_l4-8 | 14 | greedy[last] | 20 | 1.0141 | 1.0513 | 0.9600 | 0.600 | 0.00003 |
| random/bin_l4-8 | 14 | greedy[lex] | 20 | 1.0242 | 1.1539 | 0.8889 | 0.600 | 0.00003 |
| random/bin_l4-8 | 14 | greedy[random] | 20 | 1.0204 | 1.1500 | 0.8889 | 0.535 | 0.00004 |
| random/bin_l4-8 | 14 | greedy[revlex] | 20 | 1.0185 | 1.1000 | 0.9200 | 0.600 | 0.00004 |
| random/bin_l4-8 | 14 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| random/bin_l4-8 | 16 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.29424 |
| random/bin_l4-8 | 16 | greedy[first] | 20 | 1.0140 | 1.0566 | 0.9531 | 0.600 | 0.00006 |
| random/bin_l4-8 | 16 | greedy[last] | 20 | 1.0097 | 1.0800 | 0.9385 | 0.700 | 0.00004 |
| random/bin_l4-8 | 16 | greedy[lex] | 20 | 1.0151 | 1.0800 | 0.9385 | 0.600 | 0.00004 |
| random/bin_l4-8 | 16 | greedy[random] | 20 | 1.0136 | 1.1000 | 0.9180 | 0.620 | 0.00004 |
| random/bin_l4-8 | 16 | greedy[revlex] | 20 | 1.0186 | 1.0800 | 0.9333 | 0.550 | 0.00004 |
| random/bin_l4-8 | 16 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| random/dna_l5-12 | 4 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| random/dna_l5-12 | 4 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| random/dna_l5-12 | 4 | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| random/dna_l5-12 | 4 | greedy[last] | 20 | 1.0043 | 1.0294 | 0.5000 | 0.850 | 0.00001 |
| random/dna_l5-12 | 4 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| random/dna_l5-12 | 4 | greedy[random] | 20 | 1.0020 | 1.0312 | 0.5000 | 0.932 | 0.00001 |
| random/dna_l5-12 | 4 | greedy[revlex] | 20 | 1.0029 | 1.0286 | 0.6667 | 0.900 | 0.00001 |
| random/dna_l5-12 | 4 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| random/dna_l5-12 | 4 | greedy_worst_tie | 20 | 1.0059 | 1.0312 | 0.5000 | 0.800 | 0.00003 |
| random/dna_l5-12 | 4 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| random/dna_l5-12 | 6 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00032 |
| random/dna_l5-12 | 6 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00010 |
| random/dna_l5-12 | 6 | greedy[first] | 20 | 1.0014 | 1.0270 | 0.9091 | 0.950 | 0.00002 |
| random/dna_l5-12 | 6 | greedy[last] | 20 | 1.0023 | 1.0263 | 0.8571 | 0.900 | 0.00001 |
| random/dna_l5-12 | 6 | greedy[lex] | 20 | 1.0036 | 1.0270 | 0.8333 | 0.850 | 0.00001 |
| random/dna_l5-12 | 6 | greedy[random] | 20 | 1.0032 | 1.0667 | 0.8182 | 0.887 | 0.00001 |
| random/dna_l5-12 | 6 | greedy[revlex] | 20 | 1.0056 | 1.0667 | 0.8182 | 0.850 | 0.00001 |
| random/dna_l5-12 | 6 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00007 |
| random/dna_l5-12 | 6 | greedy_worst_tie | 20 | 1.0093 | 1.0667 | 0.8182 | 0.700 | 0.00007 |
| random/dna_l5-12 | 6 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| random/dna_l5-12 | 8 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00042 |
| random/dna_l5-12 | 8 | greedy[first] | 20 | 1.0034 | 1.0339 | 0.8667 | 0.850 | 0.00002 |
| random/dna_l5-12 | 8 | greedy[last] | 20 | 1.0034 | 1.0345 | 0.8462 | 0.850 | 0.00002 |
| random/dna_l5-12 | 8 | greedy[lex] | 20 | 1.0017 | 1.0175 | 0.9000 | 0.900 | 0.00002 |
| random/dna_l5-12 | 8 | greedy[random] | 20 | 1.0037 | 1.0517 | 0.7692 | 0.848 | 0.00002 |
| random/dna_l5-12 | 8 | greedy[revlex] | 20 | 1.0017 | 1.0175 | 0.9000 | 0.900 | 0.00002 |
| random/dna_l5-12 | 8 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00025 |
| random/dna_l5-12 | 8 | greedy_worst_tie | 20 | 1.0132 | 1.0517 | 0.7692 | 0.500 | 0.00025 |
| random/dna_l5-12 | 8 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| random/dna_l5-12 | 10 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00224 |
| random/dna_l5-12 | 10 | greedy[first] | 20 | 1.0014 | 1.0141 | 0.9444 | 0.900 | 0.00003 |
| random/dna_l5-12 | 10 | greedy[last] | 20 | 1.0029 | 1.0274 | 0.8889 | 0.850 | 0.00002 |
| random/dna_l5-12 | 10 | greedy[lex] | 20 | 1.0013 | 1.0139 | 0.9231 | 0.900 | 0.00002 |
| random/dna_l5-12 | 10 | greedy[random] | 20 | 1.0035 | 1.0411 | 0.8333 | 0.785 | 0.00002 |
| random/dna_l5-12 | 10 | greedy[revlex] | 20 | 1.0007 | 1.0139 | 0.9412 | 0.950 | 0.00002 |
| random/dna_l5-12 | 10 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00099 |
| random/dna_l5-12 | 10 | greedy_worst_tie | 20 | 1.0099 | 1.0411 | 0.8333 | 0.400 | 0.00099 |
| random/dna_l5-12 | 10 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| random/dna_l5-12 | 12 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01149 |
| random/dna_l5-12 | 12 | greedy[first] | 20 | 1.0039 | 1.0235 | 0.8824 | 0.750 | 0.00003 |
| random/dna_l5-12 | 12 | greedy[last] | 20 | 1.0006 | 1.0120 | 0.9583 | 0.950 | 0.00003 |
| random/dna_l5-12 | 12 | greedy[lex] | 20 | 1.0049 | 1.0385 | 0.8947 | 0.750 | 0.00002 |
| random/dna_l5-12 | 12 | greedy[random] | 20 | 1.0050 | 1.0577 | 0.8421 | 0.703 | 0.00003 |
| random/dna_l5-12 | 12 | greedy[revlex] | 20 | 1.0033 | 1.0192 | 0.9167 | 0.750 | 0.00003 |
| random/dna_l5-12 | 12 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| random/dna_l5-12 | 14 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.05869 |
| random/dna_l5-12 | 14 | greedy[first] | 20 | 1.0021 | 1.0114 | 0.9565 | 0.800 | 0.00004 |
| random/dna_l5-12 | 14 | greedy[last] | 20 | 1.0036 | 1.0114 | 0.9500 | 0.650 | 0.00003 |
| random/dna_l5-12 | 14 | greedy[lex] | 20 | 1.0020 | 1.0114 | 0.9500 | 0.800 | 0.00003 |
| random/dna_l5-12 | 14 | greedy[random] | 20 | 1.0033 | 1.0339 | 0.8462 | 0.725 | 0.00003 |
| random/dna_l5-12 | 14 | greedy[revlex] | 20 | 1.0039 | 1.0192 | 0.9130 | 0.650 | 0.00003 |
| random/dna_l5-12 | 14 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| random/dna_l5-12 | 16 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.29126 |
| random/dna_l5-12 | 16 | greedy[first] | 20 | 1.0013 | 1.0098 | 0.9600 | 0.850 | 0.00005 |
| random/dna_l5-12 | 16 | greedy[last] | 20 | 1.0028 | 1.0196 | 0.9333 | 0.750 | 0.00003 |
| random/dna_l5-12 | 16 | greedy[lex] | 20 | 1.0032 | 1.0108 | 0.9444 | 0.650 | 0.00003 |
| random/dna_l5-12 | 16 | greedy[random] | 20 | 1.0032 | 1.0392 | 0.8667 | 0.728 | 0.00004 |
| random/dna_l5-12 | 16 | greedy[revlex] | 20 | 1.0018 | 1.0196 | 0.9333 | 0.850 | 0.00004 |
| random/dna_l5-12 | 16 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| repetitive/cyclic_k6 | 4 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| repetitive/cyclic_k6 | 4 | certificate | 11 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| repetitive/cyclic_k6 | 4 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| repetitive/cyclic_k6 | 4 | greedy[first] | 20 | 1.0232 | 1.2222 | 0.8667 | 0.800 | 0.00001 |
| repetitive/cyclic_k6 | 4 | greedy[last] | 20 | 1.0167 | 1.1667 | 0.8333 | 0.850 | 0.00001 |
| repetitive/cyclic_k6 | 4 | greedy[lex] | 20 | 1.0075 | 1.0833 | 0.8889 | 0.900 | 0.00001 |
| repetitive/cyclic_k6 | 4 | greedy[random] | 20 | 1.0200 | 1.2222 | 0.8333 | 0.807 | 0.00001 |
| repetitive/cyclic_k6 | 4 | greedy[revlex] | 20 | 1.0323 | 1.2222 | 0.8333 | 0.750 | 0.00001 |
| repetitive/cyclic_k6 | 4 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| repetitive/cyclic_k6 | 4 | greedy_worst_tie | 20 | 1.0398 | 1.2222 | 0.8333 | 0.650 | 0.00005 |
| repetitive/cyclic_k6 | 4 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| repetitive/cyclic_k6 | 6 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00032 |
| repetitive/cyclic_k6 | 6 | certificate | 8 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| repetitive/cyclic_k6 | 6 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00009 |
| repetitive/cyclic_k6 | 6 | greedy[first] | 20 | 1.0587 | 1.3636 | 0.8400 | 0.650 | 0.00002 |
| repetitive/cyclic_k6 | 6 | greedy[last] | 20 | 1.0629 | 1.2727 | 0.8800 | 0.500 | 0.00001 |
| repetitive/cyclic_k6 | 6 | greedy[lex] | 20 | 1.0704 | 1.2727 | 0.8571 | 0.600 | 0.00001 |
| repetitive/cyclic_k6 | 6 | greedy[random] | 20 | 1.0531 | 1.3636 | 0.8400 | 0.610 | 0.00001 |
| repetitive/cyclic_k6 | 6 | greedy[revlex] | 20 | 1.0606 | 1.2727 | 0.8696 | 0.600 | 0.00001 |
| repetitive/cyclic_k6 | 6 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00021 |
| repetitive/cyclic_k6 | 6 | greedy_worst_tie | 20 | 1.1282 | 1.3636 | 0.8400 | 0.300 | 0.00021 |
| repetitive/cyclic_k6 | 6 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| repetitive/cyclic_k6 | 8 | certificate | 4 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| repetitive/cyclic_k6 | 8 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00043 |
| repetitive/cyclic_k6 | 8 | greedy[first] | 20 | 1.0834 | 1.2353 | 0.8710 | 0.250 | 0.00002 |
| repetitive/cyclic_k6 | 8 | greedy[last] | 20 | 1.0994 | 1.2857 | 0.8824 | 0.300 | 0.00002 |
| repetitive/cyclic_k6 | 8 | greedy[lex] | 20 | 1.0941 | 1.3077 | 0.8857 | 0.300 | 0.00002 |
| repetitive/cyclic_k6 | 8 | greedy[random] | 20 | 1.0790 | 1.3077 | 0.8667 | 0.347 | 0.00002 |
| repetitive/cyclic_k6 | 8 | greedy[revlex] | 20 | 1.1052 | 1.2353 | 0.8710 | 0.250 | 0.00002 |
| repetitive/cyclic_k6 | 8 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00095 |
| repetitive/cyclic_k6 | 8 | greedy_worst_tie | 20 | 1.2031 | 1.3077 | 0.8667 | 0.000 | 0.00095 |
| repetitive/cyclic_k6 | 8 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| repetitive/cyclic_k6 | 10 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| repetitive/cyclic_k6 | 10 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00240 |
| repetitive/cyclic_k6 | 10 | greedy[first] | 20 | 1.0902 | 1.2500 | 0.9070 | 0.150 | 0.00003 |
| repetitive/cyclic_k6 | 10 | greedy[last] | 20 | 1.1020 | 1.2353 | 0.9024 | 0.250 | 0.00002 |
| repetitive/cyclic_k6 | 10 | greedy[lex] | 20 | 1.1220 | 1.3158 | 0.8537 | 0.050 | 0.00002 |
| repetitive/cyclic_k6 | 10 | greedy[random] | 20 | 1.1004 | 1.3333 | 0.8837 | 0.210 | 0.00002 |
| repetitive/cyclic_k6 | 10 | greedy[revlex] | 20 | 1.1147 | 1.2941 | 0.8837 | 0.050 | 0.00002 |
| repetitive/cyclic_k6 | 10 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00469 |
| repetitive/cyclic_k6 | 10 | greedy_worst_tie | 20 | 1.2247 | 1.4210 | 0.8049 | 0.000 | 0.00469 |
| repetitive/cyclic_k6 | 10 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| repetitive/cyclic_k6 | 12 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| repetitive/cyclic_k6 | 12 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01158 |
| repetitive/cyclic_k6 | 12 | greedy[first] | 20 | 1.1020 | 1.2222 | 0.9167 | 0.150 | 0.00003 |
| repetitive/cyclic_k6 | 12 | greedy[last] | 20 | 1.1215 | 1.3684 | 0.8679 | 0.100 | 0.00003 |
| repetitive/cyclic_k6 | 12 | greedy[lex] | 20 | 1.1309 | 1.3889 | 0.8704 | 0.150 | 0.00003 |
| repetitive/cyclic_k6 | 12 | greedy[random] | 20 | 1.1170 | 1.4210 | 0.8491 | 0.145 | 0.00003 |
| repetitive/cyclic_k6 | 12 | greedy[revlex] | 20 | 1.1708 | 1.3333 | 0.8868 | 0.050 | 0.00003 |
| repetitive/cyclic_k6 | 12 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| repetitive/cyclic_k6 | 14 | certificate | 2 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| repetitive/cyclic_k6 | 14 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.05884 |
| repetitive/cyclic_k6 | 14 | greedy[first] | 20 | 1.1220 | 1.2727 | 0.9016 | 0.150 | 0.00005 |
| repetitive/cyclic_k6 | 14 | greedy[last] | 20 | 1.1199 | 1.2609 | 0.9016 | 0.100 | 0.00003 |
| repetitive/cyclic_k6 | 14 | greedy[lex] | 20 | 1.2107 | 1.3684 | 0.8906 | 0.000 | 0.00003 |
| repetitive/cyclic_k6 | 14 | greedy[random] | 20 | 1.1282 | 1.4210 | 0.8750 | 0.092 | 0.00004 |
| repetitive/cyclic_k6 | 14 | greedy[revlex] | 20 | 1.1670 | 1.3158 | 0.9016 | 0.000 | 0.00004 |
| repetitive/cyclic_k6 | 14 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| repetitive/cyclic_k6 | 16 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.29402 |
| repetitive/cyclic_k6 | 16 | greedy[first] | 20 | 1.1147 | 1.2593 | 0.8986 | 0.100 | 0.00006 |
| repetitive/cyclic_k6 | 16 | greedy[last] | 20 | 1.0950 | 1.2174 | 0.9286 | 0.200 | 0.00004 |
| repetitive/cyclic_k6 | 16 | greedy[lex] | 20 | 1.1572 | 1.2917 | 0.9028 | 0.000 | 0.00004 |
| repetitive/cyclic_k6 | 16 | greedy[random] | 20 | 1.1124 | 1.3077 | 0.8857 | 0.142 | 0.00004 |
| repetitive/cyclic_k6 | 16 | greedy[revlex] | 20 | 1.1588 | 1.2917 | 0.8971 | 0.050 | 0.00004 |
| repetitive/cyclic_k6 | 16 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| repetitive/kmer_k8 | 4 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| repetitive/kmer_k8 | 4 | certificate | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| repetitive/kmer_k8 | 4 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| repetitive/kmer_k8 | 4 | greedy[first] | 20 | 1.0091 | 1.1818 | 0.9048 | 0.950 | 0.00001 |
| repetitive/kmer_k8 | 4 | greedy[last] | 20 | 1.0136 | 1.0909 | 0.9524 | 0.850 | 0.00001 |
| repetitive/kmer_k8 | 4 | greedy[lex] | 20 | 1.0091 | 1.1818 | 0.9048 | 0.950 | 0.00001 |
| repetitive/kmer_k8 | 4 | greedy[random] | 20 | 1.0198 | 1.1818 | 0.9048 | 0.860 | 0.00001 |
| repetitive/kmer_k8 | 4 | greedy[revlex] | 20 | 1.0091 | 1.1818 | 0.9048 | 0.950 | 0.00001 |
| repetitive/kmer_k8 | 4 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| repetitive/kmer_k8 | 4 | greedy_worst_tie | 20 | 1.0636 | 1.1818 | 0.9048 | 0.650 | 0.00006 |
| repetitive/kmer_k8 | 4 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| repetitive/kmer_k8 | 6 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00033 |
| repetitive/kmer_k8 | 6 | certificate | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| repetitive/kmer_k8 | 6 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00010 |
| repetitive/kmer_k8 | 6 | greedy[first] | 20 | 1.0154 | 1.3077 | 0.8857 | 0.950 | 0.00002 |
| repetitive/kmer_k8 | 6 | greedy[last] | 20 | 1.0577 | 1.3077 | 0.8857 | 0.700 | 0.00001 |
| repetitive/kmer_k8 | 6 | greedy[lex] | 20 | 1.0154 | 1.1539 | 0.9429 | 0.850 | 0.00001 |
| repetitive/kmer_k8 | 6 | greedy[random] | 20 | 1.0348 | 1.3077 | 0.8857 | 0.780 | 0.00001 |
| repetitive/kmer_k8 | 6 | greedy[revlex] | 20 | 1.0308 | 1.3077 | 0.8857 | 0.800 | 0.00001 |
| repetitive/kmer_k8 | 6 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00019 |
| repetitive/kmer_k8 | 6 | greedy_worst_tie | 20 | 1.1115 | 1.3077 | 0.8857 | 0.500 | 0.00019 |
| repetitive/kmer_k8 | 6 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| repetitive/kmer_k8 | 8 | certificate | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| repetitive/kmer_k8 | 8 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00044 |
| repetitive/kmer_k8 | 8 | greedy[first] | 20 | 1.0500 | 1.4000 | 0.8776 | 0.850 | 0.00002 |
| repetitive/kmer_k8 | 8 | greedy[last] | 20 | 1.0567 | 1.4667 | 0.8571 | 0.700 | 0.00002 |
| repetitive/kmer_k8 | 8 | greedy[lex] | 20 | 1.1033 | 1.4667 | 0.8571 | 0.700 | 0.00001 |
| repetitive/kmer_k8 | 8 | greedy[random] | 20 | 1.0713 | 1.4667 | 0.8571 | 0.710 | 0.00002 |
| repetitive/kmer_k8 | 8 | greedy[revlex] | 20 | 1.0933 | 1.4667 | 0.8571 | 0.650 | 0.00002 |
| repetitive/kmer_k8 | 8 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00087 |
| repetitive/kmer_k8 | 8 | greedy_worst_tie | 20 | 1.1700 | 1.4667 | 0.8571 | 0.400 | 0.00087 |
| repetitive/kmer_k8 | 8 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| repetitive/kmer_k8 | 10 | certificate | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| repetitive/kmer_k8 | 10 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00240 |
| repetitive/kmer_k8 | 10 | greedy[first] | 20 | 1.0559 | 1.3529 | 0.9048 | 0.700 | 0.00002 |
| repetitive/kmer_k8 | 10 | greedy[last] | 20 | 1.0676 | 1.2941 | 0.9206 | 0.650 | 0.00002 |
| repetitive/kmer_k8 | 10 | greedy[lex] | 20 | 1.0618 | 1.3529 | 0.9048 | 0.700 | 0.00002 |
| repetitive/kmer_k8 | 10 | greedy[random] | 20 | 1.0526 | 1.4118 | 0.8889 | 0.715 | 0.00002 |
| repetitive/kmer_k8 | 10 | greedy[revlex] | 20 | 1.0588 | 1.4118 | 0.8889 | 0.750 | 0.00002 |
| repetitive/kmer_k8 | 10 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00444 |
| repetitive/kmer_k8 | 10 | greedy_worst_tie | 20 | 1.1765 | 1.4118 | 0.8889 | 0.300 | 0.00444 |
| repetitive/kmer_k8 | 10 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| repetitive/kmer_k8 | 12 | certificate | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| repetitive/kmer_k8 | 12 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01160 |
| repetitive/kmer_k8 | 12 | greedy[first] | 20 | 1.0526 | 1.3158 | 0.9221 | 0.750 | 0.00003 |
| repetitive/kmer_k8 | 12 | greedy[last] | 20 | 1.0237 | 1.2632 | 0.9351 | 0.850 | 0.00002 |
| repetitive/kmer_k8 | 12 | greedy[lex] | 20 | 1.1000 | 1.3684 | 0.9091 | 0.500 | 0.00002 |
| repetitive/kmer_k8 | 12 | greedy[random] | 20 | 1.0711 | 1.3684 | 0.9091 | 0.660 | 0.00002 |
| repetitive/kmer_k8 | 12 | greedy[revlex] | 20 | 1.0921 | 1.3158 | 0.9221 | 0.600 | 0.00002 |
| repetitive/kmer_k8 | 12 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| repetitive/kmer_k8 | 14 | certificate | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| repetitive/kmer_k8 | 14 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.05921 |
| repetitive/kmer_k8 | 14 | greedy[first] | 20 | 1.0571 | 1.3809 | 0.9121 | 0.700 | 0.00004 |
| repetitive/kmer_k8 | 14 | greedy[last] | 20 | 1.0881 | 1.4286 | 0.9011 | 0.600 | 0.00003 |
| repetitive/kmer_k8 | 14 | greedy[lex] | 20 | 1.0762 | 1.4286 | 0.9011 | 0.550 | 0.00003 |
| repetitive/kmer_k8 | 14 | greedy[random] | 20 | 1.1012 | 1.4286 | 0.9011 | 0.525 | 0.00003 |
| repetitive/kmer_k8 | 14 | greedy[revlex] | 20 | 1.0976 | 1.3333 | 0.9231 | 0.550 | 0.00003 |
| repetitive/kmer_k8 | 14 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| repetitive/kmer_k8 | 16 | certificate | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| repetitive/kmer_k8 | 16 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.29309 |
| repetitive/kmer_k8 | 16 | greedy[first] | 20 | 1.0609 | 1.3478 | 0.9238 | 0.650 | 0.00005 |
| repetitive/kmer_k8 | 16 | greedy[last] | 20 | 1.0848 | 1.4783 | 0.8952 | 0.500 | 0.00003 |
| repetitive/kmer_k8 | 16 | greedy[lex] | 20 | 1.1000 | 1.3913 | 0.9143 | 0.450 | 0.00003 |
| repetitive/kmer_k8 | 16 | greedy[random] | 20 | 1.0665 | 1.4783 | 0.8952 | 0.600 | 0.00003 |
| repetitive/kmer_k8 | 16 | greedy[revlex] | 20 | 1.1152 | 1.4783 | 0.8952 | 0.500 | 0.00004 |
| repetitive/kmer_k8 | 16 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| repetitive/periodic | 4 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| repetitive/periodic | 4 | certificate | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| repetitive/periodic | 4 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| repetitive/periodic | 4 | greedy[first] | 20 | 1.0025 | 1.0500 | 0.9412 | 0.950 | 0.00001 |
| repetitive/periodic | 4 | greedy[last] | 20 | 1.0163 | 1.1500 | 0.8636 | 0.850 | 0.00001 |
| repetitive/periodic | 4 | greedy[lex] | 20 | 1.0128 | 1.1500 | 0.8750 | 0.850 | 0.00001 |
| repetitive/periodic | 4 | greedy[random] | 20 | 1.0085 | 1.1500 | 0.8636 | 0.902 | 0.00001 |
| repetitive/periodic | 4 | greedy[revlex] | 20 | 1.0060 | 1.1200 | 0.8636 | 0.950 | 0.00001 |
| repetitive/periodic | 4 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| repetitive/periodic | 4 | greedy_worst_tie | 20 | 1.0188 | 1.1500 | 0.8636 | 0.800 | 0.00004 |
| repetitive/periodic | 4 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| repetitive/periodic | 6 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00034 |
| repetitive/periodic | 6 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00011 |
| repetitive/periodic | 6 | greedy[first] | 20 | 1.0290 | 1.1786 | 0.8621 | 0.750 | 0.00002 |
| repetitive/periodic | 6 | greedy[last] | 20 | 1.0273 | 1.1786 | 0.8621 | 0.700 | 0.00001 |
| repetitive/periodic | 6 | greedy[lex] | 20 | 1.0344 | 1.1786 | 0.9000 | 0.600 | 0.00001 |
| repetitive/periodic | 6 | greedy[random] | 20 | 1.0270 | 1.4783 | 0.8136 | 0.723 | 0.00001 |
| repetitive/periodic | 6 | greedy[revlex] | 20 | 1.0201 | 1.1786 | 0.9000 | 0.800 | 0.00001 |
| repetitive/periodic | 6 | greedy_best_tie | 20 | 1.0135 | 1.1786 | 0.9000 | 0.850 | 0.00008 |
| repetitive/periodic | 6 | greedy_worst_tie | 20 | 1.0602 | 1.4783 | 0.8136 | 0.550 | 0.00008 |
| repetitive/periodic | 6 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| repetitive/periodic | 8 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00045 |
| repetitive/periodic | 8 | greedy[first] | 20 | 1.0598 | 1.2963 | 0.8772 | 0.300 | 0.00002 |
| repetitive/periodic | 8 | greedy[last] | 20 | 1.0412 | 1.1579 | 0.8846 | 0.450 | 0.00002 |
| repetitive/periodic | 8 | greedy[lex] | 20 | 1.0336 | 1.1579 | 0.8846 | 0.550 | 0.00002 |
| repetitive/periodic | 8 | greedy[random] | 20 | 1.0444 | 1.2963 | 0.8596 | 0.398 | 0.00002 |
| repetitive/periodic | 8 | greedy[revlex] | 20 | 1.0599 | 1.2222 | 0.8772 | 0.250 | 0.00002 |
| repetitive/periodic | 8 | greedy_best_tie | 20 | 1.0221 | 1.1081 | 0.9310 | 0.600 | 0.00012 |
| repetitive/periodic | 8 | greedy_worst_tie | 20 | 1.0796 | 1.2963 | 0.8596 | 0.200 | 0.00012 |
| repetitive/periodic | 8 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| repetitive/periodic | 10 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00238 |
| repetitive/periodic | 10 | greedy[first] | 20 | 1.0445 | 1.1892 | 0.9268 | 0.550 | 0.00003 |
| repetitive/periodic | 10 | greedy[last] | 20 | 1.0447 | 1.2927 | 0.8667 | 0.500 | 0.00002 |
| repetitive/periodic | 10 | greedy[lex] | 20 | 1.0606 | 1.3077 | 0.9268 | 0.500 | 0.00002 |
| repetitive/periodic | 10 | greedy[random] | 20 | 1.0491 | 1.3077 | 0.8667 | 0.453 | 0.00002 |
| repetitive/periodic | 10 | greedy[revlex] | 20 | 1.0476 | 1.1429 | 0.9268 | 0.400 | 0.00002 |
| repetitive/periodic | 10 | greedy_best_tie | 20 | 1.0109 | 1.1111 | 0.9432 | 0.900 | 0.00024 |
| repetitive/periodic | 10 | greedy_worst_tie | 20 | 1.1040 | 1.3171 | 0.8556 | 0.150 | 0.00024 |
| repetitive/periodic | 10 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| repetitive/periodic | 12 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01174 |
| repetitive/periodic | 12 | greedy[first] | 20 | 1.0382 | 1.1905 | 0.9316 | 0.400 | 0.00004 |
| repetitive/periodic | 12 | greedy[last] | 20 | 1.0485 | 1.1429 | 0.9432 | 0.400 | 0.00003 |
| repetitive/periodic | 12 | greedy[lex] | 20 | 1.0492 | 1.2000 | 0.9292 | 0.450 | 0.00003 |
| repetitive/periodic | 12 | greedy[random] | 20 | 1.0424 | 1.3095 | 0.8889 | 0.463 | 0.00003 |
| repetitive/periodic | 12 | greedy[revlex] | 20 | 1.0493 | 1.1429 | 0.9348 | 0.300 | 0.00003 |
| repetitive/periodic | 12 | overlap_graph | 20 | - | - | - | - | 0.00004 |
| repetitive/periodic | 14 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.05866 |
| repetitive/periodic | 14 | greedy[first] | 20 | 1.0621 | 1.2051 | 0.9355 | 0.350 | 0.00005 |
| repetitive/periodic | 14 | greedy[last] | 20 | 1.0474 | 1.1579 | 0.9211 | 0.350 | 0.00004 |
| repetitive/periodic | 14 | greedy[lex] | 20 | 1.0557 | 1.2051 | 0.9355 | 0.450 | 0.00003 |
| repetitive/periodic | 14 | greedy[random] | 20 | 1.0528 | 1.2051 | 0.9355 | 0.355 | 0.00004 |
| repetitive/periodic | 14 | greedy[revlex] | 20 | 1.0581 | 1.1373 | 0.9375 | 0.200 | 0.00004 |
| repetitive/periodic | 14 | overlap_graph | 20 | - | - | - | - | 0.00005 |
| repetitive/periodic | 16 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.29249 |
| repetitive/periodic | 16 | greedy[first] | 20 | 1.0610 | 1.2281 | 0.9085 | 0.250 | 0.00007 |
| repetitive/periodic | 16 | greedy[last] | 20 | 1.0416 | 1.2281 | 0.9085 | 0.500 | 0.00004 |
| repetitive/periodic | 16 | greedy[lex] | 20 | 1.0592 | 1.2281 | 0.9085 | 0.350 | 0.00004 |
| repetitive/periodic | 16 | greedy[random] | 20 | 1.0510 | 1.3469 | 0.8851 | 0.355 | 0.00004 |
| repetitive/periodic | 16 | greedy[revlex] | 20 | 1.0524 | 1.2632 | 0.8944 | 0.300 | 0.00004 |
| repetitive/periodic | 16 | overlap_graph | 20 | - | - | - | - | 0.00006 |
| sampled/bin_src3n | 4 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/bin_src3n | 4 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| sampled/bin_src3n | 4 | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/bin_src3n | 4 | greedy[last] | 20 | 1.0179 | 1.2667 | 0.6923 | 0.900 | 0.00001 |
| sampled/bin_src3n | 4 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/bin_src3n | 4 | greedy[random] | 20 | 1.0058 | 1.2667 | 0.6923 | 0.960 | 0.00001 |
| sampled/bin_src3n | 4 | greedy[revlex] | 20 | 1.0179 | 1.2667 | 0.6923 | 0.900 | 0.00001 |
| sampled/bin_src3n | 4 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| sampled/bin_src3n | 4 | greedy_worst_tie | 20 | 1.0179 | 1.2667 | 0.6923 | 0.900 | 0.00004 |
| sampled/bin_src3n | 4 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| sampled/bin_src3n | 6 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00032 |
| sampled/bin_src3n | 6 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00010 |
| sampled/bin_src3n | 6 | greedy[first] | 20 | 1.0050 | 1.1000 | 0.8889 | 0.950 | 0.00002 |
| sampled/bin_src3n | 6 | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/bin_src3n | 6 | greedy[lex] | 20 | 1.0033 | 1.0667 | 0.9259 | 0.950 | 0.00001 |
| sampled/bin_src3n | 6 | greedy[random] | 20 | 1.0023 | 1.1000 | 0.8889 | 0.970 | 0.00001 |
| sampled/bin_src3n | 6 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/bin_src3n | 6 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| sampled/bin_src3n | 6 | greedy_worst_tie | 20 | 1.0050 | 1.1000 | 0.8889 | 0.950 | 0.00006 |
| sampled/bin_src3n | 6 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| sampled/bin_src3n | 8 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00043 |
| sampled/bin_src3n | 8 | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/bin_src3n | 8 | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/bin_src3n | 8 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/bin_src3n | 8 | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/bin_src3n | 8 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/bin_src3n | 8 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00007 |
| sampled/bin_src3n | 8 | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00007 |
| sampled/bin_src3n | 8 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| sampled/bin_src3n | 10 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00222 |
| sampled/bin_src3n | 10 | greedy[first] | 20 | 1.0067 | 1.1333 | 0.9500 | 0.950 | 0.00002 |
| sampled/bin_src3n | 10 | greedy[last] | 20 | 1.0033 | 1.0667 | 0.9750 | 0.950 | 0.00002 |
| sampled/bin_src3n | 10 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/bin_src3n | 10 | greedy[random] | 20 | 1.0018 | 1.1333 | 0.9500 | 0.980 | 0.00002 |
| sampled/bin_src3n | 10 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/bin_src3n | 10 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00014 |
| sampled/bin_src3n | 10 | greedy_worst_tie | 20 | 1.0067 | 1.1333 | 0.9500 | 0.950 | 0.00014 |
| sampled/bin_src3n | 10 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| sampled/bin_src3n | 12 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01159 |
| sampled/bin_src3n | 12 | greedy[first] | 20 | 1.0057 | 1.1143 | 0.9545 | 0.950 | 0.00003 |
| sampled/bin_src3n | 12 | greedy[last] | 20 | 1.0133 | 1.1515 | 0.9419 | 0.900 | 0.00003 |
| sampled/bin_src3n | 12 | greedy[lex] | 20 | 1.0087 | 1.1143 | 0.9545 | 0.900 | 0.00002 |
| sampled/bin_src3n | 12 | greedy[random] | 20 | 1.0086 | 1.1714 | 0.9318 | 0.925 | 0.00002 |
| sampled/bin_src3n | 12 | greedy[revlex] | 20 | 1.0057 | 1.1143 | 0.9545 | 0.950 | 0.00002 |
| sampled/bin_src3n | 12 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| sampled/bin_src3n | 14 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.05830 |
| sampled/bin_src3n | 14 | greedy[first] | 20 | 1.0063 | 1.1250 | 0.9457 | 0.950 | 0.00004 |
| sampled/bin_src3n | 14 | greedy[last] | 20 | 1.0024 | 1.0488 | 0.9813 | 0.950 | 0.00003 |
| sampled/bin_src3n | 14 | greedy[lex] | 20 | 1.0071 | 1.1429 | 0.9483 | 0.950 | 0.00003 |
| sampled/bin_src3n | 14 | greedy[random] | 20 | 1.0086 | 1.1429 | 0.9457 | 0.917 | 0.00003 |
| sampled/bin_src3n | 14 | greedy[revlex] | 20 | 1.0096 | 1.1429 | 0.9483 | 0.900 | 0.00003 |
| sampled/bin_src3n | 14 | overlap_graph | 20 | - | - | - | - | 0.00004 |
| sampled/bin_src3n | 16 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.28995 |
| sampled/bin_src3n | 16 | greedy[first] | 20 | 1.0106 | 1.0833 | 0.9675 | 0.750 | 0.00005 |
| sampled/bin_src3n | 16 | greedy[last] | 20 | 1.0084 | 1.0625 | 0.9781 | 0.800 | 0.00003 |
| sampled/bin_src3n | 16 | greedy[lex] | 20 | 1.0106 | 1.0833 | 0.9675 | 0.750 | 0.00003 |
| sampled/bin_src3n | 16 | greedy[random] | 20 | 1.0112 | 1.1667 | 0.9350 | 0.762 | 0.00003 |
| sampled/bin_src3n | 16 | greedy[revlex] | 20 | 1.0084 | 1.0625 | 0.9781 | 0.800 | 0.00003 |
| sampled/bin_src3n | 16 | overlap_graph | 20 | - | - | - | - | 0.00005 |
| sampled/dna_src4n | 4 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/dna_src4n | 4 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| sampled/dna_src4n | 4 | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/dna_src4n | 4 | greedy[last] | 20 | 1.0033 | 1.0667 | 0.7143 | 0.950 | 0.00001 |
| sampled/dna_src4n | 4 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/dna_src4n | 4 | greedy[random] | 20 | 1.0008 | 1.0667 | 0.7143 | 0.988 | 0.00001 |
| sampled/dna_src4n | 4 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/dna_src4n | 4 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/dna_src4n | 4 | greedy_worst_tie | 20 | 1.0033 | 1.0667 | 0.7143 | 0.950 | 0.00003 |
| sampled/dna_src4n | 4 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| sampled/dna_src4n | 6 | bruteforce | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00033 |
| sampled/dna_src4n | 6 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00011 |
| sampled/dna_src4n | 6 | greedy[first] | 20 | 1.0013 | 1.0263 | 0.9615 | 0.950 | 0.00002 |
| sampled/dna_src4n | 6 | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/dna_src4n | 6 | greedy[lex] | 20 | 1.0013 | 1.0263 | 0.9615 | 0.950 | 0.00001 |
| sampled/dna_src4n | 6 | greedy[random] | 20 | 1.0007 | 1.0263 | 0.9615 | 0.975 | 0.00001 |
| sampled/dna_src4n | 6 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/dna_src4n | 6 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00006 |
| sampled/dna_src4n | 6 | greedy_worst_tie | 20 | 1.0013 | 1.0263 | 0.9615 | 0.950 | 0.00006 |
| sampled/dna_src4n | 6 | overlap_graph | 20 | - | - | - | - | 0.00001 |
| sampled/dna_src4n | 8 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00043 |
| sampled/dna_src4n | 8 | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 8 | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 8 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/dna_src4n | 8 | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| sampled/dna_src4n | 8 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 8 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00007 |
| sampled/dna_src4n | 8 | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00007 |
| sampled/dna_src4n | 8 | overlap_graph | 20 | - | - | - | - | 0.00002 |
| sampled/dna_src4n | 10 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00224 |
| sampled/dna_src4n | 10 | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 10 | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 10 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 10 | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 10 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 10 | greedy_best_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00012 |
| sampled/dna_src4n | 10 | greedy_worst_tie | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00012 |
| sampled/dna_src4n | 10 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| sampled/dna_src4n | 12 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.01148 |
| sampled/dna_src4n | 12 | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/dna_src4n | 12 | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 12 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 12 | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 12 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 12 | overlap_graph | 20 | - | - | - | - | 0.00003 |
| sampled/dna_src4n | 14 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.05834 |
| sampled/dna_src4n | 14 | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00004 |
| sampled/dna_src4n | 14 | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/dna_src4n | 14 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 14 | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/dna_src4n | 14 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/dna_src4n | 14 | overlap_graph | 20 | - | - | - | - | 0.00004 |
| sampled/dna_src4n | 16 | dp | 20 | 1.0000 | 1 | 1 | 1.000 | 0.28821 |
| sampled/dna_src4n | 16 | greedy[first] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| sampled/dna_src4n | 16 | greedy[last] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/dna_src4n | 16 | greedy[lex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| sampled/dna_src4n | 16 | greedy[random] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/dna_src4n | 16 | greedy[revlex] | 20 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| sampled/dna_src4n | 16 | overlap_graph | 20 | - | - | - | - | 0.00005 |

## Tie sensitivity

| group | n | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | mean tie steps | mean G/OPT (first) | max G/OPT observed | max G/OPT all ties |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| random/bin_l4-8 | 4 | 20 | dp | 0.150 | 1.20 | 0.850 | 1.1 | 1.0110 | 1.1539 | 1.1539 |
| random/bin_l4-8 | 6 | 20 | dp | 0.500 | 1.55 | 0.775 | 2.5 | 1.0073 | 1.0769 | 1.0769 |
| random/bin_l4-8 | 8 | 20 | dp | 0.650 | 1.80 | 0.655 | 4.0 | 1.0180 | 1.1600 | 1.1600 |
| random/bin_l4-8 | 10 | 20 | dp | 0.700 | 1.85 | 0.745 | 5.8 | 1.0056 | 1.0732 | 1.0976 |
| random/bin_l4-8 | 12 | 20 | dp | 0.650 | 1.95 | 0.662 | 7.2 | 1.0095 | 1.1111 | - |
| random/bin_l4-8 | 14 | 20 | dp | 0.750 | 2.40 | 0.535 | 9.5 | 1.0175 | 1.1539 | - |
| random/bin_l4-8 | 16 | 20 | dp | 0.950 | 2.55 | 0.620 | 11.5 | 1.0140 | 1.1000 | - |
| random/dna_l5-12 | 4 | 20 | dp | 0.200 | 1.20 | 0.932 | 1.9 | 1.0000 | 1.0312 | 1.0312 |
| random/dna_l5-12 | 6 | 20 | dp | 0.300 | 1.30 | 0.887 | 3.1 | 1.0014 | 1.0667 | 1.0667 |
| random/dna_l5-12 | 8 | 20 | dp | 0.500 | 1.60 | 0.847 | 5.0 | 1.0034 | 1.0517 | 1.0517 |
| random/dna_l5-12 | 10 | 20 | dp | 0.600 | 1.70 | 0.785 | 6.7 | 1.0014 | 1.0411 | 1.0411 |
| random/dna_l5-12 | 12 | 20 | dp | 0.650 | 2.00 | 0.703 | 8.2 | 1.0039 | 1.0577 | - |
| random/dna_l5-12 | 14 | 20 | dp | 0.700 | 2.05 | 0.725 | 10.6 | 1.0021 | 1.0339 | - |
| random/dna_l5-12 | 16 | 20 | dp | 0.550 | 1.85 | 0.728 | 12.3 | 1.0013 | 1.0392 | - |
| repetitive/cyclic_k6 | 4 | 20 | dp | 0.350 | 1.40 | 0.807 | 2.1 | 1.0232 | 1.2222 | 1.2222 |
| repetitive/cyclic_k6 | 6 | 20 | dp | 0.700 | 2.45 | 0.610 | 4.5 | 1.0587 | 1.3636 | 1.3636 |
| repetitive/cyclic_k6 | 8 | 20 | dp | 1.000 | 3.50 | 0.348 | 6.0 | 1.0834 | 1.3077 | 1.3077 |
| repetitive/cyclic_k6 | 10 | 20 | dp | 1.000 | 4.00 | 0.210 | 7.4 | 1.0902 | 1.3333 | 1.4210 |
| repetitive/cyclic_k6 | 12 | 20 | dp | 1.000 | 5.10 | 0.145 | 9.4 | 1.1020 | 1.4210 | - |
| repetitive/cyclic_k6 | 14 | 20 | dp | 1.000 | 5.65 | 0.092 | 11.3 | 1.1220 | 1.4210 | - |
| repetitive/cyclic_k6 | 16 | 20 | dp | 1.000 | 6.10 | 0.143 | 13.1 | 1.1147 | 1.3077 | - |
| repetitive/kmer_k8 | 4 | 20 | dp | 0.350 | 1.70 | 0.860 | 2.2 | 1.0091 | 1.1818 | 1.1818 |
| repetitive/kmer_k8 | 6 | 20 | dp | 0.500 | 2.40 | 0.780 | 4.0 | 1.0154 | 1.3077 | 1.3077 |
| repetitive/kmer_k8 | 8 | 20 | dp | 0.600 | 2.40 | 0.710 | 5.8 | 1.0500 | 1.4667 | 1.4667 |
| repetitive/kmer_k8 | 10 | 20 | dp | 0.700 | 3.00 | 0.715 | 7.8 | 1.0559 | 1.4118 | 1.4118 |
| repetitive/kmer_k8 | 12 | 20 | dp | 0.650 | 3.35 | 0.660 | 9.9 | 1.0526 | 1.3684 | - |
| repetitive/kmer_k8 | 14 | 20 | dp | 0.900 | 4.45 | 0.525 | 11.8 | 1.0571 | 1.4286 | - |
| repetitive/kmer_k8 | 16 | 20 | dp | 0.850 | 4.00 | 0.600 | 13.8 | 1.0609 | 1.4783 | - |
| repetitive/periodic | 4 | 20 | dp | 0.200 | 1.20 | 0.903 | 0.8 | 1.0025 | 1.1500 | 1.1500 |
| repetitive/periodic | 6 | 20 | dp | 0.350 | 1.50 | 0.722 | 1.9 | 1.0290 | 1.4783 | 1.4783 |
| repetitive/periodic | 8 | 20 | dp | 0.600 | 1.95 | 0.398 | 3.0 | 1.0598 | 1.2963 | 1.2963 |
| repetitive/periodic | 10 | 20 | dp | 0.750 | 2.50 | 0.453 | 4.4 | 1.0445 | 1.3077 | 1.3171 |
| repetitive/periodic | 12 | 20 | dp | 0.750 | 2.35 | 0.463 | 5.6 | 1.0382 | 1.3095 | - |
| repetitive/periodic | 14 | 20 | dp | 0.750 | 2.30 | 0.355 | 7.7 | 1.0621 | 1.2051 | - |
| repetitive/periodic | 16 | 20 | dp | 0.850 | 3.20 | 0.355 | 8.7 | 1.0610 | 1.3469 | - |
| sampled/bin_src3n | 4 | 20 | dp | 0.100 | 1.10 | 0.960 | 0.4 | 1.0000 | 1.2667 | 1.2667 |
| sampled/bin_src3n | 6 | 20 | dp | 0.050 | 1.10 | 0.970 | 1.6 | 1.0050 | 1.1000 | 1.1000 |
| sampled/bin_src3n | 8 | 20 | dp | 0.000 | 1.00 | 1.000 | 2.5 | 1.0000 | 1 | 1 |
| sampled/bin_src3n | 10 | 20 | dp | 0.050 | 1.10 | 0.980 | 4.8 | 1.0067 | 1.1333 | 1.1333 |
| sampled/bin_src3n | 12 | 20 | dp | 0.100 | 1.25 | 0.925 | 6.0 | 1.0057 | 1.1714 | - |
| sampled/bin_src3n | 14 | 20 | dp | 0.150 | 1.15 | 0.918 | 7.6 | 1.0063 | 1.1429 | - |
| sampled/bin_src3n | 16 | 20 | dp | 0.150 | 1.25 | 0.762 | 9.8 | 1.0106 | 1.1667 | - |
| sampled/dna_src4n | 4 | 20 | dp | 0.050 | 1.05 | 0.988 | 0.5 | 1.0000 | 1.0667 | 1.0667 |
| sampled/dna_src4n | 6 | 20 | dp | 0.050 | 1.05 | 0.975 | 1.1 | 1.0013 | 1.0263 | 1.0263 |
| sampled/dna_src4n | 8 | 20 | dp | 0.000 | 1.00 | 1.000 | 1.9 | 1.0000 | 1 | 1 |
| sampled/dna_src4n | 10 | 20 | dp | 0.000 | 1.00 | 1.000 | 3.5 | 1.0000 | 1 | 1 |
| sampled/dna_src4n | 12 | 20 | dp | 0.000 | 1.00 | 1.000 | 4.9 | 1.0000 | 1 | - |
| sampled/dna_src4n | 14 | 20 | dp | 0.000 | 1.00 | 1.000 | 6.1 | 1.0000 | 1 | - |
| sampled/dna_src4n | 16 | 20 | dp | 0.000 | 1.00 | 1.000 | 8.0 | 1.0000 | 1 | - |
