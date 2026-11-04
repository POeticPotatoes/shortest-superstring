"""Synthetic instance generators (slide 12).

Every generator is a pure function of its parameters and an integer
``seed``.  It uses its own ``random.Random(seed)``, so an instance can be
regenerated exactly from the parameters stored with it.  Generators return an
*instance dict* (see :mod:`scs.instance_io`) whose ``params`` and ``seed``
fields are enough to rebuild it.

Families
--------
``random``
    Independent uniformly random strings.  Tests general behaviour.
``sampled``
    Fragments sampled from one random source string, like sequencing reads.
    The source is a feasible superstring, but not necessarily the shortest.
``repetitive``
    Inputs with many long, ambiguous overlaps and hence many greedy ties:

    * ``periodic``: fragments of a mutated periodic text (tandem repeats),
    * ``cyclic``: unions of cyclic k-spectra of random short words.  This is
      the structure behind all the recent bad-greedy constructions (Chukhin
      et al. 2026, Shibata 2026),
    * ``kmer``: the k-spectrum of a low-entropy text.  It is an equal-length
      instance whose OPT can often be certified exactly for large n.

With ``exact_n=True`` (the default) generators keep sampling until the
instance has exactly ``n`` strings after preprocessing.  The exact solvers'
cost depends on that count.

Input order matters for index-based tie rules (``first``/``last``).
Generators output strings in random order and never in an order that spells
the source text.
"""

from __future__ import annotations

import hashlib
import random
from typing import Sequence

from .core import preprocess

DNA = "ACGT"
GENERATOR_VERSION = 1


def derive_seed(*parts) -> int:
    """Deterministic 63-bit seed from arbitrary parts (stable across Python versions)."""
    h = hashlib.sha256(":".join(map(str, parts)).encode()).digest()
    return int.from_bytes(h[:8], "big") >> 1


def _length(rng: random.Random, length) -> int:
    if isinstance(length, int):
        return length
    lo, hi = length
    return rng.randint(lo, hi)


def _rand_word(rng: random.Random, k: int, alphabet: str) -> str:
    return "".join(rng.choice(alphabet) for _ in range(k))


class _SubstringFreeCollector:
    """Incrementally collect strings, keeping the set substring-free."""

    def __init__(self):
        self.items: list[str] = []
        self.raw = 0

    def offer(self, s: str) -> bool:
        self.raw += 1
        if any(s in t for t in self.items):
            return False
        self.items = [t for t in self.items if t not in s]
        self.items.append(s)
        return True


def _instance(family: str, strings: list[str], params: dict, seed: int, **extra) -> dict:
    inst = {
        "family": family,
        "generator": f"scs.generators.{family}",
        "generator_version": GENERATOR_VERSION,
        "params": params,
        "seed": seed,
        "strings": strings,
    }
    inst.update(extra)
    return inst


def random_strings(n: int, length=(5, 12), alphabet: str = DNA, *, seed: int,
                   exact_n: bool = True, max_tries: int | None = None) -> dict:
    """``n`` independent uniform random strings with lengths drawn from ``length`` (int or (lo, hi))."""
    rng = random.Random(seed)
    params = {"n": n, "length": length, "alphabet": alphabet, "exact_n": exact_n}
    if not exact_n:
        strings = [_rand_word(rng, _length(rng, length), alphabet) for _ in range(n)]
        return _instance("random", strings, params, seed)
    col = _SubstringFreeCollector()
    max_tries = max_tries or 200 * n + 1000
    while len(col.items) < n:
        if col.raw >= max_tries:
            raise ValueError(f"could not draw {n} substring-free random strings with {params}")
        col.offer(_rand_word(rng, _length(rng, length), alphabet))
    return _instance("random", col.items, params, seed, raw_draws=col.raw)


def sampled_fragments(n: int, source_length: int | None = None, fragment_length=(8, 15),
                      alphabet: str = DNA, *, seed: int, source: str | None = None,
                      exact_n: bool = True, max_tries: int | None = None) -> dict:
    """``n`` fragments sampled uniformly from one source string.

    By default the source is a uniform random string of length
    ``source_length`` (default ``4 * n``, so neighbouring fragments overlap
    heavily).  Pass ``source`` to sample from a given text instead.  The
    source is stored with the instance as a feasible superstring.
    """
    rng = random.Random(seed)
    if source is None:
        source_length = source_length or 4 * n
        source = _rand_word(rng, source_length, alphabet)
    params = {"n": n, "source_length": len(source), "fragment_length": fragment_length,
              "alphabet": alphabet, "exact_n": exact_n}
    lo = fragment_length if isinstance(fragment_length, int) else fragment_length[0]
    if lo > len(source):
        raise ValueError("fragments longer than the source")

    def draw() -> str:
        k = min(_length(rng, fragment_length), len(source))
        i = rng.randint(0, len(source) - k)
        return source[i:i + k]

    if not exact_n:
        return _instance("sampled", [draw() for _ in range(n)], params, seed, source=source)
    col = _SubstringFreeCollector()
    max_tries = max_tries or 200 * n + 1000
    while len(col.items) < n:
        if col.raw >= max_tries:
            raise ValueError(f"could not sample {n} substring-free fragments; use a longer source ({params})")
        col.offer(draw())
    return _instance("sampled", col.items, params, seed, source=source, raw_draws=col.raw)


def _periodic_text(rng: random.Random, length: int, motif: str, mutation_rate: float, alphabet: str) -> str:
    out = []
    for i in range(length):
        c = motif[i % len(motif)]
        if rng.random() < mutation_rate:
            c = rng.choice(alphabet)
        out.append(c)
    return "".join(out)


