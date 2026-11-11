"""Real-data helpers (FASTA/FASTQ, read simulation, exact-read filtering) and stored real-data integrity."""

import gzip
import hashlib
import json
import random
import tempfile
import unittest
from pathlib import Path

from tests._util import ROOT
from scs import is_superstring, preprocess
from scs.instance_io import load_instances
from scs.realdata import (linearize, orient_exact_reads, read_fasta, read_fastq, reverse_complement,
                          simulate_reads, window_subset)

REAL = ROOT / "data" / "real"


def random_genome(n, seed):
    rng = random.Random(seed)
    return "".join(rng.choice("ACGT") for _ in range(n))


class TestParsers(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=ROOT / "tests", prefix="_tmp")
        self.dir = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_fasta(self):
        p = self.dir / "g.fasta"
        p.write_text(">seq1 test\nACGT\nacgg\n\n>seq2\nTT\n")
        self.assertEqual(read_fasta(p), [("seq1 test", "ACGTACGG"), ("seq2", "TT")])
        bad = self.dir / "bad.fasta"
        bad.write_text("ACGT\n>x\nA\n")
        with self.assertRaises(ValueError):
            read_fasta(bad)

    def test_fastq_plain_and_gzip(self):
        text = "@r1 extra\nACGTN\n+\nIIIII\n@r2\nacg\n+\nIII\n"
        p = self.dir / "r.fastq"
        p.write_text(text)
        gz = self.dir / "r.fastq.gz"
        with gzip.open(gz, "wt") as fh:
            fh.write(text)
        for path in (p, gz):
            self.assertEqual(list(read_fastq(path)), [("r1", "ACGTN"), ("r2", "ACG")])
        self.assertEqual(len(list(read_fastq(p, limit=1))), 1)
        bad = self.dir / "bad.fastq"
        bad.write_text("r1\nACGT\n+\nIIII\n")
        with self.assertRaises(ValueError):
            list(read_fastq(bad))


class TestReads(unittest.TestCase):
    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("AACGTN"), "NACGTT")
        self.assertEqual(reverse_complement(reverse_complement("GATTACA")), "GATTACA")

    def test_linearize(self):
        self.assertEqual(linearize("ABCDEF", True, 3), "ABCDEFAB")
        self.assertEqual(linearize("ABCDEF", False, 3), "ABCDEF")

    def test_simulate_error_free(self):
        g = random_genome(2000, 1)
        for circ in (False, True):
            sim = simulate_reads(g, read_length=50, coverage=8, circular=circ, seed=3)
            self.assertEqual(sim["n_sampled"], 320)
            text = linearize(g, circ, 50)
            self.assertTrue(all(text[s:s + 50] == r for s, r in zip(sim["starts"], sim["reads"])))
            self.assertTrue(is_superstring(sim["covered"], sim["reads"]))
        self.assertEqual(simulate_reads(g, read_length=50, n=10, seed=3), simulate_reads(g, read_length=50, n=10, seed=3))
        with self.assertRaises(ValueError):
            simulate_reads(g, read_length=50, seed=3)

    def test_simulate_errors(self):
        g = random_genome(1000, 2)
        sim = simulate_reads(g, read_length=100, n=200, error_rate=0.05, seed=4)
        mism = sum(a != b for s, r in zip(sim["starts"], sim["reads"]) for a, b in zip(r, g[s:s + 100]))
        self.assertAlmostEqual(mism / (200 * 100), 0.05, delta=0.01)
        self.assertNotIn("covered", sim)

    def test_orient_exact(self):
        g = random_genome(500, 5)
        reads = [g[10:40], reverse_complement(g[100:130]), "ACGTNACGT", "A" * 30, g[480:500] + g[:10]]
        out = orient_exact_reads(reads, g, circular=True)
        self.assertEqual(out["reads"][:2], [g[10:40], g[100:130]])
        self.assertEqual(out["stats"], {"input": 5, "non_acgt": 1, "forward": 2, "reverse": 1, "no_exact_match": 1})
        self.assertEqual(out["starts"][2], 480)   # read spanning the origin of a circular genome

    def test_window_subset(self):
        g = random_genome(3000, 6)
        sim = simulate_reads(g, read_length=60, coverage=30, seed=7)
        sub = window_subset(sim["reads"], sim["starts"], g, 10, window=240, seed=8)
        self.assertEqual(len(sub["reads"]), 10)
        self.assertEqual(preprocess(sub["reads"]), sub["reads"])
        self.assertTrue(is_superstring(sub["covered"], sub["reads"]))
        self.assertLessEqual(sub["covered_span"][1] - sub["covered_span"][0], 240)


@unittest.skipUnless((REAL / "sources.json").exists(), "real data not fetched")
class TestStoredRealData(unittest.TestCase):
    def test_reference_checksums(self):
        sources = json.loads((REAL / "sources.json").read_text())
        for acc, info in sources["genomes"].items():
            path = ROOT / info["path"]
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), info["sha256"], acc)
            (_, seq), = read_fasta(path)
            self.assertEqual(len(seq), info["length"])

    def test_instances_valid(self):
        seen = 0
        for inst in load_instances(REAL / "instances"):
            if inst.get("index", 0) > 1:     # spot-check the first two of every batch
                continue
            seen += 1
            S = inst["strings"]
            self.assertEqual(len(S), len(set(S)))
            if "upper_superstring" in inst:
                self.assertTrue(is_superstring(inst["upper_superstring"], S), inst["id"])
                self.assertEqual(inst["known"]["opt_upper"], len(inst["upper_superstring"]))
            self.assertTrue(set("".join(S)) <= set("ACGT"))
        self.assertGreater(seen, 50)

    @unittest.skipUnless((REAL / "raw" / "ERR098007.fastq.gz").exists(), "raw reads not downloaded")
    def test_raw_reads_md5(self):
        sources = json.loads((REAL / "sources.json").read_text())
        run = sources["reads"]["ERR098007"]
        data = (ROOT / run["path"]).read_bytes()
        self.assertEqual(hashlib.md5(data).hexdigest(), run["fastq_md5"])


if __name__ == "__main__":
    unittest.main()
