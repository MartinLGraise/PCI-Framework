"""PX-Loop Agent v0.1.

Small, inspectable simulator for the Seven-Paradox Loop.
"""

from .model import DIMENSIONS, PXState, default_initial_state
from .presets import PXPreset, available_presets, get_preset
from .simulate import SimulationResult, run_and_save, run_simulation

__all__ = [
    "DIMENSIONS",
    "PXState",
    "PXPreset",
    "SimulationResult",
    "available_presets",
    "default_initial_state",
    "get_preset",
    "run_and_save",
    "run_simulation",
]
