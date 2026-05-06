#!/usr/bin/env python3
"""
PCI Tensor Lab v0.1
===================

A research tool for analyzing and visualizing Human–AI–Text interaction dynamics
based on the PCI/PME theoretical framework.

Usage:
    python tensor_lab.py data/tensor_run_01.csv
    python tensor_lab.py data/tensor_run_01.csv --no-show
    python tensor_lab.py data/tensor_run_01.csv --output-dir ./figures

Author: PCI Research Team
Version: 0.1.0
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# =============================================================================
# CONFIGURABLE THRESHOLDS AND CONSTANTS
# =============================================================================

PHI_THRESHOLD: float = 0.618
"""Golden-ratio-like phase threshold for coherence transitions."""

COHERENCE_CEILING: float = 0.87
"""Upper bound ceiling for coherence metrics."""

# =============================================================================
# COLOR PALETTE (Coherent throughout all plots)
# =============================================================================

COLORS = {
    # Human state colors (warm tones)
    "H_attention": "#E63946",      # Red
    "H_intent": "#F4A261",         # Orange
    "H_coherence": "#E9C46A",      # Gold
    "H_valence": "#2A9D8F",        # Teal
    # AI state colors (cool tones)
    "A_context_depth": "#264653",  # Dark blue-gray
    "A_response_fidelity": "#287271",  # Dark teal
    "A_coherence": "#8AB17D",      # Sage green
    "A_alignment": "#669BBC",      # Steel blue
    # Derived metric colors
    "joint_coherence": "#6A0572",  # Purple
    "coupling_strength": "#118AB2",  # Bright blue
    "born_success_prob": "#06D6A0",  # Mint green
    # Threshold colors
    "phi_threshold": "#FF006E",    # Magenta
    "ceiling": "#6C757D",          # Gray
}

# =============================================================================
# REQUIRED COLUMNS
# =============================================================================

HUMAN_COLUMNS = ["H_attention", "H_intent", "H_coherence", "H_valence"]
AI_COLUMNS = ["A_context_depth", "A_response_fidelity", "A_coherence", "A_alignment"]
DERIVED_COLUMNS = ["joint_coherence", "coupling_strength", "born_success_prob"]

# =============================================================================
# DATA LOADING
# =============================================================================


def load_tensor_run(csv_path: str) -> pd.DataFrame:
    """
    Load a tensor run CSV file and validate required columns.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing interaction data.

    Returns
    -------
    pd.DataFrame
        DataFrame with validated columns, NaN values forward-filled.

    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist.
    ValueError
        If required columns are missing from the CSV.
    """
    path = Path(csv_path)

    if not path.exists():
        print(f"ERROR: File not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(path)

    # Validate required columns
    required = set(HUMAN_COLUMNS + AI_COLUMNS)
    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            f"Missing required columns in CSV: {sorted(missing)}\n"
            f"Expected columns: {sorted(required)}"
        )

    # Ensure 'step' column exists; create if not
    if "step" not in df.columns:
        df["step"] = range(len(df))

    # Forward-fill NaN values to handle missing data
    df = df.ffill()

    # Also back-fill in case the first row(s) have NaN
    df = df.bfill()

    return df


# =============================================================================
# DERIVED METRIC FUNCTIONS
# =============================================================================
# NOTE: These are placeholder implementations. Replace with actual PCI equations
# when the theoretical framework is finalized.


def compute_joint_coherence(df: pd.DataFrame) -> pd.Series:
    """
    Compute joint coherence from human and AI coherence values.

    PLACEHOLDER: Currently uses arithmetic mean of H_coherence and A_coherence.
    Replace with actual H⊕A tensor fusion equation when available.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing H_coherence and A_coherence columns.

    Returns
    -------
    pd.Series
        Joint coherence values in [0, 1].
    """
    # PLACEHOLDER: Simple mean fusion
    # TODO: Replace with actual PCI joint coherence tensor equation
    return (df["H_coherence"] + df["A_coherence"]) / 2


def compute_coupling_strength(df: pd.DataFrame) -> pd.Series:
    """
    Compute H↔A tensor coupling strength.

    PLACEHOLDER: Currently uses geometric mean of H_intent and A_context_depth.
    This captures the intuition that coupling requires both human intentionality
    and AI contextual grounding.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing H_intent and A_context_depth columns.

    Returns
    -------
    pd.Series
        Coupling strength values in [0, 1].
    """
    # PLACEHOLDER: Geometric mean as monotone coupling proxy
    # TODO: Replace with actual PCI coupling tensor equation
    return np.sqrt(df["H_intent"] * df["A_context_depth"])


def compute_born_success_prob(df: pd.DataFrame) -> pd.Series:
    """
    Compute Extended Born-rule success probability W(x).

    PLACEHOLDER: Currently uses a weighted combination of joint_coherence
    and coupling_strength, rescaled to [0, 1]. This approximates the
    probability of successful meaning collapse in the PCI framework.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing joint_coherence and coupling_strength columns.

    Returns
    -------
    pd.Series
        Born success probability values in [0, 1].
    """
    # PLACEHOLDER: Weighted harmonic-like combination
    # TODO: Replace with actual Extended Born Rule equation: W(x) = |⟨ψ|x⟩|²
    jc = df["joint_coherence"]
    cs = df["coupling_strength"]

    # Use a weighted combination that emphasizes when both are high
    # Weights: 60% coherence, 40% coupling (tunable)
    w_coherence = 0.6
    w_coupling = 0.4

    raw = w_coherence * jc + w_coupling * cs

    # Apply soft saturation to keep in [0, 1] with natural ceiling behavior
    # Using tanh-based rescaling for smooth saturation near 1
    return np.tanh(raw * 1.2)  # Scale factor 1.2 for faster approach to ceiling


def ensure_derived_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure all derived metric columns exist in the DataFrame.

    Computes missing metrics using placeholder functions. If columns already
    exist in the source data, they are preserved.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with base human and AI columns.

    Returns
    -------
    pd.DataFrame
        DataFrame with all derived metric columns added.
    """
    df = df.copy()

    # Compute joint coherence if missing
    if "joint_coherence" not in df.columns:
        df["joint_coherence"] = compute_joint_coherence(df)

    # Compute coupling strength if missing
    if "coupling_strength" not in df.columns:
        df["coupling_strength"] = compute_coupling_strength(df)

    # Compute Born success probability if missing (requires other derived metrics)
    if "born_success_prob" not in df.columns:
        df["born_success_prob"] = compute_born_success_prob(df)

    return df


