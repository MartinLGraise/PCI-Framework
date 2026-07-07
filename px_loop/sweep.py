"""Small parameter sweep harness for PX-Loop Agent v0.1."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from .presets import PXPreset, get_preset
from .simulate import SimulationResult, run_and_save


@dataclass(frozen=True)
class SweepCase:
    """A reproducible perturbation of one preset's parameters."""

    name: str
    base_preset: str
    description: str
    parameter_updates: dict[str, float]


def _with_updates(base_name: str, name: str, description: str, updates: dict[str, float]) -> SweepCase:
    base = get_preset(base_name)
    return SweepCase(
        name=f"{base_name}__{name}",
        base_preset=base_name,
        description=description,
        parameter_updates={key: float(value) for key, value in updates.items() if key in base.parameters},
    )


def default_sweep_cases() -> tuple[SweepCase, ...]:
    """Conservative v0.1 sweep cases across both presets."""
    quiet = get_preset("quiet_loop")
    paradox = get_preset("paradox_amplification")

    return (
        _with_updates("quiet_loop", "baseline", "Unchanged quiet-loop baseline.", {}),
        _with_updates(
            "quiet_loop",
            "higher_reset",
            "Raises reset and silence feedback to test stronger PX-007 damping.",
            {
                "reset_pressure": quiet.parameters["reset_pressure"] * 1.30,
                "silence_feedback": quiet.parameters["silence_feedback"] * 1.20,
            },
        ),
        _with_updates(
            "quiet_loop",
            "higher_feedback",
            "Raises signal/utterance coupling to test PX-005/PX-006 sensitivity.",
            {
                "false_signal_gain": quiet.parameters["false_signal_gain"] * 1.35,
                "utterance_gain": quiet.parameters["utterance_gain"] * 1.35,
                "collapse_gain": quiet.parameters["collapse_gain"] * 1.25,
            },
        ),
        _with_updates(
            "quiet_loop",
            "damped_fracture",
            "Lowers fracture and false-signal gains to test settling behavior.",
            {
                "fracture_gain": quiet.parameters["fracture_gain"] * 0.70,
                "false_signal_gain": quiet.parameters["false_signal_gain"] * 0.75,
            },
        ),
        _with_updates(
            "paradox_amplification",
            "baseline",
            "Unchanged paradox-amplification baseline.",
            {},
        ),
        _with_updates(
            "paradox_amplification",
            "higher_reset",
            "Raises reset and silence feedback to test whether PX-007 suppresses oscillation.",
            {
                "reset_pressure": paradox.parameters["reset_pressure"] * 1.25,
                "silence_feedback": paradox.parameters["silence_feedback"] * 1.20,
            },
        ),
        _with_updates(
            "paradox_amplification",
            "higher_feedback",
            "Raises PX-005/PX-006 gains to test instability and bounded amplification.",
            {
                "false_signal_gain": paradox.parameters["false_signal_gain"] * 1.20,
                "utterance_gain": paradox.parameters["utterance_gain"] * 1.20,
                "collapse_gain": paradox.parameters["collapse_gain"] * 1.25,
            },
        ),
        _with_updates(
            "paradox_amplification",
            "damped_fracture",
            "Lowers fracture drive and raises reset pressure to test calmer trajectories.",
            {
                "fracture_gain": paradox.parameters["fracture_gain"] * 0.75,
                "false_signal_gain": paradox.parameters["false_signal_gain"] * 0.85,
                "reset_pressure": paradox.parameters["reset_pressure"] * 1.15,
            },
        ),
    )


def preset_for_case(case: SweepCase) -> PXPreset:
    base = get_preset(case.base_preset)
    parameters = dict(base.parameters)
    parameters.update(case.parameter_updates)
    return PXPreset(
        name=case.name,
        description=f"{base.description} Sweep variant: {case.description}",
        initial_state=base.initial_state,
        parameters=parameters,
    )


def write_sweep_index(results: Sequence[SimulationResult], cases: Sequence[SweepCase], output_dir: Path) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "sweep_index.json"
    csv_path = output_dir / "sweep_index.csv"

    case_by_name = {case.name: case for case in cases}
    rows = []
    for result in results:
        case = case_by_name[result.preset.name]
        rows.append(
            {
                "case": case.name,
                "base_preset": case.base_preset,
                "description": case.description,
                "classification": result.summary["classification"],
                "cycle_end_classification": result.summary["cycle_end"]["classification"],
                "cycle_end_final_delta": result.summary["cycle_end"]["final_delta"],
                "max_within_cycle_span": result.summary["cycle_end"]["max_within_cycle_span"],
                "record_count": result.summary["record_count"],
                "cycle_count": result.summary["cycle_count"],
                "summary_path": str(result.output_paths["summary"]),
                "csv_path": str(result.output_paths["csv"]),
                "plot_path": str(result.output_paths["plot"]),
                "parameter_updates": case.parameter_updates,
                "final_state": result.summary["final_state"],
            }
        )

    json_path.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "case",
            "base_preset",
            "description",
            "classification",
            "cycle_end_classification",
            "cycle_end_final_delta",
            "max_within_cycle_span",
            "record_count",
            "cycle_count",
            "summary_path",
            "csv_path",
            "plot_path",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row[key] for key in fieldnames})

    return {"json": json_path, "csv": csv_path}


def run_sweep(
    output_dir: str | Path = "outbox/ai_coordination/px_loop_runs/2026-07-07_sweeps",
    steps: int = 140,
    cases: Sequence[SweepCase] | None = None,
) -> tuple[Sequence[SimulationResult], dict[str, Path]]:
    """Run a small disciplined sweep batch and return run results plus index paths."""
    output_dir = Path(output_dir)
    cases = tuple(default_sweep_cases() if cases is None else cases)
    results = []
    for case in cases:
        result = run_and_save(
            preset=preset_for_case(case),
            steps=steps,
            output_dir=output_dir / case.name,
        )
        results.append(result)

    index_paths = write_sweep_index(results, cases, output_dir)
    return results, index_paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the PX-loop v0.1 parameter sweep batch.")
    parser.add_argument("--steps", type=int, default=140, help="full PX cycles per sweep case")
    parser.add_argument(
        "--output-dir",
        default="outbox/ai_coordination/px_loop_runs/2026-07-07_sweeps",
        help="directory where sweep case folders and sweep_index files are written",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    results, index_paths = run_sweep(output_dir=args.output_dir, steps=args.steps)
    print(f"Sweep cases: {len(results)}")
    for result in results:
        print(
            f"{result.preset.name}: {result.summary['classification']} "
            f"/ {result.summary['cycle_end']['classification']}"
        )
    print("Index files:")
    for name, path in index_paths.items():
        print(f"  {name}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
