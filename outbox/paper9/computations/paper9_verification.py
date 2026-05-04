"""
Paper 9 Numerical Verification -- Dyadic Coherence
PCI/PME Framework | MartinLGraise/PCI-Framework
Branch: paper7-foundation | Commit: 0b1fef1
Executed by: Phi | Date: 2026-05-04

Spec source: Prompt spec (raw.githubusercontent.com blocked at network layer;
             fallback per instructions).

Tasks
-----
  Task 1  Theorem 9.1    Contraction rate bound
  Task 2  Theorem 9.2    Coherence ceiling
  Task 3  Conjecture 9.3 Severance threshold / basin bifurcation
"""

import numpy as np
from numpy.linalg import norm, svd as np_svd
import json


# =====================================================================
# Shared construction helpers
# =====================================================================

def make_contraction(r, seed=42):
    """
    G2-equivariant contraction on V_7.

    Returns r * Q where Q is a 7x7 proper orthogonal matrix built
    via QR decomposition of a seeded normal draw.
    """
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((7, 7)))
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1          # ensure det(Q) = +1
    return r * Q


def coupling_map(rho):
    """
    Psi: R^14 -> R^14 with coherence parameter rho in [0, 1).

    Block form:  Psi = [[ alpha*I7,  rho*I7 ],
                        [   rho*I7, alpha*I7 ]]    alpha = sqrt(1-rho^2)

    Singular values: (alpha+rho)  [symmetric mode, > 1 for rho > 0]
                     (alpha-rho)  [antisymmetric mode]

    IMPORTANT: Psi is NOT a norm contraction -- its operator norm
    sigma_max = alpha+rho = sqrt(1-rho^2)+rho >= 1 for all rho in [0,1).
    This has direct consequences for Theorem 9.1 (Task 1).
    """
    alpha = np.sqrt(1.0 - rho**2)
    I     = np.eye(7)
    return np.block([[alpha * I, rho   * I],
                     [rho   * I, alpha * I]])


def make_T_AB(r_A, r_B, rho, seed=42):
    """
    T_AB = diag(T_A, T_B) @ Psi  on R^14.

    T_A uses seed, T_B uses seed+1 for independent orthogonal bases.
    """
    T_A    = make_contraction(r_A, seed=seed)
    T_B    = make_contraction(r_B, seed=seed + 1)
    T_diag = np.block([[T_A,              np.zeros((7, 7))],
                       [np.zeros((7, 7)), T_B            ]])
    return T_diag @ coupling_map(rho)


def operator_norm(M):
    """Operator norm = largest singular value."""
    return np_svd(M, compute_uv=False)[0]


def exact_r_AB_analytic(r_A, r_B, rho):
    """
    Exact r_AB from block-eigenvalue analysis of T_AB^T T_AB.

    T_AB^T T_AB decomposes into 7 copies of the 2x2 matrix:
      M = [[ a2*rA2+p2*rB2,  ap*(rA2+rB2) ],
           [  ap*(rA2+rB2), p2*rA2+a2*rB2 ]]
    where a2=alpha^2, p2=rho^2, ap=alpha*rho.

    trace(M) = rA2+rB2
    det(M)   = (a2-p2)^2 * rA2 * rB2

    lambda_max = [(rA2+rB2) + sqrt((rA2+rB2)^2 - 4*(a2-p2)^2*rA2*rB2)] / 2
    r_AB = sqrt(lambda_max)

    Symmetric case (r_A=r_B=r):  r_AB = r*(alpha+rho)  [exact]
    """
    a2  = 1.0 - rho**2
    p2  = rho**2
    rA2 = r_A**2
    rB2 = r_B**2
    tr  = rA2 + rB2
    disc = tr**2 - 4.0 * (a2 - p2)**2 * rA2 * rB2
    return np.sqrt((tr + np.sqrt(max(disc, 0.0))) / 2.0)


# =====================================================================
# TASK 1 -- Theorem 9.1: Contraction Rate Bound
# =====================================================================

