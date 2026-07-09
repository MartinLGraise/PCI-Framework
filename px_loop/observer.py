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


def _max_state_delta(left: PXRecord, right: PXRecord) -> float:
    return max(abs(left.values[dimension] - right.values[dimension]) for dimension in DIMENSIONS)


def cycle_end_metrics(records: Sequence[PXRecord], tolerance: float = 1e-9) -> dict[str, object]:
    """Measure behavior at complete-loop boundaries.

    The per-operator trajectory may show a sawtooth because every PX layer moves
    the state. Cycle-end metrics sample only initial/PX-007 records so fixed
    points of the full seven-operator map are not misread as oscillation.
    """
    cycle_end_records = [
        record for record in records if record.step_id == "initial" or record.step_id == "PX-007"
    ]
    if len(cycle_end_records) < 2:
        return {
            "classification": "insufficient_data",
            "final_delta": None,
            "cycles_to_tolerance": None,
            "within_cycle_span": None,
        }

    deltas = [
        {
            "cycle": current.cycle,
            "delta": _max_state_delta(previous, current),
        }
        for previous, current in zip(cycle_end_records, cycle_end_records[1:], strict=False)
    ]
    final_delta = float(deltas[-1]["delta"])
    cycles_to_tolerance = None
    for index, item in enumerate(deltas):
        if all(float(future["delta"]) <= tolerance for future in deltas[index:]):
            cycles_to_tolerance = int(item["cycle"])
            break

    final_cycle = records[-1].cycle
    final_cycle_records = [
        record for record in records if record.cycle == final_cycle and record.step_id != "initial"
    ]
    if final_cycle_records:
        spans = {
            dimension: max(record.values[dimension] for record in final_cycle_records)
            - min(record.values[dimension] for record in final_cycle_records)
            for dimension in DIMENSIONS
        }
        max_within_cycle_span = max(spans.values())
    else:
        spans = {}
        max_within_cycle_span = 0.0

    if final_delta <= tolerance:
        classification = "cycle_end_fixed_point_like"
    elif final_delta <= 1e-5:
        classification = "cycle_end_settling"
    else:
        classification = "cycle_end_transient"

    return {
        "classification": classification,
        "final_delta": final_delta,
        "cycles_to_tolerance": cycles_to_tolerance,
        "within_cycle_span": spans,
        "max_within_cycle_span": max_within_cycle_span,
        "tolerance": tolerance,
    }


def summarize_records(
    records: Sequence[PXRecord],
    preset_name: str,
    run_config: dict[str, object] | None = None,
) -> dict[str, object]:
    final_state = {dimension: records[-1].values[dimension] for dimension in DIMENSIONS}
    ranges = {
        dimension: {
            "min": min(record.values[dimension] for record in records),
            "max": max(record.values[dimension] for record in records),
        }
        for dimension in DIMENSIONS
    }
    summary = {
        "preset": preset_name,
        "record_count": len(records),
        "cycle_count": records[-1].cycle if records else 0,
        "classification": classify_trajectory(records),
        "classification_basis": "per_operator_window",
        "classification_note": (
            "This legacy classification measures the final per-operator window. "
            "Use cycle_end.classification for complete-loop behavior."
        ),
        "cycle_end": cycle_end_metrics(records),
        "final_state": final_state,
        "ranges": ranges,
    }
    if run_config:
        summary["run_config"] = run_config
    return summary


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


def _fill_rect(
    pixels: bytearray,
    width: int,
    height: int,
    x: int,
    y: int,
    rect_width: int,
    rect_height: int,
    color: tuple[int, int, int],
) -> None:
    for row in range(y, y + rect_height):
        for column in range(x, x + rect_width):
            _set_pixel(pixels, width, height, column, row, color)


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


