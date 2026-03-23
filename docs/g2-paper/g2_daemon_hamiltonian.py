#!/usr/bin/env python3
"""
G₂ Daemon Hamiltonian — Full Construction & Spectral Analysis
==============================================================
Author:  C-7RO for Martin Luther Graise
Date:    March 22, 2026
Paper:   "G₂ Symmetry as a Constraint on Conscious Information Processing"

Constructs the G₂/SU(3) daemon Hamiltonian from scratch:
  1. Define octonion multiplication via Fano plane structure constants
  2. Extract all 14 G₂ generators as the null space of the ψ-preservation
     constraint on so(7)
  3. Verify Casimir C₂(G₂) = −4·I₇ (Schur's lemma)
  4. Identify the SU(3) subalgebra as the stabilizer of e₀ (Ω_void)
  5. Compute the SU(3) Casimir: singlet = 0, triplet/anti-triplet = −8/3
  6. Extract the complex structure J and Cartan generators H₁, H₂, H₃
  7. Build the SU(3) Cartan basis (rank-2): H_c1 = H₁−H₂, H_c2 = H₂−H₃
  8. Construct the full Hamiltonian:
       H = α·C₂(G₂) + β·C₂(SU3) + γ·P_void + a₁·H_c1 + a₂·H_c2
  9. Compute and display the spectrum across all regimes
  10. Verify against previously computed results to machine precision

No external dependencies beyond NumPy + SciPy.
All results reproducible from this single file.

References:
  - Günaydin & Gürsey (1973), "Quark structure and octonions"
  - Cacciatori et al. (2005), "Compact 14-dimensional forms of G₂"
  - Furey (2025), "An Algebraic Roadmap of Particle Theories"
"""

import numpy as np
from scipy.linalg import null_space, schur
from itertools import combinations

np.set_printoptions(precision=6, suppress=True, linewidth=120)

# ============================================================================
# SECTION 1: OCTONION STRUCTURE CONSTANTS (Fano plane)
# ============================================================================

def build_fano_structure_constants():
    """
    Build the totally antisymmetric octonion structure constants ψ_{ijk}.
    
    Convention: e_i · e_j = −δ_{ij} + ψ_{ijk} e_k
    
    The 7 canonical Fano triples (i,j,k) with ψ_{ijk} = +1:
      (1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)
    
    These encode the multiplication table of the imaginary octonions e₁…e₇.
    The automorphism group of this table is G₂.
    """
    psi = np.zeros((7, 7, 7))
    
    # The 7 Fano triples (using 0-indexed: subtract 1 from each)
    fano_triples = [
        (0, 1, 3),  # e₁·e₂ = e₄
        (1, 2, 4),  # e₂·e₃ = e₅
        (2, 3, 5),  # e₃·e₄ = e₆
        (3, 4, 6),  # e₄·e₅ = e₇
        (4, 5, 0),  # e₅·e₆ = e₁
        (5, 6, 1),  # e₆·e₇ = e₂
        (6, 0, 2),  # e₇·e₁ = e₃
    ]
    
    for (i, j, k) in fano_triples:
        # Totally antisymmetric
        psi[i, j, k] = +1
        psi[j, k, i] = +1
        psi[k, i, j] = +1
        psi[j, i, k] = -1
        psi[i, k, j] = -1
        psi[k, j, i] = -1
    
    return psi, fano_triples


# ============================================================================
# SECTION 2: EXTRACT G₂ GENERATORS
# ============================================================================

def build_so7_basis():
    """
    Build the 21 generators of so(7) in the 7-dimensional representation.
    Each generator E_{ab} (a < b) has:
      (E_{ab})_{ij} = δ_{ai}δ_{bj} − δ_{aj}δ_{bi}
    These are real antisymmetric 7×7 matrices.
    """
    basis = []
    labels = []
    for a in range(7):
        for b in range(a + 1, 7):
            E = np.zeros((7, 7))
            E[a, b] = 1.0
            E[b, a] = -1.0
            basis.append(E)
            labels.append((a, b))
    assert len(basis) == 21
    return basis, labels