def task1(verbose=True):
    """
    Verify: r_AB <= sqrt(alpha^2 * max(r_A,r_B)^2 + rho^2 * min(r_A,r_B)^2)

    Tests 4 r-pairs x 6 rho values = 24 configurations.
    Returns list of result dicts.
    """
    R_PAIRS  = [(0.6, 0.6), (0.857, 0.857), (0.3, 0.857), (0.5, 0.857)]
    RHO_VALS = [0.1, 0.3, 0.5, 0.707, 0.9, 0.99]
    TOL      = 1e-10   # numerical tolerance

    if verbose:
        print("=" * 72)
        print("TASK 1 -- Theorem 9.1: Contraction Rate Bound")
        print("  Claim: r_AB <= sqrt(a^2 max(r_A,r_B)^2 + rho^2 min(r_A,r_B)^2)")
        print("         where a = sqrt(1-rho^2)")
        print("=" * 72)
        print(f"{'r_A':>6} {'r_B':>6} {'rho':>6} |"
              f" {'r_AB':>10} {'bound':>10} {'ratio':>8} | result")
        print("-" * 72)

    rows   = []
    n_pass = 0
    n_fail = 0

    for r_A, r_B in R_PAIRS:
        for rho in RHO_VALS:
            alpha = np.sqrt(1.0 - rho**2)
            T_AB  = make_T_AB(r_A, r_B, rho)
            r_AB  = operator_norm(T_AB)
            bound = np.sqrt(alpha**2 * max(r_A, r_B)**2
                            + rho**2  * min(r_A, r_B)**2)
            ratio  = r_AB / bound if bound > 0 else float('inf')
            passed = (r_AB <= bound + TOL)
            label  = "PASS" if passed else "FAIL"
            if passed:
                n_pass += 1
            else:
                n_fail += 1

            rows.append(dict(r_A=r_A, r_B=r_B, rho=rho,
                             r_AB=r_AB, bound=bound, ratio=ratio,
                             result=label))

            if verbose:
                flag = "" if passed else " <- FAIL"
                print(f"{r_A:>6.3f} {r_B:>6.3f} {rho:>6.3f} |"
                      f" {r_AB:>10.7f} {bound:>10.7f} {ratio:>8.6f} | {label}{flag}")

    if verbose:
        print("-" * 72)
        print(f"  Summary: {n_pass} PASS, {n_fail} FAIL  ({len(rows)} configurations)")
        print()
        print("  ANALYTICAL DIAGNOSIS (symmetric case r_A = r_B = r):")
        print("    Exact:  r_AB = r*(alpha+rho)    [from block eigenvalue formula]")
        print("    Bound:  r*sqrt(alpha^2+rho^2) = r   [since alpha^2+rho^2 = 1]")
        print("    (alpha+rho)^2 = 1 + 2*alpha*rho >= 1  =>  r_AB >= bound for all rho>0")
        print("    Root cause: coupling map Psi has operator norm = alpha+rho > 1,")
        print("    amplifying the symmetric mode -- not accounted for in the bound.")
        print()

    return rows


# =====================================================================
# TASK 2 -- Theorem 9.2: Coherence Ceiling
# =====================================================================

def C_predicted(rho):
    """Claimed coherence ceiling: 6/7 + (1/7) * rho^2 / (1 + rho^2)."""
    return 6.0/7.0 + (1.0/7.0) * rho**2 / (1.0 + rho**2)


def coherence_from_dominant_mode(T_AB):
    """
    Fraction of the leading right singular vector of T_AB in the
    accessible subspace (complement of u_inacc).

    Inaccessible direction: u_inacc = ones(14)/sqrt(14)
      (symmetric eigenvector of Psi, eigenvalue = alpha+rho).

    For a linear contraction T_AB with ||T_AB|| < 1, the Banach fixed
    point is 0. Power iteration converges in *direction* to the leading
    right singular vector v_1. Coherence = 1 - |v_1 . u_inacc|^2.
    """
    _, _, Vt    = np.linalg.svd(T_AB)
    v1          = Vt[0]
    u_inacc     = np.ones(14) / np.sqrt(14.0)
    proj_sq     = np.dot(v1, u_inacc)**2   # v1 is unit vector
    return 1.0 - proj_sq                   # accessible fraction


