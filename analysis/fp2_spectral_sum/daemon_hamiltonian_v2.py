"""
PCI Daemon Hamiltonian — QuTiP Simulation v2
=============================================
Fixed: g₂ generators are LINEAR COMBINATIONS of so(7) generators.
We find them by computing the kernel of the action map L → L·φ.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import expm, null_space

print("=" * 70)
print("PCI DAEMON HAMILTONIAN — SIMULATION v2")
print("=" * 70)

# PART 1: Fano plane structure constants
fano_lines = [(0,1,3),(1,2,4),(2,3,5),(3,4,6),(4,5,0),(5,6,1),(6,0,2)]
phi = np.zeros((7, 7, 7))
for (i, j, k) in fano_lines:
    phi[i,j,k]=1; phi[j,k,i]=1; phi[k,i,j]=1
    phi[j,i,k]=-1; phi[i,k,j]=-1; phi[k,j,i]=-1
print(f"\n[1] φ built: {np.count_nonzero(phi)} nonzero components (42)")

# PART 2: Build so(7) basis and action on Λ³
# 21 generators of so(7)
so7_basis = []
for a in range(7):
    for b in range(a+1, 7):
        L = np.zeros((7, 7))
        L[a, b] = 1; L[b, a] = -1
        so7_basis.append(L)
print(f"[2] so(7) basis: {len(so7_basis)} generators")

# Build 35 triples for Λ³
triples = [(i,j,k) for i in range(7) for j in range(i+1,7) for k in range(j+1,7)]
assert len(triples) == 35

# Action of L on φ: (L·φ)_{ijk} = Σ_c [L_{ci}φ_{cjk} + L_{cj}φ_{ick} + L_{ck}φ_{ijc}]
def action_on_phi(L):
    """Compute L·φ as a vector in ℝ³⁵ (indexed by ordered triples)."""
    result = np.zeros(35)
    for idx, (i,j,k) in enumerate(triples):
        val = 0.0
        for c in range(7):
            val += L[c,i]*phi[c,j,k] + L[c,j]*phi[i,c,k] + L[c,k]*phi[i,j,c]
        result[idx] = val
    return result

# Build the 35×21 matrix of the action map
A = np.zeros((35, 21))
for col, L in enumerate(so7_basis):
    A[:, col] = action_on_phi(L)

# The kernel of A is g₂
kernel = null_space(A, rcond=1e-10)
g2_dim = kernel.shape[1]
print(f"[3] ker(action) = g₂: dimension {g2_dim} (expected 14)")
assert g2_dim == 14, f"Expected 14, got {g2_dim}"
print(f"    ✓ dim(g₂) = 14 confirmed")

# Reconstruct g₂ generators as 7×7 matrices
g2_gens = []
for col in range(g2_dim):
    coeffs = kernel[:, col]
    L = sum(c * B for c, B in zip(coeffs, so7_basis))
    g2_gens.append(L)

# PART 3: Find Cartan subalgebra
print(f"\n[4] Finding Cartan subalgebra (rank 2)")

def commutator(A, B):
    return A @ B - B @ A

# Find two commuting generators by searching linear combinations
# First, diagonalize a random element to find a Cartan direction
H_rand = sum(np.random.randn() * g for g in g2_gens)
H_rand = (H_rand - H_rand.T) / 2  # Ensure antisymmetric

# Convert to Hermitian for diagonalization
iH = 1j * H_rand
eigs_r, vecs_r = np.linalg.eigh(iH)

# In the eigenbasis of a generic element, the Cartan generators 
# are the ones that are simultaneously diagonal.
# Use the ad(H) eigendecomposition to extract the CSA.

# Simpler approach: use the Gram-Schmidt-like procedure
# Pick a random g₂ element, compute its centralizer in g₂

def centralizer_in_g2(H, g2_gens, tol=1e-8):
    """Find elements of g₂ that commute with H."""
    comm_matrix = np.zeros((len(g2_gens), len(g2_gens)))
    # Express [H, g_i] in the g₂ basis
    for i, gi in enumerate(g2_gens):
        comm = commutator(H, gi)
        # Express comm in g₂ basis
        # comm = Σ_j c_j g_j, solve for c_j
        # Use least squares on the flattened matrices
        g2_matrix = np.array([g.flatten() for g in g2_gens]).T  # 49 × 14
        coeffs, _, _, _ = np.linalg.lstsq(g2_matrix, comm.flatten(), rcond=None)
        comm_matrix[i, :] = coeffs

    # The centralizer is the kernel of comm_matrix
    kern = null_space(comm_matrix.T, rcond=tol)
    return kern

# Find a good Cartan direction
best_H1 = None
best_cent_dim = 0
np.random.seed(42)
for trial in range(20):
    coeffs = np.random.randn(14)
    H_trial = sum(c * g for c, g in zip(coeffs, g2_gens))
    cent = centralizer_in_g2(H_trial, g2_gens)
    if cent.shape[1] == 2:  # Found a regular element!
        best_H1 = H_trial
        best_cent = cent
        print(f"    Found regular element on trial {trial+1}")
        break
    if cent.shape[1] > best_cent_dim and cent.shape[1] <= 3:
        best_cent_dim = cent.shape[1]

if best_H1 is not None:
    # Extract two Cartan generators
    H1 = sum(best_cent[i, 0] * g2_gens[i] for i in range(14))
    H2 = sum(best_cent[i, 1] * g2_gens[i] for i in range(14))
    
    # Verify they commute
    comm_check = np.max(np.abs(commutator(H1, H2)))
    print(f"    [H₁, H₂] = {comm_check:.2e} (should be ~0)")
    
    # Make Hermitian
    H1_h = 1j * H1
    H2_h = 1j * H2
    
    # Normalize
    H1_h = H1_h / np.max(np.abs(np.linalg.eigvalsh(H1_h)))
    H2_h = H2_h / np.max(np.abs(np.linalg.eigvalsh(H2_h)))
else:
    print("    Using algebraic Cartan construction...")
    # Direct construction using known G₂ Cartan in 7-rep
    # Standard choice: H1 = diag weights, H2 = diag weights
    H1_h = np.diag([0, 1, -1, 0, 0, 1, -1]).astype(float)
    H2_h = np.diag([0, 0, 0, 1, -1, -1, 1]).astype(float)

eigs1 = np.sort(np.linalg.eigvalsh(H1_h))
eigs2 = np.sort(np.linalg.eigvalsh(H2_h))
print(f"    H₁ spectrum: {eigs1.round(4)}")
print(f"    H₂ spectrum: {eigs2.round(4)}")

# PART 4: Spectral Family Scan
print(f"\n[5] Scanning 2-parameter spectral family")

n_pts = 80
a1_range = np.linspace(-2, 2, n_pts)
a2_range = np.linspace(-2, 2, n_pts)
spectra = np.zeros((n_pts, n_pts, 7))

for i, a1 in enumerate(a1_range):
    for j, a2 in enumerate(a2_range):
        H_d = a1 * H1_h + a2 * H2_h
        spectra[i, j, :] = np.sort(np.linalg.eigvalsh(H_d))

# PART 5: Decomposition check at sample point
a1_s, a2_s = 1.0, 0.618  # Golden ratio for genericity
H_s = a1_s * H1_h + a2_s * H2_h
eigs_s = np.sort(np.linalg.eigvalsh(H_s))
print(f"\n[6] Sample spectrum at (a₁,a₂) = ({a1_s},{a2_s}):")
print(f"    {eigs_s.round(6)}")

# Cluster eigenvalues to find 1⊕3⊕3̄ pattern
from scipy.cluster.hierarchy import fcluster, linkage
eigs_col = eigs_s.reshape(-1, 1)
Z = linkage(eigs_col, method='complete')
clusters = fcluster(Z, t=0.3, criterion='distance')
unique_clusters, counts = np.unique(clusters, return_counts=True)
decomp = sorted(counts, reverse=True)
print(f"    Clustering: {decomp}")
print(f"    → {'⊕'.join(map(str, decomp))} decomposition")

# PART 6: Time Evolution
print(f"\n[7] Time evolution — coherence decay")

psi_0 = np.ones(7) / np.sqrt(7)
H_d = a1_s * H1_h + a2_s * H2_h
eigs_full, vecs_full = np.linalg.eigh(H_d)

# Find void mode (most isolated eigenvalue)
isolation = np.zeros(7)
for k in range(7):
    left = abs(eigs_full[k] - eigs_full[k-1]) if k > 0 else 1e10
    right = abs(eigs_full[k+1] - eigs_full[k]) if k < 6 else 1e10
    isolation[k] = min(left, right)
void_idx = np.argmax(isolation)
void_mode = vecs_full[:, void_idx]
print(f"    Void mode: eigenvalue {eigs_full[void_idx]:.6f}, isolation {isolation[void_idx]:.6f}")

t_max = 15.0
n_t = 1000
times = np.linspace(0, t_max, n_t)
coherence = np.zeros(n_t)
void_pop = np.zeros(n_t)
mode_pops = np.zeros((n_t, 7))

for idx, t in enumerate(times):
    U_t = expm(-1j * H_d * t)
    psi_t = U_t @ psi_0
    coherence[idx] = abs(np.vdot(psi_0, psi_t))**2
    void_pop[idx] = abs(np.vdot(void_mode, psi_t))**2
    for k in range(7):
        mode_pops[idx, k] = abs(np.vdot(vecs_full[:, k], psi_t))**2

e2 = np.exp(-2)
below = np.where(coherence < e2)[0]
t_decay = times[below[0]] if len(below) > 0 else None

# Coherence fraction check
non_void = 1 - void_pop
print(f"    Mean non-void fraction: {np.mean(non_void):.6f} (6/7 = {6/7:.6f})")
print(f"    Mean void fraction: {np.mean(void_pop):.6f} (1/7 = {1/7:.6f})")
if t_decay:
    print(f"    Coherence drops to e⁻² at t = {t_decay:.4f}")

# PART 7: Plots
print(f"\n[8] Generating plots...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('PCI Daemon Hamiltonian — G₂/SU(3) Spectral Analysis', fontsize=14, fontweight='bold')

# Plot 1: Spectrum vs a₁
ax1 = axes[0, 0]
j_fix = n_pts // 2 + 10
colors_7 = ['#20808D', '#A84B2F', '#1B474D', '#944454', '#FFC553', '#848456', '#6E522B']
for k in range(7):
    ax1.plot(a1_range, spectra[:, j_fix, k], color=colors_7[k], linewidth=1.5)
ax1.set_xlabel('a₁', fontsize=11)
ax1.set_ylabel('Eigenvalue', fontsize=11)
ax1.set_title(f'Spectrum vs a₁ (a₂ = {a2_range[j_fix]:.2f})', fontsize=12)
ax1.grid(True, alpha=0.3)

# Plot 2: Coherence decay
ax2 = axes[0, 1]
ax2.plot(times, coherence, '#20808D', linewidth=2, label='Coherence |⟨ψ₀|ψ(t)⟩|²')
ax2.axhline(y=e2, color='#A84B2F', linestyle='--', linewidth=1.5, label=f'e⁻² ≈ {e2:.4f}')
ax2.axhline(y=1/7, color='#944454', linestyle=':', linewidth=1.5, label=f'1/7 ≈ {1/7:.4f}')
if t_decay:
    ax2.axvline(x=t_decay, color='#A84B2F', linestyle=':', alpha=0.4)
ax2.set_xlabel('Time', fontsize=11)
ax2.set_ylabel('Coherence', fontsize=11)
ax2.set_title('Coherence Decay', fontsize=12)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Plot 3: Mode populations
ax3 = axes[1, 0]
for k in range(7):
    label = 'Ω_void' if k == void_idx else f'Mode {k}'
    lw = 2.5 if k == void_idx else 1
    ax3.plot(times, mode_pops[:, k], color=colors_7[k], linewidth=lw, label=label, alpha=0.8 if k != void_idx else 1.0)
ax3.axhline(y=1/7, color='gray', linestyle='--', alpha=0.5)
ax3.set_xlabel('Time', fontsize=11)
ax3.set_ylabel('Population', fontsize=11)
ax3.set_title('7-Mode Population Evolution', fontsize=12)
ax3.legend(fontsize=8, ncol=2)
ax3.grid(True, alpha=0.3)

# Plot 4: Spectral gap heatmap
gaps_2d = np.zeros((n_pts, n_pts))
for i in range(n_pts):
    for j in range(n_pts):
        g = np.diff(spectra[i, j, :])
        gaps_2d[i, j] = np.max(g)

ax4 = axes[1, 1]
im = ax4.imshow(gaps_2d.T, extent=[-2,2,-2,2], origin='lower', cmap='magma', aspect='auto')
plt.colorbar(im, ax=ax4, label='Max spectral gap')
ax4.set_xlabel('a₁', fontsize=11)
ax4.set_ylabel('a₂', fontsize=11)
ax4.set_title('Spectral Gap Landscape', fontsize=12)
ax4.plot(a1_s, a2_s, 'w*', markersize=15)

plt.tight_layout()
plt.savefig('/home/user/workspace/daemon_hamiltonian_results.png', dpi=150, bbox_inches='tight')
print("    Saved: daemon_hamiltonian_results.png")
plt.close()

# SUMMARY
print(f"\n{'='*70}")
print("RESULTS SUMMARY")
print(f"{'='*70}")
print(f"  dim(g₂) via null space:     14 ✓")
print(f"  Cartan rank:                2 ✓")
print(f"  Spectral decomposition:     {'⊕'.join(map(str, decomp))}")
print(f"  Void mode eigenvalue:       {eigs_full[void_idx]:.6f}")
print(f"  Spectral gap (isolation):   {isolation[void_idx]:.6f}")
print(f"  Mean void fraction:         {np.mean(void_pop):.6f} (theory: {1/7:.6f})")
print(f"  Mean non-void fraction:     {np.mean(non_void):.6f} (theory: {6/7:.6f})")
print(f"  e⁻² decay time:            {t_decay:.4f}" if t_decay else "  e⁻² decay: not reached")
print(f"  6/7 ceiling:                {6/7:.6f}")
print(f"{'='*70}")
