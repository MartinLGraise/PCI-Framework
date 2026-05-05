"""Paper 9 Figure 2: 50-seed Monte Carlo summary for Conjecture 9.5'.

Three-panel histogram:
  (a) gain fraction across 50 seeds
  (b) theta* at phi=0 across 50 seeds (with pi/4 marker)
  (c) phi_max in gain region across 50 seeds (with 180° marker)

Reads computations/paper9_conjecture95_mc_seeds.csv and produces
figures/paper9_fig2_mc_summary.{png,pdf}.
"""
import csv
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(os.path.dirname(HERE), "computations",
                   "paper9_conjecture95_mc_seeds.csv")

gain_fracs, max_gains, max_phis, theta_stars = [], [], [], []
with open(CSV, newline="") as f:
    rdr = csv.DictReader(f)
    for row in rdr:
        gain_fracs.append(float(row["gain_fraction"]) * 100.0)
        max_gains.append(float(row["max_gain_dC"]))
        max_phis.append(float(row["max_phi_in_gain_deg"]))
        theta_stars.append(float(row["theta_star_at_phi0_deg"]))

gain_fracs = np.array(gain_fracs)
max_gains = np.array(max_gains)
max_phis = np.array(max_phis)
theta_stars = np.array(theta_stars)
N = len(gain_fracs)
assert N == 50, f"expected 50 seeds, got {N}"

plt.rcParams.update({
    "font.family": "DejaVu Serif",
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
})

fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.4), constrained_layout=True)

# Panel (a): gain fraction
ax = axes[0]
bins = np.linspace(0, max(gain_fracs.max() * 1.05, 25), 16)
ax.hist(gain_fracs, bins=bins, color="#3b6fb6", edgecolor="white", linewidth=0.6)
ax.axvline(0, color="k", linewidth=0.8, linestyle=":")
ax.set_xlabel(r"Gain fraction (% of $100\times20$ grid cells)")
ax.set_ylabel("Number of seeds")
ax.set_title(r"(a) $\mathcal{C}_{\min}$ improvement region size")
ax.text(0.97, 0.93,
        f"all 50 seeds non-zero\nmean {gain_fracs.mean():.1f}%, std {gain_fracs.std(ddof=0):.1f}%",
        transform=ax.transAxes, ha="right", va="top", fontsize=8,
        bbox=dict(facecolor="white", edgecolor="0.7", alpha=0.9))

# Panel (b): theta* at phi=0
ax = axes[1]
bins = np.linspace(0, 90, 19)
ax.hist(theta_stars, bins=bins, color="#5a9f5a", edgecolor="white", linewidth=0.6)
ax.axvline(45, color="#c44", linewidth=1.4, linestyle="--", label=r"$\theta^* = \pi/4$ (rejected)")
ax.set_xlabel(r"$\theta^*$ at $\varphi = 0$ (degrees)")
ax.set_ylabel("Number of seeds")
ax.set_title(r"(b) Optimal coupling angle $\theta^*$")
ax.set_xlim(0, 90)
ax.legend(loc="upper right", fontsize=8, framealpha=0.95)
ax.text(0.97, 0.62,
        f"50/50 satisfy\n$|\\theta^* - 45°| > 5°$\nmean {theta_stars.mean():.1f}°",
        transform=ax.transAxes, ha="right", va="top", fontsize=8,
        bbox=dict(facecolor="white", edgecolor="0.7", alpha=0.9))

# Panel (c): phi_max in gain region
ax = axes[2]
bins = np.linspace(0, 181, 20)
ax.hist(max_phis, bins=bins, color="#b97a3a", edgecolor="white", linewidth=0.6)
ax.axvline(180, color="#c44", linewidth=1.4, linestyle="--",
           label=r"$\varphi = 180°$ (opposed bias)")
n_at_180 = int(np.sum(max_phis >= 179.999))
n_below = N - n_at_180
ax.set_xlabel(r"$\varphi_{\max}$ in gain region (degrees)")
ax.set_ylabel("Number of seeds")
ax.set_title(r"(c) Upper bound $\varphi_{\max}$ of gain region")
ax.set_xlim(0, 185)
ax.legend(loc="upper left", fontsize=8, framealpha=0.95)
ax.text(0.97, 0.93,
        f"{n_below}/50 < 180°\n{n_at_180}/50 reach 180°\n(forced amend.\n of Conj. 9.5')",
        transform=ax.transAxes, ha="right", va="top", fontsize=8,
        bbox=dict(facecolor="white", edgecolor="0.7", alpha=0.9))

# Suptitle
fig.suptitle(
    r"Paper 9, Figure 2 — 50-seed Monte Carlo summary for Conjecture 9.5$'$ "
    r"($r=0.7$, dim 14, seeds 20260504+k for $k=0,\ldots,49$)",
    fontsize=10, y=1.04)

PNG = os.path.join(HERE, "paper9_fig2_mc_summary.png")
PDF = os.path.join(HERE, "paper9_fig2_mc_summary.pdf")
fig.savefig(PNG, dpi=200, bbox_inches="tight")
fig.savefig(PDF, bbox_inches="tight")
print(f"Wrote {PNG}")
print(f"Wrote {PDF}")
