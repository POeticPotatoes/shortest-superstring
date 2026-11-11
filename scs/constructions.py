"""Known instances from the slides and the literature, transcribed exactly.

Each function returns an instance dict (see :mod:`scs.instance_io`) with:

``known``
    Values reported in the source: ``opt``, ``greedy_bad`` (the length of
    the bad greedy execution) and, when the source only gives a common
    superstring rather than OPT, ``opt_upper`` (its length; the superstring
    itself is stored as ``upper_superstring``).  Where the source only gives a
    formula, the formula is evaluated.
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
  arXiv:2609.01365v1 (2026): the first counterexample, with ratio -> 9/4.  The
  author credits OpenAI's GPT-5.6 Sol with first finding it.  v1 is now a
  preliminary version of v2 below; :func:`shibata` keeps the v1 family.
* Chukhin, Gajjala, Harviainen, Kulikov, Mihajlin, Shibata, Smal, "The Greedy
  Superstring Conjecture Is False", arXiv:2609.01365v2 (6 Nov 2026), Theorem
  4.1: binary gap-word instances with ratio -> 12/5 (:func:`greedy_12_5`).
  The authors report that Claude Opus-5.5 found this construction.  Sections 5
  and 6 repeat the k = 3 and k >= 6 constructions of arXiv:2608.20018.
* Kulikov et al., github.com/alexanderskulikov/greedy-superstring-conjecture,
  counterexample to the *Collapsing* Superstring Conjecture (2025).
"""

from __future__ import annotations

from typing import Sequence

TU1988 = "Tarhio & Ukkonen, A greedy approximation algorithm for constructing shortest common superstrings, TCS 57 (1988) 131-145"
CHUKHIN6 = "Chukhin, Kulikov, Mihajlin, Smal, The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already, arXiv:2608.20018 (2026)"
SHIBATA = "Shibata, Disproving the Greedy Superstring Conjecture, arXiv:2609.01365v1 (2026; superseded by v2)"
CGHKMSS_V2 = ("Chukhin, Gajjala, Harviainen, Kulikov, Mihajlin, Shibata, Smal, The Greedy Superstring Conjecture "
              "Is False, arXiv:2609.01365v2 (2026), Theorem 4.1")
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
              symbols: dict | None = None, opt_upper: int | None = None,
              upper_superstring: str | None = None) -> dict:
    known = {"opt": opt, "greedy_bad": greedy_bad}
    if opt_upper is not None:
        known["opt_upper"] = opt_upper
    inst = {
        "id": name,
        "family": "literature",
        "strings": strings,
        "params": params or {},
        "seed": None,
        "citation": citation,
        "known": known,
        "tie_priority": tie_priority or [],
        "notes": notes,
        "symbols": symbols or {},
    }
    if upper_superstring is not None:
        inst["upper_superstring"] = upper_superstring
    return inst


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


# ---------------------------------------------------------------- 12/5 (arXiv:2609.01365v2)

def gap_word(left: int, gaps: Sequence[int], right: int) -> str:
    """``[L | g_1 ... g_k | R] = 0^L 1 0^(g_1 - 1) 1 ... 0^(g_k - 1) 1 0^R`` (Section 4.1)."""
    return "0" * left + "1" + "".join("0" * (g - 1) + "1" for g in gaps) + "0" * right


def greedy_12_5_formulas(r: int, P: int) -> dict:
    """Theorem 4.1 values: ``|H|`` (an upper bound on OPT) and the bad greedy length."""
    greedy_len = 12 * P * r + (115 * r * r + 7 * r) // 2
    upper = 5 * P * r + 27 * r * r + 4 * P + 19 * r + 1
    return {"n": 5 * r, "opt_upper": upper, "greedy_bad": greedy_len, "ratio_lower_bound": greedy_len / upper}


def greedy_12_5(r: int, P: int | None = None) -> dict:
    """Theorem 4.1 of arXiv:2609.01365v2: the 12/5 lower bound.

    For integers ``r >= 1`` and ``P >= r - 1`` (default ``P = r^2``), with
    ``M = P + 8r`` and ``p_i = P + r + i``, the instance has five binary gap
    words per ``i``::

        X_i = [P+2r | p_i M p_i M | P]      Y_i = [P | M p_i M p_i | P+4r]
        U_i = [P | M M p_i M | P]           V_i = [P | M p_i M M | P+r]
        Z_i = [P+r | M M p_i | 0]

    ``H = [P+r | M M p_1 M p_1 ... M M p_r M p_r M M | P+r]`` is a common
    superstring of length ``5Pr + 27r^2 + 4P + 19r + 1``.  It is only an
    *upper bound* on OPT.  The greedy execution of Section 4.4 outputs
    ``T_1 ... T_r`` of length ``12Pr + (115r^2 + 7r)/2``:

    (i)   for i = r..1 merge (X_i, Y_i) -> A_i, then (U_i, V_i) -> B_i   [overlap alpha_i]
    (ii)  merge (B_i, Z_i) -> C_i                                        [beta]
    (iii) merge (A_i, C_i) -> T_i                                        [gamma]
    (iv)  concatenate T_1 ... T_r                                        [0]

    In edge terms these are (X_i,Y_i), (U_i,V_i), (V_i,Z_i), (Y_i,U_i), (Z_i,X_{i+1}).
    The ratio G/|H| tends to 12/5 with P = r^2 as r -> infinity.  It passes
    9/4 at r = 20 and 7/3 at r = 50.
    """
    if P is None:
        P = r * r
    if r < 1 or P < r - 1:
        raise ValueError("Theorem 4.1 needs r >= 1 and P >= r - 1")
    M = P + 8 * r
    blocks, prio_i, prio_ii, prio_iii, gaps = [], [], [], [], []
    for i in range(1, r + 1):
        p = P + r + i
        X = gap_word(P + 2 * r, [p, M, p, M], P)
        Y = gap_word(P, [M, p, M, p], P + 4 * r)
        U = gap_word(P, [M, M, p, M], P)
        V = gap_word(P, [M, p, M, M], P + r)
        Z = gap_word(P + r, [M, M, p], 0)
        blocks.append((X, Y, U, V, Z))
        prio_ii.append([V, Z])
        prio_iii.append([Y, U])
        gaps += [M, M, p, M, p]
    for X, Y, U, V, Z in reversed(blocks):              # Step (i) runs i = r, ..., 1
        prio_i += [[X, Y], [U, V]]
    prio_iv = [[blocks[i][4], blocks[i + 1][0]] for i in range(r - 1)]
    H = gap_word(P + r, gaps + [M, M], P + r)
    f = greedy_12_5_formulas(r, P)
    assert len(H) == f["opt_upper"]
    strings = [s for block in blocks for s in block]
    return _instance(f"greedy125_r{r}_P{P}", strings, CGHKMSS_V2, greedy_bad=f["greedy_bad"],
                     opt_upper=f["opt_upper"], upper_superstring=H,
                     tie_priority=prio_i + prio_ii + prio_iii + prio_iv,
                     params={"r": r, "P": P, "M": M},
                     notes="OPT <= |H| only; G/|H| is a certified lower bound on G/OPT. "
                           "Ratio (12Pr+(115r^2+7r)/2)/(5Pr+27r^2+4P+19r+1) -> 12/5 for P=r^2.")


