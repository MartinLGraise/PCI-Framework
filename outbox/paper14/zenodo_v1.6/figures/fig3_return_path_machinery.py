"""
Figure 3. Return-path machinery typology.

Four substrate-specific return-path machinery classes (§6.1), each shown as a
state-diagram with:
- functional state (left)
- perturbation arrow to perturbed state (right)
- lambda_exit return arrow back to functional state
- substrate-specific name of the return-path mechanism

The common observable lambda_exit = 1/tau_R(s,c) is shared across all four.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(13, 9.5))

panels = [
    # (title, substrate, functional_state_label, perturbed_state_label,
    #  perturbation_label, return_mechanism_label, return_examples, color)
    ("(a) Proteostatic",
     "§6.1 proteostatic return-path",
     "native /\nproperly\nfolded",
     "misfolded /\naggregated /\ncondensate-aged",
     "stress,\nmisfolding,\nphase-separation",
     "Hsp70/90 + chaperones,\nUPS, autophagy, lysosomal\ndegradation, mRNA-decay\nfor stress granules",
     ["FUS granule disassembly",
      "Aβ42 / α-syn / huntingtin clearance",
      "tau monomer restoration"],
     "#C62828"),
    ("(b) Phospho-regulatory",
     "§6.1 phospho-regulatory return-path",
     "phospho-substrate\nbaseline\n(reset)",
     "constitutive\nactivation\nof signaling",
     "growth-factor,\nkinase signaling",
     "PP2A (broad-spectrum)\nand GSK3β (canonical\nbalance vs kinases)\nphosphatase activity",
     ["GSK3β / β-catenin Wnt balance",
      "PP2A loss in cancer",
      "tau phosphorylation reset"],
     "#6A1B9A"),
    ("(c) Autonomic",
     "§6.1 autonomic return-path",
     "parasympathetic\nbaseline\n(HRV-rich)",
     "sympathetic\ndominance\n(stressor regime)",
     "stressor,\northostatic load,\ninflammation",
     "vagal brake +\nbaroreflex sensitivity +\nneutrophil return-to-pool\n(CXCR4-dependent)",
     ["HRV recovery τ after cold-pressor",
      "BRS quantitative measurement",
      "neutrophil aging/return cycle"],
     "#1B5E20"),
    ("(d) Network-dynamical",
     "§6.1 network-dynamical return-path",
     "task-set\nengaged\n(CEN dominant)",
     "DMN-dominant /\nself-referential\nresidence",
     "demand load,\nrumination trigger,\ninternal narrative",
     "CEN / salience network\nswitching dynamics +\nDMN deactivation\nmachinery",
     ["return-to-task-set τ",
      "metastable dwell distribution",
      "CEN-DMN switching rate"],
     "#1565C0"),
]


def draw_panel(ax, panel):
    title, subtitle, func, pert, perturb_lbl, return_lbl, examples, color = panel

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    # Title
    ax.text(5, 9.6, title, ha="center", va="top", fontsize=13,
            fontweight="bold", color=color)
    ax.text(5, 9.0, subtitle, ha="center", va="top", fontsize=9.5,
            color="#555", style="italic")

    # Two state boxes
    func_box = Rectangle((0.5, 5.5), 3.2, 2.0,
                         facecolor="#E8F5E9", edgecolor=color, linewidth=2)
    ax.add_patch(func_box)
    ax.text(2.1, 6.5, func, ha="center", va="center", fontsize=10.5,
            color="#1B5E20", fontweight="bold")

    pert_box = Rectangle((6.3, 5.5), 3.2, 2.0,
                         facecolor="#FFEBEE", edgecolor=color, linewidth=2)
    ax.add_patch(pert_box)
    ax.text(7.9, 6.5, pert, ha="center", va="center", fontsize=10.5,
            color="#B71C1C", fontweight="bold")

    # Perturbation arrow (top, left to right)
    perturb_arrow = FancyArrowPatch(
        (3.8, 7.0), (6.2, 7.0),
        arrowstyle="->", color="#C62828", lw=2, mutation_scale=18,
    )
    ax.add_patch(perturb_arrow)
    ax.text(5.0, 7.6, perturb_lbl, ha="center", va="bottom", fontsize=9,
            color="#C62828", style="italic")

    # Return-path arrow (bottom, right to left) — labeled with lambda_exit
    return_arrow = FancyArrowPatch(
        (6.2, 6.0), (3.8, 6.0),
        arrowstyle="->", color=color, lw=2.5, mutation_scale=18,
    )
    ax.add_patch(return_arrow)
    ax.text(5.0, 5.55, r"$\lambda_{\mathrm{exit}} = 1 / \tau_R(s,c)$",
            ha="center", va="top", fontsize=10, color=color, fontweight="bold")

    # Return-path machinery label below the diagram
    ax.text(5.0, 4.4, "Return-path machinery:",
            ha="center", va="top", fontsize=10, color="#333", fontweight="bold")
    ax.text(5.0, 4.0, return_lbl,
            ha="center", va="top", fontsize=9.5, color="#333")

    # Examples (bottom)
    ax.text(5.0, 2.2, "Empirical observables of " + r"$\lambda_{\mathrm{exit}}$:",
            ha="center", va="top", fontsize=10, color=color, fontweight="bold")
    for i, ex in enumerate(examples):
        ax.text(5.0, 1.7 - i * 0.45, "• " + ex,
                ha="center", va="top", fontsize=9, color="#444")


for ax, panel in zip(axes.flat, panels):
    draw_panel(ax, panel)

fig.suptitle(
    "Figure 3. Return-path machinery typology — four substrate-specific instances of "
    r"$\lambda_{\mathrm{exit}} = 1 / \tau_R(s,c)$",
    fontsize=14, y=0.99,
)

fig.text(
    0.5, 0.01,
    "All four classes share the same observable structure: a functional baseline state, a perturbed state, "
    "and a return-rate-constant " + r"$\lambda_{\mathrm{exit}}$ "
    "set by substrate-specific machinery (§6.1).\n"
    "Disease at any substrate corresponds to fall of " + r"$\lambda_{\mathrm{exit}}$ "
    "below the threshold needed to maintain $R(s,c) = \\tau_R(s) \\times \\pi_c$ within functional bounds.",
    ha="center", fontsize=9, style="italic", color="#444"
)

plt.tight_layout(rect=[0, 0.04, 1, 0.96])
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig3_return_path_machinery.png",
            dpi=220, bbox_inches="tight", facecolor="white")
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig3_return_path_machinery.pdf",
            bbox_inches="tight", facecolor="white")
print("Figure 3 written.")