def task2(task1_rows, verbose=True):
    """
    Measure C_meas (dominant mode coherence) vs C_pred for 24 configurations.
    Skips configurations where r_AB >= 1.
    """
    r_AB_lut = {(r['r_A'], r['r_B'], r['rho']): r['r_AB'] for r in task1_rows}

    R_PAIRS  = [(0.6, 0.6), (0.857, 0.857), (0.3, 0.857), (0.5, 0.857)]
    RHO_VALS = [0.1, 0.3, 0.5, 0.707, 0.9, 0.99]

    if verbose:
        print("=" * 72)
        print("TASK 2 -- Theorem 9.2: Coherence Ceiling")
        print("  Claim: C_AB^max(rho) = 6/7 + (1/7)*rho^2/(1+rho^2)")
        print("  Method: coherence of leading right singular vector (exact SVD)")
        print("=" * 72)
        print(f"{'r_A':>6} {'r_B':>6} {'rho':>6} |"
              f" {'r_AB':>8} {'C_meas':>10} {'C_pred':>10} {'|resid|':>10} | note")
        print("-" * 76)

    rows2      = []
    n_meas     = 0
    n_skipped  = 0

    for r_A, r_B in R_PAIRS:
        for rho in RHO_VALS:
            r_AB = r_AB_lut.get((r_A, r_B, rho))

            if r_AB is not None and r_AB >= 1.0:
                note = "SKIP r_AB>=1"
                if verbose:
                    print(f"{r_A:>6.3f} {r_B:>6.3f} {rho:>6.3f} |"
                          f" {r_AB:>8.5f} {'---':>10} {'---':>10} {'---':>10} | {note}")
                rows2.append(dict(r_A=r_A, r_B=r_B, rho=rho, r_AB=r_AB,
                                  C_meas=None, C_pred=None, residual=None,
                                  note=note))
                n_skipped += 1
                continue

            T_AB  = make_T_AB(r_A, r_B, rho)
            C_m   = coherence_from_dominant_mode(T_AB)
            C_p   = C_predicted(rho)
            resid = abs(C_m - C_p)
            note  = "ok"
            n_meas += 1

            if verbose:
                print(f"{r_A:>6.3f} {r_B:>6.3f} {rho:>6.3f} |"
                      f" {r_AB:>8.5f} {C_m:>10.6f} {C_p:>10.6f} {resid:>10.6f} | {note}")

            rows2.append(dict(r_A=r_A, r_B=r_B, rho=rho, r_AB=r_AB,
                              C_meas=C_m, C_pred=C_p, residual=resid, note=note))

    if verbose:
        resids = [r['residual'] for r in rows2 if r['residual'] is not None]
        print("-" * 76)
        print(f"  Summary: {n_meas} measured, {n_skipped} skipped (r_AB>=1)")
        if resids:
            print(f"  Residual range:    {min(resids):.6f} -- {max(resids):.6f}")
            print(f"  Median residual:   {np.median(resids):.6f}")
            n_ok = sum(1 for r in resids if r < 0.05)
            print(f"  Within 5% target:  {n_ok}/{len(resids)}")
        print()
        print("  ANALYTICAL DIAGNOSIS (symmetric case):")
        print("    T_AB^T T_AB has a 7-dimensional degenerate eigenspace at lambda_max.")
        print("    Dominant right singular vector direction is initialization-dependent.")
        print("    Formula 6/7+(1/7)rho^2/(1+rho^2) is not confirmed within spec.")
        print()

    return rows2


# =====================================================================
# TASK 3 -- Conjecture 9.3: Severance Threshold
# =====================================================================

def contractivity_boundary(r):
    """
    Solve r*(sqrt(1-rho^2)+rho) = 1 for rho.
    Returns (rho_lower, rho_upper) bounding the non-contractive window,
    or (None, None) if map is always contractive.

    Algebraic reduction: 2r^2*rho^2 - 2r*rho + (1-r^2) = 0
    """
    disc = (2*r)**2 - 4 * (2*r**2) * (1 - r**2)
    if disc < 0:
        return None, None
    sqrt_disc = np.sqrt(disc)
    a = 2 * r**2
    rho_lo = (2*r - sqrt_disc) / (2*a)
    rho_hi = (2*r + sqrt_disc) / (2*a)
    return rho_lo, rho_hi


def detect_basins(r_A, r_B, rho, n_starts=30, max_iter=5000, tol=1e-10):
    """
    Run T_AB from n_starts random initial conditions.
    Cluster converged points to count distinct basins.
    Returns (n_clusters, fixed_points) or (None, []) if non-contractive.
    """
    T_AB = make_T_AB(r_A, r_B, rho)
    if operator_norm(T_AB) >= 1.0:
        return None, []

    fixed_points = []
    for seed in range(n_starts):
        rng = np.random.default_rng(seed * 1000 + 7)
        x   = rng.standard_normal(14)
        x   = x / norm(x)
        for _ in range(max_iter):
            x_new = T_AB @ x
            if norm(x_new - x) < tol:
                break
            x = x_new
        fixed_points.append(x)

    clusters = []
    for fp in fixed_points:
        if not any(norm(fp - c) < 1e-5 for c in clusters):
            clusters.append(fp.copy())

    return len(clusters), fixed_points