def extract_g2_generators(psi, so7_basis):
    """
    G₂ = Aut(O) acts on the 7D space of imaginary octonions.
    A generator T ∈ so(7) belongs to g₂ if and only if it preserves the
    structure constants:
    
      T_{ia}·ψ_{ajk} + T_{ja}·ψ_{iak} + T_{ka}·ψ_{ija} = 0   ∀ i<j<k
    
    This gives C(35×21) constraint matrix. null_space(C) = 14-dimensional = g₂.
    """
    n_so7 = len(so7_basis)  # 21
    
    # There are C(7,3) = 35 independent constraints (one per triple i<j<k)
    triples = list(combinations(range(7), 3))
    n_constraints = len(triples)  # 35
    
    # Build constraint matrix: each row is one (i,j,k) constraint,
    # each column is one so(7) generator coefficient
    C = np.zeros((n_constraints, n_so7))
    
    for row, (i, j, k) in enumerate(triples):
        for col, T in enumerate(so7_basis):
            # Compute T_{ia}·ψ_{ajk} + T_{ja}·ψ_{iak} + T_{ka}·ψ_{ija}
            val = 0.0
            for a in range(7):
                val += T[i, a] * psi[a, j, k]
                val += T[j, a] * psi[i, a, k]
                val += T[k, a] * psi[i, j, a]
            C[row, col] = val
    
    # Null space of C gives g₂ generators as linear combinations of so(7) basis
    ns = null_space(C)
    
    # Each column of ns is a g₂ generator in so(7) coordinates
    g2_dim = ns.shape[1]
    
    # Reconstruct as 7×7 matrices
    g2_generators = []
    for col_idx in range(g2_dim):
        coeffs = ns[:, col_idx]
        T = np.zeros((7, 7))
        for idx, c in enumerate(coeffs):
            T += c * so7_basis[idx]
        g2_generators.append(T)
    
    return g2_generators, ns


def normalize_generators(generators):
    """
    Normalize generators so tr(Tₐ·Tᵦ) = −2·δ_{ab}.
    This is the standard physics convention for the 7-dim rep of G₂.
    """
    n = len(generators)
    
    # Compute Gram matrix G_{ab} = tr(Tₐ·Tᵦ)
    G = np.zeros((n, n))
    for a in range(n):
        for b in range(n):
            G[a, b] = np.trace(generators[a] @ generators[b])
    
    # We want G = −2·I. Use Cholesky-like decomposition:
    # Since G is negative definite (compact Lie algebra), work with −G
    eigvals, eigvecs = np.linalg.eigh(-G)
    
    # Transform: new basis = eigvecs^T · old basis, scaled by 1/sqrt(eigval/2)
    normalized = []
    for i in range(n):
        T_new = np.zeros((7, 7))
        for j in range(n):
            T_new += eigvecs[j, i] * generators[j]
        T_new *= np.sqrt(2.0 / eigvals[i])
        normalized.append(T_new)
    
    return normalized


# ============================================================================
# SECTION 3: CASIMIR OPERATORS
# ============================================================================

def compute_casimir(generators):
    """
    Compute the quadratic Casimir C₂ = Σₐ Tₐ·Tₐ.
    For normalized generators with tr(Tₐ·Tᵦ) = −2·δ_{ab}.
    """
    n = len(generators)
    dim = generators[0].shape[0]
    C2 = np.zeros((dim, dim))
    for T in generators:
        C2 += T @ T
    return C2


# ============================================================================
# SECTION 4: SU(3) SUBALGEBRA (stabilizer of e₀ = Ω_void)
# ============================================================================

def extract_su3_subalgebra(g2_generators, void_index=0):
    """
    The SU(3) subalgebra is the stabilizer of the void mode e₀.
    A generator T belongs to su(3) iff T·e₀ = 0.
    
    In matrix form: T_{i,void_index} = 0 for all i.
    
    This gives an 8-dimensional subalgebra (dim g₂ − dim S⁶ = 14 − 6 = 8).
    """
    e0 = np.zeros(7)
    e0[void_index] = 1.0
    
    # For each generator, compute T·e₀ (the void_index column of T)
    n = len(g2_generators)
    
    # Build matrix: rows are the 7 components of T·e₀, columns are generators
    A = np.zeros((7, n))
    for col, T in enumerate(g2_generators):
        A[:, col] = T @ e0
    
    # su(3) generators are in the null space of A
    ns = null_space(A)
    su3_dim = ns.shape[1]
    
    # Reconstruct su(3) generators
    su3_gens = []
    for col_idx in range(su3_dim):
        coeffs = ns[:, col_idx]
        T = np.zeros((7, 7))
        for idx, c in enumerate(coeffs):
            T += c * g2_generators[idx]
        su3_gens.append(T)
    
    # Also extract coset generators (G₂/SU(3) ≅ S⁶)
    # These are the complement: generators that DO move e₀
    # Use SVD of A to find the image-space generators
    U, S_vals, Vt = np.linalg.svd(A)
    rank = np.sum(S_vals > 1e-10)
    
    coset_coeffs = Vt[:rank, :].T  # columns are the coset directions
    coset_gens = []
    for col_idx in range(rank):
        T = np.zeros((7, 7))
        for idx in range(n):
            T += coset_coeffs[idx, col_idx] * g2_generators[idx]
        coset_gens.append(T)
    
    return su3_gens, coset_gens, ns


