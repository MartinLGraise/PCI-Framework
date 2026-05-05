"""
Monte Carlo across 50 seeded (R_A, R_B) pairs to test Conjecture 9.5'.

Reproducibility record for Paper 9 v1.3.2 "Rate Lock and Affine Consensus
in G₂-Structured Dyadic Observers".

  DOI:        10.5281/zenodo.20034821
  Repository: github.com/MartinLGraise/PCI-Framework (branch paper7-foundation)
  Section:    Appendix V.3.i (50-seed Monte Carlo for Conjecture 9.5')
  Outputs:    paper9_conjecture95_mc_seeds.csv (per-seed)
              paper9_conjecture95_mc_summary.json (aggregate)

For each seed pair:
  - Construct R_A, R_B via QR of standard-normal matrix
  - Sweep (φ, θ) on the 100×20 grid
  - Evaluate ΔC_min(φ, θ)
  - Record: gain fraction, max gain, max φ in gain region, max φ at θ=π/2, θ* = argmax C_min

Aggregate across seeds. Report:
  - distribution of gain fraction
  - distribution of max φ (testing "bounded away from π")
  - distribution of θ* (testing "not generically π/4")
  - count of zero-gain seeds (Conjecture 9.5' negative cases)

Output: paper9_conjecture95_mc_seeds.csv
        paper9_conjecture95_mc_summary.json
"""

import numpy as np
import csv
import json
import os
import time

SEED_LIST = list(range(20260504, 20260554))   # 50 seeds, base+0..49
N = 14
r = 0.7

PHIS = np.linspace(0, np.pi, 100)
THETAS = np.linspace(0, np.pi/2, 20)

I = np.eye(N)
e1 = np.zeros(N); e1[0] = 1.0
e2 = np.zeros(N); e2[1] = 1.0


def make_rotation(seed):
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((N, N)))
    return Q


def joint_fixed_point(rA, rB, RA, RB, bA, bB, theta):
    c, s = np.cos(theta), np.sin(theta)
    M = np.block([[I - rA*c*RA,   rA*s*RA],
                  [-rB*s*RB,      I - rB*c*RB]])
    z = np.linalg.solve(M, np.concatenate([bA, bB]))
    return z[:N], z[N:]


def cos_sim(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v) + 1e-300)


def evaluate_seed_pair(seed_a, seed_b):
    """Returns gain_fraction, max_gain, max_phi_in_gain, max_phi_at_pi2, theta_star_at_phi0."""
    R_A = make_rotation(seed_a)
    R_B = make_rotation(seed_b)

    # Decoupled C_min for phi=0: bA=bB=e1
    x_dec_e1 = np.linalg.solve(I - r * R_A, e1)
    C1_dec_e1 = abs(cos_sim(x_dec_e1, e1))

    n_gain = 0
    max_gain = -np.inf
    gain_phis = []
    gain_phis_at_pi2 = []
    Cmin_at_phi0 = np.zeros(len(THETAS))

    for j, phi in enumerate(PHIS):
        bB_phi = np.cos(phi) * e1 + np.sin(phi) * e2
        bB_phi /= np.linalg.norm(bB_phi)
        y_dec = np.linalg.solve(I - r * R_B, bB_phi)
        C2_dec = abs(cos_sim(y_dec, bB_phi))
        Cmin_dec = min(C1_dec_e1, C2_dec)
        for i, theta in enumerate(THETAS):
            x, y = joint_fixed_point(r, r, R_A, R_B, e1, bB_phi, theta)
            C1 = abs(cos_sim(x, e1))
            C2 = abs(cos_sim(y, bB_phi))
            Cmin_joint = min(C1, C2)
            dC = Cmin_joint - Cmin_dec
            if dC > 1e-10:
                n_gain += 1
                gain_phis.append(np.degrees(phi))
                if abs(theta - np.pi/2) < 1e-8 or i == len(THETAS) - 1:
                    gain_phis_at_pi2.append(np.degrees(phi))
            if dC > max_gain:
                max_gain = dC
            if j == 0:
                Cmin_at_phi0[i] = Cmin_joint

    # θ* at aligned bias (φ=0)
    theta_star = float(np.degrees(THETAS[int(np.argmax(Cmin_at_phi0))]))
    gain_fraction = n_gain / (len(PHIS) * len(THETAS))
    max_phi = max(gain_phis) if gain_phis else 0.0
    return {
        "gain_fraction": gain_fraction,
        "max_gain_dC": float(max_gain) if max_gain > -np.inf else 0.0,
        "max_phi_in_gain_deg": float(max_phi),
        "theta_star_at_phi0_deg": theta_star,
        "n_gain_cells": n_gain,
    }


