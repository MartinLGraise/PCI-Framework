"""Observer logging, trajectory classification, and lightweight PNG plotting."""

from __future__ import annotations

import csv
import json
import math
import struct
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

from .model import DIMENSIONS


@dataclass(frozen=True)
class PXRecord:
    """One observer log row after a PX step."""

    index: int
    cycle: int
    phase_index: int
    step_id: str
    operator_name: str
    values: dict[str, float]

    def as_row(self) -> dict[str, float | int | str]:
        row: dict[str, float | int | str] = {
            "index": self.index,
            "cycle": self.cycle,
            "phase_index": self.phase_index,
            "step_id": self.step_id,
            "operator_name": self.operator_name,
        }
        row.update({dimension: self.values[dimension] for dimension in DIMENSIONS})
        return row


def write_csv_log(records: Sequence[PXRecord], path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["index", "cycle", "phase_index", "step_id", "operator_name", *DIMENSIONS]

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for record in records:
            writer.writerow(record.as_row())

    return path


def _window(records: Sequence[PXRecord], size: int) -> Sequence[PXRecord]:
    return records[-size:] if len(records) > size else records


def classify_trajectory(records: Sequence[PXRecord], window_size: int = 28) -> str:
    """Classify final behavior without pretending to prove dynamics."""
    if len(records) < 3:
        return "insufficient_data"

    final_window = _window(records, window_size)
    spans = {
        dimension: max(record.values[dimension] for record in final_window)
        - min(record.values[dimension] for record in final_window)
        for dimension in DIMENSIONS
    }
    max_span = max(spans.values())
    final_delta = max(
        abs(records[-1].values[dimension] - records[-2].values[dimension])
        for dimension in DIMENSIONS
    )

    if max_span < 0.012 and final_delta < 0.003:
        return "fixed_point_like"
    if max_span < 0.06 and final_delta < 0.012:
        return "settling_bounded"
    if max_span >= 0.06:
        return "bounded_oscillation_or_amplification"
    return "bounded_transient"


def summarize_records(records: Sequence[PXRecord], preset_name: str) -> dict[str, object]:
    final_state = {dimension: records[-1].values[dimension] for dimension in DIMENSIONS}
    ranges = {
        dimension: {
            "min": min(record.values[dimension] for record in records),
            "max": max(record.values[dimension] for record in records),
        }
        for dimension in DIMENSIONS
    }
    return {
        "preset": preset_name,
        "record_count": len(records),
        "cycle_count": records[-1].cycle if records else 0,
        "classification": classify_trajectory(records),
        "final_state": final_state,
        "ranges": ranges,
    }


def write_summary_json(summary: dict[str, object], path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _png_chunk(tag: bytes, data: bytes) -> bytes:
    checksum = zlib.crc32(tag + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", checksum)


def _write_rgb_png(path: Path, width: int, height: int, pixels: bytearray) -> None:
    rows = []
    stride = width * 3
    for y in range(height):
        rows.append(b"\x00" + bytes(pixels[y * stride : (y + 1) * stride]))

    payload = b"".join(
        [
            b"\x89PNG\r\n\x1a\n",
            _png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)),
            _png_chunk(b"IDAT", zlib.compress(b"".join(rows), 9)),
            _png_chunk(b"IEND", b""),
        ]
    )
    path.write_bytes(payload)


def _set_pixel(pixels: bytearray, width: int, height: int, x: int, y: int, color: tuple[int, int, int]) -> None:
    if 0 <= x < width and 0 <= y < height:
        offset = (y * width + x) * 3
        pixels[offset : offset + 3] = bytes(color)


def _draw_line(
    pixels: bytearray,
    width: int,
    height: int,
    start: tuple[int, int],
    end: tuple[int, int],
    color: tuple[int, int, int],
) -> None:
    x0, y0 = start
    x1, y1 = end
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    error = dx + dy

    while True:
        _set_pixel(pixels, width, height, x0, y0, color)
        _set_pixel(pixels, width, height, x0 + 1, y0, color)
        if x0 == x1 and y0 == y1:
            break
        twice_error = 2 * error
        if twice_error >= dy:
            error += dy
            x0 += sx
        if twice_error <= dx:
            error += dx
            y0 += sy


def write_trajectory_png(records: Sequence[PXRecord], path: str | Path, width: int = 1200, height: int = 720) -> Path:
    """Write a dependency-free PNG line plot of all seven state dimensions."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pixels = bytearray([255] * (width * height * 3))

    margin_left = 64
    margin_top = 36
    margin_right = 32
    margin_bottom = 64
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    grid = (225, 228, 232)
    axis = (72, 78, 86)
    for fraction in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = margin_top + int((1.0 - fraction) * plot_height)
        _draw_line(pixels, width, height, (margin_left, y), (width - margin_right, y), grid)
    _draw_line(
        pixels,
        width,
        height,
        (margin_left, margin_top),
        (margin_left, height - margin_bottom),
        axis,
    )
    _draw_line(
        pixels,
        width,
        height,
        (margin_left, height - margin_bottom),
        (width - margin_right, height - margin_bottom),
        axis,
    )

    colors = (
        (31, 119, 180),
        (214, 39, 40),
        (44, 160, 44),
        (148, 103, 189),
        (255, 127, 14),
        (23, 190, 207),
        (127, 127, 127),
    )

    denominator = max(1, len(records) - 1)
    for dimension, color in zip(DIMENSIONS, colors, strict=True):
        points: list[tuple[int, int]] = []
        for index, record in enumerate(records):
            x = margin_left + int(index * plot_width / denominator)
            y = margin_top + int((1.0 - record.values[dimension]) * plot_height)
            points.append((x, y))

        for start, end in zip(points, points[1:], strict=False):
            _draw_line(pixels, width, height, start, end, color)

    # Color-key strip; dimension names are documented in the README and CSV header.
    strip_y = height - 34
    strip_x = margin_left
    for color in colors:
        _draw_line(pixels, width, height, (strip_x, strip_y), (strip_x + 80, strip_y), color)
        strip_x += 116

    # Mark loop boundaries lightly so full PX cycles can be inspected.
    cycle_count = max(record.cycle for record in records) if records else 0
    if cycle_count > 0:
        for cycle in range(1, cycle_count + 1):
            index = cycle * 7
            x = margin_left + int(index * plot_width / denominator)
            if x >= width - margin_right:
                continue
            for y in range(margin_top, height - margin_bottom, 8):
                _set_pixel(pixels, width, height, x, y, (238, 240, 243))

    _write_rgb_png(path, width, height, pixels)
    return path


def finite_records(records: Iterable[PXRecord]) -> bool:
    for record in records:
        for dimension in DIMENSIONS:
            if not math.isfinite(record.values[dimension]):
                return False
    return True