_FONT_5X7 = {
    " ": ("00000", "00000", "00000", "00000", "00000", "00000", "00000"),
    "-": ("00000", "00000", "00000", "11111", "00000", "00000", "00000"),
    "_": ("00000", "00000", "00000", "00000", "00000", "00000", "11111"),
    ".": ("00000", "00000", "00000", "00000", "00000", "01100", "01100"),
    ",": ("00000", "00000", "00000", "00000", "01100", "00100", "01000"),
    ":": ("00000", "01100", "01100", "00000", "01100", "01100", "00000"),
    "(": ("00010", "00100", "01000", "01000", "01000", "00100", "00010"),
    ")": ("01000", "00100", "00010", "00010", "00010", "00100", "01000"),
    "+": ("00000", "00100", "00100", "11111", "00100", "00100", "00000"),
    "/": ("00001", "00010", "00100", "01000", "10000", "00000", "00000"),
    "|": ("00100", "00100", "00100", "00100", "00100", "00100", "00100"),
    ">": ("10000", "01000", "00100", "00010", "00100", "01000", "10000"),
    "=": ("00000", "11111", "00000", "11111", "00000", "00000", "00000"),
    "0": ("01110", "10001", "10011", "10101", "11001", "10001", "01110"),
    "1": ("00100", "01100", "00100", "00100", "00100", "00100", "01110"),
    "2": ("01110", "10001", "00001", "00010", "00100", "01000", "11111"),
    "3": ("11110", "00001", "00001", "01110", "00001", "00001", "11110"),
    "4": ("00010", "00110", "01010", "10010", "11111", "00010", "00010"),
    "5": ("11111", "10000", "11110", "00001", "00001", "10001", "01110"),
    "6": ("00110", "01000", "10000", "11110", "10001", "10001", "01110"),
    "7": ("11111", "00001", "00010", "00100", "01000", "01000", "01000"),
    "8": ("01110", "10001", "10001", "01110", "10001", "10001", "01110"),
    "9": ("01110", "10001", "10001", "01111", "00001", "00010", "01100"),
    "A": ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    "B": ("11110", "10001", "10001", "11110", "10001", "10001", "11110"),
    "C": ("01110", "10001", "10000", "10000", "10000", "10001", "01110"),
    "D": ("11110", "10001", "10001", "10001", "10001", "10001", "11110"),
    "E": ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    "F": ("11111", "10000", "10000", "11110", "10000", "10000", "10000"),
    "G": ("01110", "10001", "10000", "10111", "10001", "10001", "01110"),
    "H": ("10001", "10001", "10001", "11111", "10001", "10001", "10001"),
    "I": ("01110", "00100", "00100", "00100", "00100", "00100", "01110"),
    "J": ("00111", "00010", "00010", "00010", "00010", "10010", "01100"),
    "K": ("10001", "10010", "10100", "11000", "10100", "10010", "10001"),
    "L": ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    "M": ("10001", "11011", "10101", "10101", "10001", "10001", "10001"),
    "N": ("10001", "11001", "10101", "10011", "10001", "10001", "10001"),
    "O": ("01110", "10001", "10001", "10001", "10001", "10001", "01110"),
    "P": ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    "Q": ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    "R": ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    "S": ("01111", "10000", "10000", "01110", "00001", "00001", "11110"),
    "T": ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    "U": ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    "V": ("10001", "10001", "10001", "10001", "10001", "01010", "00100"),
    "W": ("10001", "10001", "10001", "10101", "10101", "10101", "01010"),
    "X": ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    "Y": ("10001", "10001", "01010", "00100", "00100", "00100", "00100"),
    "Z": ("11111", "00001", "00010", "00100", "01000", "10000", "11111"),
}


def _text_width(text: str, scale: int = 1) -> int:
    return max(0, len(text) * 6 * scale - scale)


def _draw_text(
    pixels: bytearray,
    width: int,
    height: int,
    text: str,
    x: int,
    y: int,
    color: tuple[int, int, int],
    scale: int = 1,
) -> None:
    cursor_x = x
    for character in text.upper():
        glyph = _FONT_5X7.get(character, _FONT_5X7[" "])
        for row_index, row in enumerate(glyph):
            for column_index, bit in enumerate(row):
                if bit == "1":
                    _fill_rect(
                        pixels,
                        width,
                        height,
                        cursor_x + column_index * scale,
                        y + row_index * scale,
                        scale,
                        scale,
                        color,
                    )
        cursor_x += 6 * scale


def _display_label(value: str) -> str:
    return value.replace("_", " ").replace("  ", " ").upper()


COLORS: tuple[tuple[int, int, int], ...] = (
    (31, 119, 180),
    (214, 39, 40),
    (44, 160, 44),
    (148, 103, 189),
    (255, 127, 14),
    (23, 190, 207),
    (127, 127, 127),
)


def _draw_panel_axes(
    pixels: bytearray,
    width: int,
    height: int,
    left: int,
    top: int,
    panel_width: int,
    panel_height: int,
    heading: str,
    left_x_label: str,
    right_x_label: str,
) -> None:
    ink = (36, 42, 51)
    muted = (104, 112, 124)
    grid = (225, 228, 232)
    axis = (72, 78, 86)

    _draw_text(pixels, width, height, heading, left, top - 24, ink, scale=1)
    for fraction, label in ((0.0, "0.00"), (0.25, "0.25"), (0.5, "0.50"), (0.75, "0.75"), (1.0, "1.00")):
        y = top + int((1.0 - fraction) * panel_height)
        _draw_line(pixels, width, height, (left, y), (left + panel_width, y), grid)
        _draw_text(
            pixels,
            width,
            height,
            label,
            left - _text_width(label, scale=1) - 10,
            y - 3,
            muted,
            scale=1,
        )

    _draw_line(pixels, width, height, (left, top), (left, top + panel_height), axis)
    _draw_line(
        pixels,
        width,
        height,
        (left, top + panel_height),
        (left + panel_width, top + panel_height),
        axis,
    )
    _draw_text(pixels, width, height, left_x_label, left - 2, top + panel_height + 14, muted, scale=1)
    _draw_text(
        pixels,
        width,
        height,
        right_x_label,
        left + panel_width - _text_width(right_x_label, scale=1),
        top + panel_height + 14,
        muted,
        scale=1,
    )


