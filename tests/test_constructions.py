"""The literature instances reproduce the values reported in their papers."""

import unittest

from tests._util import ROOT  # noqa: F401
from scs import (Priority, dp_exact, greedy, greedy_naive, greedy_outcomes, is_superstring, kspectrum_certificate,
                 overlap, preprocess)
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


class Test12Over5(unittest.TestCase):
    """arXiv:2609.01365v2, Theorem 4.1 (lower bound 12/5)."""

    def test_gap_words(self):
        self.assertEqual(C.gap_word(3, [3, 4, 3, 4, 3], 3), "000100100010010001001000")  # Figure 2, L
        self.assertEqual(C.gap_word(2, [], 1), "0010")
        # Lemma 4.2 / Figure 2: ov(L, R) = [3 | 3 4 3 | 3]
        L, R = C.gap_word(3, [3, 4, 3, 4, 3], 3), C.gap_word(3, [3, 4, 3, 6], 3)
        self.assertEqual(overlap(L, R), len(C.gap_word(3, [3, 4, 3], 3)))

    def test_theorem_values(self):
        for r, P in ((1, 0), (1, 1), (2, 1), (2, 4), (3, 2), (3, 9), (5, 25), (8, 64)):
            inst = C.greedy_12_5(r, P)
            S, H = inst["strings"], inst["upper_superstring"]
            f = C.greedy_12_5_formulas(r, P)
            self.assertEqual(len(S), 5 * r)
            self.assertEqual(preprocess(S), S)                    # substring-free
            self.assertTrue(set("".join(S)) <= {"0", "1"})        # binary
            self.assertTrue(is_superstring(H, S))
            self.assertEqual(len(H), f["opt_upper"])
            g = greedy(S, Priority(inst["tie_priority"]), trace=True)
            self.assertEqual(g.length, f["greedy_bad"])
            ws = [m[2] for m in g.merges]
            self.assertEqual(ws, sorted(ws, reverse=True))

    def test_overlap_lengths_from_paper(self):
        r, P = 3, 9
        M = P + 8 * r
        inst = C.greedy_12_5(r, P)
        g = greedy(inst["strings"], Priority(inst["tie_priority"]))
        by_ov = sorted({w for _, _, w in g.merges}, reverse=True)
        alphas = [5 * P + 17 * r + i + 1 for i in range(1, r + 1)]
        beta, gamma = 4 * P + 18 * r + 1, 2 * P + 4 * r + 1
        self.assertEqual(by_ov, sorted(alphas + [beta, gamma, 0], reverse=True))
        self.assertEqual(2 * P + 2 * M + (P + r + 1) + 1, alphas[0])

    def test_exact_opt_small(self):
        for r, P in ((1, 0), (2, 1), (2, 4), (3, 2)):
            inst = C.greedy_12_5(r, P)
            opt = dp_exact(inst["strings"]).length
            self.assertLessEqual(opt, len(inst["upper_superstring"]))
            self.assertLessEqual(len(inst["upper_superstring"]) - opt, 3)

    def test_naive_greedy_agrees(self):
        """The paper reasons about overlaps of *merged* strings; the literal-merge greedy must agree."""
        for r, P in ((1, 0), (2, 1), (2, 4)):
            inst = C.greedy_12_5(r, P)
            prio = Priority(inst["tie_priority"])
            self.assertEqual(greedy(inst["strings"], prio).superstring,
                             greedy_naive(inst["strings"], Priority(inst["tie_priority"])).superstring)

    def test_beats_previous_bounds(self):
        f = C.greedy_12_5_formulas
        self.assertGreater(f(20, 400)["ratio_lower_bound"], 9 / 4)
        self.assertGreater(f(50, 2500)["ratio_lower_bound"], 7 / 3)
        self.assertLess(f(10 ** 4, 10 ** 8)["ratio_lower_bound"], 12 / 5)
        self.assertGreater(f(10 ** 4, 10 ** 8)["ratio_lower_bound"], 2.399)
        inst = C.greedy_12_5(20)
        g = greedy(inst["strings"], Priority(inst["tie_priority"]))
        self.assertGreater(g.length / len(inst["upper_superstring"]), 9 / 4)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            C.greedy_12_5(3, 1)   # P < r - 1


class Test12Over5Adapted(unittest.TestCase):
    """The team report's single-parameter adaptation (report Section 4.4 and Appendix B)."""

    def test_report_claims(self):
        for n in range(2, 10):
            inst = C.greedy_12_5_adapted(n)
            S, H = inst["strings"], inst["upper_superstring"]
            N = n * n
            self.assertEqual(len(S), 5 * (n - 1))
            self.assertEqual(preprocess(S), S)
            self.assertTrue(is_superstring(H, S))
            self.assertEqual(len(H), 5 * n ** 3 + 12 * n ** 2 - 2 * n - 1)
            g = greedy(S, Priority(inst["tie_priority"]))
            self.assertEqual(g.length, 12 * n ** 3 + (31 * n * n - 43 * n - 12) // 2)
            alphas = [5 * N + 8 * n + i + 1 for i in range(2, n + 1)]
            betas = [4 * N + 8 * n + i + 1 for i in range(2, n + 1)]
            expected = sorted(2 * alphas + betas + [2 * N + 2 * n + 1] * (n - 1) + [0] * (n - 2), reverse=True)
            self.assertEqual([w for _, _, w in g.merges], expected)

    def test_h_optimal_small(self):
        for n in (2, 3, 4):
            inst = C.greedy_12_5_adapted(n)
            self.assertEqual(dp_exact(inst["strings"]).length, len(inst["upper_superstring"]))

    def test_lex_is_optimal_small(self):
        for n in (2, 3, 4):
            inst = C.greedy_12_5_adapted(n)
            self.assertEqual(greedy(inst["strings"], "lex").length, len(inst["upper_superstring"]))


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