def greedy_12_5_adapted_formulas(n: int) -> dict:
    """Exact |H_n| and G_n of the report's single-parameter adaptation (report Appendix, 'For reference')."""
    upper = 5 * n ** 3 + 12 * n ** 2 - 2 * n - 1
    greedy_len = 12 * n ** 3 + (31 * n * n - 43 * n - 12) // 2
    return {"n_strings": 5 * (n - 1), "opt_upper": upper, "greedy_bad": greedy_len,
            "ratio_lower_bound": greedy_len / upper}


def greedy_12_5_adapted(n: int) -> dict:
    """The team report's single-parameter adaptation of Theorem 4.1 (report Section 4.4 / Appendix B).

    For ``n >= 2``, with ``N = n^2``, ``M = N + 4n`` and ``p_i = N + i`` for ``2 <= i <= n``::

        X_i = [N+n | p_i M p_i M | N]       Y_i = [N | M p_i M p_i | N+2n]
        U_i = [N | M M p_i M | N]           V_i = [N | M p_i M M | N+1]
        Z_i = [p_i-1 | M M p_i | 0]

    ``H_n = [p_n-1 | (M M p_n M p_n)(M M p_{n-1} M p_{n-1}) ... (M M p_2 M p_2)(M M) | N+1]``.
    The prescribed execution forms A_i = X_i+Y_i and B_i = U_i+V_i (i = n..2), then
    C_i = B_i+Z_i (i = n..2), then T_i = A_i+C_i, and concatenates.  The overlaps are
    alpha_i = 5N+8n+i+1, beta_i = 4N+8n+i+1 and gamma = 2N+2n+1.
    """
    if n < 2:
        raise ValueError("the adapted construction needs n >= 2")
    N, M = n * n, n * n + 4 * n
    blocks = {}
    for i in range(2, n + 1):
        p = N + i
        blocks[i] = (gap_word(N + n, [p, M, p, M], N), gap_word(N, [M, p, M, p], N + 2 * n),
                     gap_word(N, [M, M, p, M], N), gap_word(N, [M, p, M, M], N + 1), gap_word(p - 1, [M, M, p], 0))
    down = range(n, 1, -1)
    prio = [e for i in down for e in ([blocks[i][0], blocks[i][1]], [blocks[i][2], blocks[i][3]])]
    prio += [[blocks[i][3], blocks[i][4]] for i in down]                 # B_i -> Z_i
    prio += [[blocks[i][1], blocks[i][2]] for i in down]                 # A_i -> C_i (Y_i -> U_i)
    prio += [[blocks[i][4], blocks[i - 1][0]] for i in range(n, 2, -1)]  # concatenate (overlap 0)
    H = gap_word(N + n - 1, [g for i in down for g in (M, M, N + i, M, N + i)] + [M, M], N + 1)
    f = greedy_12_5_adapted_formulas(n)
    assert len(H) == f["opt_upper"]
    strings = [s for i in range(2, n + 1) for s in blocks[i]]
    return _instance(f"greedy125adapted_n{n}", strings, "Team report, Section 4.4: single-parameter adaptation of "
                     + CGHKMSS_V2, greedy_bad=f["greedy_bad"], opt_upper=f["opt_upper"], upper_superstring=H,
                     tie_priority=prio, params={"n": n, "N": N, "M": M},
                     notes="OPT <= |H_n|; G_n/|H_n| -> 12/5.")


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
    # 12/5 family: minimal P = r - 1 and P = r^2 for DP-sized r, then P = r^2 up to r = 50.
    out += [greedy_12_5(r, r - 1) for r in (1, 2, 3, 4)]
    # Larger r (30, 50, 100, ...) is generated on the fly by scripts/experiment_12_5.py instead of stored.
    out += [greedy_12_5(r) for r in (1, 2, 3, 4, 6, 10, 20)]
    out += [greedy_12_5_adapted(n) for n in (2, 3, 4, 5, 6, 10)]   # the report's Section 4.4 family
    return out
