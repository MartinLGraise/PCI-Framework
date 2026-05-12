"""
Figure 1. The two-axis residence observable R(s,c) = tau_R(s) * pi_c.

Phase diagram showing:
- Functional residence bounds as a central rectangle
- Four canonical disease cases plotted as labeled points
- Each case escapes the functional box on one or both axes:
    3.1 FUS  -> escapes on tau_R only (pure temporal)
    3.2 PrP  -> escapes on pi_c only (pure spatial)
    3.3 mHtt -> escapes on both axes
    3.4 tau  -> escapes on both axes
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(8.5, 7.5))

# Functional residence bounds (the "design intent" box)
tau_min, tau_max = 0.2, 0.55
pi_min, pi_max = 0.25, 0.55

functional_box = patches.Rectangle(
    (tau_min, pi_min),
    tau_max - tau_min,
    pi_max - pi_min,
    linewidth=2.0,
    edgecolor="#2E7D32",
    facecolor="#C8E6C9",
    alpha=0.35,
    label="Functional residence bounds",
)
ax.add_patch(functional_box)

# Label the functional region (placed in upper-left of the box where there's room)
ax.text(
    tau_min + 0.025,
    pi_max - 0.025,
    "Functional\nresidence\nbounds",
    ha="left",
    va="top",
    fontsize=10.5,
    color="#1B5E20",
    fontweight="bold",
    style="italic",
)

# A "healthy" representative point inside the box (lower-right of box, away from label)
healthy_pt = (0.45, 0.32)
ax.scatter([healthy_pt[0]], [healthy_pt[1]], s=90, marker="o",
           facecolor="#1B5E20", edgecolor="white", zorder=5)
ax.text(healthy_pt[0] + 0.015, healthy_pt[1], "Healthy\noperation",
        va="center", ha="left", fontsize=9.5, color="#1B5E20")

# Pathological cases - separated so labels don't overlap
cases = [
    # (tau_R, pi_c, label, color, marker_size, label_x, label_y, ha, va)
    # FUS: pure temporal (right side, below center)
    (0.88, 0.40, r"3.1 FUS" "\n" r"(stress granules)" "\n" r"→ escapes $\tau_R$",
     "#C62828", 140, 0.86, 0.18, "center", "top"),
    # PrP: pure spatial (left side, above center)
    (0.38, 0.88, r"3.2 PrP" "\n" r"(topology)" "\n" r"→ escapes $\pi_c$",
     "#1565C0", 140, 0.15, 0.88, "left", "center"),
    # mHtt: both, plotted slightly right-of-corner so label can go left
    (0.90, 0.78, "3.3 mHtt\n(nuclear vs mito)\n→ escapes both axes",
     "#6A1B9A", 140, 0.62, 0.71, "center", "top"),
    # tau: both, plotted slightly above-of-corner so label can go right
    (0.74, 0.93, "3.4 tau\n(multi-compartment)\n→ escapes both axes",
     "#E65100", 140, 0.62, 0.97, "center", "center"),
]

for tau, pi, label, color, size, lbl_x, lbl_y, ha, va in cases:
    ax.scatter([tau], [pi], s=size, marker="X", facecolor=color, edgecolor="white",
               linewidth=1.5, zorder=5)
    ax.text(lbl_x, lbl_y, label, fontsize=9.5, color=color,
            ha=ha, va=va, fontweight="bold")
    # Thin line connecting label to marker
    ax.plot([lbl_x, tau], [lbl_y, pi], color=color, lw=0.7, alpha=0.4, zorder=3)

# Arrows from healthy operation to each case showing the residence-pathology direction
for tau, pi, _, color, _, _, _, _, _ in cases:
    ax.annotate("", xy=(tau, pi), xytext=healthy_pt,
                arrowprops=dict(arrowstyle="->", color=color, lw=1.0,
                               alpha=0.3, linestyle="--", shrinkA=8, shrinkB=14))

# Axes labels and ticks
ax.set_xlabel(r"$\tau_R(s)$  —  temporal residence (state dwell time, normalized)", fontsize=12)
ax.set_ylabel(r"$\pi_c$  —  spatial residence (compartmental occupancy)", fontsize=12)

ax.set_xlim(0, 1.0)
ax.set_ylim(0, 1.0)
ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.tick_params(labelsize=10)

# Quadrant labels at corners
ax.text(0.04, 0.96, "Spatial-axis\npathology", fontsize=9, color="#1565C0",
        style="italic", va="top")
ax.text(0.96, 0.04, "Temporal-axis\npathology", fontsize=9, color="#C62828",
        style="italic", ha="right", va="bottom")
ax.text(0.96, 0.96, "Both-axes\npathology", fontsize=9, color="#6A1B9A",
        style="italic", ha="right", va="top")

# Title
ax.set_title(
    r"Figure 1. The two-axis residence observable $R(s,c) = \tau_R(s) \times \pi_c$" + "\n"
    r"with four canonical disease cases (§3) demonstrating two-axis necessity",
    fontsize=12, pad=14
)

# Subtle grid
ax.grid(True, alpha=0.15, linestyle=":")
ax.set_axisbelow(True)

# Caption-style note below
fig.text(
    0.5, 0.02,
    "Pathology corresponds to $R(s,c)$ escaping the functional residence bounds on $\\tau_R$, $\\pi_c$, or both. "
    "Pure-axis cases (3.1, 3.2) establish independent empirical content of each axis;\n"
    "both-axes cases (3.3, 3.4) establish that one-axis observables cannot resolve "
    "clinical heterogeneity within a single protein.",
    ha="center", fontsize=8.5, style="italic", color="#444",
)

plt.tight_layout(rect=[0, 0.06, 1, 1])
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig1_two_axis_observable.png",
            dpi=240, bbox_inches="tight", facecolor="white")
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig1_two_axis_observable.pdf",
            bbox_inches="tight", facecolor="white")
print("Figure 1 written.")
