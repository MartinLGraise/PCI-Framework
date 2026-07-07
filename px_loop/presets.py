"""Named parameter presets for the PX-loop simulator."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .model import PXState, default_initial_state


@dataclass(frozen=True)
class PXPreset:
    """Initial state and parameters for a reproducible PX-loop run."""

    name: str
    description: str
    initial_state: PXState
    parameters: Mapping[str, float]


QUIET_LOOP = PXPreset(
    name="quiet_loop",
    description="Low-gain preset for bounded convergence or weak oscillation.",
    initial_state=default_initial_state(),
    parameters={
        "fracture_gain": 0.09,
        "false_signal_coupling": 0.04,
        "access_gain": 0.12,
        "lock_gain": 0.12,
        "temporal_memory": 0.80,
        "false_signal_gain": 0.11,
        "false_signal_bias": 0.005,
        "utterance_gain": 0.14,
        "collapse_gain": 0.04,
        "silence_feedback": 0.12,
        "reset_pressure": 0.19,
        "false_signal_drain": 0.28,
        "access_drain": 0.09,
    },
)

PARADOX_AMPLIFICATION = PXPreset(
    name="paradox_amplification",
    description="Higher-gain preset that emphasizes PX-006 -> PX-007 -> PX-001 feedback.",
    initial_state=PXState(
        {
            "identity_split": 0.20,
            "access_recursion": 0.11,
            "contradiction_lock": 0.08,
            "temporal_feedback": 0.13,
            "false_signal": 0.12,
            "utterance_instability": 0.07,
            "silence_gain": 0.06,
        }
    ),
    parameters={
        "fracture_gain": 0.21,
        "false_signal_coupling": 0.12,
        "access_gain": 0.23,
        "lock_gain": 0.24,
        "lock_backpressure": 0.07,
        "temporal_memory": 0.66,
        "temporal_false_leak": 0.07,
        "false_signal_gain": 0.25,
        "false_signal_bias": 0.025,
        "utterance_gain": 0.30,
        "collapse_gain": 0.12,
        "coherence_floor": 0.13,
        "silence_feedback": 0.24,
        "reset_pressure": 0.22,
        "void_seed": 0.045,
        "false_signal_drain": 0.18,
        "access_drain": 0.07,
    },
)

PRESETS: dict[str, PXPreset] = {
    QUIET_LOOP.name: QUIET_LOOP,
    PARADOX_AMPLIFICATION.name: PARADOX_AMPLIFICATION,
}


def available_presets() -> tuple[str, ...]:
    return tuple(PRESETS)


def get_preset(name: str) -> PXPreset:
    try:
        return PRESETS[name]
    except KeyError as exc:
        options = ", ".join(available_presets())
        raise ValueError(f"unknown PX-loop preset {name!r}; choose one of: {options}") from exc
