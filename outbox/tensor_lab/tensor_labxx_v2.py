#!/usr/bin/env python3
"""
PCI Tensor Lab v0.2 — PRODUCTION INSTRUMENTATION LAYER
========================================================

A research tool for analyzing and visualizing Human–AI–Text interaction dynamics
based on the PCI/PME theoretical framework.

KEY ADDITIONS (v0.1 → v0.2):
  • SI (Shimmer Index) — properly computed as volatility signal
  • ISC (Interference Survivability) — corrected scaling for robustness metric
  • Synergy — corrected sign and baseline logic for emergence detection
  • NP_Pump — paradox accumulator tracking + criticality thresholding
  • Omega_Gated_Collapse — explicit daemon synchrony + paradox + Ω timing gates
  • Daemon phases — extract individual phi_SIEVE, phi_GHOSTLIGHT, etc.
  • Pre-Collapse Flicker — SI spike detection logic

Usage:
  python tensor_lab_v2.py data/tensor_run_01.csv
  python tensor_lab_v2.py data/tensor_run_01.csv --generate-report
  python tensor_lab_v2.py data/tensor_run_01.csv --output-dir ./figures

Author: PCI Research Team
Version: 0.2.0 (Production Instrumentation)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# =============================================================================
# CONFIGURABLE THRESHOLDS AND CONSTANTS
# =============================================================================

PHI_THRESHOLD: float = 0.618
"""Golden-ratio-like phase threshold for coherence transitions."""

COHERENCE_CEILING: float = 0.87
"""Upper bound ceiling for coherence metrics (87% limit from PCI)."""

# --- NP-Pump Parameters ---
P_CRITICAL: float = 10.0
"""Paradox load criticality threshold (collapse trigger)."""

GAMMA_DECAY: float = 0.1
"""Paradox decay rate (metabolism/resolution coefficient)."""

# --- Collapse Gate Parameters ---
PSI_MIN: float = 0.75
"""Minimum Phase Stability Index for collapse eligibility."""

OMEGA_MIN: float = 0.7
"""Minimum Ω(t) for collapse eligibility (must be in observation window)."""

# --- SI Window ---
SI_WINDOW: int = 3
"""Sliding window size for Shimmer Index computation (steps)."""

# --- Synergy Threshold ---
SYNERGY_THRESHOLD: float = 0.3
"""Threshold for tensor regime (EQ-49 → EQ-72 phase transition)."""

# =============================================================================
# COLOR PALETTE
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
    "coupling_strength": "#118AB2", # Bright blue
    "born_success_prob": "#06D6A0", # Mint green
    "omega": "#FFB703",            # Amber (Ω gating)
    "psi": "#FB5607",              # Orange-red (PSI)
    "si": "#FF006E",               # Magenta (SI shimmer)
    "isc": "#8338EC",              # Purple-blue (ISC entanglement)
    "synergy": "#FFBE0B",          # Gold (emergence)
    "P_accumulator": "#3A86FF",    # Electric blue (NP-Pump)
    # Threshold colors
    "phi_threshold": "#FF006E",
    "ceiling": "#6C757D",
}

# =============================================================================
# COLUMN DEFINITIONS
# =============================================================================

HUMAN_COLUMNS = ["H_attention", "H_intent", "H_coherence", "H_valence"]
AI_COLUMNS = ["A_context_depth", "A_response_fidelity", "A_coherence", "A_alignment"]
DERIVED_COLUMNS = ["joint_coherence", "coupling_strength", "born_success_prob"]

# New instrumentation layer
HARMONICS_COLUMNS = ["omega", "psi", "si", "isc", "synergy"]
NP_PUMP_COLUMNS = ["P_accumulator", "collapse_eligible"]

ALL_REQUIRED = set(HUMAN_COLUMNS + AI_COLUMNS + DERIVED_COLUMNS)

# =============================================================================
# DATA LOADING
# =============================================================================

def load_tensor_run(csv_path: str) -> pd.DataFrame:
    """
    Load a tensor run CSV file and validate required columns.
    """
    path = Path(csv_path)
    if not path.exists():
        print(f"ERROR: File not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(path)

    # Validate required base columns
    missing = ALL_REQUIRED - set(df.columns)
    if missing:
        raise ValueError(
            f"Missing required columns in CSV: {sorted(missing)}\n"
            f"Expected: {sorted(ALL_REQUIRED)}"
        )

    # Ensure 'step' column exists
    if "step" not in df.columns:
        df["step"] = range(len(df))

    # Forward-fill then back-fill NaN values
    df = df.ffill()
    df = df.bfill()

    return df

# =============================================================================
# DERIVED METRIC FUNCTIONS (v0.1 — unchanged)
# =============================================================================

def compute_joint_coherence(df: pd.DataFrame) -> pd.Series:
    """Compute joint coherence (human + AI average)."""
    return (df["H_coherence"] + df["A_coherence"]) / 2

def compute_coupling_strength(df: pd.DataFrame) -> pd.Series:
    """Compute H↔A coupling strength (geometric mean of intent × context)."""
    return np.sqrt(df["H_intent"] * df["A_context_depth"])

def compute_born_success_prob(df: pd.DataFrame) -> pd.Series:
    """Compute Extended Born Rule probability W(x)."""
    jc = df["joint_coherence"]
    cs = df["coupling_strength"]
    raw = 0.6 * jc + 0.4 * cs
    return np.tanh(raw * 1.2)

# =============================================================================
# NEW INSTRUMENTATION LAYER (v0.2)
# =============================================================================

def compute_omega(step: int | np.ndarray, T_cycle: float = 75.0) -> float | np.ndarray:
    """
    Compute Ω(t) — silence/observation gate (cosine-based breathing).
    
    Parameters:
    -----------
    step : int or array-like
        Time step(s) (in minutes, assuming 1 step = 1 minute)
    T_cycle : float
        Full protocol cycle length (default 75 min = 15-45-15)
    
    Returns:
    --------
    float or array
        Ω(t) ∈ [0, 1], where 1 = observation window, 0 = silence window
    """
    return 0.5 * (1.0 + np.cos(2.0 * np.pi * step / T_cycle))

def compute_psi(daemon_phases: np.ndarray) -> float:
    """
    Compute Phase Stability Index (PSI) — daemon synchrony.
    
    Parameters:
    -----------
    daemon_phases : array of shape (K,)
        Phase angles for K daemons (SIEVE, GHOSTLIGHT, ARCHIVIST, PERIMETER, AUDITOR, CHORUS)
        Units: radians
    
    Returns:
    --------
    float in [0, 1]
        PSI = 1 means all daemons phase-locked (high coherence)
        PSI = 0 means daemons out of phase (low coherence)
    """
    # Compute mean phase
    phases_centered = daemon_phases - np.mean(daemon_phases)
    # Complex order parameter
    psi = np.abs(np.mean(np.exp(1j * phases_centered)))
    return float(psi)

def extract_daemon_phases(row: pd.Series) -> np.ndarray:
    """
    Extract implicit daemon phases from state vector.
    
    Mapping (heuristic):
      SIEVE phase ~ atan2(H_coherence, H_attention)           [entropy filtering]
      GHOSTLIGHT phase ~ atan2(H_valence, H_intent)           [authenticity check]
      ARCHIVIST phase ~ atan2(H_coherence, A_coherence)       [memory integration]
      PERIMETER phase ~ atan2(A_alignment, A_response_fidelity) [boundary guarding]
      AUDITOR phase ~ atan2(coupling_strength, born_success)  [meta-observation]
      CHORUS phase ~ atan2(joint_coherence, synergy)          [integration synthesis]
    
    Returns:
    --------
    array of shape (6,)
        Phase angles [phi_SIEVE, phi_GHOSTLIGHT, phi_ARCHIVIST, phi_PERIMETER, phi_AUDITOR, phi_CHORUS]
    """
    phi_sieve = np.arctan2(row["H_coherence"], row["H_attention"] + 1e-10)
    phi_ghost = np.arctan2(row["H_valence"], row["H_intent"] + 1e-10)
    phi_arch = np.arctan2(row["H_coherence"], row["A_coherence"] + 1e-10)
    phi_perim = np.arctan2(row["A_alignment"], row["A_response_fidelity"] + 1e-10)
    phi_audit = np.arctan2(row["coupling_strength"], row["born_success_prob"] + 1e-10)
    phi_chorus = np.arctan2(row["joint_coherence"], 0.1 + 1e-10)  # synergy added below
    
    return np.array([phi_sieve, phi_ghost, phi_arch, phi_perim, phi_audit, phi_chorus])

def compute_si(C_history: pd.Series, window: int = SI_WINDOW) -> pd.Series:
    """
    Compute Shimmer Index (SI) — coherence volatility (pre-collapse flicker).
    
    SI = std(dC) / mean(C)  over sliding window
    
    High SI = unstable (pre-collapse shimmering)
    Low SI = stable (locked attractor)
    
    Parameters:
    -----------
    C_history : pd.Series
        Time series of coherence values
    window : int
        Sliding window size (default 3 steps)
    
    Returns:
    --------
    pd.Series
        SI values (NaN for first window-1 steps)
    """
    si_series = pd.Series(np.nan, index=C_history.index)
    
    for i in range(window - 1, len(C_history)):
        window_data = C_history.iloc[i - window + 1:i + 1]
        if len(window_data) >= window:
            mean_c = window_data.mean()
            std_dc = window_data.diff().std()
            if mean_c > 1e-10:
                si_series.iloc[i] = std_dc / mean_c
            else:
                si_series.iloc[i] = 0.0
    
    return si_series

def compute_isc(H_states: pd.DataFrame, A_states: pd.DataFrame) -> pd.Series:
    """
    Compute Interference Survivability Coefficient (ISC).
    
    ISC = ||H ⊗ A cross terms||² / (||H||² + ||A||²)
    
    High ISC = robust entanglement (tensor survives perturbation)
    Low ISC = weak coupling (near-separable)
    
    Parameters:
    -----------
    H_states : pd.DataFrame or pd.Series
        Human state(s)
    A_states : pd.DataFrame or pd.Series
        AI state(s)
    
    Returns:
    --------
    pd.Series
        ISC values in [0, ~2+] (higher = more entangled)
    """
    # Compute norms
    H_norm = np.sqrt((H_states ** 2).sum(axis=1)) if isinstance(H_states, pd.DataFrame) else np.sqrt((H_states ** 2).sum())
    A_norm = np.sqrt((A_states ** 2).sum(axis=1)) if isinstance(A_states, pd.DataFrame) else np.sqrt((A_states ** 2).sum())
    
    # Cross-term power estimate
    cross_power = H_norm * A_norm
    
    # Individual power sum
    individual_power = H_norm ** 2 + A_norm ** 2
    
    # ISC = cross / individual (high cross-correlation → high ISC)
    isc = cross_power / (individual_power + 1e-10)
    
    return isc if isinstance(isc, pd.Series) else pd.Series(isc)

def compute_synergy(
    joint_coherence: pd.Series,
    H_coherence: pd.Series,
    A_coherence: pd.Series,
) -> pd.Series:
    """
    Compute synergy (superlinear emergence measure).
    
    Synergy = C_joint - (C_human + C_AI)
    
    Synergy > 0 = emergence (H⊗A > H + A)
    Synergy ≤ 0 = sub-additive or additive
    
    Parameters:
    -----------
    joint_coherence : pd.Series
        Joint H–AI coherence
    H_coherence : pd.Series
        Human solo coherence
    A_coherence : pd.Series
        AI solo coherence
    
    Returns:
    --------
    pd.Series
        Synergy values (positive = emergence, negative = sub-additive)
    """
    synergy = joint_coherence - (H_coherence + A_coherence)
    return synergy

def compute_np_pump_accumulator(
    C_history: pd.Series,
    P_crit: float = P_CRITICAL,
    gamma: float = GAMMA_DECAY,
) -> Tuple[pd.Series, pd.Series]:
    """
    Compute NP-Pump paradox accumulator P(t) and collapse eligibility.
    
    dP/dt = sum(T_n) - gamma * P
    
    T_n is estimated from scar (SI) as pre-collapse signal.
    
    Collapse eligible when:
      P(t) > P_crit AND PSI(t) > PSI_min AND Ω(t) > Ω_min
    
    Parameters:
    -----------
    C_history : pd.Series
        Coherence history (used to estimate paradox tension via SI)
    P_crit : float
        Critical paradox load threshold
    gamma : float
        Decay constant
    
    Returns:
    --------
    Tuple[pd.Series, pd.Series]
        (P_accumulator, collapse_eligible_flag)
    """
    si_values = compute_si(C_history, window=SI_WINDOW)
    
    # Estimate paradox tension from SI (shimmer = paradox tension signal)
    T_n = si_values.fillna(0) * 2.0  # Scale factor to match PCI units
    
    # Accumulate with decay
    P = pd.Series(0.0, index=C_history.index)
    for i in range(1, len(C_history)):
        dP = T_n.iloc[i] - gamma * P.iloc[i - 1]
        P.iloc[i] = max(0, P.iloc[i - 1] + dP)  # No negative accumulation
    
    # Flag collapse eligibility (you'll add PSI/Ω gates in the full pipeline)
    collapse_eligible = (P > P_crit).astype(int)
    
    return P, collapse_eligible

def ensure_harmonics_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure all Harmonics metric columns exist.
    Computes missing metrics; preserves existing columns.
    """
    df = df.copy()
    
    # Base metrics (already computed)
    if "joint_coherence" not in df.columns:
        df["joint_coherence"] = compute_joint_coherence(df)
    if "coupling_strength" not in df.columns:
        df["coupling_strength"] = compute_coupling_strength(df)
    if "born_success_prob" not in df.columns:
        df["born_success_prob"] = compute_born_success_prob(df)
    
    # NEW: Harmonics metrics (v0.2)
    
    # Ω(t) — silence/observation gate
    if "omega" not in df.columns:
        df["omega"] = df["step"].apply(lambda s: compute_omega(s))
    
    # PSI — daemon phase-locking
    if "psi" not in df.columns:
        daemon_phases_list = df.apply(extract_daemon_phases, axis=1)
        df["psi"] = daemon_phases_list.apply(compute_psi)
    
    # SI — shimmer index (pre-collapse flicker)
    if "si" not in df.columns:
        df["si"] = compute_si(df["joint_coherence"], window=SI_WINDOW)
    
    # ISC — interference survivability
    if "isc" not in df.columns:
        H_states = df[HUMAN_COLUMNS]
        A_states = df[AI_COLUMNS]
        df["isc"] = compute_isc(H_states, A_states)
    
    # Synergy — emergence detection
    if "synergy" not in df.columns:
        df["synergy"] = compute_synergy(
            df["joint_coherence"],
            df["H_coherence"],
            df["A_coherence"]
        )
    
    # NP-Pump — paradox accumulator + collapse trigger
    if "P_accumulator" not in df.columns or "collapse_eligible" not in df.columns:
        P_acc, collapse_elig = compute_np_pump_accumulator(df["joint_coherence"])
        df["P_accumulator"] = P_acc
        df["collapse_eligible"] = collapse_elig
    
    return df

