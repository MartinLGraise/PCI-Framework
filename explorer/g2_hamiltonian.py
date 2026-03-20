"""
G2 seven-dimensional representation:
  - explicit generator construction via Fano-plane structure constants
  - SU(3) subalgebra identification (stabilizer of e7)
  - quadratic Hamiltonian H = alpha*C2(G2) + beta*C2(SU3) + gamma*P_void
  - Cartan-generator term to split sextet 6 -> 3 + 3bar
  - spectral analysis and eigenvalue ratio tables

Mathematical context
--------------------
G2 has a unique 7-dim irrep (the fundamental representation).
Its maximal SU(3) subgroup stabilizes one distinguished direction ("e7").
Under SU(3):  7_R  -->  1_R  +  6_R       (real decomposition)
                     -->  1_C  +  3_C + 3bar_C  (complex decomposition)

The 6_R is real-irreducible: 3 and 3bar are complex-conjugate reps and cannot
be separated by any G2-invariant quadratic operator. Schur's lemma forces:
    C2(G2) = -2 * I    (constant on every vector, single level)
    C2(SU3) = {0 on singlet, -4/3 on sextet}   (two levels)

To produce a [3, 3, 1] spectral pattern we must break the SU(3) symmetry with
a Cartan-element term Q: the U(1) ⊂ SU(3) generator that distinguishes 3 from
3bar. Q acts on the sextet with eigenvalues {±i lambda} in pairs; Q^2 gives
negative-definite but (generically) three different 2-fold degenerate values,
yielding pattern [2, 2, 2, 1]. A single Cartan element that is proportional
to diag(i,-i,i,-i,i,-i) in the complex triplet basis yields a [3, 3, 1]
pattern in the real basis via its square.
"""

import numpy as np
from collections import Counter

# ---------------------------------------------------------------------------
# Fano plane structure constants (0-indexed)
# ---------------------------------------------------------------------------
FANO_TRIPLES = [
    (0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6),
    (4, 5, 0), (5, 6, 1), (6, 0, 2),
]


def build_eps():
    eps = np.zeros((7, 7, 7))
    for (a, b, c) in FANO_TRIPLES:
        for (i, j, k, s) in [
            (a,b,c,1),(b,c,a,1),(c,a,b,1),
            (b,a,c,-1),(a,c,b,-1),(c,b,a,-1)
        ]:
            eps[i, j, k] = s
    return eps


def build_so7_basis():
    basis = []
    for i in range(7):
        for j in range(i+1, 7):
            E = np.zeros((7, 7))
            E[i, j] = 1.0; E[j, i] = -1.0
            basis.append(E)
    return basis


def project_to_g2(so7_basis, eps):
    """Return 14 g2 generators as 7x7 matrices via Fano 3-form constraint."""
    triples = [(i,j,k) for i in range(7) for j in range(i+1,7) for k in range(j+1,7)]
    n = len(so7_basis)
    C = np.zeros((len(triples), n))
    for alpha, T in enumerate(so7_basis):
        for t, (i,j,k) in enumerate(triples):
            v = sum(T[i,a]*eps[a,j,k] + T[j,a]*eps[i,a,k] + T[k,a]*eps[i,j,a]
                    for a in range(7))
            C[t, alpha] = v
    _, s, Vt = np.linalg.svd(C)
    full_s = np.concatenate([s, np.zeros(n - len(s))])
    null_rows = np.where(full_s < 1e-8)[0]
    return [sum(Vt[r, alpha] * so7_basis[alpha] for alpha in range(n)) for r in null_rows]


def gram_schmidt(gens):
    """Orthonormalize under <A,B> = -Tr(AB) (positive definite on antisym matrices)."""
    basis = []
    for T in gens:
        v = T.copy()
        for B in basis:
            v -= (-np.trace(v @ B)) * B
        n2 = -np.trace(v @ v)
        if n2 > 1e-12:
            basis.append(v / np.sqrt(n2))
    return basis