def _cyclic_spectrum(word: str, k: int) -> list[str]:
    w = word * (k // len(word) + 2)
    return [w[i:i + k] for i in range(len(word))]


def repetitive_strings(n: int, mode: str = "periodic", *, seed: int, alphabet: str = DNA,
                       motif_length=(2, 4), mutation_rate: float = 0.08, fragment_length=(8, 14),
                       k: int = 6, word_length=None, source_length: int | None = None,
                       exact_n: bool = True, max_tries: int | None = None) -> dict:
    """Repetitive inputs that cause long, ambiguous overlaps and greedy ties.

    ``mode="periodic"``
        Sample fragments (``fragment_length``) from a periodic text whose
        motif has length ``motif_length``, mutating each character with
        probability ``mutation_rate``.
    ``mode="cyclic"``
        Union of cyclic ``k``-spectra of random words of length
        ``word_length`` (default ``(k//2, k)``), added until ``n`` strings exist.
        All strings have length ``k``.
    ``mode="kmer"``
        All distinct ``k``-mers of a mutated periodic text, grown until ``n``
        distinct k-mers exist, steering away from repeated k-mers.  The text is
        stored as ``source``.  With ``repeated_kmers == 0`` it is an optimal
        superstring (OPT = n + k - 1).
    """
    rng = random.Random(seed)
    params = {"n": n, "mode": mode, "alphabet": alphabet, "exact_n": exact_n}
    max_tries = max_tries or 200 * n + 1000

    if mode == "periodic":
        src_len = source_length or max(8 * n, 80)
        params.update(motif_length=motif_length, mutation_rate=mutation_rate,
                      fragment_length=fragment_length, source_length=src_len)
        # A text with a short motif and few mutations may not contain n
        # substring-free fragments.  Retry with a new text (deterministically).
        for attempt in range(10):
            motif = _rand_word(rng, _length(rng, motif_length), alphabet)
            text = _periodic_text(rng, src_len, motif, mutation_rate, alphabet)
            try:
                inst = sampled_fragments(n, fragment_length=fragment_length, alphabet=alphabet,
                                         seed=derive_seed(seed, "fragments", attempt), source=text,
                                         exact_n=exact_n, max_tries=max_tries)
            except ValueError:
                continue
            return _instance("repetitive", inst["strings"], params, seed, source=text, motif=motif,
                             raw_draws=inst.get("raw_draws"), attempt=attempt)
        raise ValueError(f"could not sample {n} substring-free periodic fragments; raise source_length "
                         f"or mutation_rate ({params})")

    if mode == "cyclic":
        word_length = word_length or (max(2, k // 2), k)
        params.update(k=k, word_length=word_length)
        col = _SubstringFreeCollector()
        words = []
        while len(col.items) < n:
            if col.raw >= max_tries:
                raise ValueError(f"could not build {n} cyclic-spectrum strings with {params}")
            word = _rand_word(rng, _length(rng, word_length), alphabet)
            words.append(word)
            for s in _cyclic_spectrum(word, k):
                if len(col.items) >= n and exact_n:
                    break
                col.offer(s)
        strings = col.items[:]
        rng.shuffle(strings)  # rotations come out in cyclic order, which would leak a good merge order
        return _instance("repetitive", strings, params, seed, words=words, raw_draws=col.raw)

    if mode == "kmer":
        motif = _rand_word(rng, _length(rng, motif_length), alphabet)
        params.update(k=k, motif_length=motif_length, mutation_rate=mutation_rate)
        # Self-avoiding walk in the de Bruijn graph: if the next character would
        # repeat a k-mer, try the other characters (random order).  When no
        # k-mer repeats, the text is an Eulerian trail of its own spectrum, so
        # OPT = len(text) = n + k - 1 is certified (see scs.exact.kspectrum_certificate).
        text = _periodic_text(rng, k - 1, motif, mutation_rate, alphabet)
        kmers: dict[str, None] = {}
        repeats = 0
        while len(kmers) < n:
            if len(text) > max_tries + k:
                raise ValueError(f"could not reach {n} distinct {k}-mers; raise mutation_rate ({params})")
            c = motif[len(text) % len(motif)]
            if rng.random() < mutation_rate:
                c = rng.choice(alphabet)
            if text[len(text) - k + 1:] + c in kmers:
                others = [a for a in alphabet if a != c]
                rng.shuffle(others)
                fresh = [a for a in others if text[len(text) - k + 1:] + a not in kmers]
                if fresh:
                    c = fresh[0]
                else:
                    repeats += 1
            text += c
            kmers.setdefault(text[-k:], None)
        strings = list(kmers)
        rng.shuffle(strings)  # text order would hand index-based tie rules the optimal order
        return _instance("repetitive", strings, params, seed, source=text, motif=motif,
                         repeated_kmers=repeats)

    raise ValueError(f"unknown repetitive mode {mode!r}")


def shuffled(strings: Sequence[str], seed: int) -> list[str]:
    """Shuffle input order, e.g. to test sensitivity of index-based tie rules."""
    out = list(strings)
    random.Random(seed).shuffle(out)
    return out


GENERATORS = {
    "random": random_strings,
    "sampled": sampled_fragments,
    "repetitive": repetitive_strings,
}


def generate(family: str, seed: int, **params) -> dict:
    """Dispatch to a generator by family name, e.g. ``generate("random", 1, n=8)``."""
    inst = GENERATORS[family](seed=seed, **params)
    assert family != "random" or not inst["params"]["exact_n"] or len(preprocess(inst["strings"])) == params["n"]
    return inst
