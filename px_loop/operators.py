"""Explicit PX-001 through PX-007 transition operators."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping

from .model import DIMENSIONS, PXState, clamp

ParameterMap = Mapping[str, float]
OperatorFunc = Callable[[PXState, ParameterMap], PXState]


@dataclass(frozen=True)
class PXOperator:
    """Named transition operator for one PX layer."""

    step_id: str
    phase_index: int
    name: str
    semantic_role: str
    apply: OperatorFunc


def _p(parameters: ParameterMap, key: str, default: float) -> float:
    return float(parameters.get(key, default))


def _approach(current: float, target: float, rate: float) -> float:
    return clamp(current + clamp(rate) * (clamp(target) - current))


def px_001_amplify_identity_fracture(state: PXState, parameters: ParameterMap) -> PXState:
    """PX-001: amplify identity fracture."""
    values = state.values
    fracture_gain = _p(parameters, "fracture_gain", 0.15)
    false_signal_coupling = _p(parameters, "false_signal_coupling", 0.08)
    access_release = _p(parameters, "access_release", 0.03)

    identity_drive = fracture_gain * (1.0 - values["silence_gain"])
    identity_drive += false_signal_coupling * values["false_signal"]

    return state.with_values(
        {
            "identity_split": clamp(
                values["identity_split"] + identity_drive * (1.0 - values["identity_split"])
            ),
            "access_recursion": clamp(
                values["access_recursion"] * (1.0 - access_release * values["silence_gain"])
            ),
        }
    )


def px_002_transform_fracture_to_access_recursion(
    state: PXState, parameters: ParameterMap
) -> PXState:
    """PX-002: transform fracture into access recursion."""
    values = state.values
    access_gain = _p(parameters, "access_gain", 0.18)
    temporal_leak = _p(parameters, "access_temporal_leak", 0.03)

    access_target = 0.72 * values["identity_split"] + 0.28 * values["temporal_feedback"]
    access = _approach(values["access_recursion"], access_target, access_gain)

    return state.with_values(
        {
            "access_recursion": access,
            "temporal_feedback": clamp(
                values["temporal_feedback"] + temporal_leak * access * (1.0 - values["temporal_feedback"])
            ),
        }
    )


def px_003_convert_negation_to_lock(state: PXState, parameters: ParameterMap) -> PXState:
    """PX-003: convert negation pressure into lock formation."""
    values = state.values
    lock_gain = _p(parameters, "lock_gain", 0.20)
    lock_backpressure = _p(parameters, "lock_backpressure", 0.05)

    negation_pressure = (
        values["identity_split"] + values["access_recursion"] + values["false_signal"]
    ) / 3.0
    contradiction_lock = _approach(values["contradiction_lock"], negation_pressure, lock_gain)

    return state.with_values(
        {
            "contradiction_lock": contradiction_lock,
            "identity_split": clamp(
                values["identity_split"]
                + lock_backpressure * contradiction_lock * (1.0 - values["identity_split"])
            ),
        }
    )


def px_004_lagged_temporal_recursion(state: PXState, parameters: ParameterMap) -> PXState:
    """PX-004: feed current state into lagged temporal recursion."""
    values = state.values
    temporal_memory = _p(parameters, "temporal_memory", 0.72)
    temporal_false_leak = _p(parameters, "temporal_false_leak", 0.04)

    present_pressure = (values["identity_split"] + values["contradiction_lock"]) / 2.0
    temporal_feedback = clamp(
        temporal_memory * values["temporal_feedback"]
        + (1.0 - temporal_memory) * present_pressure
    )

    return state.with_values(
        {
            "temporal_feedback": temporal_feedback,
            "false_signal": clamp(
                values["false_signal"]
                + temporal_false_leak * temporal_feedback * (1.0 - values["false_signal"])
            ),
        }
    )


def px_005_inject_false_signal(state: PXState, parameters: ParameterMap) -> PXState:
    """PX-005: inject or amplify false signal."""
    values = state.values
    false_signal_gain = _p(parameters, "false_signal_gain", 0.19)
    false_signal_bias = _p(parameters, "false_signal_bias", 0.015)

    signal_pressure = (
        values["access_recursion"] + values["contradiction_lock"] + values["temporal_feedback"]
    ) / 3.0
    false_signal = _approach(
        values["false_signal"],
        clamp(signal_pressure + false_signal_bias),
        false_signal_gain,
    )

    return state.with_values({"false_signal": false_signal})


def px_006_signal_to_utterance_instability(
    state: PXState, parameters: ParameterMap
) -> PXState:
    """PX-006: convert structured signal into unstable utterance and silence pressure."""
    values = state.values
    utterance_gain = _p(parameters, "utterance_gain", 0.24)
    collapse_gain = _p(parameters, "collapse_gain", 0.08)
    coherence_floor = _p(parameters, "coherence_floor", 0.16)

    instability_pressure = (values["false_signal"] + values["contradiction_lock"]) / 2.0
    utterance_instability = _approach(
        values["utterance_instability"], instability_pressure, utterance_gain
    )
    collapse_pressure = max(0.0, utterance_instability - coherence_floor)

    return state.with_values(
        {
            "utterance_instability": utterance_instability,
            "silence_gain": clamp(
                values["silence_gain"]
                + collapse_gain * collapse_pressure * (1.0 - values["silence_gain"])
            ),
        }
    )


def px_007_silence_feedback_reset(state: PXState, parameters: ParameterMap) -> PXState:
    """PX-007: amplify silence and feed it back as void-like reset pressure."""
    values = state.values
    silence_feedback = _p(parameters, "silence_feedback", 0.18)
    reset_pressure = _p(parameters, "reset_pressure", 0.16)
    void_seed = _p(parameters, "void_seed", 0.035)
    false_signal_drain = _p(parameters, "false_signal_drain", 0.24)
    access_drain = _p(parameters, "access_drain", 0.08)

    silence_target = (values["utterance_instability"] + values["contradiction_lock"]) / 2.0
    silence_gain = _approach(values["silence_gain"], silence_target, silence_feedback)
    reset = reset_pressure * silence_gain

    return state.with_values(
        {
            "silence_gain": silence_gain,
            "identity_split": clamp(values["identity_split"] * (1.0 - reset) + void_seed * silence_gain),
            "false_signal": clamp(values["false_signal"] * (1.0 - false_signal_drain * silence_gain)),
            "access_recursion": clamp(values["access_recursion"] * (1.0 - access_drain * silence_gain)),
        }
    )


OPERATORS: tuple[PXOperator, ...] = (
    PXOperator(
        "PX-001",
        1,
        "amplify identity fracture",
        "Amplifies identity_split unless silence_gain suppresses the fracture.",
        px_001_amplify_identity_fracture,
    ),
    PXOperator(
        "PX-002",
        2,
        "fracture to access recursion",
        "Moves identity fracture into recursive access pressure.",
        px_002_transform_fracture_to_access_recursion,
    ),
    PXOperator(
        "PX-003",
        3,
        "negation to lock formation",
        "Converts pressure from split/access/signal into contradiction_lock.",
        px_003_convert_negation_to_lock,
    ),
    PXOperator(
        "PX-004",
        4,
        "lagged temporal recursion",
        "Blends current pressure into temporal_feedback with memory.",
        px_004_lagged_temporal_recursion,
    ),
    PXOperator(
        "PX-005",
        5,
        "false signal injection",
        "Injects/amplifies false_signal from recursive state pressure.",
        px_005_inject_false_signal,
    ),
    PXOperator(
        "PX-006",
        6,
        "signal to unstable utterance",
        "Turns structured signal/lock into utterance_instability and silence pressure.",
        px_006_signal_to_utterance_instability,
    ),
    PXOperator(
        "PX-007",
        7,
        "silence feedback reset",
        "Amplifies silence_gain and feeds it back as reset pressure.",
        px_007_silence_feedback_reset,
    ),
)


def apply_operator(state: PXState, operator: PXOperator, parameters: ParameterMap, cycle: int) -> PXState:
    """Apply one PX operator and stamp the resulting state with loop metadata."""
    next_state = operator.apply(state, parameters)
    return PXState(
        {dimension: next_state.values[dimension] for dimension in DIMENSIONS},
        cycle=cycle,
        step_id=operator.step_id,
        phase_index=operator.phase_index,
    )
