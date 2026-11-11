# Benchmark summary: `results/greedy125_adapted`

11 instances, 844 solver runs.

## Solution quality and runtime

Ratio basis `G/OPT` uses an exact optimum (DP or certificate).  `G/|H| (lower bound)` uses a known common superstring H >= OPT, so it is a certified lower bound on G/OPT; these rows are reported separately.

| group | n | basis | algo | inst | mean ratio | max ratio | min compr. ratio | optimal rate | mean time (s) |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.4784 | 1.6783 | - | - | 0.00039 |
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.1572 | 2.1572 | - | - | 0.00039 |
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.6156 | 1.6156 | - | - | 0.00029 |
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.00017 |
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.1572 | 2.1572 | - | - | 0.00035 |
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.4029 | 1.7302 | - | - | 0.00031 |
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.4991 | 1.4991 | - | - | 0.00030 |
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.01348 |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.4836 | 1.6620 | - | - | 0.00092 |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.2339 | 2.2339 | - | - | 0.00083 |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.6720 | 1.6720 | - | - | 0.00069 |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.00043 |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.2339 | 2.2339 | - | - | 0.00085 |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.4474 | 1.6452 | - | - | 0.00074 |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5341 | 1.5341 | - | - | 0.00074 |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.00977 |
| greedy125adapted_n2 | 5 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00016 |
| greedy125adapted_n2 | 5 | G/OPT | greedy[first@shuffled] | 1 | 1.1060 | 1.3133 | 0.8289 | 0.600 | 0.00002 |
| greedy125adapted_n2 | 5 | G/OPT | greedy[first] | 1 | 1.3133 | 1.3133 | 0.8289 | 0.000 | 0.00004 |
| greedy125adapted_n2 | 5 | G/OPT | greedy[last] | 1 | 1.2048 | 1.2048 | 0.8882 | 0.000 | 0.00002 |
| greedy125adapted_n2 | 5 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00001 |
| greedy125adapted_n2 | 5 | G/OPT | greedy[paper] | 1 | 1.3133 | 1.3133 | 0.8289 | 0.000 | 0.00002 |
| greedy125adapted_n2 | 5 | G/OPT | greedy[random] | 1 | 1.1443 | 1.3133 | 0.8289 | 0.460 | 0.00001 |
| greedy125adapted_n2 | 5 | G/OPT | greedy[revlex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| greedy125adapted_n2 | 5 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00017 |
| greedy125adapted_n2 | 5 | G/OPT | greedy_worst_tie | 1 | 1.3133 | 1.3133 | 0.8289 | 0.000 | 0.00017 |
| greedy125adapted_n2 | 5 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00005 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.5195 | 1.6669 | - | - | 0.00166 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.2736 | 2.2736 | - | - | 0.00161 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.7019 | 1.7019 | - | - | 0.00133 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.00083 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.2736 | 2.2736 | - | - | 0.00153 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.4459 | 1.6944 | - | - | 0.00132 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5512 | 1.5512 | - | - | 0.00130 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.03858 |
| greedy125adapted_n3 | 10 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00392 |
| greedy125adapted_n3 | 10 | G/OPT | greedy[first@shuffled] | 1 | 1.1663 | 1.3983 | 0.8494 | 0.200 | 0.00004 |
| greedy125adapted_n3 | 10 | G/OPT | greedy[first] | 1 | 1.6652 | 1.6652 | 0.7484 | 0.000 | 0.00005 |
| greedy125adapted_n3 | 10 | G/OPT | greedy[last] | 1 | 1.3263 | 1.3263 | 0.8766 | 0.000 | 0.00003 |
| greedy125adapted_n3 | 10 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00002 |
| greedy125adapted_n3 | 10 | G/OPT | greedy[paper] | 1 | 1.6652 | 1.6652 | 0.7484 | 0.000 | 0.00004 |
| greedy125adapted_n3 | 10 | G/OPT | greedy[random] | 1 | 1.2296 | 1.5593 | 0.7885 | 0.100 | 0.00003 |
| greedy125adapted_n3 | 10 | G/OPT | greedy[revlex] | 1 | 1.2246 | 1.2246 | 0.9151 | 0.000 | 0.00003 |
| greedy125adapted_n3 | 10 | G/OPT | greedy_best_tie | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00101 |
| greedy125adapted_n3 | 10 | G/OPT | greedy_worst_tie | 1 | 1.6652 | 1.6652 | 0.7484 | 0.000 | 0.00101 |
| greedy125adapted_n3 | 10 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00019 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.5115 | 1.6721 | - | - | 0.00392 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.3144 | 2.3144 | - | - | 0.00349 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.7330 | 1.7330 | - | - | 0.00300 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.00171 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.3144 | 2.3144 | - | - | 0.00365 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.5030 | 1.6577 | - | - | 0.00308 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5678 | 1.5678 | - | - | 0.00309 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.29117 |
| greedy125adapted_n4 | 15 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 0.14315 |
| greedy125adapted_n4 | 15 | G/OPT | greedy[first@shuffled] | 1 | 1.2951 | 1.5745 | 0.8123 | 0.000 | 0.00006 |
| greedy125adapted_n4 | 15 | G/OPT | greedy[first] | 1 | 1.8370 | 1.8370 | 0.7266 | 0.000 | 0.00008 |
| greedy125adapted_n4 | 15 | G/OPT | greedy[last] | 1 | 1.3936 | 1.3936 | 0.8714 | 0.000 | 0.00005 |
| greedy125adapted_n4 | 15 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00003 |
| greedy125adapted_n4 | 15 | G/OPT | greedy[paper] | 1 | 1.8370 | 1.8370 | 0.7266 | 0.000 | 0.00006 |
| greedy125adapted_n4 | 15 | G/OPT | greedy[random] | 1 | 1.2856 | 1.5984 | 0.8045 | 0.080 | 0.00005 |
| greedy125adapted_n4 | 15 | G/OPT | greedy[revlex] | 1 | 1.3280 | 1.3280 | 0.8929 | 0.000 | 0.00005 |
| greedy125adapted_n4 | 15 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00051 |
| greedy125adapted_n5 | 20 | G/OPT | dp | 1 | 1.0000 | 1 | 1 | 1.000 | 7.59091 |
| greedy125adapted_n5 | 20 | G/OPT | greedy[first@shuffled] | 1 | 1.3834 | 1.6937 | 0.7913 | 0.000 | 0.00010 |
| greedy125adapted_n5 | 20 | G/OPT | greedy[first] | 1 | 1.9409 | 1.9409 | 0.7169 | 0.000 | 0.00011 |
| greedy125adapted_n5 | 20 | G/OPT | greedy[last] | 1 | 1.4639 | 1.4639 | 0.8604 | 0.000 | 0.00008 |
| greedy125adapted_n5 | 20 | G/OPT | greedy[lex] | 1 | 1.0000 | 1 | 1 | 1.000 | 0.00005 |
| greedy125adapted_n5 | 20 | G/OPT | greedy[paper] | 1 | 1.9409 | 1.9409 | 0.7169 | 0.000 | 0.00010 |
| greedy125adapted_n5 | 20 | G/OPT | greedy[random] | 1 | 1.3611 | 1.7265 | 0.7814 | 0.000 | 0.00008 |
| greedy125adapted_n5 | 20 | G/OPT | greedy[revlex] | 1 | 1.3873 | 1.3873 | 0.8835 | 0.000 | 0.00009 |
| greedy125adapted_n5 | 20 | G/OPT | overlap_graph | 1 | - | - | - | - | 0.00104 |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.5362 | 1.6400 | - | - | 0.01069 |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.3479 | 2.3479 | - | - | 0.01011 |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.7590 | 1.7590 | - | - | 0.00899 |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.00494 |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.3479 | 2.3479 | - | - | 0.01066 |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.5056 | 1.6022 | - | - | 0.00896 |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5809 | 1.5809 | - | - | 0.00842 |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 2.17919 |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.3411 | 1.6331 | - | - | 0.00013 |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.0113 | 2.0113 | - | - | 0.00013 |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.5123 | 1.5123 | - | - | 0.00010 |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.00006 |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.0113 | 2.0113 | - | - | 0.00013 |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3902 | 1.7992 | - | - | 0.00011 |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.4256 | 1.4256 | - | - | 0.00011 |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.00197 |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.4758 | 1.6844 | - | - | 0.00024 |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.1015 | 2.1015 | - | - | 0.00022 |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.5757 | 1.5757 | - | - | 0.00018 |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.00011 |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.1015 | 2.1015 | - | - | 0.00022 |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.3993 | 1.6741 | - | - | 0.00019 |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.4721 | 1.4721 | - | - | 0.00019 |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 0.00549 |

## Tie sensitivity

| group | n | basis | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | mean tie steps | mean ratio (first) | max ratio observed | max ratio all ties |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | 1 | none | 1.000 | 50.00 | - | - | 2.1572 | 2.1572 | - |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | 1 | none | 1.000 | 50.00 | - | - | 2.2339 | 2.2339 | - |
| greedy125adapted_n2 | 5 | G/OPT | 1 | dp | 1.000 | 5.00 | 0.460 | - | 1.3133 | 1.3133 | 1.3133 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | 1 | none | 1.000 | 50.00 | - | - | 2.2736 | 2.2736 | - |
| greedy125adapted_n3 | 10 | G/OPT | 1 | dp | 1.000 | 12.00 | 0.100 | - | 1.6652 | 1.6652 | 1.6652 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | 1 | none | 1.000 | 50.00 | - | - | 2.3144 | 2.3144 | - |
| greedy125adapted_n4 | 15 | G/OPT | 1 | dp | 1.000 | 30.00 | 0.080 | - | 1.8370 | 1.8370 | - |
| greedy125adapted_n5 | 20 | G/OPT | 1 | dp | 1.000 | 39.00 | 0.000 | - | 1.9409 | 1.9409 | - |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | 1 | none | 1.000 | 50.00 | - | - | 2.3479 | 2.3479 | - |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | 1 | none | 1.000 | 48.00 | - | - | 2.0113 | 2.0113 | - |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | 1 | none | 1.000 | 49.00 | - | - | 2.1015 | 2.1015 | - |

## Prescribed (paper) execution vs tie rules

| instance | n | basis | ref | OPT | \|H\| | G (paper) | ratio paper | ratio first | ratio random mean | ratio random max | random reaches paper |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| greedy125adapted_n2 | 5 | G/OPT | 83 | 83 | 83 | 109 | 1.3133 | 1.3133 | 1.1443 | 1.3133 | 1 |
| greedy125adapted_n3 | 10 | G/OPT | 236 | 236 | 236 | 393 | 1.6652 | 1.6652 | 1.2296 | 1.5593 | 0 |
| greedy125adapted_n4 | 15 | G/OPT | 503 | 503 | 503 | 924 | 1.8370 | 1.8370 | 1.2856 | 1.5984 | 0 |
| greedy125adapted_n5 | 20 | G/OPT | 914 | 914 | 914 | 1774 | 1.9409 | 1.9409 | 1.3611 | 1.7265 | 0 |
| greedy125adapted_n10 | 45 | G/\|H\| (lower bound) | 6179 | - | 6179 | 13329 | 2.1572 | 2.1572 | 1.4029 | 1.7302 | 0 |
| greedy125adapted_n15 | 70 | G/\|H\| (lower bound) | 19544 | - | 19544 | 43659 | 2.2339 | 2.2339 | 1.4474 | 1.6452 | 0 |
| greedy125adapted_n20 | 95 | G/\|H\| (lower bound) | 44759 | - | 44759 | 101764 | 2.2736 | 2.2736 | 1.4459 | 1.6944 | 0 |
| greedy125adapted_n30 | 145 | G/\|H\| (lower bound) | 145739 | - | 145739 | 337299 | 2.3144 | 2.3144 | 1.5030 | 1.6577 | 0 |
| greedy125adapted_n50 | 245 | G/\|H\| (lower bound) | 654899 | - | 654899 | 1537669 | 2.3479 | 2.3479 | 1.5056 | 1.6022 | 0 |
| greedy125adapted_n6 | 25 | G/\|H\| (lower bound) | 1499 | - | 1499 | 3015 | 2.0113 | 2.0113 | 1.3901 | 1.7992 | 0 |
| greedy125adapted_n8 | 35 | G/\|H\| (lower bound) | 3311 | - | 3311 | 6958 | 2.1015 | 2.1015 | 1.3994 | 1.6741 | 0 |
