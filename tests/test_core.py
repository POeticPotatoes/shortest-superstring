import itertools
import unittest

from tests._util import small_instances
from scs.core import (is_substring_free, is_superstring, merge, overlap, overlap_graph, overlap_matrix, preprocess,
                      superstring_from_order)


class TestOverlap(unittest.TestCase):
    def test_slide_examples(self):
        self.assertEqual(overlap("ATT", "TTA"), 2)
        self.assertEqual(overlap("TTA", "ATT"), 1)
        self.assertEqual(overlap("TTA", "TAC"), 2)
        self.assertEqual(overlap("ATT", "TAC"), 1)
        self.assertEqual(overlap("TAC", "ATT"), 0)
        self.assertEqual(merge("ATT", "TTA"), "ATTA")
        self.assertEqual(merge("AABA", "ABAA"), "AABAA")

    def test_overlap_graph_matches_pairwise(self):
        for S in small_instances(40):
            g = overlap_graph(S)
            m = overlap_matrix(S)
            for u, v in itertools.permutations(range(len(S)), 2):
                k = overlap(S[u], S[v])
                self.assertEqual(g[u].get(v, 0), k)
                self.assertEqual(m[u][v], k)
                self.assertLess(k, min(len(S[u]), len(S[v])))


class TestPreprocess(unittest.TestCase):
    def test_slide2(self):
        self.assertEqual(preprocess(["ATT", "TT", "TTA", "ATT", "TAC"]), ["ATT", "TTA", "TAC"])

    def test_keeps_first_occurrence_order(self):
        self.assertEqual(preprocess(["c", "abc", "b", "xyz", "ab", "xyz"]), ["abc", "xyz"])

    def test_against_naive(self):
        import random
        rng = random.Random(0)
        for _ in range(300):
            S = ["".join(rng.choice("AB") for _ in range(rng.randint(1, 6))) for _ in range(rng.randint(1, 10))]
            uniq = list(dict.fromkeys(S))
            naive = [s for s in uniq if not any(s != t and s in t for t in uniq)]
            self.assertEqual(preprocess(S), naive)
            self.assertTrue(is_substring_free(naive))

    def test_rejects_nul(self):
        with self.assertRaises(ValueError):
            preprocess(["a\x00b"])


class TestSuperstringFromOrder(unittest.TestCase):
    def test_lengths(self):
        S = ["ATT", "TTA", "TAC"]
        self.assertEqual(superstring_from_order(S, [0, 1, 2]), "ATTAC")
        self.assertEqual(superstring_from_order(S, [2, 1, 0]), "TACTTATT")
        for S in small_instances(20):
            for order in itertools.islice(itertools.permutations(range(len(S))), 30):
                sup = superstring_from_order(S, order)
                self.assertTrue(is_superstring(sup, S))


if __name__ == "__main__":
    unittest.main()
