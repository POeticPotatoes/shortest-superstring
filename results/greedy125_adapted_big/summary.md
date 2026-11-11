# Benchmark summary: `results/greedy125_adapted_big`

2 instances, 32 solver runs.

## Solution quality and runtime

Ratio basis `G/OPT` uses an exact optimum (DP or certificate).  `G/|H| (lower bound)` uses a known common superstring H >= OPT, so it is a certified lower bound on G/OPT; these rows are reported separately.

| group | n | basis | algo | inst | mean ratio | max ratio | min compr. ratio | optimal rate | mean time (s) |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.5539 | 1.6053 | - | - | 0.05850 |
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.3737 | 2.3737 | - | - | 0.05619 |
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.7792 | 1.7792 | - | - | 0.03970 |
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.02436 |
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.3737 | 2.3737 | - | - | 0.04859 |
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.5138 | 1.5488 | - | - | 0.04538 |
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5905 | 1.5905 | - | - | 0.04892 |
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 34.41450 |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.5717 | 1.6185 | - | - | 0.02487 |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.3626 | 2.3626 | - | - | 0.02339 |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | greedy[last] | 1 | 1.7704 | 1.7704 | - | - | 0.02027 |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.0000 | 1 | - | - | 0.01301 |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.3626 | 2.3626 | - | - | 0.02293 |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.5196 | 1.5924 | - | - | 0.01930 |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5864 | 1.5864 | - | - | 0.01921 |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 8.39363 |

## Tie sensitivity

| group | n | basis | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | mean tie steps | mean ratio (first) | max ratio observed | max ratio all ties |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | 1 | none | 1.000 | 5.00 | - | - | 2.3737 | 2.3737 | - |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | 1 | none | 1.000 | 5.00 | - | - | 2.3626 | 2.3626 | - |

## Prescribed (paper) execution vs tie rules

| instance | n | basis | ref | OPT | \|H\| | G (paper) | ratio paper | ratio first | ratio random mean | ratio random max | random reaches paper |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| greedy125adapted_n100 | 495 | G/\|H\| (lower bound) | 5119799 | - | 5119799 | 12152844 | 2.3737 | 2.3737 | 1.5138 | 1.5488 | 0 |
| greedy125adapted_n70 | 345 | G/\|H\| (lower bound) | 1773659 | - | 1773659 | 4190439 | 2.3626 | 2.3626 | 1.5196 | 1.5924 | 0 |