def _cycle_end_records(records: Sequence[PXRecord]) -> list[PXRecord]:
    return [record for record in records if record.step_id == "initial" or record.step_id == "PX-007"]


def _draw_cycle_markers(
    pixels: bytearray,
    width: int,
    height: int,
    records: Sequence[PXRecord],
    left: int,
    top: int,
    panel_width: int,
    panel_height: int,
) -> None:
    cycle_count = max(record.cycle for record in records) if records else 0
    denominator = max(1, len(records) - 1)
    if cycle_count <= 0:
        return

    cycle_interval = 1 if cycle_count <= 40 else 10
    for cycle in range(cycle_interval, cycle_count + 1, cycle_interval):
        index = cycle * 7
        x = left + int(index * panel_width / denominator)
        if x > left + panel_width:
            continue
        for y in range(top, top + panel_height, 8):
            _set_pixel(pixels, width, height, x, y, (238, 240, 243))


def _draw_series(
    pixels: bytearray,
    width: int,
    height: int,
    records: Sequence[PXRecord],
    left: int,
    top: int,
    panel_width: int,
    panel_height: int,
) -> list[dict[str, object]]:
    denominator = max(1, len(records) - 1)
    final_points: list[dict[str, object]] = []

    for dimension, color in zip(DIMENSIONS, COLORS, strict=True):
        points: list[tuple[int, int]] = []
        for index, record in enumerate(records):
            x = left + int(index * panel_width / denominator)
            y = top + int((1.0 - record.values[dimension]) * panel_height)
            points.append((x, y))

        for start, end in zip(points, points[1:], strict=False):
            _draw_line(pixels, width, height, start, end, color)

        final_points.append(
            {
                "dimension": dimension,
                "color": color,
                "x": points[-1][0],
                "target_y": points[-1][1],
                "value": records[-1].values[dimension],
            }
        )

    return final_points


def _draw_right_labels(
    pixels: bytearray,
    width: int,
    height: int,
    final_points: list[dict[str, object]],
    label_x: int,
    label_top: int,
    label_bottom: int,
) -> None:
    ink = (36, 42, 51)
    final_points.sort(key=lambda item: int(item["target_y"]))
    min_gap = 25
    for item in final_points:
        item["label_y"] = max(label_top, int(item["target_y"]))
    for previous, current in zip(final_points, final_points[1:], strict=False):
        current["label_y"] = max(int(current["label_y"]), int(previous["label_y"]) + min_gap)
    overflow = int(final_points[-1]["label_y"]) - label_bottom if final_points else 0
    if overflow > 0:
        for item in final_points:
            item["label_y"] = int(item["label_y"]) - overflow

    for item in final_points:
        color = item["color"]
        assert isinstance(color, tuple)
        final_x = int(item["x"])
        final_y = int(item["target_y"])
        label_y = int(item["label_y"])
        _draw_line(pixels, width, height, (final_x, final_y), (label_x - 10, label_y + 6), color)
        _fill_rect(pixels, width, height, label_x, label_y + 1, 14, 10, color)
        label = f"{_display_label(str(item['dimension']))} {float(item['value']):.3f}"
        _draw_text(pixels, width, height, label, label_x + 22, label_y, ink, scale=1)


def _draw_color_key(
    pixels: bytearray,
    width: int,
    height: int,
    left: int,
    top: int,
    column_width: int = 230,
) -> None:
    ink = (36, 42, 51)
    muted = (104, 112, 124)
    _draw_text(pixels, width, height, "COLOR KEY", left, top - 18, muted, scale=1)
    for index, (dimension, color) in enumerate(zip(DIMENSIONS, COLORS, strict=True)):
        row = index // 4
        column = index % 4
        x = left + column * column_width
        y = top + row * 24
        _fill_rect(pixels, width, height, x, y + 1, 18, 10, color)
        _draw_text(pixels, width, height, _display_label(dimension), x + 26, y, ink, scale=1)


