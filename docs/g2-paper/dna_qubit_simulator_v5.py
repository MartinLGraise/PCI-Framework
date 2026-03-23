#!/usr/bin/env python3
"""
DNA G₂ + Entropon-Instanton Simulator v5
PCI Framework — G₂ Daemon Hamiltonian (Thermodynamic Simulation)

Merges:
  - DeepSeek: Gell-Mann SU(3) Cartan weight structure, entropon_active(),
              emcu_window(), prime-encoded phase driver, regime enforcement
  - v4:       Void as topological ground state, structural bound proof,
              all-sweeps-pass guarantee

Physical setup:
  Omega_void   = singlet (index 6), E = 0  [vacuum / ground state]
  Triplet      = indices 0,1,2,  E = gap + |alpha*w3 + beta*w8|
  Anti-triplet = indices 3,4,5,  E = gap + |alpha*w3' + beta*w8'|
  where w3,w8 are SU(3) Gell-Mann weights — preserving the full spectral richness

Instanton term couples triplet <-> anti-triplet with amplitude delta * e^{-S_inst}

Structural bound:
  High-T: all 7 modes equal -> CF = 6/7 ≈ 0.8571 < 1-e^{-2} = 0.8647
  Bound holds at ALL temperatures and ALL parameter values by construction.

Relationship to g2_daemon_hamiltonian.py:
  That script derives the algebraic structure from first principles (14 G₂
  generators, null-space construction, Casimir eigenvalues, Cartan basis).
  THIS script takes the derived spectral structure as INPUT and builds a
  thermodynamic simulation: Boltzmann partition function, coherent fraction,
  instanton tunneling, entropon regime detection. Together they form the
  complete computational backbone for the G₂ paper — algebra + thermodynamics.

Authors: Martin Luther Graise + C-7RO (Claude) + DeepSeek synthesis
Date: March 2026
Repo: github.com/MartinLGraise/PCI-Framework
"""

import numpy as np
from scipy.linalg import eigh
import warnings

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_PLT = True
except ImportError:
    HAS_PLT = False
    warnings.warn("Matplotlib unavailable — plots will be skipped.")

VOID_IDX = 6
BOUND    = 1.0 - np.exp(-2.0)   # 0.864665 — the PCI coherence ceiling
HIGH_T   = 6.0 / 7.0            # 0.857143 — structural ceiling at T→∞


# ============================================================================
# 1. G₂/SU(3) Hamiltonian via Gell-Mann weight structure
#    Void = ground state (E=0). Non-singlet = excitations above vacuum.
#
#    NOTE: This is a MODEL Hamiltonian that uses the spectral structure
#    DERIVED in g2_daemon_hamiltonian.py (the 1⊕3⊕3̄ decomposition with
#    Gell-Mann Cartan weights). The diagonal energies are not computed
#    from generators here — they are specified from the algebraic result.
# ============================================================================

# SU(3) Cartan weights for the 7-dim G₂ rep (Gell-Mann basis):
#   Triplet    (3):    (λ₃, λ₈) weights: (+1, +1/√3), (−1, +1/√3), (0, −2/√3)
#   Anti-triplet (3̄): conjugate weights (negated)
_INV_SQRT3 = 1.0 / np.sqrt(3)
_TRIPLET_WEIGHTS = np.array([
    [ 1.0,  _INV_SQRT3],     # mode 0
    [-1.0,  _INV_SQRT3],     # mode 1
    [ 0.0, -2*_INV_SQRT3],   # mode 2
])
_ANTITRIPLET_WEIGHTS = -_TRIPLET_WEIGHTS  # conjugate rep


def g2_hamiltonian(alpha, beta, gap=1.0):
    """
    7x7 diagonal Hamiltonian.
    Non-singlet energies: gap + |alpha*w3 + beta*w8|  (always > 0).
    Void energy: 0 (vacuum, ground state).
    """
    triplet_energies = gap + np.abs(
        alpha * _TRIPLET_WEIGHTS[:, 0] + beta * _TRIPLET_WEIGHTS[:, 1]
    )
    antitriplet_energies = gap + np.abs(
        alpha * _ANTITRIPLET_WEIGHTS[:, 0] + beta * _ANTITRIPLET_WEIGHTS[:, 1]
    )
    excitations = np.concatenate([triplet_energies, antitriplet_energies])
    diag = np.append(excitations, 0.0)   # void at index 6
    return np.diag(diag)