def task3(verbose=True):
    """
    Sweep rho in [0, 0.8] at 200 points for r_A = r_B = 0.857.
    Detect basin bifurcation at rho_c = 1/sqrt(6).
    """
    r_A = r_B = 0.857
    N_RHO      = 200
    rho_sweep  = np.linspace(0.0, 0.8, N_RHO)
    rho_c_pred = 1.0 / np.sqrt(6.0)

    if verbose:
        print("=" * 72)
        print("TASK 3 -- Conjecture 9.3: Severance Threshold")
        print(f"  Claim: bifurcation at rho_c = 1/sqrt(6) = {rho_c_pred:.6f}")
        print(f"  Configuration: r_A = r_B = {r_A}")
        print("=" * 72)

        rho_lo, rho_hi = contractivity_boundary(r_A)
        if rho_lo is not None:
            print(f"  Contractivity boundary: r_AB=1 at rho = {rho_lo:.6f} and {rho_hi:.6f}")
            print(f"  Map is NON-contractive for rho in [{rho_lo:.6f}, {rho_hi:.6f}]")
            print(f"  Predicted rho_c = {rho_c_pred:.6f} lies INSIDE this window.")
        print()
        print(f"  Sweeping {N_RHO} points in [0, 0.8] ...")

    data           = []
    transition_rho = None
    prev_n         = None

    for rho in rho_sweep:
        n_basins, _ = detect_basins(r_A, r_B, rho)
        entry       = (float(rho), n_basins if n_basins is not None else -1)
        data.append(entry)

        if (prev_n is not None and prev_n > 1
                and n_basins is not None and n_basins == 1
                and transition_rho is None):
            transition_rho = rho
        prev_n = n_basins

    if verbose:
        print()
        print(f"  {'rho':>7}  n_basins  note")
        print(f"  {'---':>7}  --------  ----")
        for i, (rho, nb) in enumerate(data):
            near = abs(rho - rho_c_pred) < 0.025
            if i % 10 == 0 or near:
                nb_s = str(nb) if nb >= 0 else "skip"
                ann  = "<-- near rho_c" if near else ""
                print(f"  {rho:>7.4f}  {nb_s:<8}  {ann}")
        print()
        print(f"  rho_c (predicted)  = 1/sqrt(6) = {rho_c_pred:.6f}")
        if transition_rho is not None:
            res = abs(transition_rho - rho_c_pred)
            print(f"  rho_c (numerical)  = {transition_rho:.6f}")
            print(f"  |residual|         = {res:.6f}")
        else:
            print("  rho_c (numerical)  = NOT DETECTED in [0, 0.8]")
            print()
            print("  Reasons (two independent issues):")
            print("  1. A linear contraction has a UNIQUE fixed point (Banach).")
            print("     Basin bifurcation (2->1 basins) requires a nonlinear map.")
            print("  2. Predicted rho_c falls inside the non-contractive window;")
            print("     Banach does not apply there, and iteration diverges.")
        print()

    return data, transition_rho, rho_c_pred


# =====================================================================
# Main
# =====================================================================

def main():
    print()
    print("+" + "="*70 + "+")
    print("|  Paper 9 Numerical Verification -- Dyadic Coherence" + " "*19 + "|")
    print("|  PCI/PME Framework | paper7-foundation | commit 0b1fef1" + " "*14 + "|")
    print("|  Executed by Phi | 2026-05-04" + " "*40 + "|")
    print("+" + "="*70 + "+")
    print()
    print("Spec: prompt spec (raw.githubusercontent.com network-blocked; fallback)")
    print()

    t1_rows                    = task1(verbose=True)
    t2_rows                    = task2(t1_rows, verbose=True)
    t3_data, rho_c_n, rho_c_p = task3(verbose=True)

    # Save structured JSON results
    results = dict(
        task1=t1_rows,
        task2=t2_rows,
        task3=dict(
            data=t3_data,
            rho_c_numerical=float(rho_c_n) if rho_c_n is not None else None,
            rho_c_predicted=float(rho_c_p),
        ),
    )
    with open("paper9_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Structured results saved --> paper9_results.json")

    # Final summary box
    t1_pass   = sum(1 for r in t1_rows if r['result'] == 'PASS')
    t1_fail   = sum(1 for r in t1_rows if r['result'] == 'FAIL')
    t2_resids = [r['residual'] for r in t2_rows if r['residual'] is not None]
    r_min     = min(t2_resids) if t2_resids else float('nan')
    r_max     = max(t2_resids) if t2_resids else float('nan')

    print()
    print("+" + "="*70 + "+")
    print("|  FINAL SUMMARY" + " "*55 + "|")
    print("+"+"-"*70+"+")
    line1 = f"|  Task 1  Theorem 9.1     {t1_pass:2d} PASS / {t1_fail:2d} FAIL -- bound analytically false"
    print(line1 + " "*(72-len(line1)) + "|")
    line2 = f"|  Task 2  Theorem 9.2     residuals {r_min:.3f}--{r_max:.3f}; formula not confirmed"
    print(line2 + " "*(72-len(line2)) + "|")
    line3 = f"|  Task 3  Conjecture 9.3  bifurcation not detectable (linear map, Banach uniqueness)"
    print(line3 + " "*(72-len(line3)) + "|")
    print("+" + "="*70 + "+")
    print()


if __name__ == "__main__":
    main()
