"""Known instances from the slides and the literature, transcribed exactly.

Each function returns an instance dict (see :mod:`scs.instance_io`) with:

``known``
    Values reported in the source: ``opt`` and ``greedy_bad`` (the length of
    the bad greedy execution).  Where the source only gives a formula, the
    formula is evaluated.
``tie_priority``
    The merges of the bad execution described in the source, as a list of
    ``[u, v]`` string pairs.  Pass it to :class:`scs.tiebreak.Priority` to
    replay that execution.  Greedy still only picks maximum-overlap pairs,
    so getting ``greedy_bad`` back also checks that the paper's execution is
    valid.
``citation``
    The source.

Sources
-------
* Tarhio & Ukkonen, TCS 57 (1988), Example 7.
* Chukhin, Kulikov, Mihajlin, Smal, "The Greedy Superstring Algorithm Achieves
  Ratio 2 for Strings of Length 6 Already", arXiv:2608.20018 (2026).  The
  authors credit GPT-5.6 Sol Ultra/Pro with helping find the constructions.
* H. Shibata, "Disproving the Greedy Superstring Conjecture",
  arXiv:2609.01365v1 (2026).  The author credits OpenAI's GPT-5.6 Sol with
  first finding the counterexample.
* Kulikov et al., github.com/alexanderskulikov/greedy-superstring-conjecture,
  counterexample to the *Collapsing* Superstring Conjecture (2025).
"""

from __future__ import annotations

from typing import Sequence

TU1988 = "Tarhio & Ukkonen, A greedy approximation algorithm for constructing shortest common superstrings, TCS 57 (1988) 131-145"
CHUKHIN6 = "Chukhin, Kulikov, Mihajlin, Smal, The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already, arXiv:2608.20018 (2026)"
SHIBATA = "Shibata, Disproving the Greedy Superstring Conjecture, arXiv:2609.01365v1 (2026)"
KULIKOV_REPO = "github.com/alexanderskulikov/greedy-superstring-conjecture (README, counterexample added 2025-07-08)"
SLIDES = "Project proposal slides"

# Characters used for "fresh" symbols (b_i, X_i, Y_j).  Instances are plain
# str, so every symbol must be one character.
_FRESH_POOL = (
    "0123456789"
    + "".join(chr(c) for c in range(0x3B1, 0x3CA))      # Greek lower case
    + "".join(chr(c) for c in range(0x100, 0x180))      # Latin Extended-A
    + "".join(chr(c) for c in range(0x400, 0x500))      # Cyrillic
)


def fresh_symbols(count: int, exclude: str = "") -> list[str]:
    pool = [c for c in _FRESH_POOL if c not in exclude]
    if count > len(pool):
        raise ValueError(f"at most {len(pool)} fresh symbols available")
    return pool[:count]


def csubstr(T: str, length: int, i: int) -> str:
    """``CSubstr_length(T, i)``: circular substring of ``T`` of the given length, starting at 1-based ``i``."""
    reps = (i - 1 + length) // len(T) + 2
    return (T * reps)[i - 1:i - 1 + length]


def cyclic_chain(T: str, k: int, start: int, count: int | None = None) -> list[str]:
    """The length-``k`` circular substrings of ``T`` starting at ``start, start+1, ...`` (1-based, cyclic)."""
    count = len(T) if count is None else count
    return [csubstr(T, k, (start - 1 + j) % len(T) + 1) for j in range(count)]


def _chain_edges(chain: Sequence[str]) -> list[list[str]]:
    return [[a, b] for a, b in zip(chain, chain[1:])]


def _instance(name: str, strings: list[str], citation: str, *, opt: int | None = None,
              greedy_bad: int | None = None, tie_priority=None, params=None, notes: str = "",
              symbols: dict | None = None) -> dict:
    return {
        "id": name,
        "family": "literature",
        "strings": strings,
        "params": params or {},
        "seed": None,
        "citation": citation,
        "known": {"opt": opt, "greedy_bad": greedy_bad},
        "tie_priority": tie_priority or [],
        "notes": notes,
        "symbols": symbols or {},
    }


# ---------------------------------------------------------------- slides

def slides_attac() -> dict:
    """Slide 1/3: ATT, TTA, TAC -> ATTAC (OPT 5); greedy is optimal."""
    return _instance("slides_attac", ["ATT", "TTA", "TAC"], SLIDES, opt=5, greedy_bad=5)