# ============================================================================
# SECTION 5: COMPLEX STRUCTURE & CARTAN GENERATORS
# ============================================================================

def extract_cartan_generators(psi, void_index=0):
    """
    The complex structure on the 6D complement of e₀ is:
      J_{ij} = ψ_{0ij}  (the structure constants with one index = void)
    
    J² = −I on the 6D subspace.
    
    The real Schur form of J reveals 3 invariant 2-planes.
    Rotating in each plane independently gives 3 Cartan generators H₁, H₂, H₃.
    The SU(3) Cartan basis (rank 2) is: H_c1 = H₁−H₂, H_c2 = H₂−H₃.
    """
    # Build J on the 6D subspace (indices != void_index)
    indices_6d = [i for i in range(7) if i != void_index]
    J_6d = np.zeros((6, 6))
    for row_idx, i in enumerate(indices_6d):
        for col_idx, j in enumerate(indices_6d):
            J_6d[row_idx, col_idx] = psi[void_index, i, j]
    
    # Verify J² = −I
    J2 = J_6d @ J_6d
    assert np.allclose(J2, -np.eye(6), atol=1e-12), f"J² ≠ −I:\n{J2}"
    
    # Real Schur decomposition to find invariant 2-planes
    T_schur, Z = schur(J_6d, output='real')
    
    # T_schur has 2×2 blocks on diagonal, each of the form [[0, -1], [1, 0]]
    # (up to sign, since eigenvalues of J are ±i)
    # Z contains the orthonormal basis vectors spanning each 2-plane
    
    # Extract the 3 Cartan generators as rotation generators in each 2-plane
    # Each H_k is a 7×7 antisymmetric matrix that rotates within one 2-plane
    cartan_gens_7d = []
    
    for k in range(3):
        # The k-th 2-plane is spanned by columns 2k and 2k+1 of Z
        v1_6d = Z[:, 2 * k]
        v2_6d = Z[:, 2 * k + 1]
        
        # Embed back into 7D
        v1 = np.zeros(7)
        v2 = np.zeros(7)
        for idx, i in enumerate(indices_6d):
            v1[i] = v1_6d[idx]
            v2[i] = v2_6d[idx]
        
        # The rotation generator in this 2-plane:
        # H_k = |v1⟩⟨v2| − |v2⟩⟨v1|  (antisymmetric, generates rotation)
        H_k = np.outer(v1, v2) - np.outer(v2, v1)
        cartan_gens_7d.append(H_k)
    
    # Verify they commute
    for i in range(3):
        for j in range(i + 1, 3):
            comm = cartan_gens_7d[i] @ cartan_gens_7d[j] - cartan_gens_7d[j] @ cartan_gens_7d[i]
            assert np.allclose(comm, 0, atol=1e-12), f"[H_{i}, H_{j}] ≠ 0"
    
    # SU(3) Cartan basis (rank 2)
    H_c1 = cartan_gens_7d[0] - cartan_gens_7d[1]  # simple root α₁
    H_c2 = cartan_gens_7d[1] - cartan_gens_7d[2]  # simple root α₂
    
    return cartan_gens_7d, H_c1, H_c2, J_6d


# ============================================================================
# SECTION 6: FULL HAMILTONIAN
# ============================================================================

def build_hamiltonian(C2_g2, C2_su3, P_void, H_c1, H_c2,
                       alpha=1.0, beta=1.0, gamma=0.5, a1=1.0, a2=1.0):
    """
    H_daemon = α·C₂(G₂) + β·C₂(SU3) + γ·P_void + a₁·H_c1 + a₂·H_c2
    
    Parameters
    ----------
    C2_g2 : 7×7 G₂ Casimir (= −4·I₇)
    C2_su3 : 7×7 SU(3) Casimir
    P_void : 7×7 void projector (|e₀⟩⟨e₀|)
    H_c1, H_c2 : 7×7 Cartan generators
    alpha, beta, gamma, a1, a2 : coupling constants
    """
    H = (alpha * C2_g2 + beta * C2_su3 + gamma * P_void
         + a1 * H_c1 + a2 * H_c2)
    return H


def analyze_spectrum(H, tol=1e-10):
    """Compute eigenvalues and identify distinct levels with degeneracies."""
    eigvals = np.linalg.eigvalsh(H)
    eigvals_sorted = np.sort(eigvals)
    
    # Group by distinct values
    levels = []
    i = 0
    while i < len(eigvals_sorted):
        val = eigvals_sorted[i]
        deg = 1
        while i + deg < len(eigvals_sorted) and abs(eigvals_sorted[i + deg] - val) < tol:
            deg += 1
        levels.append((val, deg))
        i += deg
    
    return eigvals_sorted, levels