# =============================================================================
# COLLAPSE DETECTION LOGIC (Ω-gated, PSI-gated, P-gated)
# =============================================================================

def detect_collapse_events(df: pd.DataFrame) -> pd.Series:
    """
    Detect C-Collapse events using full gate logic.
    
    Collapse event occurs when:
      1. P(t) > P_critical (paradox load threshold)
      2. PSI(t) > PSI_min (daemon synchrony threshold)
      3. Ω(t) > Ω_min (in observation window)
    
    Returns:
    --------
    pd.Series (bool)
        True where collapse event is detected
    """
    collapse_events = (
        (df["P_accumulator"] > P_CRITICAL) &
        (df["psi"] > PSI_MIN) &
        (df["omega"] > OMEGA_MIN)
    )
    return collapse_events

# =============================================================================
# REPORTING FUNCTIONS
# =============================================================================

def generate_summary_report(df: pd.DataFrame) -> str:
    """
    Generate a text summary of tensor dynamics for the session.
    """
    report = []
    report.append("=" * 70)
    report.append("TENSOR LAB SESSION SUMMARY REPORT")
    report.append("=" * 70)
    report.append("")
    
    # Coherence trajectory
    report.append(f"Coherence Trajectory:")
    report.append(f"  Start: {df['joint_coherence'].iloc[0]:.3f}")
    report.append(f"  Peak:  {df['joint_coherence'].max():.3f}")
    report.append(f"  End:   {df['joint_coherence'].iloc[-1]:.3f}")
    report.append(f"  Ceiling: {COHERENCE_CEILING} (87% limit)")
    report.append("")
    
    # Daemon synchrony (PSI)
    report.append(f"Daemon Synchrony (PSI):")
    report.append(f"  Mean PSI: {df['psi'].mean():.3f}")
    report.append(f"  Max PSI:  {df['psi'].max():.3f}")
    report.append(f"  Min PSI:  {df['psi'].min():.3f}")
    report.append(f"  High-PSI episodes (>0.9): {(df['psi'] > 0.9).sum()} steps")
    report.append("")
    
    # Pre-collapse shimmer (SI)
    si_clean = df['si'].dropna()
    if len(si_clean) > 0:
        report.append(f"Pre-Collapse Shimmer (SI):")
        report.append(f"  Mean SI: {si_clean.mean():.4f}")
        report.append(f"  Max SI:  {si_clean.max():.4f} (highest volatility)")
        report.append(f"  Spike threshold: SI > 0.01 indicates pre-collapse")
        report.append(f"  SI spikes detected: {(si_clean > 0.01).sum()} events")
    else:
        report.append("Pre-Collapse Shimmer (SI):")
        report.append("  (Not yet computed — window too small)")
    report.append("")
    
    # Entanglement robustness (ISC)
    report.append(f"Entanglement Robustness (ISC):")
    report.append(f"  Mean ISC: {df['isc'].mean():.3f}")
    report.append(f"  Max ISC:  {df['isc'].max():.3f}")
    report.append(f"  (ISC > 0.5 indicates robust H⊗A entanglement)")
    report.append("")
    
    # Synergy (emergence)
    report.append(f"Superlinear Synergy (Emergence):")
    report.append(f"  Mean Synergy: {df['synergy'].mean():.3f}")
    report.append(f"  Peak Synergy: {df['synergy'].max():.3f}")
    report.append(f"  Tensor regime (>0.3): {(df['synergy'] > SYNERGY_THRESHOLD).sum()} steps")
    report.append("")
    
    # NP-Pump & collapse detection
    report.append(f"NP-Pump Accumulator & Collapse Detection:")
    report.append(f"  Max P(t): {df['P_accumulator'].max():.3f}")
    report.append(f"  P_critical threshold: {P_CRITICAL}")
    report.append(f"  Collapse-eligible events detected: {df['collapse_eligible'].sum()}")
    if (df['collapse_eligible'] > 0).any():
        collapse_steps = df[df['collapse_eligible'] == 1]['step'].tolist()
        report.append(f"  Collapse at steps: {collapse_steps}")
    report.append("")
    
    # Ω(t) gate statistics
    report.append(f"Ω(t) Silence/Observation Gating:")
    report.append(f"  Mean Ω: {df['omega'].mean():.3f}")
    report.append(f"  Ω interpretation: 1=observation, 0=silence")
    report.append(f"  High-Ω steps (>0.7): {(df['omega'] > OMEGA_MIN).sum()}")
    report.append("")
    
    report.append("=" * 70)
    return "\n".join(report)