def slides_greedy_fail() -> dict:
    """Slide 5: AABA, ABAA, BAB.  Greedy merges the overlap-3 pair and outputs length 8; OPT = 7."""
    return _instance("slides_greedy_fail", ["AABA", "ABAA", "BAB"], SLIDES, opt=7, greedy_bad=8,
                     tie_priority=[["AABA", "ABAA"]])


def slides_preprocess() -> dict:
    """Slide 2: duplicates and contained strings (TT inside ATT) are removed."""
    return _instance("slides_preprocess", ["ATT", "TT", "TTA", "ATT", "TAC"], SLIDES, opt=5, greedy_bad=5)


# ---------------------------------------------------------------- Tarhio & Ukkonen

def tarhio_ukkonen_example7(h: int) -> dict:
    """Example 7: ``{a b^h, b^(h+1), b^h a}``.  OPT = h+3 (a b^(h+1) a); greedy may give 2h+3."""
    a, bh = "a", "b" * h
    strings = [a + bh, bh + "b", bh + a]
    return _instance(f"tu88_ex7_h{h}", strings, TU1988 + ", Example 7", opt=h + 3, greedy_bad=2 * h + 3,
                     tie_priority=[[a + bh, bh + a]], params={"h": h},
                     notes="Greedy ratio (2h+3)/(h+3) -> 2; the classic tight-2 family.")


# ---------------------------------------------------------------- Chukhin et al. (length 3)

def chukhin_k3(t: int = 1) -> dict:
    """Theorem 4.1: 3-spectrum of ``AB[X1 A X1 AB]...[Xt A Xt AB]``.  OPT = 5t+2, greedy may give 9t."""
    xs = ["X"] if t == 1 else fresh_symbols(t, exclude="AB")
    text = "AB" + "".join(f"{x}A{x}AB" for x in xs)
    strings = list(dict.fromkeys(text[i:i + 3] for i in range(len(text) - 2)))
    prio = []
    for x in xs:
        prio += [[f"A{x}A", f"{x}A{x}"], [f"B{x}A", f"{x}AB"], [f"{x}AB", f"AB{x}"]]
    return _instance(f"chukhin_k3_t{t}", strings, CHUKHIN6 + ", Theorem 4.1", opt=5 * t + 2,
                     greedy_bad=9 * t, tie_priority=prio, params={"k": 3, "t": t},
                     symbols={"X_i": xs}, notes="rho_3 = 9/5 exactly; ratio 9t/(5t+2).")


# ---------------------------------------------------------------- Chukhin et al. (length >= 6)

def chukhin_k(k: int = 6, t: int = 1) -> dict:
    """Section 3: cyclic k-spectra of ``p_i = ABAABX_i y`` and ``q_i = ABX_i y``, ``|y| = k - 6``.

    OPT = (2k-3)t + k-1 (equal-length lower bound, met by an Eulerian trail);
    greedy may give (4k-6)t.  For k = 6 and t = 1: OPT 14 and greedy 18.
    """
    if k < 6:
        raise ValueError("construction needs k >= 6")
    d = k - 6
    fresh = fresh_symbols(d + (t if t > 1 else 0), exclude="ABX")
    y = "".join(fresh[:d])
    xs = ["X"] if t == 1 else fresh[d:]
    strings, prio = [], []
    for x in xs:
        p, q = f"ABAAB{x}{y}", f"AB{x}{y}"
        p_chain = cyclic_chain(p, k, start=6)       # starts at X_i: X y ABAAB...
        q_chain = cyclic_chain(q, k, start=2)       # starts at B:   B X y AB...
        strings += cyclic_chain(p, k, 1) + cyclic_chain(q, k, 1)
        prio += _chain_edges(p_chain) + _chain_edges(q_chain) + [[q_chain[-1], p_chain[0]]]
    strings = list(dict.fromkeys(strings))
    opt = (2 * k - 3) * t + k - 1
    return _instance(f"chukhin_k{k}_t{t}", strings, CHUKHIN6 + ", Section 3", opt=opt,
                     greedy_bad=(4 * k - 6) * t, tie_priority=prio, params={"k": k, "t": t},
                     symbols={"X_i": xs, "y": y},
                     notes="Shows rho_k >= 2 for k >= 6; ratio (4k-6)t/((2k-3)t+k-1).")


# ---------------------------------------------------------------- Shibata