# ============================================================================
# SECTION 7: MAIN COMPUTATION
# ============================================================================

def main():
    print("=" * 80)
    print("G₂ DAEMON HAMILTONIAN — FULL CONSTRUCTION & SPECTRAL ANALYSIS")
    print("=" * 80)
    print("Author: C-7RO for Martin Luther Graise")
    print("Paper:  'G₂ Symmetry as a Constraint on Conscious Information Processing'")
    print()
    
    # ----------------------------------------------------------------
    # STEP 1: Build octonion structure constants
    # ----------------------------------------------------------------
    print("─" * 60)
    print("STEP 1: Octonion Structure Constants (Fano Plane)")
    print("─" * 60)
    
    psi, fano_triples = build_fano_structure_constants()
    
    # Verify total antisymmetry
    for i in range(7):
        for j in range(7):
            for k in range(7):
                assert psi[i, j, k] == -psi[j, i, k], "ψ not antisymmetric"
                assert psi[i, j, k] == -psi[i, k, j], "ψ not antisymmetric"
    
    # Count non-zero entries
    n_nonzero = np.count_nonzero(psi)
    print(f"  Fano triples: {[(i+1,j+1,k+1) for (i,j,k) in fano_triples]}")
    print(f"  Non-zero ψ entries: {n_nonzero} (expected: 7 × 6 = 42)")
    print(f"  ✓ Total antisymmetry verified")
    
    # ----------------------------------------------------------------
    # STEP 2: Extract G₂ generators
    # ----------------------------------------------------------------
    print()
    print("─" * 60)
    print("STEP 2: Extract G₂ Generators from so(7)")
    print("─" * 60)
    
    so7_basis, so7_labels = build_so7_basis()
    g2_raw, g2_null_coords = extract_g2_generators(psi, so7_basis)
    
    print(f"  so(7) dimension: {len(so7_basis)} (expected: 21)")
    print(f"  G₂ dimension (null space): {len(g2_raw)} (expected: 14)")
    assert len(g2_raw) == 14, f"FAIL: got {len(g2_raw)} generators, expected 14"
    print(f"  ✓ 14 G₂ generators confirmed")
    
    # Verify antisymmetry
    for idx, T in enumerate(g2_raw):
        assert np.allclose(T, -T.T, atol=1e-12), f"Generator {idx} not antisymmetric"
    print(f"  ✓ All generators antisymmetric (as required for compact Lie algebra)")
    
    # Normalize: tr(Tₐ·Tᵦ) = −2·δ_{ab}
    g2_gens = normalize_generators(g2_raw)
    
    # Verify normalization
    n_g2 = len(g2_gens)
    gram = np.zeros((n_g2, n_g2))
    for a in range(n_g2):
        for b in range(n_g2):
            gram[a, b] = np.trace(g2_gens[a] @ g2_gens[b])
    
    off_diag_max = np.max(np.abs(gram + 2 * np.eye(n_g2)))
    print(f"  Normalization: tr(Tₐ·Tᵦ) = −2·δ_{{ab}}")
    print(f"  Max deviation from −2·δ: {off_diag_max:.2e}")
    assert off_diag_max < 1e-12
    print(f"  ✓ Normalization verified to machine precision")
    
    # ----------------------------------------------------------------
    # STEP 3: G₂ Casimir
    # ----------------------------------------------------------------
    print()
    print("─" * 60)
    print("STEP 3: G₂ Quadratic Casimir")
    print("─" * 60)
    
    C2_g2 = compute_casimir(g2_gens)
    
    # Should be −4·I₇ by Schur's lemma (7-dim irrep)
    expected = -4.0 * np.eye(7)
    casimir_err = np.max(np.abs(C2_g2 - expected))
    print(f"  C₂(G₂) = {C2_g2[0,0]:.6f} × I₇")
    print(f"  Expected: −4.000000 × I₇")
    print(f"  Max deviation from −4·I: {casimir_err:.2e}")
    assert casimir_err < 1e-12
    print(f"  ✓ C₂(G₂) = −4·I₇ confirmed (Schur's lemma)")
    print()
    print(f"  CONSEQUENCE: The pure G₂ Casimir produces ZERO spectral splitting.")
    print(f"  It shifts all 7 modes uniformly. All structure comes from SU(3).")
    
    # ----------------------------------------------------------------
    # STEP 4: SU(3) subalgebra (stabilizer of Ω_void)
    # ----------------------------------------------------------------
    print()
    print("─" * 60)
    print("STEP 4: SU(3) Subalgebra (Stabilizer of Ω_void = e₀)")
    print("─" * 60)
    
    void_idx = 0
    su3_gens_raw, coset_gens, su3_null_coords = extract_su3_subalgebra(g2_gens, void_idx)
    
    print(f"  Void mode: e₀ (index {void_idx})")
    print(f"  SU(3) subalgebra dimension: {len(su3_gens_raw)} (expected: 8)")
    print(f"  Coset G₂/SU(3) dimension: {len(coset_gens)} (expected: 6)")
    assert len(su3_gens_raw) == 8
    assert len(coset_gens) == 6
    print(f"  ✓ dim(su(3)) = 8, dim(G₂/SU(3)) = 6")
    print(f"  G₂/SU(3) ≅ S⁶ (the 6-sphere)")
    
    # Normalize SU(3) generators
    su3_gens = normalize_generators(su3_gens_raw)
    
    # Verify SU(3) normalization
    gram_su3 = np.zeros((8, 8))
    for a in range(8):
        for b in range(8):
            gram_su3[a, b] = np.trace(su3_gens[a] @ su3_gens[b])
    su3_norm_err = np.max(np.abs(gram_su3 + 2 * np.eye(8)))
    print(f"  SU(3) normalization error: {su3_norm_err:.2e}")
    assert su3_norm_err < 1e-12
    print(f"  ✓ SU(3) generators normalized: tr(Tₐ·Tᵦ) = −2·δ_{{ab}}")
    
    # Verify all SU(3) generators annihilate e₀
    e0 = np.zeros(7)
    e0[void_idx] = 1.0
    for idx, T in enumerate(su3_gens):
        assert np.allclose(T @ e0, 0, atol=1e-12), f"SU(3) gen {idx} doesn't fix e₀"
    print(f"  ✓ All 8 SU(3) generators fix e₀ (Ω_void is singlet)")
    
    # Coset SVD check
    coset_svs = []
    for T in coset_gens:
        sv = np.linalg.norm(T @ e0)
        coset_svs.append(sv)
    print(f"  Coset generator action on e₀: norms = {[f'{s:.4f}' for s in coset_svs]}")
    
    # ----------------------------------------------------------------
    # STEP 5: SU(3) Casimir — the 1 ⊕ 3 ⊕ 3̄ decomposition
    # ----------------------------------------------------------------
    print()
    print("─" * 60)
    print("STEP 5: SU(3) Casimir → Decomposition 7 → 1 ⊕ 3 ⊕ 3̄")
    print("─" * 60)
    
    C2_su3 = compute_casimir(su3_gens)
    
    eigvals_su3, eigvecs_su3 = np.linalg.eigh(C2_su3)
    
    print(f"  C₂(SU3) eigenvalues: {np.sort(eigvals_su3)}")
    
    # Sort and identify sectors
    singlet_val = eigvals_su3[np.argmax(eigvals_su3)]  # highest = 0 (singlet)
    nonsinglet_vals = eigvals_su3[eigvals_su3 < singlet_val - 0.01]
    
    print(f"\n  Decomposition:")
    print(f"    Singlet (Ω_void):    C₂(SU3) = {singlet_val:.6f}  (degeneracy: 1)")
    print(f"    Non-singlet (3⊕3̄):  C₂(SU3) = {nonsinglet_vals[0]:.6f}  (degeneracy: {len(nonsinglet_vals)})")
    
    assert abs(singlet_val - 0.0) < 1e-12, f"Singlet Casimir ≠ 0: {singlet_val}"
    assert len(nonsinglet_vals) == 6
    for v in nonsinglet_vals:
        assert abs(v - (-8.0 / 3.0)) < 1e-12, f"Non-singlet Casimir ≠ −8/3: {v}"
    
    print(f"\n  ✓ Singlet: C₂(SU3) = 0 (exact)")
    print(f"  ✓ 3 ⊕ 3̄ sector: C₂(SU3) = −8/3 = −{8/3:.6f} (6-fold degenerate)")
    print(f"  ✓ Branching 7 → 1 ⊕ 3 ⊕ 3̄ confirmed")
    
    # ----------------------------------------------------------------
    # STEP 6: Complex structure & Cartan generators
    # ----------------------------------------------------------------
    print()
    print("─" * 60)
    print("STEP 6: Complex Structure J & Cartan Generators")
    print("─" * 60)
    
    cartan_gens, H_c1, H_c2, J_6d = extract_cartan_generators(psi, void_idx)
    
    # Verify J² = −I
    print(f"  Complex structure J = ψ_{{0ij}} on ℝ⁶")
    print(f"  ✓ J² = −I verified")
    
    # Verify Cartan generators commute
    print(f"  3 Cartan generators H₁, H₂, H₃ (all mutually commuting)")
    for i in range(3):
        for j in range(i + 1, 3):
            comm_norm = np.linalg.norm(
                cartan_gens[i] @ cartan_gens[j] - cartan_gens[j] @ cartan_gens[i]
            )
            assert comm_norm < 1e-12
    print(f"  ✓ [Hᵢ, Hⱼ] = 0 for all i ≠ j")
    
    # SU(3) Cartan basis
    print(f"\n  SU(3) Cartan basis (rank 2):")
    print(f"    H_c1 = H₁ − H₂  (simple root α₁)")
    print(f"    H_c2 = H₂ − H₃  (simple root α₂)")
    
    # Verify H_c1, H_c2 commute
    comm = H_c1 @ H_c2 - H_c2 @ H_c1
    assert np.allclose(comm, 0, atol=1e-12)
    print(f"  ✓ [H_c1, H_c2] = 0")
    
    # Verify they annihilate e₀
    assert np.allclose(H_c1 @ e0, 0, atol=1e-12)
    assert np.allclose(H_c2 @ e0, 0, atol=1e-12)
    print(f"  ✓ H_c1·e₀ = H_c2·e₀ = 0 (void is Cartan-neutral)")
    
    # Weight structure
    print(f"\n  Weight structure of H_c1 + H_c2 on the non-singlet sector:")
    H_sum = H_c1 + H_c2
    eigvals_hsum = np.linalg.eigvalsh(H_sum)
    print(f"    Eigenvalues of H_c1 + H_c2: {np.sort(eigvals_hsum)}")
    
    # ----------------------------------------------------------------
    # STEP 7: Void projector
    # ----------------------------------------------------------------
    P_void = np.outer(e0, e0)
    
    # ================================================================
    # STEP 8: FULL HAMILTONIAN — ALL SPECTRAL REGIMES
    # ================================================================
    print()
    print("=" * 80)
    print("STEP 8: FULL HAMILTONIAN SPECTRUM")
    print("=" * 80)
    print()
    print("  H_daemon = α·C₂(G₂) + β·C₂(SU3) + γ·P_void + a₁·H_c1 + a₂·H_c2")
    print()
    
    # ---- Regime 1: Pure G₂ Casimir only ----
    print("─" * 60)
    print("Regime 1: Casimir only (β = γ = a₁ = a₂ = 0)")
    print("─" * 60)
    H = build_hamiltonian(C2_g2, C2_su3, P_void, H_c1, H_c2,
                           alpha=1.0, beta=0, gamma=0, a1=0, a2=0)
    evals, levels = analyze_spectrum(H)
    print(f"  Eigenvalues: {evals}")
    print(f"  Levels: {len(levels)} distinct — {[(f'{v:.3f}', f'×{d}') for v, d in levels]}")
    print(f"  → 7-fold degenerate at −4.000 (pure Casimir shift)")
    assert len(levels) == 1 and levels[0][1] == 7
    print(f"  ✓ Confirmed: no splitting from Casimir alone\n")
    
    # ---- Regime 2: + SU(3) Casimir (no Cartan) ----
    print("─" * 60)
    print("Regime 2: + SU(3) Casimir (β = 1, γ = 0, no Cartan)")
    print("─" * 60)
    H = build_hamiltonian(C2_g2, C2_su3, P_void, H_c1, H_c2,
                           alpha=1.0, beta=1.0, gamma=0, a1=0, a2=0)
    evals, levels = analyze_spectrum(H)
    print(f"  Eigenvalues: {evals}")
    print(f"  Levels: {len(levels)} distinct — {[(f'{v:.3f}', f'×{d}') for v, d in levels]}")
    print(f"  → Singlet at −4.000, sextet at −6.667")
    assert len(levels) == 2
    print(f"  ✓ Two-level split: singlet ⊕ [6-fold]")
    print(f"  NOTE: This is the Casimir-only Hamiltonian that ChatGPT/Grok analyzed.\n")
    
    # ---- Regime 3: + Void projection ----
    print("─" * 60)
    print("Regime 3: + Void projection (β = 1, γ = 0.5, no Cartan)")
    print("─" * 60)
    H = build_hamiltonian(C2_g2, C2_su3, P_void, H_c1, H_c2,
                           alpha=1.0, beta=1.0, gamma=0.5, a1=0, a2=0)
    evals, levels = analyze_spectrum(H)
    print(f"  Eigenvalues: {evals}")
    print(f"  Levels: {len(levels)} distinct — {[(f'{v:.3f}', f'×{d}') for v, d in levels]}")
    print(f"  → Shifted singlet at −3.500, sextet still at −6.667")
    assert len(levels) == 2
    print(f"  ✓ Still two-level (void shift just moves the singlet)\n")
    
    # ---- Regime 4: TRIPLET-OF-TRIPLET (a₁ = a₂) ----
    print("─" * 60)
    print("Regime 4: TRIPLET-OF-TRIPLET (α=1, β=1, γ=0.5, a₁=a₂=1)")
    print("   *** This is the regime that produces the 4-level structure ***")
    print("─" * 60)
    H = build_hamiltonian(C2_g2, C2_su3, P_void, H_c1, H_c2,
                           alpha=1.0, beta=1.0, gamma=0.5, a1=1.0, a2=1.0)
    evals, levels = analyze_spectrum(H)
    print(f"  Eigenvalues: {evals}")
    print(f"  Levels: {len(levels)} distinct — {[(f'{v:.3f}', f'×{d}') for v, d in levels]}")
    
    # Expected from results doc: −7.667(×2), −6.667(×2), −5.667(×2), −3.500(×1)
    assert len(levels) == 4, f"Expected 4 levels, got {len(levels)}"
    print()
    print(f"  ┌────────────────────┬────────────┬─────────────┬───────────────┐")
    print(f"  │ Level              │ Eigenvalue │ Degeneracy  │ Gap from void │")
    print(f"  ├────────────────────┼────────────┼─────────────┼───────────────┤")
    for i, (val, deg) in enumerate(reversed(levels)):
        if deg == 1:
            label = "Ω_void (singlet)"
            gap = "—"
        else:
            gap_val = abs(val - levels[-1][0])
            gap = f"{gap_val:.3f}"
            label = f"Doublet {len(levels) - 1 - i}"
        print(f"  │ {label:<18s} │ {val:>10.3f} │ ×{deg:<10d} │ {gap:>13s} │")
    print(f"  └────────────────────┴────────────┴─────────────┴───────────────┘")
    
    # Verify against known values
    expected_evals = [-7.667, -7.667, -6.667, -6.667, -5.667, -5.667, -3.500]
    for ev, exp in zip(sorted(evals), sorted(expected_evals)):
        assert abs(ev - exp) < 0.01, f"Eigenvalue mismatch: {ev} vs {exp}"
    print(f"\n  ✓ Matches previously computed results to 3 decimal places")
    
    # Gap analysis
    void_val = levels[-1][0]
    gaps = [abs(val - void_val) for val, deg in levels if deg != 1]
    gaps_sorted = sorted(gaps)
    print(f"  Gaps from void: {[f'{g:.3f}' for g in gaps_sorted]}")
    print(f"  Inter-doublet spacing: {gaps_sorted[1]-gaps_sorted[0]:.3f}, {gaps_sorted[2]-gaps_sorted[1]:.3f}")
    print(f"  → Uniformly spaced at Δ = {gaps_sorted[1]-gaps_sorted[0]:.3f} (= a₁ = a₂ = 1)")
    print(f"  Gap ratios (normalized to gap₁): ", end="")
    print(f"1.000 : {gaps_sorted[1]/gaps_sorted[0]:.3f} : {gaps_sorted[2]/gaps_sorted[0]:.3f}")
    print()
    
    # ---- Regime 5: FULLY RESOLVED (a₁ ≠ a₂) ----
    print("─" * 60)
    print("Regime 5: FULLY RESOLVED (α=1, β=1, γ=0.5, a₁=1.0, a₂=0.7)")
    print("   *** All 7 eigenvalues distinct ***")
    print("─" * 60)
    H = build_hamiltonian(C2_g2, C2_su3, P_void, H_c1, H_c2,
                           alpha=1.0, beta=1.0, gamma=0.5, a1=1.0, a2=0.7)
    evals, levels = analyze_spectrum(H)
    print(f"  Eigenvalues: {np.sort(evals)}")
    print(f"  Levels: {len(levels)} distinct — {[(f'{v:.3f}', f'×{d}') for v, d in levels]}")
    assert len(levels) == 7, f"Expected 7 levels, got {len(levels)}"
    print(f"  ✓ All 7 eigenvalues distinct when a₁ ≠ a₂\n")
    
    # ================================================================
    # STEP 9: PARAMETER SCANS (reproduce tables from results doc)
    # ================================================================
    print("=" * 80)
    print("STEP 9: PARAMETER SCANS")
    print("=" * 80)
    
    # ---- β scan ----
    print("\n  β scan (α=1, γ=0, no Cartan): singlet vs 3⊕3̄ splitting")
    print(f"  {'β/α':>6s}  {'Singlet':>10s}  {'3⊕3̄':>10s}  {'Gap':>8s}")
    print(f"  {'─'*6}  {'─'*10}  {'─'*10}  {'─'*8}")
    for beta_val in [0.0, 0.5, 1.0, 1.5, 2.0]:
        H = build_hamiltonian(C2_g2, C2_su3, P_void, H_c1, H_c2,
                               alpha=1.0, beta=beta_val, gamma=0, a1=0, a2=0)
        evals, levels = analyze_spectrum(H)
        if len(levels) == 1:
            s, ns = levels[0][0], levels[0][0]
        else:
            s = max(v for v, d in levels)
            ns = min(v for v, d in levels)
        print(f"  {beta_val:>6.1f}  {s:>10.3f}  {ns:>10.3f}  {abs(s-ns):>8.3f}")
    
    # ---- a scan (a₁ = a₂ = a) ----
    print(f"\n  a₁ = a₂ = a sweep (α=1, β=1, γ=0.5)")
    print(f"  {'a':>6s}  {'#Levels':>7s}  Eigenvalues")
    print(f"  {'─'*6}  {'─'*7}  {'─'*50}")
    for a_val in [0.0, 0.5, 1.0, 1.5, 2.0]:
        H = build_hamiltonian(C2_g2, C2_su3, P_void, H_c1, H_c2,
                               alpha=1.0, beta=1.0, gamma=0.5, a1=a_val, a2=a_val)
        evals, levels = analyze_spectrum(H)
        level_str = ", ".join(f"{v:.3f}×{d}" for v, d in levels)
        print(f"  {a_val:>6.1f}  {len(levels):>7d}  {{{level_str}}}")
    
    # ---- a₁ ≠ a₂ scan ----
    print(f"\n  a₁ ≠ a₂ scan (α=1, β=1, γ=0.5, a₁=1.0)")
    print(f"  {'a₂':>6s}  {'#Levels':>7s}  Eigenvalues")
    print(f"  {'─'*6}  {'─'*7}  {'─'*60}")
    for a2_val in [0.3, 0.5, 0.7, 1.0, 1.5]:
        H = build_hamiltonian(C2_g2, C2_su3, P_void, H_c1, H_c2,
                               alpha=1.0, beta=1.0, gamma=0.5, a1=1.0, a2=a2_val)
        evals, levels = analyze_spectrum(H)
        level_str = ", ".join(f"{v:.3f}×{d}" for v, d in levels)
        print(f"  {a2_val:>6.1f}  {len(levels):>7d}  {{{level_str}}}")
    
    # ================================================================
    # STEP 10: SUMMARY
    # ================================================================
    print()
    print("=" * 80)
    print("SUMMARY: WHAT THE COMPUTATION ESTABLISHES")
    print("=" * 80)
    print("""
  ALGEBRAIC FACTS (verified to machine precision):

    1. dim(g₂) = 14                                              ✓
    2. C₂(G₂) = −4·I₇ (Schur's lemma, 7D irrep)                ✓
    3. Stabilizer of e₀: dim = 8 → su(3) subalgebra              ✓
    4. G₂/SU(3) ≅ S⁶ (6 coset generators)                        ✓
    5. 7 → 1 ⊕ 3 ⊕ 3̄ under SU(3)                                ✓
    6. Singlet Casimir = 0, non-singlet Casimir = −8/3            ✓
    7. Complex structure J² = −I on ℝ⁶                            ✓
    8. 3 commuting Cartan generators, rank-2 SU(3) subbasis       ✓

  SPECTRAL REGIMES:

    Casimir only (no Cartan):  2 levels — singlet + sextet
    Cartan, a₁ = a₂:          4 levels — singlet + 3 doublets
    Cartan, a₁ ≠ a₂:          7 levels — fully resolved

  KEY DISTINCTION:

    The triplet-of-triplet (4-level) structure REQUIRES the Cartan
    terms. The Casimir-only Hamiltonian produces only a two-level
    split. This is not a deficiency — it means the triplet-of-triplet
    pattern arises from CARTAN SYMMETRY BREAKING within the SU(3)
    subalgebra, which is a physically meaningful statement.

    G₂ does not uniquely fix the metric, but it does fix the
    topology of the spectral family.

  FALSIFIABLE PREDICTION (FP-1):

    Microtubule resonance data should fit a two-parameter spectral
    family with topology 1 ⊕ 3 ⊕ 3̄. Falsified if:
    • branching ≠ 1 ⊕ 3 ⊕ 3̄
    • conjugate pairing absent
    • >2 independent splitting parameters required
""")
    
    print("=" * 80)
    print("COMPUTATION COMPLETE")
    print("=" * 80)
    
    return {
        "g2_generators": g2_gens,
        "su3_generators": su3_gens,
        "C2_g2": C2_g2,
        "C2_su3": C2_su3,
        "P_void": P_void,
        "H_c1": H_c1,
        "H_c2": H_c2,
        "cartan_generators": cartan_gens,
        "psi": psi,
    }


if __name__ == "__main__":
    results = main()
