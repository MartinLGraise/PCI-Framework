"""
Figure 2. Cross-substrate residence-pathology grammar.

Visual matrix showing the eight substrates of §8 with their substrate-specific
realizations of:
- state s
- compartment c
- tau_R observable
- pi_c observable
- return-path machinery
- canonical pathology under residence failure
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

substrates = [
    # (substrate, state s, compartment c, tau_R, pi_c, return-path, canonical pathology)
    ("§8.1 Pharmacology",
     "drug-target\nbinding state",
     "tissue\ncompartment",
     "1/k_off\n(residence time)",
     "tissue-occupancy\nprobability",
     "drug clearance\n+ tissue redistribution",
     "long-residence\ntoxicity"),
    ("§8.2 Cancer phospho-reg",
     "phospho-substrate\nstate",
     "intracellular\nlocalization",
     "phospho-state\ndwell time",
     "compartment\noccupancy",
     "PP2A / GSK3β\nphosphatases",
     "constitutive\nactivation"),
    ("§8.3 Autonomic\nphysiology",
     "sympathetic vs\nparasympathetic\ntone",
     "baseline vs\nperturbation\nregime",
     "recovery τ\nafter stressor",
     "regime\noccupancy",
     "vagal-brake /\nbaroreflex",
     "depression,\nCV disease"),
    ("§8.4 Exercise\nphysiology",
     "metabolic\nboundary state",
     "muscle / cardiac /\nhepatic /\nneuroendocrine",
     "boundary\ndwell time",
     "compartment\nover-occupancy",
     "endogenous\ncutoffs\n(PCr/H+/sympatho-\nexhaustion)",
     "operator-sustained\ncardiomyopathy\n(HAARLEM)"),
    ("§8.5 Brain network\ndynamics",
     "metastable\nbrain state\n(HMM)",
     "regional\noccupancy",
     "state dwell\ntime",
     "network occupancy\nprobability",
     "network-dynamical\nswitching\n(CEN ↔ DMN)",
     "depression,\nanxiety,\nrumination"),
    ("§8.6.1 Memory\nphenomenology",
     "retrieval-\ncoupled state",
     "present-axis vs\npast-axis\ngrounding",
     "retrieval\ncoupling time",
     "compartment\noccupancy",
     "reconsolidation\nwindow",
     "PTSD, regret,\nnostalgia, grief"),
    ("§8.6.2 Public-\nepistemic",
     "interpretive\nframe",
     "info-source\ncluster",
     "frame dwell\ntime",
     "cluster\nsegregation index",
     "cross-cutting\nexposure +\nfact-checking",
     "echo chambers,\nmisinformation\npersistence"),
    ("§8.7 AI / data\nsubstrate",
     "model-distribution\nmode",
     "training-data\nregime",
     "mode dwell\nunder iter.\ninference",
     "regime\nsegregation",
     "real-data\ncirculation +\nhuman cognition",
     "model collapse,\nepistemic\ndegradation"),
]

# Cell-color scheme: distinct color per substrate row, kept light
row_colors = [
    "#FFEBEE", "#F3E5F5", "#E8F5E9", "#FFF3E0",
    "#E3F2FD", "#FCE4EC", "#F1F8E9", "#E0F2F1",
]
row_text_colors = [
    "#B71C1C", "#4A148C", "#1B5E20", "#E65100",
    "#0D47A1", "#880E4F", "#33691E", "#004D40",
]

columns = ["Substrate", "State (s)", "Compartment (c)",
           r"$\tau_R$ observable", r"$\pi_c$ observable",
           "Return-path\nmachinery",
           "Canonical pathology\nunder residence failure"]

n_rows = len(substrates)
n_cols = len(columns)

# Column widths (proportional)
col_widths = [1.5, 1.3, 1.3, 1.2, 1.2, 1.5, 1.6]
total_w = sum(col_widths)
col_widths_norm = [w / total_w for w in col_widths]
col_x = [0]
for w in col_widths_norm[:-1]:
    col_x.append(col_x[-1] + w)

row_height = 0.95
header_height = 1.2

fig_w = 16
fig_h = header_height + row_height * n_rows + 0.6
fig, ax = plt.subplots(figsize=(fig_w, fig_h * 0.85))

# Header row
header_y = header_height * (n_rows + 0.0) / (n_rows + 1) + row_height * n_rows
header_top = row_height * n_rows + header_height
for i, col in enumerate(columns):
    x = col_x[i]
    w = col_widths_norm[i]
    rect = Rectangle((x, row_height * n_rows), w, header_height,
                     facecolor="#37474F", edgecolor="white", linewidth=1)
    ax.add_patch(rect)
    ax.text(x + w / 2, row_height * n_rows + header_height / 2, col,
            ha="center", va="center", fontsize=11, color="white",
            fontweight="bold")

# Data rows (drawn top-to-bottom, but we want substrate #1 at top)
for r_idx, sub in enumerate(substrates):
    # invert: top row of plot is substrate index 0
    y_bottom = row_height * (n_rows - 1 - r_idx)
    row_color = row_colors[r_idx]
    row_text_color = row_text_colors[r_idx]

    for c_idx, val in enumerate(sub):
        x = col_x[c_idx]
        w = col_widths_norm[c_idx]
        rect = Rectangle((x, y_bottom), w, row_height,
                         facecolor=row_color, edgecolor="white", linewidth=1)
        ax.add_patch(rect)

        # Substrate name column gets bold + colored
        if c_idx == 0:
            ax.text(x + w / 2, y_bottom + row_height / 2, val,
                    ha="center", va="center", fontsize=9.5,
                    color=row_text_color, fontweight="bold")
        else:
            ax.text(x + w / 2, y_bottom + row_height / 2, val,
                    ha="center", va="center", fontsize=9,
                    color="#1A1A1A")

ax.set_xlim(0, 1)
ax.set_ylim(0, row_height * n_rows + header_height)
ax.axis("off")

# Title above the figure area
fig.suptitle(
    r"Figure 2. Cross-substrate residence-pathology grammar across eight substrates"
    "\n"
    r"one principle, one observable $R(s,c)=\tau_R(s)\times\pi_c$, eight substrate-specific realizations",
    fontsize=13, y=0.98, fontweight="normal"
)

# Caption below
fig.text(
    0.5, 0.01,
    "Each row instantiates the residence-pathology principle at a substrate developed independently in its own literature. "
    "The framework's contribution is the explicit composition rule, not new substrate-level claims at any one row.",
    ha="center", fontsize=9, style="italic", color="#444"
)

plt.subplots_adjust(top=0.92, bottom=0.04, left=0.01, right=0.99)
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig2_cross_substrate_grammar.png",
            dpi=220, bbox_inches="tight", facecolor="white")
plt.savefig("/tmp/p7v3-commit/repo/outbox/paper14/figures/fig2_cross_substrate_grammar.pdf",
            bbox_inches="tight", facecolor="white")
print("Figure 2 written.")