def split_su3(g2_raw, singlet_idx=6):
    """
    Split raw g2 generators into SU(3) (stabilizer of e_{singlet_idx}) and coset.
    Uses SVD projection when the direct check fails (rotated SVD basis).
    """
    # Direct check first
    su3, coset = [], []
    for T in g2_raw:
        if np.linalg.norm(T[singlet_idx,:]) + np.linalg.norm(T[:,singlet_idx]) < 1e-8:
            su3.append(T)
        else:
            coset.append(T)
    if len(su3) == 8:
        return gram_schmidt(su3), gram_schmidt(coset)

    # SVD projection: find null space of "touches e7" constraint
    n = len(g2_raw)
    vecs = np.array([T.flatten() for T in g2_raw]).T  # (49, 14)
    zero_rows = sorted(set([singlet_idx*7+j for j in range(7)] +
                            [i*7+singlet_idx for i in range(7)]))
    C_su3 = vecs[zero_rows, :]              # (13, 14)
    _, s_su3, Vt_su3 = np.linalg.svd(C_su3)
    full_s = np.concatenate([s_su3, np.zeros(14 - len(s_su3))])
    null_mask = full_s < 1e-8              # length-14 boolean
    su3_coeffs   = Vt_su3[null_mask, :]   # (8, 14)
    coset_coeffs = Vt_su3[~null_mask, :]  # (6, 14)

    su3_raw   = [sum(su3_coeffs[k,i]*g2_raw[i]   for i in range(n)) for k in range(su3_coeffs.shape[0])]
    coset_raw = [sum(coset_coeffs[k,i]*g2_raw[i] for i in range(n)) for k in range(coset_coeffs.shape[0])]
    return gram_schmidt(su3_raw), gram_schmidt(coset_raw)


def casimirs(su3_on, coset_on, singlet_idx):
    C2_G2  = sum(T @ T for T in su3_on + coset_on)
    C2_SU3 = sum(T @ T for T in su3_on)
    P_void = np.zeros((7, 7))
    P_void[singlet_idx, singlet_idx] = 1.0
    return C2_G2, C2_SU3, P_void


def spectrum(H):
    vals, vecs = np.linalg.eigh(H)
    idx = np.argsort(vals)
    return vals[idx], vecs[:, idx]


def deg_pattern(ev, tol=1e-3):
    rounded = np.round(ev / tol) * tol
    cnt = Counter(rounded)
    return sorted(cnt.values(), reverse=True), dict(cnt)


def find_cartan_generators(su3_on, singlet_idx=6):
    """
    Identify the two Cartan generators (rank-2 Cartan subalgebra of SU(3))
    from the 8 orthonormal SU(3) generators.

    A Cartan generator H satisfies [H, H'] = 0 for all other Cartan generators.
    We find them by looking for generators that are diagonal in the 6x6 block
    (i.e., T^2 has 3 distinct 2-fold eigenvalues in the sextet).

    Returns the two Cartan generators and the 6 root generators.
    """
    # Compute all pairwise commutators within the 6x6 complement block
    idx6 = [i for i in range(7) if i != singlet_idx]
    scores = []
    for k, T in enumerate(su3_on):
        # T restricted to 6x6 block
        T6 = T[np.ix_(idx6, idx6)]
        T6sq = T6 @ T6
        # Cartan generators have T6 that is block-diagonal (2x2 blocks)
        # Measure "diagonality" by off-block-diagonal norm
        # Alternatively: T^2 eigenvalues — Cartan should have max distinct eigenvalues
        ev6 = np.sort(np.linalg.eigvalsh(T6sq))
        # Number of distinct eigenvalues (Cartan has 3 distinct pairs)
        n_distinct = len(np.unique(np.round(ev6, 4)))
        scores.append((n_distinct, k, T6sq, np.linalg.norm(T6sq - np.diag(np.diag(T6sq)))))
    scores.sort(key=lambda x: (-x[0], x[3]))
    return scores


