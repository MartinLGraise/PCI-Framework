"""
Paper 12 v2 supporting computation — interior-sup for boundary-KKT seeds.

Addresses Council Issue S3-7 (Opus 4.7 review, 2026-05-06):
  "For the 28 boundary-KKT seeds, what is sup_{(0,pi/2)} c(theta) and is it
   > c(0) anywhere? If no, the escape lands the trajectory in lower-coherence
   territory."

Method:
  For each of the 28 boundary-KKT seeds (25 boundary-left + 3 boundary-right
  per outbox/paper12/computations/paper12_q5_kappa0_audit.csv), compute
  c(theta) on a fine grid theta in [delta, pi/2 - delta] with delta = 1e-3,
  and compare sup interior c to the boundary value c(theta_star).

  Outputs:
    - paper12_q5_boundary_interior_sup.csv (per-seed, includes
      c_at_boundary, sup_c_interior, theta_argmax_interior, gain_indicator)
    - paper12_q5_boundary_interior_sup.json (aggregate stats)

This determines whether Theorem 3.6.1's "escape into the interior" framing
delivers a meaningful coherence gain for boundary-KKT seeds, or whether the
escape lands the trajectory in lower-coherence territory.
"""

import csv
import json
import os
import time

import numpy as np

# Match Paper 9 conventions exactly
N = 14
r = 0.7
I_mat = np.eye(N)
e1 = np.zeros(N); e1[0] = 1.0


def make_rotation(seed):
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((N, N)))
    return Q


def cmin_value(theta, R_A, R_B, b_A, b_B):
    c, s = np.cos(theta), np.sin(theta)
    M = np.block([[I_mat - r*c*R_A,   r*s*R_A],
                  [-r*s*R_B,          I_mat - r*c*R_B]])
    z = np.linalg.solve(M, np.concatenate([b_A, b_B]))
    x, y = z[:N], z[N:]
    cA = abs(float(np.dot(x, b_A) / (np.linalg.norm(x) * np.linalg.norm(b_A))))
    cB = abs(float(np.dot(y, b_B) / (np.linalg.norm(y) * np.linalg.norm(b_B))))
    return min(cA, cB)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    audit_csv = os.path.join(here, "paper12_q5_kappa0_audit.csv")

    # Load the audit results to identify boundary-KKT seeds.
    boundary_seeds = []
    with open(audit_csv) as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            cls = row["classification"]
            if cls in ("boundary_left_KKT", "boundary_right_KKT"):
                boundary_seeds.append({
                    "seed_a": int(row["seed_a"]),
                    "seed_b": int(row["seed_b"]),
                    "theta_star_deg_audit": float(row["theta_star_deg"]),
                    "c_at_boundary_audit": float(row["c_star"]),
                    "classification": cls,
                })

    print(f"Boundary-KKT seeds to audit: {len(boundary_seeds)}")
    print("=" * 78)

    # Fine interior grid: 2000 points on (delta, pi/2 - delta).
    delta = 1e-3
    grid = np.linspace(delta, 0.5 * np.pi - delta, 2000)

    rows = []
    t0 = time.time()
    for seed in boundary_seeds:
        R_A = make_rotation(seed["seed_a"])
        R_B = make_rotation(seed["seed_b"])
        b_A = e1.copy()
        b_B = e1.copy()  # phi = 0 aligned bias

        c_at_boundary = seed["c_at_boundary_audit"]

        c_grid = np.array([cmin_value(th, R_A, R_B, b_A, b_B) for th in grid])
        idx_max = int(np.argmax(c_grid))
        sup_c_interior = float(c_grid[idx_max])
        theta_argmax_int = float(np.degrees(grid[idx_max]))

        # Did interior beat boundary?
        gain_over_boundary = sup_c_interior - c_at_boundary
        gain_indicator = "INTERIOR_BEATS_BOUNDARY" if gain_over_boundary > 1e-8 \
                         else ("INTERIOR_LOSES" if gain_over_boundary < -1e-8 else "TIE")

        rows.append({
            **seed,
            "sup_c_interior": sup_c_interior,
            "theta_argmax_interior_deg": theta_argmax_int,
            "gain_over_boundary": gain_over_boundary,
            "gain_indicator": gain_indicator,
        })
        print(f"  seeds=({seed['seed_a']:8d}, {seed['seed_b']:8d}) "
              f"c_bd={c_at_boundary:.4f}  sup_int={sup_c_interior:.4f} "
              f"@ {theta_argmax_int:6.2f}°  delta={gain_over_boundary:+.4e}  "
              f"-> {gain_indicator}")

    elapsed = time.time() - t0

    n_int_beats = sum(1 for r_ in rows if r_["gain_indicator"] == "INTERIOR_BEATS_BOUNDARY")
    n_int_loses = sum(1 for r_ in rows if r_["gain_indicator"] == "INTERIOR_LOSES")
    n_tie = sum(1 for r_ in rows if r_["gain_indicator"] == "TIE")
    gains = np.array([r_["gain_over_boundary"] for r_ in rows])

    summary = {
        "n_boundary_kkt_seeds": len(rows),
        "n_interior_beats_boundary": n_int_beats,
        "n_interior_loses": n_int_loses,
        "n_tie": n_tie,
        "gain_range": [float(gains.min()), float(gains.max())],
        "gain_mean": float(gains.mean()),
        "gain_median": float(np.median(gains)),
        "interior_sup_range": [float(min(r_["sup_c_interior"] for r_ in rows)),
                                float(max(r_["sup_c_interior"] for r_ in rows))],
        "boundary_value_range": [float(min(r_["c_at_boundary_audit"] for r_ in rows)),
                                  float(max(r_["c_at_boundary_audit"] for r_ in rows))],
        "grid_resolution_rad": float(grid[1] - grid[0]),
        "grid_size": int(len(grid)),
        "runtime_seconds": elapsed,
        "interpretation": (
            "INTERIOR_BEATS_BOUNDARY count > 0 means escape into interior "
            "is in fact a coherence-improvement direction; "
            "INTERIOR_LOSES count > 0 means Thm 3.6.1 transports trajectory "
            "into lower-coherence territory and the framing must be revised."
        ),
    }

    print()
    print("=" * 78)
    print("AGGREGATE")
    print("=" * 78)
    print(f"  Total boundary-KKT seeds:      {len(rows)}")
    print(f"  INTERIOR_BEATS_BOUNDARY:       {n_int_beats}")
    print(f"  INTERIOR_LOSES (worse):        {n_int_loses}")
    print(f"  TIE:                           {n_tie}")
    print(f"  Gain range:                    [{gains.min():.4e}, {gains.max():.4e}]")
    print(f"  Gain mean:                     {gains.mean():.4e}")
    print(f"  Runtime:                       {elapsed:.2f}s")

    out_csv = os.path.join(here, "paper12_q5_boundary_interior_sup.csv")
    with open(out_csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "seed_a", "seed_b", "classification", "theta_star_deg_audit",
            "c_at_boundary_audit", "sup_c_interior", "theta_argmax_interior_deg",
            "gain_over_boundary", "gain_indicator",
        ])
        w.writeheader()
        for r_ in rows:
            w.writerow({k: r_[k] for k in w.fieldnames})

    out_json = os.path.join(here, "paper12_q5_boundary_interior_sup.json")
    with open(out_json, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nCSV: {out_csv}")
    print(f"JSON: {out_json}")


if __name__ == "__main__":
    main()