def main():
    t0 = time.time()
    print(f"Running Monte Carlo: {len(SEED_LIST)} seed pairs")
    print(f"Each: {len(PHIS)} φ × {len(THETAS)} θ = {len(PHIS)*len(THETAS)} grid cells")
    print(f"Grid: φ∈[0°,180°]×{len(PHIS)}, θ∈[0°,90°]×{len(THETAS)}, r=0.7")
    print()

    rows = []
    for k, base in enumerate(SEED_LIST):
        result = evaluate_seed_pair(base, base + 1)
        result["seed_a"] = base
        result["seed_b"] = base + 1
        rows.append(result)
        if (k + 1) % 10 == 0:
            elapsed = time.time() - t0
            print(f"  [{k+1}/{len(SEED_LIST)}] elapsed {elapsed:.1f}s  "
                  f"gain={result['gain_fraction']*100:.1f}%  "
                  f"θ*={result['theta_star_at_phi0_deg']:.1f}°  "
                  f"max_φ={result['max_phi_in_gain_deg']:.1f}°")

    out_dir = "/tmp/p7v3-commit/repo/outbox/paper9/computations"
    csv_path = f"{out_dir}/paper9_conjecture95_mc_seeds.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["seed_a","seed_b","gain_fraction","max_gain_dC",
                                          "max_phi_in_gain_deg","theta_star_at_phi0_deg",
                                          "n_gain_cells"])
        w.writeheader()
        for r_ in rows:
            w.writerow({k: f"{v:.6f}" if isinstance(v, float) else v for k, v in r_.items()})

    fractions = np.array([r_["gain_fraction"] for r_ in rows])
    max_phis  = np.array([r_["max_phi_in_gain_deg"] for r_ in rows])
    theta_stars = np.array([r_["theta_star_at_phi0_deg"] for r_ in rows])
    max_gains = np.array([r_["max_gain_dC"] for r_ in rows])
    n_zero    = int(np.sum(fractions < 1e-12))
    n_with_gain = len(fractions) - n_zero

    summary = {
        "n_seeds": len(rows),
        "n_seeds_with_gain": n_with_gain,
        "n_seeds_zero_gain": n_zero,
        "fraction_range": [float(fractions.min()), float(fractions.max())],
        "fraction_mean": float(fractions.mean()),
        "fraction_std": float(fractions.std()),
        "max_phi_range_deg": [float(max_phis[fractions>0].min()) if n_with_gain > 0 else None,
                               float(max_phis.max())],
        "max_phi_mean_deg": float(max_phis[fractions>0].mean()) if n_with_gain > 0 else None,
        "max_phi_lt_180_seeds": int(np.sum((max_phis < 180.0) & (fractions > 0))),
        "max_phi_eq_180_seeds": int(np.sum((max_phis >= 180.0 - 1e-3) & (fractions > 0))),
        "theta_star_range_deg": [float(theta_stars.min()), float(theta_stars.max())],
        "theta_star_mean_deg": float(theta_stars.mean()),
        "theta_star_neq_45deg_seeds": int(np.sum(np.abs(theta_stars - 45.0) > 5.0)),
        "max_gain_range": [float(max_gains.min()), float(max_gains.max())],
        "elapsed_seconds": time.time() - t0,
    }

    json_path = f"{out_dir}/paper9_conjecture95_mc_summary.json"
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)

    print()
    print("=" * 72)
    print("MONTE CARLO SUMMARY")
    print("=" * 72)
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print()
    print(f"CSV:  {csv_path}")
    print(f"JSON: {json_path}")


if __name__ == "__main__":
    main()
