import json
import unittest

from tests._util import ROOT  # noqa: F401  (puts repo on sys.path)
from scs import kspectrum_certificate, preprocess
from scs.generators import derive_seed, generate, random_strings, repetitive_strings, sampled_fragments, shuffled


class TestSeeds(unittest.TestCase):
    def test_derive_seed_is_stable(self):
        # Pinned value: changing derive_seed would silently change every dataset.
        self.assertEqual(derive_seed(20261105, "random/dna_l5-12", 8, 0), derive_seed("20261105", "random/dna_l5-12", "8", "0"))
        self.assertEqual(derive_seed(1, 2, 3), 8899725253796173630)
        self.assertLess(derive_seed("x"), 2 ** 63)

    def test_same_seed_same_instance(self):
        for fam, params in [("random", {"n": 10}), ("sampled", {"n": 10}),
                            ("repetitive", {"n": 10, "mode": "periodic"}),
                            ("repetitive", {"n": 10, "mode": "cyclic"}),
                            ("repetitive", {"n": 10, "mode": "kmer"})]:
            a, b = generate(fam, 42, **params), generate(fam, 42, **params)
            self.assertEqual(a, b)
            self.assertNotEqual(a["strings"], generate(fam, 43, **params)["strings"])

    def test_regenerate_from_stored_json_params(self):
        """Round-tripping params through JSON (tuples become lists) must regenerate the same instance."""
        inst = generate("sampled", 5, n=12, fragment_length=(6, 10), alphabet="AB", source_length=60)
        params = json.loads(json.dumps(inst["params"]))
        self.assertEqual(generate("sampled", inst["seed"], **params)["strings"], inst["strings"])


class TestFamilies(unittest.TestCase):
    def test_exact_n_substring_free(self):
        for seed in range(10):
            for inst in [random_strings(12, (4, 9), "AB", seed=seed),
                         sampled_fragments(12, 60, (5, 10), seed=seed),
                         repetitive_strings(12, "periodic", seed=seed),
                         repetitive_strings(12, "cyclic", k=6, alphabet="AB", seed=seed),
                         repetitive_strings(12, "kmer", k=6, seed=seed)]:
                S = inst["strings"]
                self.assertEqual(len(S), 12)
                self.assertEqual(preprocess(S), S)

    def test_random_lengths_and_alphabet(self):
        S = random_strings(20, (3, 7), "XY", seed=1)["strings"]
        self.assertTrue(all(3 <= len(s) <= 7 and set(s) <= {"X", "Y"} for s in S))
        self.assertEqual(len(random_strings(5, 4, seed=1, exact_n=False)["strings"]), 5)

    def test_sampled_are_substrings_of_source(self):
        inst = sampled_fragments(15, 50, (6, 12), seed=3)
        self.assertTrue(all(s in inst["source"] for s in inst["strings"]))
        inst = sampled_fragments(5, fragment_length=4, seed=3, source="ABCDEFGHIJKL")
        self.assertTrue(all(s in "ABCDEFGHIJKL" for s in inst["strings"]))

    def test_repetitive_modes(self):
        cyc = repetitive_strings(10, "cyclic", k=6, alphabet="AB", seed=2)
        self.assertTrue(all(len(s) == 6 for s in cyc["strings"]))
        km = repetitive_strings(50, "kmer", k=8, seed=2)
        self.assertTrue(all(len(s) == 8 for s in km["strings"]))
        self.assertTrue(all(s in km["source"] for s in km["strings"]))
        if km["repeated_kmers"] == 0:
            self.assertEqual(len(kspectrum_certificate(km["strings"])), len(km["source"]))
        per = repetitive_strings(10, "periodic", seed=2)
        self.assertTrue(all(s in per["source"] for s in per["strings"]))
        with self.assertRaises(ValueError):
            repetitive_strings(5, "nope", seed=1)

    def test_infeasible_raises(self):
        with self.assertRaises(ValueError):
            random_strings(50, 2, "AB", seed=1)  # only 4 binary strings of length 2
        with self.assertRaises(ValueError):
            sampled_fragments(20, 10, 5, seed=1)

    def test_shuffled(self):
        S = list("abcdefgh")
        self.assertEqual(sorted(shuffled(S, 1)), S)
        self.assertEqual(shuffled(S, 1), shuffled(S, 1))


if __name__ == "__main__":
    unittest.main()
