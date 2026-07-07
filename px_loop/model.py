"""Core state model for the PX-loop prototype."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

DIMENSIONS: tuple[str, ...] = (
    "identity_split",
    "access_recursion",
    "contradiction_lock",
    "temporal_feedback",
    "false_signal",
    "utterance_instability",
    "silence_gain",
)

PX_IDS: tuple[str, ...] = (
    "PX-001",
    "PX-002",
    "PX-003",
    "PX-004",
    "PX-005",
    "PX-006",
    "PX-007",
)

LOWER_BOUND = 0.0
UPPER_BOUND = 1.0


def clamp(value: float, lower: float = LOWER_BOUND, upper: float = UPPER_BOUND) -> float:
    """Clamp a scalar to the bounded state interval."""
    return max(lower, min(upper, float(value)))


def normalize_values(values: Mapping[str, float]) -> dict[str, float]:
    missing = [dimension for dimension in DIMENSIONS if dimension not in values]
    if missing:
        raise ValueError(f"missing PX state dimensions: {', '.join(missing)}")

    return {dimension: clamp(values[dimension]) for dimension in DIMENSIONS}


@dataclass(frozen=True)
class PXState:
    """Bounded seven-dimensional paradox state."""

    values: Mapping[str, float]
    cycle: int = 0
    step_id: str = "initial"
    phase_index: int = 0

    def __post_init__(self) -> None:
        object.__setattr__(self, "values", normalize_values(self.values))

    def with_values(
        self,
        updates: Mapping[str, float],
        *,
        cycle: int | None = None,
        step_id: str | None = None,
        phase_index: int | None = None,
    ) -> "PXState":
        values = dict(self.values)
        values.update(updates)
        return PXState(
            values,
            cycle=self.cycle if cycle is None else cycle,
            step_id=self.step_id if step_id is None else step_id,
            phase_index=self.phase_index if phase_index is None else phase_index,
        )

    def distance_to(self, other: "PXState") -> float:
        return max(abs(self.values[dimension] - other.values[dimension]) for dimension in DIMENSIONS)

    def as_row(self) -> dict[str, float | int | str]:
        row: dict[str, float | int | str] = {
            "cycle": self.cycle,
            "phase_index": self.phase_index,
            "step_id": self.step_id,
        }
        row.update({dimension: self.values[dimension] for dimension in DIMENSIONS})
        return row


def default_initial_state() -> PXState:
    """Low-energy starting point used when no preset is supplied."""
    return PXState(
        {
            "identity_split": 0.12,
            "access_recursion": 0.08,
            "contradiction_lock": 0.05,
            "temporal_feedback": 0.10,
            "false_signal": 0.06,
            "utterance_instability": 0.04,
            "silence_gain": 0.05,
        }
    )