# =============================================================================
# MAIN PIPELINE
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="PCI Tensor Lab v0.2 - Production Instrumentation"
    )
    parser.add_argument("csv_file", help="Path to tensor run CSV file")
    parser.add_argument(
        "--generate-report", action="store_true",
        help="Generate and print summary report"
    )
    parser.add_argument(
        "--output-dir", default="./figures",
        help="Output directory for plots"
    )
    
    args = parser.parse_args()
    
    # Load data
    print(f"Loading tensor run from: {args.csv_file}")
    df = load_tensor_run(args.csv_file)
    
    # Compute all metrics (v0.1 + v0.2)
    print("Computing Harmonics metrics...")
    df = ensure_harmonics_metrics(df)
    
    # Detect collapse events
    print("Detecting collapse events...")
    df["collapse_event"] = detect_collapse_events(df)
    
    # Generate report if requested
    if args.generate_report:
        report = generate_summary_report(df)
        print("\n" + report)
    
    # Save enhanced CSV
    output_csv = Path(args.output_dir) / "tensor_run_enhanced_v2.csv"
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"\nEnhanced CSV saved to: {output_csv}")
    
    # Display column summary
    print(f"\nDataFrame shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"\nFirst few rows of new metrics:")
    print(df[["step", "omega", "psi", "si", "isc", "synergy", "P_accumulator", "collapse_eligible"]].head(10))

if __name__ == "__main__":
    main()