def main():
    eps = build_eps()
    so7 = build_so7_basis()

    print("=" * 70)
    print("G2 SEVEN-DIMENSIONAL REPRESENTATION — SPECTRAL ANALYSIS")
    print("=" * 70)

    # ---- 1. G2 generators ----
    print("\n[1] G2 generators via Fano 3-form constraint on so(7)")
    g2_raw = project_to_g2(so7, eps)
    print(f"    Null-space dimension: {len(g2_raw)}  (expected 14)")

    # ---- 2. SU(3) split ----
    print("\n[2] SU(3) subalgebra = stabilizer of e7 (index 6)")
    SINGLET = 6
    su3_on, coset_on = split_su3(g2_raw, singlet_idx=SINGLET)
    print(f"    SU(3) generators (orthonormal): {len(su3_on)}  (expected 8)")
    print(f"    Coset generators (orthonormal): {len(coset_on)}  (expected 6)")
    mix = max(np.linalg.norm(T[SINGLET,:]) + np.linalg.norm(T[:,SINGLET]) for T in su3_on)
    print(f"    Max e7-mixing in SU(3) generators: {mix:.1e}  (should be ~0)")

    # ---- 3. Casimirs ----
    print("\n[3] Casimir operators")
    C2_G2, C2_SU3, P_void = casimirs(su3_on, coset_on, SINGLET)

    ev_g2 = np.linalg.eigvalsh(C2_G2)
    ev_su3 = np.linalg.eigvalsh(C2_SU3)
    print(f"    C2(G2)  eigenvalues: {np.round(ev_g2, 6)}")
    print(f"    C2(SU3) eigenvalues: {np.round(ev_su3, 4)}")
    print(f"    C2(SU3) levels:")
    print(f"      Singlet (e7): {C2_SU3[SINGLET, SINGLET]:.4f}")
    idx6 = [i for i in range(7) if i != SINGLET]
    ev6 = np.linalg.eigvalsh(C2_SU3[np.ix_(idx6, idx6)])
    print(f"      Sextet eigenvalues: {np.round(ev6, 4)}")
    print(f"    --> C2(SU3) gives two levels: {{0}} and {{-4/3}} = {-4/3:.4f}")
    print(f"    --> Sextet 6 = 3 + 3bar is REAL-IRREDUCIBLE; C2 cannot split it.")

    # ---- 4. Full Hamiltonian scan ----
    print("\n[4] H = alpha*C2(G2) + beta*C2(SU3) + gamma*P_void  (alpha=1)")
    print("    Analytic eigenvalues:")
    print("      E_singlet = -2*alpha + gamma")
    print("      E_sextet  = -2*alpha - (4/3)*beta   [6-fold degenerate]")
    print()
    print(f"    {'beta':>5} {'gamma':>6} | E_singlet   E_sextet  | ratio E_s/E_6")
    print("    " + "-" * 52)
    for beta in [0.0, 0.25, 0.5, 0.75, 1.0, 2.0]:
        for gamma in [0.0, 0.5, 1.0, 2.0]:
            E_s = -2.0 + gamma
            E_6 = -2.0 - (4.0/3.0)*beta
            ratio = E_s/E_6 if abs(E_6) > 1e-12 else float('inf')
            print(f"    {beta:>5.2f} {gamma:>6.2f} | {E_s:+10.4f}  {E_6:+10.4f} | {ratio:+8.4f}")

    # ---- 5. Cartan generator analysis ----
    print("\n[5] Cartan generators of SU(3): splitting sextet into 2+2+2")
    print("    Each antisymmetric SU(3) Cartan generator T has eigenvalues")
    print("    {0, ±i*a, ±i*b, ±i*c} in the complex basis.")
    print("    T^2 gives {0, -a^2, -a^2, -b^2, -b^2, -c^2, -c^2} -> pattern [2,2,2,1]")
    print()
    scores = find_cartan_generators(su3_on, SINGLET)
    idx6 = [i for i in range(7) if i != SINGLET]

    print(f"    {'Gen':>4} | T^2 eigenvalues in 6-dim sextet | n_distinct | pattern")
    print("    " + "-" * 65)
    for n_dist, k, T6sq, offdiag in scores:
        ev6 = np.round(np.sort(np.linalg.eigvalsh(T6sq)), 4)
        pattern, _ = deg_pattern(ev6)
        print(f"    T_{k+1:02d} | {ev6} | {n_dist} | {pattern}")

    # Identify best Cartan candidate (3 distinct pairs -> [2,2,2] pattern in 6-dim)
    best = next(((n_dist, k) for n_dist, k, _, _ in scores if n_dist == 3), None)
    if best is not None:
        _, k_best = best
    else:
        _, k_best, _, _ = scores[0]
    Q = su3_on[k_best]
    Q2 = Q @ Q
    print(f"\n    Best Cartan-type generator: T_{k_best+1}")
    ev_Q2 = np.sort(np.linalg.eigvalsh(Q2))
    print(f"    Q^2 eigenvalues: {np.round(ev_Q2, 4)}")
    patt, cnt = deg_pattern(ev_Q2)
    print(f"    Degeneracy pattern: {patt}  -> {dict(cnt)}")

    # ---- 6. Extended Hamiltonian with Cartan term ----
    print("\n[6] Extended Hamiltonian: H = C2(G2) + beta*C2(SU3) + gamma*P_void + delta*Q^2")
    print("    Q = best Cartan generator of SU(3) ⊂ G2")
    print("    Q^2 splits sextet into sub-eigenvalue groups")
    print()
    print(f"    {'beta':>5} {'gamma':>6} {'delta':>6} | eigenvalues (sorted)                | pattern")
    print("    " + "-" * 80)

    param_sets = [
        (0.0, 0.0, 0.0),
        (0.0, 0.0, 1.0),
        (0.0, 1.0, 1.0),
        (1.0, 0.0, 0.0),
        (1.0, 0.0, 1.0),
        (1.0, 1.0, 0.0),
        (1.0, 1.0, 1.0),
        (0.0, 2.0, 1.0),
        (2.0, 2.0, 1.0),
    ]
    for beta, gamma, delta in param_sets:
        H = C2_G2 + beta*C2_SU3 + gamma*P_void + delta*Q2
        ev, _ = spectrum(H)
        patt, cnt = deg_pattern(ev)
        ev_str = " ".join(f"{v:+7.4f}" for v in ev)
        print(f"    {beta:>5.1f} {gamma:>6.1f} {delta:>6.1f} | {ev_str} | {patt}")

    # ---- 7. [3,3,1] pattern search over Q^2 from all SU(3) Cartan candidates ----
    print("\n[7] Searching all SU(3) generators for [3,3,1] eigenvalue pattern")
    print("    H = C2(G2) + beta*C2(SU3) + gamma*P_void + delta*(T_k)^2")
    print()
    found = []
    for k, T in enumerate(su3_on):
        Tk2 = T @ T
        for beta in np.linspace(0, 3, 7):
            for gamma in np.linspace(0, 3, 7):
                for delta in np.linspace(0, 3, 7):
                    H = C2_G2 + beta*C2_SU3 + gamma*P_void + delta*Tk2
                    ev, _ = spectrum(H)
                    patt, cnt = deg_pattern(ev, tol=5e-3)
                    if patt == [3, 3, 1]:
                        found.append((k, beta, gamma, delta, ev.copy()))

    if found:
        print(f"    Found {len(found)} parameter combinations giving [3,3,1]!")
        for k, b, g, d, ev in found[:10]:
            print(f"      T_{k+1}, beta={b:.2f}, gamma={g:.2f}, delta={d:.2f}: {np.round(ev,4)}")
            nonzero_levels = np.unique(np.round(ev, 2))
            print(f"        Levels: {nonzero_levels}")
            if len(nonzero_levels) >= 2:
                ratios = nonzero_levels / nonzero_levels[0]
                print(f"        Ratios: {np.round(ratios, 4)}")
    else:
        print("    No exact [3,3,1] found. Reporting best 2-level splits:")
        print("    (The 6_R = 3+3bar is real-irreducible under SU(3);")
        print("     [3,3,1] requires a complex structure or external U(1) coupling.)")
        # Show best approximate case
        print()
        print("    Closest patterns with T_k^2 breaking:")
        shown = set()
        for k, T in enumerate(su3_on[:4]):
            Tk2 = T @ T
            for delta in [0.5, 1.0, 2.0]:
                H = C2_G2 + 1.0*C2_SU3 + 1.0*P_void + delta*Tk2
                ev, _ = spectrum(H)
                patt, _ = deg_pattern(ev, tol=5e-3)
                key = str(patt)
                if key not in shown:
                    shown.add(key)
                    print(f"      T_{k+1}, delta={delta}: {np.round(ev,4)} pattern={patt}")

    # ---- 8. Summary of two-level structure ----
    print("\n[8] SUMMARY: Eigenvalue structure of G2 7-dim Hamiltonian")
    print("=" * 70)
    print()
    print("  Level structure of H = alpha*C2(G2) + beta*C2(SU3) + gamma*P_void:")
    print()
    print("    Mode        | Multiplicity | C2(G2) | C2(SU3) | P_void")
    print("    " + "-" * 55)
    print("    Singlet 1   |      1       |   -2   |    0    |   1")
    print("    Sextet 3+3bar|     6       |   -2   |  -4/3   |   0")
    print()
    print("    Eigenvalues:")
    print("      E_singlet = -2*alpha + gamma")
    print("      E_sextet  = -2*alpha - (4/3)*beta")
    print()
    print("    Physical ratio E_singlet / E_sextet:")
    for beta in [0.0, 0.5, 1.0, 2.0, 5.0]:
        for gamma in [0.0, 1.0, 2.0, 4.0]:
            E_s = -2.0 + gamma
            E_6 = -2.0 - (4.0/3.0)*beta
            if abs(E_6) > 1e-10 and abs(E_s) > 1e-10:
                ratio = E_s / E_6
                print(f"      beta={beta:.1f}, gamma={gamma:.1f}: ratio = {ratio:+.4f}")

    print()
    print("  Key result: The quadratic G2 Hamiltonian on the 7-dim rep gives")
    print("  at most a TWO-LEVEL spectrum: one singlet and one 6-fold degenerate")
    print("  sextet. The sextet is real-irreducible under SU(3) (= 3 + 3bar over C).")
    print("  To achieve a [3, 3, 1] split, a U(1) generator linear term or")
    print("  complex structure must be added (going beyond quadratic G2 invariants).")
    print()

    # ---- 9. Generator matrices ----
    print("[9] First 3 SU(3) generators (7×7 antisymmetric):")
    for k in range(3):
        T = su3_on[k]
        print(f"\n    T_{k+1} (SU3 generator, Frob-norm = {np.sqrt(-np.trace(T@T)):.4f}):")
        print(np.round(T, 4))

    print("\n[10] First 2 coset generators (G2/SU3):")
    for k in range(2):
        T = coset_on[k]
        print(f"\n    K_{k+1} (coset generator):")
        print(np.round(T, 4))

    print("\n" + "=" * 70)
    print("DONE")
    print("=" * 70)


if __name__ == "__main__":
    main()
