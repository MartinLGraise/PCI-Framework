"""
Paper 7 figure generation.
Aesthetic: paper-academic, minimal, monochrome with single accent.
Output: 300 dpi PNG (for embedding) + PDF (for submission).
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import matplotlib as mpl

# --- Style: paper-academic ---
# Use Times-like serif for figure text to match the manuscript's body style.
# Single accent: warm rust (#7A2818) consistent with the project's website palette.
mpl.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Liberation Serif", "Times New Roman"],
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "axes.linewidth": 0.8,
    "axes.edgecolor": "#1A1815",
    "xtick.color": "#1A1815",
    "ytick.color": "#1A1815",
    "text.color": "#1A1815",
    "axes.labelcolor": "#1A1815",
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "legend.frameon": False,
    "savefig.bbox": "tight",
    "savefig.dpi": 300,
})

INK = "#1A1815"
ACCENT = "#7A2818"
MUTED = "#7A7974"
PAPER = "#FEFCF8"

OUT = "/home/user/workspace/paper7_figures"
os.makedirs(OUT, exist_ok=True)


# =====================================================================
# Figure 1 — G₂ torsion decomposition schematic
# =====================================================================
def figure_1():
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.set_aspect("equal")
    ax.axis("off")

    # 49 unit cells laid out as a horizontal stacked bar.
    # Show 49 squares total. 42 in muted/INK = torsion. 7 in ACCENT = attractor V_7.
    # Labelled groups: T_1 (1), T_14 (14), T_27 (27), V_7 (7).
    n_total = 49
    cell_w = 1.6
    cell_h = 6.0
    x0 = 4.0
    y0 = 24.0
    gap_groups = 1.0

    groups = [
        ("T₁", 1, "#D4D1CA", INK),
        ("T₁₄", 14, "#A8A29C", INK),
        ("T₂₇", 27, "#7A7974", "white"),
        ("V₇", 7, ACCENT, "white"),
    ]

    # Draw cells
    cur_x = x0
    group_starts = []
    for label, n, fill, _ in groups:
        group_starts.append((label, cur_x, n, fill))
        for i in range(n):
            rect = Rectangle((cur_x, y0), cell_w, cell_h,
                             facecolor=fill, edgecolor=PAPER, linewidth=0.6)
            ax.add_patch(rect)
            cur_x += cell_w
        cur_x += gap_groups

    # Group labels above each block
    for label, gx, n, fill in group_starts:
        block_w = n * cell_w
        ax.annotate(label, xy=(gx + block_w / 2, y0 + cell_h + 1.3),
                    ha="center", va="bottom", fontsize=11,
                    color=INK if label != "V₇" else ACCENT,
                    fontweight="bold")
        ax.annotate(f"dim = {n}", xy=(gx + block_w / 2, y0 - 1.6),
                    ha="center", va="top", fontsize=8.5, color=MUTED)

    # Big braces below: 42 (torsion) and 7 (attractor)
    # Torsion brace
    t_left = group_starts[0][1]
    t_right = group_starts[2][1] + group_starts[2][2] * cell_w
    a_left = group_starts[3][1]
    a_right = a_left + group_starts[3][2] * cell_w

    brace_y = y0 - 6.0
    text_y = brace_y - 4.5

    # Simple brackets (lines instead of fancy braces for clean look)
    for (lx, rx, label, color) in [
        (t_left, t_right, "Torsion: dim = 1 + 14 + 27 = 42", INK),
        (a_left, a_right, "Attractor V₇: dim = 7", ACCENT),
    ]:
        ax.plot([lx, lx, rx, rx], [brace_y + 1.2, brace_y, brace_y, brace_y + 1.2],
                color=color, linewidth=1.0)
        ax.annotate(label, xy=((lx + rx) / 2, text_y),
                    ha="center", va="top", fontsize=10, color=color)

    # Headline ratio at top
    ax.annotate("Total ambient dimension: 1 + 14 + 27 + 7 = 49",
                xy=(50, y0 + cell_h + 9.5), ha="center", va="bottom",
                fontsize=11, color=INK, fontweight="bold")
    ax.annotate("Torsion fraction  42/49 = 6/7  ≈  0.857     ·     Attractor fraction  7/49 = 1/7  ≈  0.143",
                xy=(50, y0 - 14), ha="center", va="top",
                fontsize=10.5, color=INK)

    # Caption note
    ax.annotate(
        "Figure 1. The G₂ torsion-decomposition dimension count. The Fernández–Gray torsion classes T₁, T₁₄, T₂₇ and\n"
        "the fundamental representation V₇ live in different tensor bundles (Ω⁰, Ω¹, a subspace of Ω², a subspace of S²,\n"
        "and V₇ itself); the 49 is therefore a representation-theoretic dimension count, not a single fiber bundle.",
        xy=(50, 1.5), ha="center", va="bottom", fontsize=8, color=MUTED, style="italic")

    plt.tight_layout()
    fig.savefig(f"{OUT}/figure1_torsion_decomposition.png", facecolor="white")
    fig.savefig(f"{OUT}/figure1_torsion_decomposition.pdf", facecolor="white")
    plt.close(fig)
    print("Figure 1 written.")


# =====================================================================
# Figure 2 — PSL(2,7) / F_21 Cayley graph (8 cosets, distances 0..3)
# =====================================================================
def figure_2():
    """
    Conceptual schematic of the 8-coset graph with Cayley-graph distances
    indicated by node placement in concentric rings around a chosen reference
    coset. We do NOT claim this is the literal Cayley graph of PSL(2,7) acting
    on PSL(2,7)/F_21; we present it as an abstract distance schematic, which is
    what the prediction (c) actually uses.
    """
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    ax.set_aspect("equal")
    ax.axis("off")

    # Distance shells: d = 0 (center), d = 1, d = 2, d = 3
    # 8 cosets total. Layout: 1 at d=0, 3 at d=1, 3 at d=2, 1 at d=3.
    # This matches a typical diameter-3 distance distribution for a vertex-transitive
    # graph on 8 vertices; we present it as schematic.
    shells = {
        0: [(0, 0)],
        1: [(np.cos(a), np.sin(a)) for a in np.linspace(np.pi / 2, np.pi / 2 + 4 * np.pi / 3, 3, endpoint=False)],
        2: [(2 * np.cos(a), 2 * np.sin(a)) for a in np.linspace(-np.pi / 2, -np.pi / 2 + 4 * np.pi / 3, 3, endpoint=False)],
        3: [(0, -3)],
    }

    # Draw concentric guide rings (light)
    for r in [1, 2, 3]:
        circ = plt.Circle((0, 0), r, fill=False, color=MUTED, linewidth=0.5,
                          linestyle=(0, (3, 3)), alpha=0.6)
        ax.add_patch(circ)
        ax.annotate(f"d = {r}", xy=(r * np.cos(np.deg2rad(15)), r * np.sin(np.deg2rad(15))),
                    fontsize=9, color=MUTED, ha="left", va="bottom")
    ax.annotate("d = 0", xy=(0.13, 0.13), fontsize=9, color=MUTED, ha="left", va="bottom")

    # Edges between adjacent shells (illustrative; not a literal Cayley graph)
    rng = np.random.default_rng(7)
    edges = []
    # connect d=0 to all d=1
    for p in shells[1]:
        edges.append(((0, 0), p))
    # connect each d=1 to one or two d=2
    d2 = shells[2]
    for i, p in enumerate(shells[1]):
        edges.append((p, d2[i % 3]))
        edges.append((p, d2[(i + 1) % 3]))
    # connect each d=2 to d=3
    for p in shells[2]:
        edges.append((p, shells[3][0]))

    for (a, b) in edges:
        ax.plot([a[0], b[0]], [a[1], b[1]], color=MUTED, linewidth=0.8, alpha=0.7, zorder=1)

    # Plot nodes
    for d, pts in shells.items():
        color = ACCENT if d == 0 else INK
        size = 220 if d == 0 else 160
        edgecolor = ACCENT if d == 0 else INK
        for (x, y) in pts:
            ax.scatter([x], [y], s=size, c="white", edgecolors=edgecolor, linewidths=1.4, zorder=3)

    # Reference label
    ax.annotate("reference\nobserver", xy=(0, 0), xytext=(0.5, 0.55),
                fontsize=9, color=ACCENT, ha="left", va="bottom",
                arrowprops=dict(arrowstyle="-", color=ACCENT, lw=0.6))

    # Title and bottom caption
    ax.set_xlim(-3.6, 3.6)
    ax.set_ylim(-4.4, 3.4)
    ax.annotate("PSL(2,7)/F₂₁: 8 cosets · diameter d ∈ {0, 1, 2, 3}",
                xy=(0, 3.05), ha="center", va="bottom", fontsize=11.5,
                color=INK, fontweight="bold")
    ax.annotate("Inter-observer entropy difference  ΔS_d ≈ (d/7) × S_reference  (conjecture, §4.3)",
                xy=(0, 2.45), ha="center", va="bottom", fontsize=10, color=INK)
    ax.annotate(
        "Figure 2. Schematic Cayley-graph distance structure on the 8 cosets of PSL(2,7)/F₂₁. The exact graph\n"
        "depends on the choice of generators and octonion multiplication-table convention (open computation,\n"
        "§6.3 Problem 2); the four-level entropy structure depicted here is a conjectured representation-theoretic\n"
        "ansatz (§4.3 modeling-choice stack), not a derived theorem.",
        xy=(0, -4.25), ha="center", va="bottom", fontsize=8, color=MUTED, style="italic")

    plt.tight_layout()
    fig.savefig(f"{OUT}/figure2_psl27_cayley.png", facecolor="white")
    fig.savefig(f"{OUT}/figure2_psl27_cayley.pdf", facecolor="white")
    plt.close(fig)
    print("Figure 2 written.")


# =====================================================================
# Figure 3 — Predictions × anchors × evidential status table
# =====================================================================
def figure_3():
    fig, ax = plt.subplots(figsize=(8.4, 5.6))
    ax.axis("off")

    headers = ["Prediction", "Predicted quantity", "Empirical anchor", "Status"]
    rows = [
        ("(a) FDT floor",
         "ε ≥ 1/7 ≈ 0.143",
         "Berjaga-Buisan 2025\n(bioRxiv preprint v2)",
         "Preprint match,\npending peer review"),
        ("(b1) Biological\nLandauer",
         "ΔE_min ≈ 16 zJ\nper G₂/M event",
         "Imamura et al. 2009\n(PNAS, peer-reviewed)",
         "Floor satisfied\n(measured >> floor)"),
        ("(b2) Mode-\ncounting floor",
         "S ≥ log₂(7) k_B ln 2\n≈ 1.95 k_B per tick",
         "Wadhia et al. 2025\n(PRL, Ge/SiGe DQD)",
         "Design target;\nnot a confirmed match"),
        ("(c) Coset entropy\nstructure",
         "ΔS_d ≈ (d/7) × S_ref,\nd ∈ {0,1,2,3}",
         "Basso–Céleri 2025;\nDe Vuyst et al. 2025",
         "Design target;\nopen Bogoliubov calc"),
        ("(d) Branching ratio",
         "σ = 1 − 1/49\n≈ 0.9796",
         "Wilting & Priesemann 2018\n(Nature Comm., peer-rev.)",
         "Published match\n(within uncertainty)"),
    ]

    n_rows = len(rows) + 1
    n_cols = len(headers)
    col_widths = [0.22, 0.27, 0.27, 0.24]
    col_lefts = [sum(col_widths[:i]) for i in range(n_cols)]
    table_top = 0.92
    table_bot = 0.18
    avail = table_top - table_bot
    row_h = avail / n_rows

    # Header
    y_top = table_top
    ax.add_patch(Rectangle((0, y_top - row_h), 1, row_h,
                           facecolor=INK, edgecolor="none", transform=ax.transAxes))
    for j, h in enumerate(headers):
        ax.text(col_lefts[j] + col_widths[j] / 2, y_top - row_h / 2, h,
                ha="center", va="center", color="white", fontsize=10,
                fontweight="bold", transform=ax.transAxes)

    # Status color mapping (subtle accent)
    status_colors = {
        "Preprint match,\npending peer review": "#F0EBE0",
        "Floor satisfied\n(measured >> floor)": "#E8F0E5",
        "Design target;\nnot a confirmed match": "#F8EFEA",
        "Design target;\nopen Bogoliubov calc": "#F8EFEA",
        "Published match\n(within uncertainty)": "#E8F0E5",
    }

    for i, row in enumerate(rows):
        y = y_top - row_h * (i + 2)
        bg = "#FBFAF7" if i % 2 == 0 else "white"
        ax.add_patch(Rectangle((0, y), 1, row_h, facecolor=bg, edgecolor="none",
                               transform=ax.transAxes))
        # status cell tinted
        ax.add_patch(Rectangle((col_lefts[3], y), col_widths[3], row_h,
                               facecolor=status_colors[row[3]], edgecolor="none",
                               transform=ax.transAxes))
        for j, cell in enumerate(row):
            color = INK
            weight = "normal"
            if j == 0:
                weight = "bold"
            ax.text(col_lefts[j] + col_widths[j] / 2, y + row_h / 2, cell,
                    ha="center", va="center", color=color, fontsize=9,
                    fontweight=weight, transform=ax.transAxes)

    # Border
    ax.add_patch(Rectangle((0, table_top - row_h * n_rows), 1, row_h * n_rows,
                           facecolor="none", edgecolor=INK, linewidth=0.8,
                           transform=ax.transAxes))

    # Title
    ax.text(0.5, 0.97, "Predictions × empirical anchors × evidential status",
            ha="center", va="top", fontsize=11.5, fontweight="bold",
            color=INK, transform=ax.transAxes)
    ax.text(0.5, 0.10,
            "Figure 3. Summary of the four predictions of §4 and their current evidential status.\n"
            "All four predictions are labeled Conjecture (not theorem) in the manuscript.",
            ha="center", va="top", fontsize=8.5, color=MUTED, style="italic",
            transform=ax.transAxes)

    fig.savefig(f"{OUT}/figure3_predictions_table.png", facecolor="white")
    fig.savefig(f"{OUT}/figure3_predictions_table.pdf", facecolor="white")
    plt.close(fig)
    print("Figure 3 written.")


# =====================================================================
# Figure 4 — σ_pred = 0.9796 vs Wilting-Priesemann awake-cortex distribution
# =====================================================================
def figure_4():
    fig, ax = plt.subplots(figsize=(7.4, 5.0))

    # Schematic distribution centered at 0.98 with sd ~ 0.015 — represents
    # the published Wilting-Priesemann awake-rat-cortex range.
    rng = np.random.default_rng(42)
    samples = rng.normal(loc=0.98, scale=0.015, size=4000)

    bins = np.linspace(0.90, 1.04, 60)
    ax.hist(samples, bins=bins, color="#D4D1CA", edgecolor=INK,
            linewidth=0.4, alpha=0.85,
            label="Wilting & Priesemann 2018, σ ≈ 0.98 (schematic)")

    sigma_pred = 1 - 1 / 49
    ax.axvline(sigma_pred, color=ACCENT, linewidth=2.0,
               label=f"σ_pred = 1 − 1/49 ≈ {sigma_pred:.4f}  (G₂ conjecture, §4.4)")

    ax.axvline(1.0, color=MUTED, linewidth=1.0, linestyle=(0, (4, 3)),
               label="σ = 1 (critical / corpus-level Hengen-Shew)")

    # Annotate σ_pred to the right side (away from legend box)
    ax.annotate(f"σ_pred ≈ {sigma_pred:.4f}",
                xy=(sigma_pred, 200),
                xytext=(sigma_pred + 0.012, 230),
                color=ACCENT, fontsize=10, ha="left", va="bottom",
                arrowprops=dict(arrowstyle="-", color=ACCENT, lw=0.8))

    ax.set_xlim(0.90, 1.04)
    ax.set_ylim(0, 320)
    ax.set_xlabel("Branching ratio σ")
    ax.set_ylabel("Frequency (schematic distribution)")
    ax.set_title("Prediction (d): σ_pred vs awake-cortex empirical anchor",
                 fontsize=11.5, fontweight="bold", pad=10)
    ax.legend(loc="upper left", fontsize=8.5)

    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)

    # Caption strictly below axes
    fig.text(0.5, 0.02,
             "Figure 4. The G₂ prediction σ_pred ≈ 0.9796 against an illustrative distribution centered at the Wilting & Priesemann (2018)\n"
             "awake-rat-cortex value σ ≈ 0.98 (subsampling-corrected, multiscale regression estimator). The histogram is a schematic\n"
             "representation of the published value and its stated uncertainty, not raw data; current measurement precision does not\n"
             "yet distinguish σ_pred from σ = 1 with high confidence. Per-dataset reanalysis of the Hengen-Shew corpus (§6.3 Problem 3)\n"
             "is the strongest test.",
             ha="center", va="bottom", fontsize=7.8, color=MUTED, style="italic")

    plt.subplots_adjust(top=0.92, bottom=0.32, left=0.10, right=0.97)
    fig.savefig(f"{OUT}/figure4_sigma_prediction.png", facecolor="white", bbox_inches=None)
    fig.savefig(f"{OUT}/figure4_sigma_prediction.pdf", facecolor="white", bbox_inches=None)
    plt.close(fig)
    print("Figure 4 written.")


if __name__ == "__main__":
    figure_1()
    figure_2()
    figure_3()
    figure_4()
    print("All figures written to", OUT)
