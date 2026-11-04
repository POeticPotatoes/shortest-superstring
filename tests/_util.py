"""Shared helpers for tests: small seeded instance pools."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scs.generators import random_strings, repetitive_strings, sampled_fragments  # noqa: E402


def small_instances(count=60, n=6):
    """Mixed small instances (binary alphabets, so there are plenty of ties)."""
    out = []
    for seed in range(count):
        kind = seed % 4
        if kind == 0:
            inst = random_strings(n, (3, 6), "AB", seed=seed)
        elif kind == 1:
            inst = sampled_fragments(n, 20, (4, 7), "AB", seed=seed)
        elif kind == 2:
            inst = repetitive_strings(n, "cyclic", k=5, alphabet="AB", seed=seed)
        else:
            inst = repetitive_strings(n, "periodic", alphabet="AB", mutation_rate=0.2, fragment_length=(4, 8), source_length=80,
                                      seed=seed)
        out.append(inst["strings"])
    return out