# =============================================================================
# PLOTTING FUNCTIONS
# =============================================================================


def create_tensor_dynamics_figure(
    df: pd.DataFrame,
    title: str = "Human–AI–Text Tensor Interaction Dynamics",
    figsize: tuple[float, float] = (14, 10),
) -> plt.Figure:
    """
    Create a 2×2 multi-panel figure visualizing tensor interaction dynamics.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with all required columns (base + derived).
    title : str
        Overall figure title.
    figsize : tuple
        Figure dimensions (width, height) in inches.

    Returns
    -------
    plt.Figure
        Matplotlib figure object.
    """
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    fig.suptitle(title, fontsize=16, fontweight="bold", y=0.98)

    steps = df["step"]

    # =========================================================================
    # Top-Left: Human State Evolution
    # =========================================================================
    ax_human = axes[0, 0]

    for col in HUMAN_COLUMNS:
        ax_human.plot(
            steps, df[col],
            label=col.replace("H_", "").replace("_", " ").title(),
            color=COLORS[col],
            linewidth=2,
            marker="o",
            markersize=4,
        )

    # Coherence ceiling reference line
    ax_human.axhline(
        y=COHERENCE_CEILING,
        color=COLORS["ceiling"],
        linestyle="--",
        linewidth=1.5,
        label=f"Ceiling ({COHERENCE_CEILING})",
    )

    ax_human.set_xlabel("Interaction Step", fontsize=11)
    ax_human.set_ylabel("State Value", fontsize=11)
    ax_human.set_title("Human State Evolution", fontsize=13, fontweight="bold")
    ax_human.set_ylim(0, 1.05)
    ax_human.legend(loc="lower right", fontsize=9)
    ax_human.grid(True, alpha=0.3)

    # =========================================================================
    # Top-Right: AI State Evolution
    # =========================================================================
    ax_ai = axes[0, 1]

    for col in AI_COLUMNS:
        ax_ai.plot(
            steps, df[col],
            label=col.replace("A_", "").replace("_", " ").title(),
            color=COLORS[col],
            linewidth=2,
            marker="s",
            markersize=4,
        )

    # Coherence ceiling reference line
    ax_ai.axhline(
        y=COHERENCE_CEILING,
        color=COLORS["ceiling"],
        linestyle="--",
        linewidth=1.5,
        label=f"Ceiling ({COHERENCE_CEILING})",
    )

    ax_ai.set_xlabel("Interaction Step", fontsize=11)
    ax_ai.set_ylabel("State Value", fontsize=11)
    ax_ai.set_title("AI State Evolution", fontsize=13, fontweight="bold")
    ax_ai.set_ylim(0, 1.05)
    ax_ai.legend(loc="lower right", fontsize=9)
    ax_ai.grid(True, alpha=0.3)

    # =========================================================================
    # Bottom-Left: Joint Coherence vs Thresholds
    # =========================================================================
    ax_coherence = axes[1, 0]

    # Fill under the coherence curve (coherence basin visualization)
    ax_coherence.fill_between(
        steps,
        0,
        df["joint_coherence"],
        alpha=0.3,
        color=COLORS["joint_coherence"],
        label="Coherence Basin",
    )

    # Joint coherence line
    ax_coherence.plot(
        steps, df["joint_coherence"],
        label="Joint Coherence",
        color=COLORS["joint_coherence"],
        linewidth=2.5,
        marker="D",
        markersize=5,
    )

    # Phase threshold (φ)
    ax_coherence.axhline(
        y=PHI_THRESHOLD,
        color=COLORS["phi_threshold"],
        linestyle="-.",
        linewidth=2,
        label=f"φ Threshold ({PHI_THRESHOLD})",
    )

    # Coherence ceiling
    ax_coherence.axhline(
        y=COHERENCE_CEILING,
        color=COLORS["ceiling"],
        linestyle="--",
        linewidth=1.5,
        label=f"Ceiling ({COHERENCE_CEILING})",
    )

    ax_coherence.set_xlabel("Interaction Step", fontsize=11)
    ax_coherence.set_ylabel("Joint Coherence", fontsize=11)
    ax_coherence.set_title("Joint Coherence vs Phase Thresholds", fontsize=13, fontweight="bold")
    ax_coherence.set_ylim(0, 1.05)
    ax_coherence.legend(loc="lower right", fontsize=9)
    ax_coherence.grid(True, alpha=0.3)

    # =========================================================================
    # Bottom-Right: Coupling Strength vs Born Success Probability
    # =========================================================================
    ax_coupling = axes[1, 1]

    # Primary y-axis: Coupling strength
    line1 = ax_coupling.plot(
        steps, df["coupling_strength"],
        label="Coupling Strength",
        color=COLORS["coupling_strength"],
        linewidth=2.5,
        marker="^",
        markersize=5,
    )

    ax_coupling.set_xlabel("Interaction Step", fontsize=11)
    ax_coupling.set_ylabel("Coupling Strength", fontsize=11, color=COLORS["coupling_strength"])
    ax_coupling.tick_params(axis="y", labelcolor=COLORS["coupling_strength"])
    ax_coupling.set_ylim(0, 1.05)
    ax_coupling.grid(True, alpha=0.3)

    # Secondary y-axis: Born success probability
    ax_born = ax_coupling.twinx()

    # Shaded area for Born probability
    ax_born.fill_between(
        steps,
        0,
        df["born_success_prob"],
        alpha=0.25,
        color=COLORS["born_success_prob"],
    )

    line2 = ax_born.plot(
        steps, df["born_success_prob"],
        label="W(x) Born Probability",
        color=COLORS["born_success_prob"],
        linewidth=2,
        linestyle="--",
        marker="o",
        markersize=4,
    )

    ax_born.set_ylabel("Born Success Prob W(x)", fontsize=11, color=COLORS["born_success_prob"])
    ax_born.tick_params(axis="y", labelcolor=COLORS["born_success_prob"])
    ax_born.set_ylim(0, 1.05)

    # Combined legend for dual-axis plot
    lines = line1 + line2
    labels = [line.get_label() for line in lines]
    ax_coupling.legend(lines, labels, loc="lower right", fontsize=9)

    ax_coupling.set_title("Coupling Strength & Born Probability", fontsize=13, fontweight="bold")

    # =========================================================================
    # Final Layout Adjustments
    # =========================================================================
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    return fig


