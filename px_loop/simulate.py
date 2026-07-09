"""Simulation harness for PX-Loop Agent v0.1."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from .model import DIMENSIONS, PX_IDS, PXState
from .observer import (
    PXRecord,
    summarize_records,
    write_csv_log,
    write_summary_json,
    write_trajectory_png,
)
from .operators import OPERATORS, apply_operator
from .presets import PXPreset, get_preset


@dataclass(frozen=True)
class SimulationResult:
    """In-memory result and optional output paths for a PX-loop run."""

    preset: PXPreset
    records: Sequence[PXRecord]
    summary: dict[str, object]
    output_paths: dict[str, Path]


def _record(index: int, state: PXState, operator_name: str) -> PXRecord:
    return PXRecord(
        index=index,
        cycle=state.cycle,
        phase_index=state.phase_index,
        step_id=state.step_id,
        operator_name=operator_name,
        values={dimension: state.values[dimension] for dimension in DIMENSIONS},
    )


def run_simulation(preset: str | PXPreset = "quiet_loop", steps: int = 120) -> SimulationResult:
    """Run repeated composition of PX-001 through PX-007.

    ``steps`` counts full seven-operator cycles. Observer records are written
    after each PX operator, plus one initial row.
    """
    if steps < 1:
        raise ValueError("steps must be at least 1")

    preset_object = get_preset(preset) if isinstance(preset, str) else preset
    state = preset_object.initial_state
    records: list[PXRecord] = [_record(0, state, "initial")]

    for cycle in range(1, steps + 1):
        for operator in OPERATORS:
            state = apply_operator(state, operator, preset_object.parameters, cycle)
            records.append(_record(len(records), state, operator.name))

    summary = summarize_records(
        records,
        preset_object.name,
        run_config={
            "steps": steps,
            "dimensions": list(DIMENSIONS),
            "operators": list(PX_IDS),
            "initial_state": dict(preset_object.initial_state.values),
            "parameters": dict(preset_object.parameters),
        },
    )
    return SimulationResult(preset_object, records, summary, {})


def run_and_save(
    preset: str | PXPreset = "quiet_loop",
    steps: int = 120,
    output_dir: str | Path = "outbox/ai_coordination/px_loop_runs/latest",
) -> SimulationResult:
    """Run a simulation and write CSV, JSON summary, and PNG plot artifacts."""
    result = run_simulation(preset=preset, steps=steps)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = write_csv_log(result.records, output_dir / "trajectory.csv")
    summary_path = write_summary_json(result.summary, output_dir / "summary.json")
    title = f"PX-LOOP V0.1 - {result.preset.name.replace('_', ' ').upper()}"
    subtitle = (
        f"PER-OPERATOR: {str(result.summary['classification']).replace('_', ' ').upper()} | "
        f"CYCLE-END: {str(result.summary['cycle_end']['classification']).replace('_', ' ').upper()}"
    )
    plot_path = write_trajectory_png(
        result.records,
        output_dir / "trajectory.png",
        title=title,
        subtitle=subtitle,
    )

    return SimulationResult(
        preset=result.preset,
        records=result.records,
        summary=result.summary,
        output_paths={
            "csv": csv_path,
            "summary": summary_path,
            "plot": plot_path,
        },
    )