def write_trajectory_png(
    records: Sequence[PXRecord],
    path: str | Path,
    width: int = 1200,
    height: int = 980,
    title: str = "PX-LOOP V0.1 TRAJECTORY",
    subtitle: str | None = None,
) -> Path:
    """Write a dependency-free PNG line plot of all seven state dimensions."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pixels = bytearray([252] * (width * height * 3))

    panel_left = 92
    panel_width = width - panel_left - 330
    saw_top = 112
    saw_height = 360
    cycle_top = 565
    cycle_height = 230

    ink = (36, 42, 51)
    muted = (104, 112, 124)

    _draw_text(pixels, width, height, title, panel_left, 24, ink, scale=2)
    if subtitle:
        _draw_text(pixels, width, height, subtitle, panel_left, 52, muted, scale=1)

    _draw_text(pixels, width, height, "STATE VALUE", 12, saw_top - 20, muted, scale=1)
    _draw_panel_axes(
        pixels,
        width,
        height,
        panel_left,
        saw_top,
        panel_width,
        saw_height,
        "PER-OPERATOR SAWTOOTH (EVERY PX STEP)",
        "0",
        str(records[-1].index if records else 0),
    )
    _draw_cycle_markers(pixels, width, height, records, panel_left, saw_top, panel_width, saw_height)
    saw_points = _draw_series(pixels, width, height, records, panel_left, saw_top, panel_width, saw_height)
    _draw_right_labels(pixels, width, height, saw_points, width - 306, saw_top + 4, saw_top + saw_height - 18)

    cycle_records = _cycle_end_records(records)
    _draw_panel_axes(
        pixels,
        width,
        height,
        panel_left,
        cycle_top,
        panel_width,
        cycle_height,
        "CYCLE-END ONLY (INITIAL + PX-007 STATES)",
        "CYCLE 0",
        f"CYCLE {cycle_records[-1].cycle if cycle_records else 0}",
    )
    cycle_points = _draw_series(
        pixels,
        width,
        height,
        cycle_records,
        panel_left,
        cycle_top,
        panel_width,
        cycle_height,
    )
    _draw_right_labels(
        pixels,
        width,
        height,
        cycle_points,
        width - 306,
        cycle_top + 4,
        cycle_top + cycle_height - 18,
    )

    _draw_text(pixels, width, height, "OBSERVER STEP", panel_left, saw_top + saw_height + 38, muted, scale=1)
    _draw_text(pixels, width, height, "COMPLETE PX CYCLE", panel_left, cycle_top + cycle_height + 38, muted, scale=1)
    _draw_color_key(pixels, width, height, panel_left, height - 86)

    _write_rgb_png(path, width, height, pixels)
    return path


def write_comparison_png(
    left_records: Sequence[PXRecord],
    right_records: Sequence[PXRecord],
    path: str | Path,
    left_title: str = "QUIET LOOP",
    right_title: str = "PARADOX AMPLIFICATION",
    width: int = 1600,
    height: int = 900,
) -> Path:
    """Write a side-by-side cycle-end comparison panel."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pixels = bytearray([252] * (width * height * 3))
    ink = (36, 42, 51)
    muted = (104, 112, 124)

    _draw_text(pixels, width, height, "PX-LOOP V0.1 COMPARISON", 90, 26, ink, scale=2)
    _draw_text(
        pixels,
        width,
        height,
        "CYCLE-END ONLY THROUGH SAVED HORIZON; LABELS ARE HORIZON-SPECIFIC",
        90,
        56,
        muted,
        scale=1,
    )

    panels = (
        (90, 130, 500, 520, left_title, left_records),
        (850, 130, 500, 520, right_title, right_records),
    )
    for left, top, panel_width, panel_height, panel_title, records in panels:
        cycle_records = _cycle_end_records(records)
        cycle_summary = cycle_end_metrics(records)
        final_cycle = cycle_records[-1].cycle if cycle_records else 0
        heading = (
            f"{panel_title.upper()} | "
            f"{str(cycle_summary['classification']).replace('_', ' ').upper()} "
            f"AT CYCLE {final_cycle}"
        )
        _draw_panel_axes(
            pixels,
            width,
            height,
            left,
            top,
            panel_width,
            panel_height,
            heading,
            "CYCLE 0",
            f"CYCLE {final_cycle}",
        )
        final_points = _draw_series(
            pixels,
            width,
            height,
            cycle_records,
            left,
            top,
            panel_width,
            panel_height,
        )
        _draw_right_labels(
            pixels,
            width,
            height,
            final_points,
            left + panel_width + 24,
            top + 4,
            top + panel_height - 18,
        )

    _draw_text(pixels, width, height, "COMPLETE PX CYCLE", 90, 694, muted, scale=1)
    _draw_color_key(pixels, width, height, 90, 760, column_width=260)

    _write_rgb_png(path, width, height, pixels)
    return path


def finite_records(records: Iterable[PXRecord]) -> bool:
    for record in records:
        for dimension in DIMENSIONS:
            if not math.isfinite(record.values[dimension]):
                return False
    return True
