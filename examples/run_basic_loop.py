"""Example PX-loop run from Python code."""

from px_loop import run_and_save


if __name__ == "__main__":
    result = run_and_save(
        preset="quiet_loop",
        steps=120,
        output_dir="outbox/ai_coordination/px_loop_runs/example_quiet_loop",
    )
    print(result.summary["classification"])
    print(result.output_paths)
