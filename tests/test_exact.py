import unittest

from tests._util import small_instances
from scs import (brute_force_exact, dp_exact, equal_length_lower_bound, is_superstring, kspectrum_certificate,
                 optimal_length, preprocess)
from scs.generators import random_strings, repetitive_strings


class TestDP(unittest.TestCase):
    def test_slide11(self):
        r = dp_exact(["ATT", "TTA", "TAC"])
        self.assertEqual((r.length, r.superstring), (5, "ATTAC"))

    def test_matches_brute_force(self):
        """The slide's planned check: enumerate all orderings on the tiniest cases."""
        pools = small_instances(80, n=6) + small_instances(20, n=7)
        pools += [random_strings(n, (2, 5), "ABC", seed=100 + n)["strings"] for n in range(1, 8)]
        for S in pools:
            d, b = dp_exact(S), brute_force_exact(S)
            self.assertEqual(d.length, b.length, S)
            self.assertTrue(is_superstring(d.superstring, S))
            self.assertEqual(len(d.superstring), d.length)
            self.assertEqual(sorted(d.order), list(range(len(d.strings))))

    def test_dp_scales_to_moderate_n(self):
        S = random_strings(14, (5, 10), "AB", seed=7)["strings"]
        r = dp_exact(S)
        self.assertTrue(is_superstring(r.superstring, S))

    def test_limits(self):
        with self.assertRaises(ValueError):
            dp_exact(random_strings(6, 5, seed=1)["strings"], max_n=5)
        self.assertEqual(dp_exact([]).length, 0)
        self.assertEqual(dp_exact(["xyz"]).superstring, "xyz")


class TestCertificate(unittest.TestCase):
    def test_kmer_spectrum_certificate_is_optimal(self):
        for seed in range(30):
            inst = repetitive_strings(9, "kmer", k=4, alphabet="AB", mutation_rate=0.3, seed=seed)
            S = inst["strings"]
            cert = kspectrum_certificate(S)
            if cert is None:
                continue
            self.assertTrue(is_superstring(cert, S))
            self.assertEqual(len(cert), equal_length_lower_bound(S))
            self.assertEqual(len(cert), dp_exact(S).length)

    def test_lower_bound_holds(self):
        for seed in range(30):
            S = repetitive_strings(8, "cyclic", k=5, alphabet="AB", seed=seed)["strings"]
            self.assertGreaterEqual(dp_exact(S).length, equal_length_lower_bound(S))

    def test_no_certificate_cases(self):
        self.assertIsNone(kspectrum_certificate(["AB", "BCD"]))   # unequal lengths
        self.assertIsNone(kspectrum_certificate(["AB", "CD"]))    # disconnected
        self.assertIsNone(equal_length_lower_bound(["AB", "ABC", "Q"]))

    def test_optimal_length_dispatch(self):
        self.assertEqual(optimal_length(["ATT", "TTA", "TAC"]), (5, "certificate"))
        self.assertEqual(optimal_length(["AABA", "ABAA", "BAB"]), (7, "dp"))
        big = random_strings(30, (5, 9), seed=3)["strings"]
        self.assertEqual(optimal_length(big, dp_max_n=10), (None, "none"))
        self.assertEqual(optimal_length(big, dp_max_n=10, known=99), (99, "known"))
        self.assertEqual(len(preprocess(big)), 30)


if __name__ == "__main__":
    unittest.main()