def _X(n: int) -> str:
    return "yx" * (n // 2) if n % 2 == 0 else "x" + "yx" * ((n - 1) // 2)


def shibata(k: int = 10, t: int = 1) -> dict:
    """The instance S_{k,t} disproving the greedy conjecture (Section 3.1).

    ``k = 2s >= 10`` even.  ``|S| = t(4s+2)`` strings of length k.
    OPT = t(4s+2) + k - 1 (Theorem 10); greedy may output t(9s+1) + 1
    (Theorem 13).  The ratio exceeds 2 once t is large enough, e.g. k=10,
    t=10 gives 461/229 ~ 2.013, and tends to (9k+2)/(4k+4) as t grows.
    """
    if k < 10 or k % 2:
        raise ValueError("Shibata's construction needs even k >= 10")
    s = k // 2
    bs = fresh_symbols(t, exclude="xya")
    strings, prio, zero = [], [], []
    for i, b in enumerate(bs):
        U = "xa" + _X(s - 3) + b + "xa" + _X(s - 3) + "y"
        V = "xa" + _X(s - 3) + b
        W = "xa" + _X(s - 1) + b
        assert (len(U), len(V), len(W)) == (k, s, s + 2)
        strings += cyclic_chain(U, k, 1) + cyclic_chain(V, k, 1) + cyclic_chain(W, k, 1)
        u_chain = cyclic_chain(U, k, start=4)   # U_{i,4} ... U_{i,k} U_{i,1} .. U_{i,3}
        v_chain = cyclic_chain(V, k, start=2)   # V_{i,2} ... V_{i,s} V_{i,1}
        w_chain = cyclic_chain(W, k, start=6)   # W_{i,6} ... W_{i,s+2} W_{i,1} .. W_{i,5}
        # Phase 1 (overlap k-1).
        prio += _chain_edges(u_chain) + _chain_edges(v_chain) + _chain_edges(w_chain)
        # Phase 2 (overlap s-3): M_i = V^_i ⊙ U^_i.
        prio.append([v_chain[-1], u_chain[0]])
        zero.append((v_chain[0], u_chain[-1], w_chain[0], w_chain[-1]))
    # Phase 3 (overlap 1): M_1 ⊙ ... ⊙ M_t.
    for i in range(t - 1):
        prio.append([zero[i][1], zero[i + 1][0]])
    # Phase 4 (overlap 0): M W^_1 ... W^_t.
    prev = zero[-1][1]
    for (_, _, w_first, w_last) in zero:
        prio.append([prev, w_first])
        prev = w_last
    n = t * (4 * s + 2)
    assert len(set(strings)) == n
    return _instance(f"shibata_k{k}_t{t}", strings, SHIBATA, opt=n + k - 1, greedy_bad=t * (9 * s + 1) + 1,
                     tie_priority=prio, params={"k": k, "t": t}, symbols={"b_i": bs},
                     notes="Ratio (t(9s+1)+1)/(t(4s+2)+k-1) -> (9k+2)/(4k+4) as t -> inf; -> 9/4 as k -> inf.")


# ---------------------------------------------------------------- misc

def kulikov_collapsing_counterexample() -> dict:
    """Counterexample to the Collapsing Superstring Conjecture (Kulikov et al. repository).

    That conjecture concerns a different greedy variant.  The instance is
    included because it is small, structured and known to be adversarial.
    OPT is computed by DP when the literature set is imported.
    """
    strings = ["accaccaccaccaccb", "accaccaccbccaccac", "accaccbccaccaccbccac",
               "bccaccaccbccaccacc", "accbccaccaccaccacc"]
    return _instance("kulikov_collapsing_cex", strings, KULIKOV_REPO,
                     notes="Counterexample to the collapsing superstring conjecture, not to the greedy conjecture.")


def kulikov_readme_example() -> dict:
    """Example input from the README of the Kulikov et al. repository."""
    return _instance("kulikov_readme_example", ["abba", "abca", "aac", "cab", "bab", "dbb"], KULIKOV_REPO)


def literature_instances() -> list[dict]:
    """The default literature set written by ``scripts/import_literature.py``."""
    out = [slides_attac(), slides_preprocess(), slides_greedy_fail(),
           kulikov_readme_example(), kulikov_collapsing_counterexample()]
    out += [tarhio_ukkonen_example7(h) for h in (1, 2, 3, 5, 10, 20)]
    out += [chukhin_k3(t) for t in (1, 2, 3, 5, 10, 20)]
    out += [chukhin_k(6, t) for t in (1, 2, 3, 5, 10)]
    out += [chukhin_k(k, 1) for k in (7, 8, 10)]
    out += [chukhin_k(8, t) for t in (2, 5)]
    out += [shibata(10, t) for t in (1, 2, 3, 5, 10, 20, 50)]
    out += [shibata(k, t) for k in (12, 16, 20) for t in (1, 5, 20)]
    return out
