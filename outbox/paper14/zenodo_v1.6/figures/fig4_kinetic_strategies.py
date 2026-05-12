"""
Figure 4. Symmetric kinetic-stabilization strategies (§5).

Five symmetric strategies for residence-control across substrates, organized
as a 2x2 grid on (temporal-axis vs spatial-axis) x (stabilize-functional vs
destabilize-pathological), plus strategy E (restore return-path machinery)
as a meta-strategy operating on lambda_exit directly.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
import numpy as np

fig = plt.figure(figsize=(16, 11))
ax = fig.add_subplot(111)
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis("off")

# Title
ax.text(8, 10.6, "Figure 4. Symmetric kinetic-stabilization strategies (§5)",
        ha="center", va="top", fontsize=14, fontweight="bold")
ax.text(8, 10.05,
        "Five strategies for residence control across both axes; Strategy E restores the return-path machinery directly.",
        ha="center", va="top", fontsize=10, style="italic", color="#555")

# Axis labels for the 2x2 strategy grid
ax.text(0.5, 6.6, "Temporal axis\n($\\tau_R$)",
        ha="center", va="center", fontsize=12, fontweight="bold",
        color="#37474F", rotation=90)
ax.text(0.5, 2.9, "Spatial axis\n($\\pi_c$)",
        ha="center", va="center", fontsize=12, fontweight="bold",
        color="#37474F", rotation=90)
ax.text(4.0, 9.15, "Stabilize functional state",
        ha="center", va="center", fontsize=11, fontweight="bold",
        color="#1B5E20")
ax.text(9.0, 9.15, "Destabilize pathological state",
        ha="center", va="center", fontsize=11, fontweight="bold",
        color="#C62828")

# Four strategy boxes in 2x2 - widened, taller, properly labeled A/B/C/D
strategies = [
    # (x, y, label, title, body, color, examples)
    (1.5, 5.0, "A", "extend native dwell",
     "Stabilize the native / functional\nstate so that $\\tau_R$ in s_native\nincreases and transition to\ns_pathological is kinetically\nsuppressed.",
     "#2E7D32",
     ["Tafamidis (Kelly 1996)",
      "Stabilizing chaperones",
      "Kinetic-trap stabilizers"]),
    (6.5, 5.0, "B", "destabilize pathological dwell",
     "Reduce $\\tau_R$ in s_pathological\nby targeting the pathological-\nstate energy minimum or its\nkinetic barriers.",
     "#C62828",
     ["Tau aggregation disruptors",
      "α-syn fibril destabilizers",
      "Granule-aging inhibitors"]),
    (1.5, 1.3, "D", "route to protective compartment",
     "Increase $\\pi_c$ for the protective\ncompartment (e.g., autophagosomal\ndelivery, proteasome routing,\nlysosome targeting).",
     "#2E7D32",
     ["Autophagy inducers",
      "PROTACs (targeted degradation)",
      "Lysosomal-targeted clearance"]),
    (6.5, 1.3, "C", "reroute from pathological compartment",
     "Decrease $\\pi_c$ for the pathological\ncompartment (e.g., block aberrant\ntrafficking, prevent mislocalization).",
     "#C62828",
     ["NLS/NES-pathway inhibitors",
      "Mitochondrial entry blockers",
      "Aberrant-membrane targeting"]),
]

box_w, box_h = 4.5, 3.5

from matplotlib.patches import Circle

for x, y, letter, title, body, color, examples in strategies:
    rect = Rectangle((x, y), box_w, box_h,
                     facecolor="white", edgecolor=color, linewidth=2.5)
    ax.add_patch(rect)
    # Strategy letter circle (top-left)
    circ = Circle((x + 0.45, y + box_h - 0.4), 0.32,
                  facecolor=color, edgecolor="white", linewidth=2, zorder=5)
    ax.add_patch(circ)
    ax.text(x + 0.45, y + box_h - 0.4, letter,
            ha="center", va="center", fontsize=14, fontweight="bold",
            color="white", zorder=6)
    # Title to the right of the circle
    ax.text(x + 0.95, y + box_h - 0.4, title,
            ha="left", va="center", fontsize=10, fontweight="bold",
            color=color)
    # Body
    ax.text(x + 0.15, y + box_h - 1.0, body,
            ha="left", va="top", fontsize=9, color="#222")
    # Examples
    ax.text(x + 0.15, y + 1.05, "Examples:",
            ha="left", va="top", fontsize=9, fontweight="bold", color=color)
    for i, ex in enumerate(examples):
        ax.text(x + 0.15, y + 0.75 - i * 0.25, "• " + ex,
                ha="left", va="top", fontsize=8.5, color="#444")

# Strategy E — restore return-path machinery (large box, right side, spans both rows)
e_x, e_y = 12.0, 1.3
e_w, e_h = 3.5, 7.2
e_color = "#1565C0"
rect_e = Rectangle((e_x, e_y), e_w, e_h,
                   facecolor="#E3F2FD", edgecolor=e_color, linewidth=2.5)
ax.add_patch(rect_e)
from matplotlib.patches import Circle
circ_e = Circle((e_x + e_w / 2, e_y + e_h - 0.5), 0.42,
                facecolor=e_color, edgecolor="white", linewidth=2, zorder=5)
ax.add_patch(circ_e)
ax.text(e_x + e_w / 2, e_y + e_h - 0.5, "E",
        ha="center", va="center", fontsize=16, fontweight="bold",
        color="white", zorder=6)
ax.text(e_x + e_w / 2, e_y + e_h - 1.4,
        "Strategy E\nrestore return-path machinery",
        ha="center", va="top", fontsize=10.5, fontweight="bold",
        color=e_color)
ax.text(e_x + 0.25, e_y + e_h - 2.7,
        "Meta-strategy: restore $\\lambda_{\\mathrm{exit}}$\ndirectly by repairing the\nsubstrate-specific machinery.\n\nWorks on both axes simultaneously\nby restoring the function that\nwould have kept $R(s,c)$ within\nfunctional bounds.",
        ha="left", va="top", fontsize=9.5, color="#0D47A1")
ax.text(e_x + 0.25, e_y + 2.5, "Examples:",
        ha="left", va="top", fontsize=10, fontweight="bold", color=e_color)
e_examples = [
    "HSP-inducing chaperone therapy\n  (proteostatic)",
    "Lithium / GSK3β-modulating\n  agents (phospho-regulatory)",
    "tVNS / HRV biofeedback\n  (autonomic)",
    "Psychedelic-assisted therapy\n  (network-dynamical)",
]
for i, ex in enumerate(e_examples):
    ax.text(e_x + 0.25, e_y + 2.2 - i * 0.55, "• " + ex,
            ha="left", va="top", fontsize=9, color="#0D47A1")

# Caption
fig.text(
    0.5, 0.005,
    "The five strategies are symmetric across the two axes and across the stabilize/destabilize direction; "
    "strategy E acts on $\\lambda_{\\mathrm{exit}}$ directly. "
    "Kelly's 1996 transthyretin work (Strategy A) is the canonical published precedent;\n"
    "Strategies B–E are symmetric extensions developed in §5 as the molecular substrate's incremental contribution to the framework.",
    ha="center", fontsize=9, style="italic", color="#444"
)

plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig4_kinetic_strategies.png",
            dpi=220, bbox_inches="tight", facecolor="white")
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig4_kinetic_strategies.pdf",
            bbox_inches="tight", facecolor="white")
print("Figure 4 written.")