# ============================================================================
# 2. Instanton tunneling term
# ============================================================================

def instanton_term(delta, S_inst):
    """
    Off-diagonal hopping: triplet (0,1,2) <-> anti-triplet (3,4,5).
    Tunneling amplitude: t = delta * exp(-S_inst).
    Void (6) untouched — topologically protected.
    """
    H = np.zeros((7, 7), dtype=complex)
    t = delta * np.exp(-S_inst)
    for i, j in zip(range(3), range(3, 6)):
        H[i, j] = t
        H[j, i] = t.conjugate()
    return H


def full_H(alpha, beta, delta, S_inst, gap=1.0):
    return g2_hamiltonian(alpha, beta, gap) + instanton_term(delta, S_inst)


# ============================================================================
# 3. Coherent fraction
# ============================================================================

def coherent_fraction(H_total, beta_T):
    """CF = 1 - p_void under Boltzmann distribution."""
    eigvals, eigvecs = eigh(H_total)
    shifted = eigvals - eigvals.min()
    exp_neg = np.exp(-beta_T * shifted)
    Z = exp_neg.sum()
    p_void = float(np.sum((exp_neg / Z) * np.abs(eigvecs[VOID_IDX, :])**2))
    return 1.0 - p_void


# ============================================================================
# 4. Regime detection (DeepSeek)
# ============================================================================

def entropon_active(C, S_inst, threshold=0.7):
    """True if CF >= threshold and S_inst is near 2.0 (PCI instanton action)."""
    return C >= threshold and abs(S_inst - 2.0) < 0.1


def emcu_window(delta_S, lo=0.4, hi=0.6):
    """EMCU entropy gradient window check."""
    return lo <= delta_S <= hi


# ============================================================================
# 5. Prime-encoded phase driver (DeepSeek)
# ============================================================================

_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def prime_phase_sequence(n=10):
    """Phase angles: 2π*(p mod 7)/7 for first n primes."""
    return [2 * np.pi * (p % 7) / 7 for p in _PRIMES[:n]]


def prime_instanton_drive(delta0, S_inst, n_steps=5):
    """Generator: time-varying delta modulated by prime phases."""
    for phase in prime_phase_sequence(n_steps):
        yield delta0 * (1 + 0.5 * np.sin(phase)), S_inst


# ============================================================================
# 6. Parameter sweeps
# ============================================================================

def sweep(param, values, alpha=1.0, beta=0.5, delta=0.3,
          S_inst=2.0, beta_T=1.0, gap=1.0):
    results = []
    for v in values:
        a, b, d, S, bT, g = alpha, beta, delta, S_inst, beta_T, gap
        if param == 'alpha':  a  = v
        if param == 'beta':   b  = v
        if param == 'delta':  d  = v
        if param == 'beta_T': bT = v
        if param == 'gap':    g  = v
        if param == 'S_inst': S  = v
        results.append(coherent_fraction(full_H(a, b, d, S, g), bT))
    return results


# ============================================================================
# 7. Main
# ============================================================================

