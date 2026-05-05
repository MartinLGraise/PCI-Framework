import numpy as np
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SEED = 20260504
N = 14

def make_rotation(n, seed):
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((n, n)))
    return Q

def joint_fixed_point(rA, rB, RA, RB, bA, bB, theta):
    c, s = np.cos(theta), np.sin(theta)
    I = np.eye(len(bA))
    M = np.block([[I - rA*c*RA,   rA*s*RA],
                  [-rB*s*RB,      I - rB*c*RB]])
    z = np.linalg.solve(M, np.concatenate([bA, bB]))
    return z[:N], z[N:]

def cos_sim(u, v):
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v) + 1e-300)

R_A = make_rotation(N, SEED)
R_B = make_rotation(N, SEED + 1)
I = np.eye(N)
r = 0.7

# Reference: bA = e1, bB = cos(phi) e1 + sin(phi) e2 for phi in [0, pi]
e1 = np.zeros(N); e1[0] = 1.0
e2 = np.zeros(N); e2[1] = 1.0

phis = np.linspace(0, np.pi, 100)
thetas = np.linspace(0, np.pi/2, 20)

Z_avg = np.zeros((len(thetas), len(phis)))
Z_min = np.zeros((len(thetas), len(phis)))

x_dec_e1 = np.linalg.solve(I - r * R_A, e1)
C1_dec_e1 = abs(cos_sim(x_dec_e1, e1))

for j, phi in enumerate(phis):
    bB_phi = np.cos(phi) * e1 + np.sin(phi) * e2
    bB_phi = bB_phi / np.linalg.norm(bB_phi)
    y_dec = np.linalg.solve(I - r * R_B, bB_phi)
    C2_dec = abs(cos_sim(y_dec, bB_phi))
    C_avg_dec = 0.5 * (C1_dec_e1 + C2_dec)
    C_min_dec = min(C1_dec_e1, C2_dec)
    for i, theta in enumerate(thetas):
        x, y = joint_fixed_point(r, r, R_A, R_B, e1, bB_phi, theta)
        C1 = abs(cos_sim(x, e1))
        C2 = abs(cos_sim(y, bB_phi))
        Z_avg[i, j] = 0.5*(C1 + C2) - C_avg_dec
        Z_min[i, j] = min(C1, C2) - C_min_dec

# Save Cmin heatmap CSV
with open("/tmp/p7v3-commit/repo/outbox/paper9/computations/paper9_task5_heatmap_cmin.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["phi_deg", "theta_deg", "delta_C_avg", "delta_C_min"])
    for i, th in enumerate(thetas):
        for j, ph in enumerate(phis):
            w.writerow([f"{np.degrees(ph):.6f}", f"{np.degrees(th):.6f}",
                        f"{Z_avg[i,j]:.8f}", f"{Z_min[i,j]:.8f}"])

n_gain_avg = int(np.sum(Z_avg > 0))
n_gain_min = int(np.sum(Z_min > 0))
print(f"ΔC_avg positive: {n_gain_avg}/{Z_avg.size} ({100*n_gain_avg/Z_avg.size:.1f}%)")
print(f"ΔC_min positive: {n_gain_min}/{Z_min.size} ({100*n_gain_min/Z_min.size:.1f}%)")
print(f"ΔC_avg range: [{Z_avg.min():.4f}, {Z_avg.max():.4f}]")
print(f"ΔC_min range: [{Z_min.min():.4f}, {Z_min.max():.4f}]")

phis_deg = np.degrees(phis)
thetas_deg = np.degrees(thetas)
pos_min_phis = [phis_deg[j] for j in range(len(phis)) for i in range(len(thetas)) if Z_min[i,j] > 0]
if pos_min_phis:
    print(f"ΔC_min > 0 region: phi in [{min(pos_min_phis):.1f}°, {max(pos_min_phis):.1f}°]")

# Two-panel figure: Cavg and Cmin side by side
fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))

vmax_avg = max(abs(Z_avg.min()), abs(Z_avg.max()))
im1 = ax[0].pcolormesh(phis_deg, thetas_deg, Z_avg,
                        cmap="RdBu_r", shading="auto", vmin=-vmax_avg, vmax=vmax_avg)
ax[0].set_xlabel(r"Bias-alignment angle $\varphi$ (degrees)")
ax[0].set_ylabel(r"Coupling angle $\theta$ (degrees)")
ax[0].set_title(r"(a) $\Delta\mathcal{C}_\mathrm{avg}(\varphi,\theta)$")
plt.colorbar(im1, ax=ax[0])

vmax_min = max(abs(Z_min.min()), abs(Z_min.max()))
im2 = ax[1].pcolormesh(phis_deg, thetas_deg, Z_min,
                        cmap="RdBu_r", shading="auto", vmin=-vmax_min, vmax=vmax_min)
ax[1].set_xlabel(r"Bias-alignment angle $\varphi$ (degrees)")
ax[1].set_ylabel(r"Coupling angle $\theta$ (degrees)")
ax[1].set_title(r"(b) $\Delta\mathcal{C}_\min(\varphi,\theta)$")
plt.colorbar(im2, ax=ax[1])

for a in ax:
    a.set_xlim(0, 180)
    a.set_ylim(0, 90)
    a.set_xticks([0, 45, 90, 135, 180])
    a.set_yticks([0, 30, 60, 90])
    a.axvline(170, color="darkred", linestyle="--", linewidth=0.8, alpha=0.6)

fig.suptitle(
    f"Paper 9, Fig. 1: Conditional improvement region for the seeded G₂-structured affine dyad\n"
    f"(a) averaging functional: {100*n_gain_avg/Z_avg.size:.1f}% of cells gain; "
    f"(b) minimum functional: {100*n_gain_min/Z_min.size:.1f}% of cells gain. "
    f"$r_A=r_B=0.7$; $R_A,R_B$ random orthogonal in 14D (seeds 20260504/20260505).",
    fontsize=10)
plt.tight_layout()
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper9/figures/paper9_fig1_heatmap.png",
            dpi=200, bbox_inches="tight")
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper9/figures/paper9_fig1_heatmap.pdf",
            bbox_inches="tight")
print("Figure updated with two-panel C_avg vs C_min.")
