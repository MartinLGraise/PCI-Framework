"""Command-line runner for PX-Loop Agent v0.1."""

from __future__ import annotations

import argparse
import json

from .presets import available_presets
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
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = run_and_save(preset=args.preset, steps=args.steps, output_dir=args.output_dir)

    print(f"PX-loop preset: {result.preset.name}")
    print(f"Records: {len(result.records)}")
    print(f"Classification: {result.summary['classification']}")
    print("Outputs:")
    for name, path in result.output_paths.items():
        print(f"  {name}: {path}")
    print("Final state:")
    print(json.dumps(result.summary["final_state"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
