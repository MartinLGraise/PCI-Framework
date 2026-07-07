"""Command-line runner for PX-Loop Agent v0.1."""

from __future__ import annotations

import argparse
import json

from .presets import PXPreset, available_presets, get_preset
from .simulate import run_and_save


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a bounded PX-loop v0.1 simulation.")
    parser.add_argument(
        "--preset",
        choices=available_presets(),
        default="quiet_loop",
        help="named parameter preset to run",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=120,
        help="number of full seven-operator cycles",
    )
    parser.add_argument(
        "--output-dir",
        default="outbox/ai_coordination/px_loop_runs/latest",
        help="directory for trajectory.csv, summary.json, and trajectory.png",
    )
    parser.add_argument(
        "--param",
        action="append",
        default=[],
        metavar="KEY=VALUE",
        help="override one preset parameter without changing saved preset definitions",
    )
    return parser


def preset_with_overrides(preset_name: str, param_items: list[str]) -> PXPreset:
    preset = get_preset(preset_name)
    if not param_items:
        return preset

    parameters = dict(preset.parameters)
    for item in param_items:
        if "=" not in item:
            raise ValueError(f"parameter override must use KEY=VALUE format: {item!r}")
        key, raw_value = item.split("=", 1)
        key = key.strip()
        if key not in parameters:
            options = ", ".join(sorted(parameters))
            raise ValueError(f"unknown parameter {key!r}; choose one of: {options}")
        try:
            parameters[key] = float(raw_value)
        except ValueError as exc:
            raise ValueError(f"parameter {key!r} must be a float, got {raw_value!r}") from exc

    return PXPreset(
        name=f"{preset.name}__custom",
        description=f"{preset.description} Runtime parameter overlay.",
        initial_state=preset.initial_state,
        parameters=parameters,
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        preset = preset_with_overrides(args.preset, args.param)
    except ValueError as exc:
        parser.error(str(exc))

    result = run_and_save(preset=preset, steps=args.steps, output_dir=args.output_dir)

    print(f"PX-loop preset: {result.preset.name}")
    print(f"Records: {len(result.records)}")
    print(f"Classification: {result.summary['classification']}")
    print(f"Cycle-end classification: {result.summary['cycle_end']['classification']}")
    print("Outputs:")
    for name, path in result.output_paths.items():
        print(f"  {name}: {path}")
    print("Final state:")
    print(json.dumps(result.summary["final_state"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
