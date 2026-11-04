"""The literature instances reproduce the values reported in their papers."""

import unittest

from tests._util import ROOT  # noqa: F401
from scs import Priority, dp_exact, greedy, greedy_outcomes, kspectrum_certificate, preprocess
from scs import constructions as C


def check(tc: unittest.TestCase, inst: dict, explore: bool = False):
    S = inst["strings"]
    known = inst["known"]
    cert = kspectrum_certificate(S)
    opt = len(cert) if cert is not None else dp_exact(S).length
    if known["opt"] is not None:
        tc.assertEqual(opt, known["opt"], inst["id"])
    if inst["tie_priority"]:
        g = greedy(S, Priority(inst["tie_priority"]), trace=True)
        tc.assertEqual(g.length, known["greedy_bad"], inst["id"])
        # The replayed execution is a valid greedy run: overlaps never increase.
        ws = [m[2] for m in g.merges]
        tc.assertEqual(ws, sorted(ws, reverse=True))
    if explore:
        ex = greedy_outcomes(S)
        tc.assertEqual(ex.min_length if known["opt"] is None else min(ex.lengths), ex.min_length)
        if known["greedy_bad"] is not None:
            tc.assertIn(known["greedy_bad"], ex.lengths)
    return opt


class TestSmallConstructions(unittest.TestCase):
    def test_slides(self):
        for inst in (C.slides_attac(), C.slides_preprocess(), C.slides_greedy_fail()):
            check(self, inst, explore=True)

    def test_tarhio_ukkonen(self):
        for h in (1, 2, 3, 7):
            inst = C.tarhio_ukkonen_example7(h)
            check(self, inst, explore=True)
            self.assertEqual(greedy_outcomes(inst["strings"]).lengths, [h + 3, 2 * h + 3])

    def test_chukhin_k3(self):
        inst = C.chukhin_k3(1)
        self.assertEqual(sorted(inst["strings"]), sorted(["ABX", "BXA", "XAX", "AXA", "XAB"]))
        check(self, inst, explore=True)
        self.assertEqual(max(greedy_outcomes(inst["strings"]).lengths), 9)
        for t in (2, 4, 8):
            check(self, C.chukhin_k3(t))

    def test_chukhin_k6_matches_paper_strings(self):
        inst = C.chukhin_k(6, 1)
        self.assertEqual(set(inst["strings"]), {"ABAABX", "BAABXA", "AABXAB", "ABXABA", "BXABAA", "XABAAB",
                                                "ABXABX", "BXABXA", "XABXAB"})
        check(self, inst, explore=True)
        g = greedy(inst["strings"], Priority(inst["tie_priority"]))
        self.assertEqual(g.superstring, "BXABXABXABAABXABAA")  # verbatim from the paper

    def test_chukhin_general_k(self):
        for k, t in ((6, 3), (7, 1), (7, 2), (9, 2)):
            inst = C.chukhin_k(k, t)
            self.assertEqual(len(inst["strings"]), (2 * k - 3) * t)
            check(self, inst)

    def test_kulikov(self):
        for inst in (C.kulikov_readme_example(), C.kulikov_collapsing_counterexample()):
            check(self, inst, explore=True)


class TestShibata(unittest.TestCase):
    def test_k10_t1_strings(self):
        inst = C.shibata(10, 1)
        b = inst["symbols"]["b_i"][0]
        S = inst["strings"]
        self.assertEqual(len(S), 22)
        self.assertIn(f"xayx{b}xayxy", S)        # U_{1,1}
        self.assertIn(f"ayx{b}xayxyx", S)        # U_{1,2}
        self.assertTrue(all(len(s) == 10 for s in S))
        self.assertEqual(preprocess(S), S)

    def test_reported_values(self):
        for k, t in ((10, 1), (10, 2), (10, 10), (12, 3), (14, 2)):
            inst = C.shibata(k, t)
            s = k // 2
            self.assertEqual(check(self, inst), t * (4 * s + 2) + k - 1)
            self.assertEqual(inst["known"]["greedy_bad"], t * (9 * s + 1) + 1)

    def test_breaks_factor_two(self):
        inst = C.shibata(10, 10)
        g = greedy(inst["strings"], Priority(inst["tie_priority"]))
        opt = len(kspectrum_certificate(inst["strings"]))
        self.assertEqual((g.length, opt), (461, 229))
        self.assertGreater(g.length, 2 * opt)

    def test_invalid_parameters(self):
        with self.assertRaises(ValueError):
            C.shibata(9, 1)
        with self.assertRaises(ValueError):
            C.chukhin_k(5, 1)


class TestHelpers(unittest.TestCase):
    def test_csubstr(self):
        self.assertEqual(C.csubstr("abcd", 6, 3), "cdabcd")
        self.assertEqual(C.cyclic_chain("abc", 4, 2), ["bcab", "cabc", "abca"])

    def test_fresh_symbols(self):
        syms = C.fresh_symbols(300, exclude="xya")
        self.assertEqual(len(set(syms)), 300)
        self.assertFalse(set(syms) & set("xya"))

    def test_literature_set(self):
        ids = [i["id"] for i in C.literature_instances()]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
