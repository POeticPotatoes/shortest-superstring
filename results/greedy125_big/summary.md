# Benchmark summary: `results/greedy125_big`

2 instances, 32 solver runs.

## Solution quality and runtime

Ratio basis `G/OPT` uses an exact optimum (DP or certificate).  `G/|H| (lower bound)` uses a known common superstring H >= OPT, so it is a certified lower bound on G/OPT; these rows are reported separately.

| group | n | basis | algo | inst | mean ratio | max ratio | min compr. ratio | optimal rate | mean time (s) |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.4099 | 1.4945 | - | - | 0.06327 |
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.3674 | 2.3674 | - | - | 0.05482 |
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | greedy[last] | 1 | 2.3576 | 2.3576 | - | - | 0.04676 |
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.5857 | 1.5857 | - | - | 0.05910 |
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.3674 | 2.3674 | - | - | 0.05180 |
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.4084 | 1.4266 | - | - | 0.04908 |
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5917 | 1.5917 | - | - | 0.05470 |
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 36.08560 |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | greedy[first@shuffled] | 1 | 1.3878 | 1.4625 | - | - | 0.02632 |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | greedy[first] | 1 | 2.3541 | 2.3541 | - | - | 0.02478 |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | greedy[last] | 1 | 2.3402 | 2.3402 | - | - | 0.02560 |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | greedy[lex] | 1 | 1.5796 | 1.5796 | - | - | 0.02407 |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | greedy[paper] | 1 | 2.3541 | 2.3541 | - | - | 0.02508 |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | greedy[random] | 1 | 1.4460 | 1.4840 | - | - | 0.02230 |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | greedy[revlex] | 1 | 1.5882 | 1.5882 | - | - | 0.02143 |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | overlap_graph | 1 | - | - | - | - | 8.79786 |

## Tie sensitivity

| group | n | basis | inst | OPT via | tie-sensitive | mean distinct (random) | random optimal | mean tie steps | mean ratio (first) | max ratio observed | max ratio all ties |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | 1 | none | 1.000 | 5.00 | - | - | 2.3674 | 2.3674 | - |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | 1 | none | 1.000 | 5.00 | - | - | 2.3541 | 2.3541 | - |

## Prescribed (paper) execution vs tie rules

| instance | n | basis | ref | OPT | \|H\| | G (paper) | ratio paper | ratio first | ratio random mean | ratio random max | random reaches paper |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| greedy125_r100_P10000 | 500 | G/\|H\| (lower bound) | 5311901 | - | 5311901 | 12575350 | 2.3674 | 2.3674 | 1.4084 | 1.4266 | 0 |
| greedy125_r70_P4900 | 350 | G/\|H\| (lower bound) | 1868231 | - | 1868231 | 4397995 | 2.3541 | 2.3541 | 1.4460 | 1.4840 | 0 |
