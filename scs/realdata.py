"""Real-world (genome sequencing) data: FASTA/FASTQ parsing, read simulation, and read filtering.

Shortest superstring is the textbook model of *de novo* genome assembly: the
reads are the input strings and the genome is (ideally) a short common
superstring.  Real data differs from the clean SCS model in two ways, and the
instance builders below make each choice explicit:

* **Sequencing errors.**  A read with an error is not a substring of the genome,
  so the genome is no longer a common superstring.  :func:`orient_exact_reads`
  keeps only reads that occur exactly in the reference ("exact" instances).
  Raw reads keep the errors, and then no reference bound on OPT exists.
* **Strands.**  Reads come from both DNA strands, but SCS has no notion of
  reverse complements.  "Exact" instances flip reverse-strand reads onto the
  forward strand using the reference (a reference-guided step, recorded in the
  instance).  Raw instances keep both strands.
* **Circular genomes** (phages such as phiX174) are linearised as
  ``genome + genome[:read_length - 1]`` so reads that span the origin are
  substrings.

For error-free reads the (linearised) genome, or the window of it that the
reads cover, is a common superstring.  It is stored as ``upper_superstring``,
so benchmarks report the certified lower bound G/|H| <= G/OPT, as for the 12/5
construction.
"""

from __future__ import annotations

import gzip
import random
from typing import Iterator, Sequence

DNA = "ACGT"
_COMPLEMENT = str.maketrans("ACGTN", "TGCAN")


def _open_text(path):
    path = str(path)
    return gzip.open(path, "rt", encoding="ascii") if path.endswith(".gz") else open(path, encoding="ascii")


def read_fasta(path) -> list[tuple[str, str]]:
    """Parse a (possibly gzipped) FASTA file into ``[(header, SEQUENCE)]`` (upper case)."""
    records: list[tuple[str, str]] = []
    header, parts = None, []
    with _open_text(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    records.append((header, "".join(parts).upper()))
                header, parts = line[1:], []
            elif header is None:
                raise ValueError(f"{path}: sequence data before the first FASTA header")
            else:
                parts.append(line)
    if header is not None:
        records.append((header, "".join(parts).upper()))
    return records


def read_fastq(path, limit: int | None = None) -> Iterator[tuple[str, str]]:
    """Yield ``(read_id, SEQUENCE)`` from a (possibly gzipped) 4-line FASTQ file."""
    with _open_text(path) as fh:
        count = 0
        while limit is None or count < limit:
            head = fh.readline()
            if not head:
                return
            seq, plus, qual = fh.readline().strip(), fh.readline(), fh.readline()
            if not head.startswith("@") or not plus.startswith("+") or not qual:
                raise ValueError(f"{path}: malformed FASTQ record near read {count + 1}")
            yield head[1:].split()[0], seq.upper()
            count += 1


def reverse_complement(s: str) -> str:
    return s.translate(_COMPLEMENT)[::-1]


def linearize(genome: str, circular: bool, read_length: int) -> str:
    """Genome as a linear text in which every read (including origin-spanning ones) occurs."""
    return genome + genome[:read_length - 1] if circular else genome


def simulate_reads(genome: str, *, read_length: int, n: int | None = None, coverage: float | None = None,
                   error_rate: float = 0.0, circular: bool = False, seed: int,
                   window: tuple[int, int] | None = None) -> dict:
    """Sample forward-strand reads uniformly from ``genome`` (or ``genome[window]``).

    Exactly one of ``n`` and ``coverage`` must be given (``coverage`` = n *
    read_length / length).  With ``error_rate > 0`` each base is substituted
    independently with that probability (substitutions only).  Returns the reads,
    their start positions and, for error-free reads, the covered stretch of the
    (linearised) genome, which is a common superstring.
    """
    rng = random.Random(seed)
    text = linearize(genome, circular, read_length)
    lo, hi = window if window is not None else (0, len(genome) if circular else len(genome) - read_length + 1)
    starts_range = hi - lo if window is None else hi - lo - read_length + 1
    if starts_range <= 0:
        raise ValueError("window shorter than a read")
    if (n is None) == (coverage is None):
        raise ValueError("give exactly one of n and coverage")
    span = (len(genome) if window is None else hi - lo)
    if n is None:
        assert coverage is not None
        n = max(1, round(coverage * span / read_length))
    reads, starts = [], []
    for _ in range(n):
        s = lo + rng.randrange(starts_range)
        r = text[s:s + read_length]
        if error_rate:
            r = "".join(rng.choice([b for b in DNA if b != c]) if rng.random() < error_rate else c for c in r)
        reads.append(r)
        starts.append(s)
    out = {"reads": reads, "starts": starts, "n_sampled": n}
    if not error_rate:
        a, b = min(starts), max(starts) + read_length
        out["covered"] = text[a:b]
        out["covered_span"] = [a, b]
    return out


def orient_exact_reads(reads: Sequence[str], genome: str, circular: bool) -> dict:
    """Keep reads that occur exactly in the genome (either strand); flip reverse-strand ones.

    Reads containing non-ACGT symbols are dropped.  Returns the oriented reads,
    their positions on the forward strand (first occurrence), and counts.
    """
    longest = max((len(r) for r in reads), default=1)
    text = linearize(genome, circular, longest)
    rc_text = reverse_complement(text)
    kept, starts = [], []
    stats = {"input": len(reads), "non_acgt": 0, "forward": 0, "reverse": 0, "no_exact_match": 0}
    for r in reads:
        if r.strip(DNA):
            stats["non_acgt"] += 1
            continue
        pos = text.find(r)
        if pos >= 0:
            stats["forward"] += 1
        else:
            rpos = rc_text.find(r)
            if rpos < 0:
                stats["no_exact_match"] += 1
                continue
            r = reverse_complement(r)
            pos = text.find(r)
            stats["reverse"] += 1
        kept.append(r)
        starts.append(pos)
    return {"reads": kept, "starts": starts, "stats": stats, "text": text}


def window_subset(reads: Sequence[str], starts: Sequence[int], text: str, n: int, window: int,
                  seed: int, max_tries: int = 200) -> dict:
    """Pick ``n`` substring-free reads lying inside one random window of ``text``.

    Used for the small tier (exact DP).  The reads overlap because they come
    from one window.  ``covered`` is the stretch of ``text`` they span, which is
    a common superstring.
    """
    from .core import preprocess

    rng = random.Random(seed)
    order = sorted(range(len(reads)), key=lambda i: starts[i])
    max_start = max(starts)
    for attempt in range(max_tries):
        a = rng.randrange(max(1, max_start - window // 2))
        pool = [i for i in order if a <= starts[i] and starts[i] + len(reads[i]) <= a + window]
        uniq = list(dict.fromkeys(reads[i] for i in pool))
        if len(preprocess(uniq)) < n:
            continue
        chosen: list[int] = []
        candidates = pool[:]
        rng.shuffle(candidates)
        for i in candidates:
            trial = [reads[j] for j in chosen] + [reads[i]]
            if len(preprocess(trial)) == len(trial):
                chosen.append(i)
                if len(chosen) == n:
                    break
        if len(chosen) == n:
            lo = min(starts[i] for i in chosen)
            hi = max(starts[i] + len(reads[i]) for i in chosen)
            picked = [reads[i] for i in chosen]
            return {"reads": picked, "starts": [starts[i] for i in chosen], "window_start": a,
                    "covered": text[lo:hi], "covered_span": [lo, hi], "attempt": attempt}
    raise ValueError(f"no window of length {window} holds {n} substring-free reads")
