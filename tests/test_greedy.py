import unittest

from tests._util import small_instances
from scs import (ExplorationBudgetExceeded, Priority, dp_exact, greedy, greedy_naive, greedy_outcomes,
                 is_superstring, overlap_graph, preprocess, total_length)
from scs.constructions import tarhio_ukkonen_example7
from scs.tiebreak import CallableTie, RandomTie, make_tiebreaker

STATIC_RULES = ["first", "last", "lex", "revlex", "random:0", "random:12345"]
ALL_RULES = STATIC_RULES + ["short-frag", "long-frag"]


class TestSlides(unittest.TestCase):
    def test_attac(self):
        r = greedy(["ATT", "TTA", "TAC"])
        self.assertEqual(r.superstring, "ATTAC")
        self.assertEqual(r.compression, 4)

    def test_slide5_greedy_fails(self):
        S = ["AABA", "ABAA", "BAB"]
        r = greedy(S)
        self.assertEqual(r.superstring, "AABAABAB")
        self.assertEqual(r.merges[0], (0, 1, 3))
        # Every tie choice gives 8 here; OPT is 7.
        self.assertEqual(greedy_outcomes(S).lengths, [8])
        self.assertEqual(dp_exact(S).length, 7)

    def test_preprocessing_applied(self):
        r = greedy(["ATT", "TT", "TTA", "ATT", "TAC"])
        self.assertEqual(r.strings, ["ATT", "TTA", "TAC"])
        self.assertEqual(r.superstring, "ATTAC")

    def test_edge_cases(self):
        self.assertEqual(greedy([]).superstring, "")
        self.assertEqual(greedy(["abc"]).superstring, "abc")
        self.assertEqual(greedy(["ab", "cd"]).length, 4)


class TestImplementationsAgree(unittest.TestCase):
    def test_fast_naive_traced_identical(self):
        """Edge-based greedy == literal merge greedy == step-wise (traced) greedy, for every static rule."""
        for S in small_instances(80, n=7):
            for rule in STATIC_RULES:
                fast = greedy(S, rule)
                naive = greedy_naive(S, rule)
                traced = greedy(S, rule, trace=True)
                self.assertEqual(fast.superstring, naive.superstring, (S, rule))
                self.assertEqual(fast.superstring, traced.superstring, (S, rule))
                self.assertEqual(fast.merges, traced.merges)

    def test_precomputed_graph(self):
        for S in small_instances(10):
            R = preprocess(S)
            g = overlap_graph(R)
            self.assertEqual(greedy(R, "lex", preprocess=False, graph=g).superstring, greedy(S, "lex").superstring)
        with self.assertRaises(ValueError):
            greedy(["ab"], graph=[{}])


class TestGreedyProperties(unittest.TestCase):
    def test_outputs_are_valid_greedy_executions(self):
        for S in small_instances(60, n=7):
            ex = greedy_outcomes(S)
            opt = dp_exact(S).length
            self.assertGreaterEqual(ex.min_length, opt)
            for rule in ALL_RULES:
                r = greedy(S, rule)
                self.assertTrue(is_superstring(r.superstring, S))
                self.assertEqual(len(r.superstring), r.length)
                self.assertIn(r.length, ex.lengths, (S, rule))
            for sup in (ex.min_superstring, ex.max_superstring):
                self.assertTrue(is_superstring(sup, S))
            self.assertEqual(len(ex.min_superstring), ex.min_length)
            self.assertEqual(len(ex.max_superstring), ex.max_length)

    def test_merges_are_maximum_overlap_choices(self):
        for S in small_instances(30):
            r = greedy(S, "random:3", trace=True)
            ws = [m[2] for m in r.merges]
            self.assertEqual(ws, sorted(ws, reverse=True))  # max overlap never increases (Shibata Lemma 3)
            self.assertEqual(total_length(r.strings) - sum(ws), r.length)

    def test_half_compression_theorem(self):
        """Tarhio-Ukkonen / Kalugin-Nikolaev: L - G >= (L - OPT) / 2 for EVERY greedy execution."""
        for S in small_instances(80, n=7):
            L = total_length(preprocess(S))
            opt = dp_exact(S).length
            worst = greedy_outcomes(S).max_length
            self.assertGreaterEqual(2 * (L - worst), L - opt, S)
            self.assertLessEqual(worst, 3 * opt)  # Chukhin et al. 2026 upper bound

    def test_exploration_budget(self):
        S = small_instances(1, n=8)[0]
        with self.assertRaises(ExplorationBudgetExceeded):
            greedy_outcomes(S, max_states=1)


class TestTieBreaking(unittest.TestCase):
    def setUp(self):
        self.inst = tarhio_ukkonen_example7(4)  # {ab^4, b^5, b^4 a}: greedy gives 7 or 11
        self.S = self.inst["strings"]

    def test_rules_change_the_outcome(self):
        self.assertEqual(greedy(self.S, "first").length, 7)
        self.assertEqual(greedy(self.S, "lex").length, 11)
        self.assertEqual(greedy_outcomes(self.S).lengths, [7, 11])

    def test_priority_replays_paper(self):
        r = greedy(self.S, Priority(self.inst["tie_priority"]))
        self.assertEqual(r.length, self.inst["known"]["greedy_bad"])
        self.assertEqual(r.merges[0][:2], (0, 2))

    def test_priority_cannot_force_non_maximum_merge(self):
        # Prefer an overlap-0 merge first: greedy must ignore it while overlap-4 merges exist.
        r = greedy(self.S, Priority([["abbbbbb", "abbbb"], ["bbbba", "bbbbb"]]))
        self.assertEqual(r.merges[0][2], 4)

    def test_random_reproducible_and_varied(self):
        a = [greedy(self.S, f"random:{s}").superstring for s in range(40)]
        b = [greedy(self.S, RandomTie(s)).superstring for s in range(40)]
        self.assertEqual(a, b)
        self.assertEqual({len(x) for x in a}, {7, 11})

    def test_random_is_roughly_uniform(self):
        # First step: 3 tied overlap-4 edges, exactly one of which (ab^4 -> b^4 a) leads to length 11.
        bad = sum(greedy(self.S, f"random:{s}").length == 11 for s in range(3000))
        self.assertAlmostEqual(bad / 3000, 1 / 3, delta=0.04)

    def test_custom_callable(self):
        seen = []

        def rule(cands, state):
            seen.append(len(cands))
            self.assertTrue(all(state.valid(u, v) for u, v in cands))
            return max(cands)

        r = greedy(self.S, rule)
        self.assertTrue(seen and seen[0] == 3)
        self.assertEqual(r.tie_rule, "custom")
        self.assertIsInstance(make_tiebreaker(rule), CallableTie)

    def test_bad_callable_rejected(self):
        with self.assertRaises(ValueError):
            greedy(self.S, lambda cands, state: (99, 99))

    def test_unknown_rule(self):
        with self.assertRaises(ValueError):
            make_tiebreaker("nope")

    def test_trace_counts_ties(self):
        r = greedy(self.S, "first", trace=True)
        self.assertEqual(r.trace[0]["candidates"], 3)
        self.assertGreaterEqual(r.tie_steps, 1)
        self.assertIsNone(greedy(self.S).tie_steps)

    def test_dynamic_state_helpers(self):
        lengths = []

        def rule(cands, state):
            u, v = cands[0]
            lengths.append((state.fragment_length(u), len(state.fragment(u))))
            return cands[0]

        greedy(["ATT", "TTA", "TAC"], rule)
        for a, b in lengths:
            self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