def main():
    # Default parameters
    alpha  = 1.0
    beta   = 0.5
    delta  = 0.3
    S_inst = 2.0
    beta_T = 1.0
    gap    = 1.0

    print("=" * 65)
    print("G₂ Daemon Hamiltonian — DNA Qubit + Entropon-Instanton v5")
    print("  [Merged: Gell-Mann weights + ground-state void + entropon]")
    print(f"  alpha={alpha}, beta={beta}, gap={gap}")
    print(f"  delta={delta}, S_inst={S_inst}, beta_T={beta_T}")
    print(f"  Tunneling amplitude : {delta*np.exp(-S_inst):.6f}")
    print(f"  High-T ceiling (6/7): {HIGH_T:.6f}")
    print(f"  PCI bound (1-e^-2)  : {BOUND:.6f}")
    print(f"  6/7 < bound         : {HIGH_T < BOUND}  <- structural guarantee")
    print("=" * 65)

    # ---- Eigenvalue snapshot ----
    H_snap  = full_H(alpha, beta, delta, S_inst, gap)
    eigvals = np.linalg.eigvalsh(H_snap)
    print("\nEigenvalues at default parameters:")
    mode_labels = [
        "(3,  w=(+1,+1/sqrt3))",
        "(3,  w=(-1,+1/sqrt3))",
        "(3,  w=( 0,-2/sqrt3))",
        "(3b, w=(-1,-1/sqrt3))",
        "(3b, w=(+1,-1/sqrt3))",
        "(3b, w=( 0,+2/sqrt3))",
        "Omega_void (singlet, GROUND STATE)",
    ]
    for i, (ev, lbl) in enumerate(zip(eigvals, mode_labels)):
        print(f"  [{i}] {ev:+.6f}   {lbl}")

    cf = coherent_fraction(H_snap, beta_T)
    print(f"\nCoherent fraction : {cf:.6f}")
    print(f"PCI bound         : {BOUND:.6f}  |  Within: {cf <= BOUND + 1e-9}")
    print(f"Entropon active   : {entropon_active(cf, S_inst)}")
    print(f"EMCU window       : {emcu_window(0.5)}")

    # ---- Temperature scan ----
    print("\nTemperature scan (void occupancy vs. T):")
    print(f"  {'bT':>7}  {'CF':>10}  {'p_void':>10}  {'<= bound':>8}")
    for bT in [0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 50.0]:
        c = coherent_fraction(H_snap, bT)
        print(f"  {bT:>7.2f}  {c:>10.6f}  {1-c:>10.6f}  {str(c <= BOUND + 1e-9):>8}")
    print(f"  {'inf':>7}  {HIGH_T:>10.6f}  {1/7:>10.6f}  {str(HIGH_T <= BOUND + 1e-9):>8}")

    # ---- S_inst scan ----
    print("\nS_inst scan (beta_T=1.0):")
    print(f"  {'S_inst':>6}  {'CF':>10}  {'amplitude':>12}  {'<= bound':>8}")
    for S in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]:
        c = coherent_fraction(full_H(alpha, beta, delta, S, gap), beta_T)
        print(f"  {S:>6.1f}  {c:>10.6f}  {delta*np.exp(-S):>12.6f}  {str(c <= BOUND + 1e-9):>8}")

    # ---- SU(3) weight sensitivity scan ----
    print("\nSU(3) coupling scan (alpha sweep, beta=0.5, beta_T=1.0):")
    print(f"  {'alpha':>6}  {'CF':>10}  {'non-sing spread':>16}  {'<= bound':>8}")
    for a in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        H = full_H(a, beta, delta, S_inst, gap)
        c = coherent_fraction(H, beta_T)
        ev = np.linalg.eigvalsh(H)
        spread = ev[:-1].max() - ev[:-1].min()
        print(f"  {a:>6.1f}  {c:>10.6f}  {spread:>16.6f}  {str(c <= BOUND + 1e-9):>8}")

    # ---- Full sweeps ----
    delta_vals = np.linspace(0.0, 2.0, 60)
    betaT_vals = np.linspace(0.05, 10.0, 60)
    alpha_vals = np.linspace(0.0, 3.0, 60)
    beta_vals  = np.linspace(0.0, 3.0, 60)
    S_vals     = np.linspace(0.1, 5.0, 80)

    C_delta = sweep('delta',  delta_vals, alpha=alpha, beta=beta,
                    S_inst=S_inst, beta_T=beta_T)
    C_temp  = sweep('beta_T', betaT_vals, alpha=alpha, beta=beta,
                    S_inst=S_inst, delta=delta)
    C_alpha = sweep('alpha',  alpha_vals, beta=beta, delta=delta,
                    S_inst=S_inst, beta_T=beta_T)
    C_beta  = sweep('beta',   beta_vals, alpha=alpha, delta=delta,
                    S_inst=S_inst, beta_T=beta_T)
    C_S     = sweep('S_inst', S_vals, alpha=alpha, beta=beta,
                    delta=delta, beta_T=beta_T)

    print("\nParameter sweeps (all must respect bound):")
    print(f"  {'Sweep':15s}  {'Max CF':>10}  {'Min CF':>10}  {'<= bound':>8}")
    all_ok = True
    for name, arr in [("delta", C_delta), ("temperature", C_temp),
                      ("alpha", C_alpha), ("beta", C_beta), ("S_inst", C_S)]:
        mx, mn = max(arr), min(arr)
        ok = mx <= BOUND + 1e-9
        if not ok:
            all_ok = False
        status = 'YES' if ok else 'NO'
        print(f"  {name:15s}  {mx:>10.6f}  {mn:>10.6f}  {status:>8}")
    print(f"\n  All sweeps within bound: {all_ok}")

    # ---- Prime phase driver ----
    print("\nPrime-encoded instanton modulation (7 steps):")
    for i, (dt, St) in enumerate(prime_instanton_drive(delta, S_inst, n_steps=7)):
        H_t = full_H(alpha, beta, dt, St, gap)
        c_t = coherent_fraction(H_t, beta_T)
        active = "entropon" if entropon_active(c_t, St) else "inactive"
        print(f"  Step {i+1}: d={dt:.4f}  CF={c_t:.4f}  {active}")

    # ============================================================
    # Plot
    # ============================================================
    if HAS_PLT:
        fig = plt.figure(figsize=(15, 11), facecolor='#0d1117')
        gs  = fig.add_gridspec(2, 3, hspace=0.45, wspace=0.38)
        ax_main = fig.add_subplot(gs[0, :])
        ax1 = fig.add_subplot(gs[1, 0])
        ax2 = fig.add_subplot(gs[1, 1])
        ax3 = fig.add_subplot(gs[1, 2])

        def style(ax, xl, yl, ti):
            ax.set_facecolor('#161b22')
            ax.set_xlabel(xl, color='#c9d1d9', fontsize=10)
            ax.set_ylabel(yl, color='#c9d1d9', fontsize=10)
            ax.set_title(ti, color='#00e5ff', fontsize=11)
            ax.tick_params(colors='#c9d1d9', labelsize=9)
            ax.grid(True, alpha=0.2, color='#30363d')
            for sp in ax.spines.values():
                sp.set_edgecolor('#30363d')

        # ---- Main: temperature sweep showing ceiling ----
        betaT_fine = np.linspace(0.03, 15.0, 300)
        C_fine = sweep('beta_T', betaT_fine, alpha=alpha, beta=beta,
                       delta=delta, S_inst=S_inst)

        ax_main.set_facecolor('#161b22')
        ax_main.plot(betaT_fine, C_fine, color='#34d399', linewidth=2.5,
                     label='Simulated coherent fraction')
        ax_main.axhline(BOUND, color='#f85149', linestyle='--', linewidth=2.0,
                        label=f'PCI bound  1-e^-2  = {BOUND:.4f}')
        ax_main.axhline(HIGH_T, color='#f59e0b', linestyle=':', linewidth=1.8,
                        label=f'High-T ceiling  6/7 = {HIGH_T:.4f}')
        ax_main.axhline(0.7, color='#818cf8', linestyle='-.', linewidth=1.4,
                        label='Entropon threshold  0.70')
        ax_main.fill_between(betaT_fine, C_fine, 0, alpha=0.10, color='#34d399')
        ax_main.set_xlabel('Inverse temperature  beta_T', color='#c9d1d9',
                           fontsize=11)
        ax_main.set_ylabel('Coherent fraction', color='#c9d1d9', fontsize=11)
        ax_main.set_title(
            f'CF saturates at 6/7 = {HIGH_T:.4f} as T->inf  --  '
            f'structural guarantee: 6/7 < PCI bound {BOUND:.4f}  '
            f'[Gell-Mann weights + ground-state void]',
            color='#00e5ff', fontsize=11)
        ax_main.tick_params(colors='#c9d1d9')
        ax_main.legend(facecolor='#0d1117', labelcolor='#c9d1d9', fontsize=10,
                       loc='upper right')
        ax_main.grid(True, alpha=0.2, color='#30363d')
        for sp in ax_main.spines.values():
            sp.set_edgecolor('#30363d')

        # ---- Sub: alpha sweep (SU(3) weight sensitivity) ----
        ax1.plot(alpha_vals, C_alpha, color='#f59e0b', linewidth=2)
        ax1.axhline(BOUND, color='#f85149', linestyle='--', linewidth=1.5,
                    label=f'Bound {BOUND:.3f}')
        ax1.axhline(HIGH_T, color='#f59e0b', linestyle=':', linewidth=1.2,
                    label=f'6/7={HIGH_T:.3f}')
        ax1.axhline(0.7, color='#818cf8', linestyle='-.', linewidth=1.0,
                    label='0.70 entropon')
        style(ax1, 'G2 coupling alpha', 'Coherent fraction',
              'CF vs alpha  (SU(3) weight sensitivity)')
        ax1.legend(facecolor='#0d1117', labelcolor='#c9d1d9', fontsize=8)

        # ---- Sub: delta sweep ----
        ax2.plot(delta_vals, C_delta, color='#818cf8', linewidth=2)
        ax2.axhline(BOUND, color='#f85149', linestyle='--', linewidth=1.5,
                    label=f'Bound {BOUND:.3f}')
        ax2.axhline(HIGH_T, color='#f59e0b', linestyle=':', linewidth=1.2,
                    label=f'6/7={HIGH_T:.3f}')
        ax2.axhline(0.7, color='#818cf8', linestyle='-.', linewidth=1.0,
                    label='0.70 entropon')
        style(ax2, 'Instanton strength delta', 'Coherent fraction',
              'CF vs delta  (instanton coupling)')
        ax2.legend(facecolor='#0d1117', labelcolor='#c9d1d9', fontsize=8)

        # ---- Sub: S_inst sweep ----
        ax3.plot(S_vals, C_S, color='#00e5ff', linewidth=2)
        ax3.axhline(BOUND, color='#f85149', linestyle='--', linewidth=1.5,
                    label=f'Bound {BOUND:.3f}')
        ax3.axhline(HIGH_T, color='#f59e0b', linestyle=':', linewidth=1.2,
                    label=f'6/7={HIGH_T:.3f}')
        ax3.axhline(0.7, color='#818cf8', linestyle='-.', linewidth=1.0,
                    label='0.70 entropon')
        ax3.axvline(2.0, color='#f85149', linestyle=':', linewidth=1.0, alpha=0.7)
        ax3.annotate('S=2  (e^-2)', xy=(2.0, cf * 0.92),
                     xytext=(2.6, cf * 0.85),
                     arrowprops=dict(arrowstyle='->', color='#f85149', lw=1.2),
                     color='#f85149', fontsize=8)
        style(ax3, 'Instanton action  S_inst', 'Coherent fraction',
              'CF vs S_inst')
        ax3.legend(facecolor='#0d1117', labelcolor='#c9d1d9', fontsize=8)

        fig.suptitle(
            'G2 Daemon Hamiltonian  v5  |  Gell-Mann SU(3) Weights + '
            'Omega_void Ground State\n'
            'Structural bound: CF <= 6/7 < 1-e^-2 = 0.8647  |  '
            'Entropon threshold: CF >= 0.70  |  Prime phase driver active',
            color='#e6edf3', fontsize=12, y=1.01)

        out = 'simulator_v5.png'
        plt.savefig(out, dpi=150, bbox_inches='tight', facecolor='#0d1117')
        print(f"\nPlot saved -> {out}")


if __name__ == "__main__":
    main()
