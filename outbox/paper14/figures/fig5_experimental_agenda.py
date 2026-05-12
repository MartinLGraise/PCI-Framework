"""
Figure 5. Experimental agenda (§11) — thirteen experiments organized by
question, dependency, and tractability tier.

Cluster A: Cross-substrate recovery-kinetics (E1-E8)
Cluster B: Pharmacology-to-psychedelics bridge (E9-E13)
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
import numpy as np

fig, ax = plt.subplots(figsize=(17, 11))
ax.set_xlim(0, 17)
ax.set_ylim(0, 11)
ax.axis("off")

# Title
ax.text(8.5, 10.6, "Figure 5. Cross-domain experimental agenda (§11)",
        ha="center", va="top", fontsize=14, fontweight="bold")
ax.text(8.5, 10.15,
        "Thirteen experiments organized by cluster, tractability tier, and dependency.",
        ha="center", va="top", fontsize=10, style="italic", color="#555")

# Cluster headers
ax.text(5.0, 9.6, "Cluster A — Cross-substrate recovery-kinetics",
        ha="center", va="center", fontsize=12, fontweight="bold", color="#1565C0")
ax.text(13.0, 9.6, "Cluster B — Pharmacology-to-psychedelics bridge",
        ha="center", va="center", fontsize=12, fontweight="bold", color="#6A1B9A")

# Vertical divider
ax.plot([9.5, 9.5], [0.6, 9.4], color="#999", lw=1, linestyle=":")

# Tier rows (horizontal bands with subtle background)
# Labels placed in dedicated narrow left-margin column (x = 0.1 to 0.6),
# experiment boxes start at x >= 0.8
tier_bands = [
    (7.2, 9.0, "#E8F5E9", "Tier 1\ntractable\nnow", "#1B5E20"),
    (4.8, 7.1, "#FFF3E0", "Tier 2\nlarger cohort\nor multi-site", "#E65100"),
    (2.0, 4.5, "#FFEBEE", "Tier 3\nblocked on\npre-work", "#B71C1C"),
]
for y_low, y_high, bg, lbl, lbl_color in tier_bands:
    # Narrow band on the left for the label
    label_band = Rectangle((0.2, y_low), 0.7, y_high - y_low,
                           facecolor=lbl_color, edgecolor=None, alpha=0.20, zorder=0)
    ax.add_patch(label_band)
    # Main band for content (starts at x = 0.9)
    band = Rectangle((0.9, y_low), 16.0, y_high - y_low,
                     facecolor=bg, edgecolor=None, alpha=0.35, zorder=0)
    ax.add_patch(band)
    ax.text(0.55, (y_low + y_high) / 2, lbl, ha="center", va="center", fontsize=9,
            fontweight="bold", color=lbl_color, style="italic", zorder=2)

# Experiment boxes
# Format: (id, title, x, y, color, falsification one-liner)
# Cluster A (x range ~ 1.0 to 9.0)
# Box positions: Cluster A x = 2.0, 4.8, 7.6; Cluster B x = 11.5, 14.5; centered y per tier.
exps_A = [
    # Tier 1 (y = 8.4 row + a second row at 7.6 for E8)
    ("E1", "Cross-domain perturbation\n+ recovery battery", 2.4, 8.4, "#1565C0",
     "Within-subject τ correlated\nacross substrates (r > 0.4)"),
    ("E3", "Proteostasis-phospho-\nregulation coupling", 5.0, 8.4, "#1565C0",
     "Shared dominant eigenvalue\nacross substrates"),
    ("E4", "Dominant-eigenvalue\nmodeling of recovery", 7.6, 8.4, "#1565C0",
     "Eigenvalues correlate\nwith bulk τ within substrate"),
    ("E8", "Boundary-condition\nself-falsification", 2.4, 7.5, "#1565C0",
     "Two-axis observable detects\nintact-machinery cases"),
    # Tier 2 (y = 6.3, plus E7 at y = 5.3)
    ("E2", "Multimodal HRV + fMRI\nin depression", 2.4, 6.3, "#1565C0",
     "HRV + DMN τ jointly\npredict treatment response"),
    ("E5", "Longitudinal early-warning\ndesigns", 5.0, 6.3, "#1565C0",
     "Cross-substrate composite\npredicts relapse"),
    ("E6", "Return-path composite\nindex validation", 7.6, 6.3, "#1565C0",
     "Composite > best single\nsubstrate (d ≥ 0.3)"),
    ("E7", "Intervention-convergence\nanalysis", 5.0, 5.3, "#1565C0",
     "All active arms improve\ncomposite at 6 weeks"),
]
# Cluster B (x range ~ 10.0 to 16.5)
exps_B = [
    # Tier 1
    ("E10", "Antagonist-termination\n(KILLER EXPERIMENT)", 11.8, 8.4, "#6A1B9A",
     "Ketanserin truncates\npost-acute neural effects"),
    ("E12", "Spontaneous-vs-\nperturbational dissociation", 14.6, 8.4, "#6A1B9A",
     "Three readouts dissociate\n(r < 0.5 pairwise)"),
    ("E13", "Baseline-rigidity-\nas-moderator", 11.8, 7.5, "#6A1B9A",
     "Higher baseline rigidity ⇒\nlarger improvement"),
    # Tier 2
    ("E11", "Clinical occupancy-to-\ndynamics PK/PD model", 13.2, 6.3, "#6A1B9A",
     "Residence-time predictor >\npeak-occupancy predictor"),
    # Tier 3
    ("E9", "Matched-exposure varied\n$k_{\\mathrm{off}}$ 5-HT$_{2A}$ panel", 13.2, 3.2, "#6A1B9A",
     "Effect scales with $k_{\\mathrm{off}}$\nrather than peak occupancy"),
]


def draw_exp(exp_id, title, x, y, main_color, falsification):
    box_w, box_h = 2.5, 0.95
    rect = Rectangle((x - box_w / 2, y - box_h / 2), box_w, box_h,
                     facecolor="white", edgecolor=main_color, linewidth=1.8,
                     zorder=3)
    ax.add_patch(rect)
    # Experiment ID badge top-left
    badge_x = x - box_w / 2 + 0.22
    badge_y = y + box_h / 2 - 0.18
    circ = Circle((badge_x, badge_y), 0.16,
                  facecolor=main_color, edgecolor="white", linewidth=1.2, zorder=5)
    ax.add_patch(circ)
    ax.text(badge_x, badge_y, exp_id,
            ha="center", va="center", fontsize=7, fontweight="bold",
            color="white", zorder=6)
    # Title to the right of badge (top of box)
    ax.text(x - box_w / 2 + 0.42, y + 0.18, title,
            ha="left", va="center", fontsize=8,
            color="#1A1A1A", fontweight="bold")
    # Falsification one-liner at bottom of box (italic, smaller)
    ax.text(x, y - box_h / 2 + 0.13, falsification,
            ha="center", va="bottom", fontsize=6.8, color="#555", style="italic")


for exp in exps_A + exps_B:
    draw_exp(*exp)

# Dependency arrows (subtle, curved)
def draw_dep(from_xy, to_xy, color="#888"):
    arrow = FancyArrowPatch(from_xy, to_xy,
                            arrowstyle="->", color=color, lw=1.0,
                            mutation_scale=10, alpha=0.45,
                            connectionstyle="arc3,rad=0.15",
                            zorder=2)
    ax.add_patch(arrow)


# Cluster A dependencies: E1, E3, E4 → E6 (composite needs substrate kinetics)
draw_dep((2.4, 7.93), (6.8, 6.78))    # E1 -> E6
draw_dep((5.0, 7.93), (7.2, 6.78))    # E3 -> E6
draw_dep((7.6, 7.93), (7.6, 6.78))    # E4 -> E6
# E2, E5 also feed into E6
draw_dep((3.3, 6.3), (6.6, 6.3))      # E2 -> E6
draw_dep((5.9, 6.3), (6.6, 6.3))      # E5 -> E6
# E6 → E7 (intervention needs composite)
draw_dep((6.8, 5.95), (5.7, 5.55))    # E6 -> E7

# Cluster B dependencies: E10 (killer) feeds E11 (PK/PD modeling)
draw_dep((11.8, 7.93), (12.6, 6.78))  # E10 -> E11

# Caption
fig.text(
    0.5, 0.01,
    "Experiments are placed in tractability bands (top = Tier 1, current technology; middle = Tier 2, larger or multi-site; bottom = Tier 3, blocked on pre-work).\n"
    "Dotted arrows show experimental dependency. Experiment 10 (ketanserin antagonist-termination during psilocybin) is the killer experiment: "
    "it requires no new technology and directly tests the residence-pathology reading.",
    ha="center", fontsize=9, style="italic", color="#444"
)

plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig5_experimental_agenda.png",
            dpi=220, bbox_inches="tight", facecolor="white")
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig5_experimental_agenda.pdf",
            bbox_inches="tight", facecolor="white")
print("Figure 5 written.")