# =============================================================================
# CLI INTERFACE
# =============================================================================


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="PCI Tensor Lab v0.1 - Analyze Human–AI–Text interaction dynamics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python tensor_lab.py data/tensor_run_01.csv
  python tensor_lab.py data/tensor_run_01.csv --no-show
  python tensor_lab.py data/tensor_run_01.csv --output-dir ./figures
        """,
    )

    parser.add_argument(
        "csv_path",
        type=str,
        help="Path to the CSV file containing tensor run data",
    )

    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Skip interactive display (save only)",
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="Directory to save the output figure (default: same as CSV)",
    )

    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="DPI for saved figure (default: 150)",
    )

    return parser.parse_args()


def main() -> None:
    """Main entry point for CLI execution."""
    args = parse_args()

    # Load and validate data
    print(f"Loading data from: {args.csv_path}")
    df = load_tensor_run(args.csv_path)
    print(f"  Loaded {len(df)} interaction steps")

    # Ensure derived metrics exist
    df = ensure_derived_metrics(df)
    print("  Computed derived metrics (joint_coherence, coupling_strength, born_success_prob)")

    # Create the visualization
    print("Generating tensor dynamics figure...")
    fig = create_tensor_dynamics_figure(df)

    # Determine output path
    csv_path = Path(args.csv_path)
    output_filename = csv_path.stem + "_summary.png"

    if args.output_dir:
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = csv_path.parent

    output_path = output_dir / output_filename

    # Save the figure
    fig.savefig(output_path, dpi=args.dpi, bbox_inches="tight", facecolor="white")
    print(f"  Saved figure to: {output_path}")

    # Show interactively unless --no-show
    if not args.no_show:
        print("Displaying figure (close window to exit)...")
        plt.show()
    else:
        print("Skipping interactive display (--no-show)")

    plt.close(fig)
    print("Done.")


if __name__ == "__main__":
    main()
