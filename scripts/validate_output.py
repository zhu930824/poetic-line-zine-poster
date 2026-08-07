#!/usr/bin/env python3
"""Validate dimensions, source-photo fidelity, and clean panel corners."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageOps, ImageStat

from compose_poster import auto_photo_share, cover


def parse_ratio(value: str) -> float:
    try:
        width, height = (float(part) for part in value.split(":", 1))
        return width / height
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError("ratio must look like 9:16") from exc


def parse_hex(value: str) -> tuple[int, int, int]:
    clean = value.strip().lstrip("#")
    if len(clean) != 6:
        raise argparse.ArgumentTypeError("color must use six hexadecimal digits")
    try:
        return tuple(int(clean[index : index + 2], 16) for index in (0, 2, 4))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("color must use hexadecimal digits") from exc


def mean_error(left: Image.Image, right: Image.Image) -> float:
    difference = ImageChops.difference(left, right)
    return sum(ImageStat.Stat(difference).mean) / 3


def corner_error(image: Image.Image, panel_top: int, ivory: tuple[int, int, int]) -> float:
    width, height = image.size
    sample = max(4, round(min(width, height - panel_top) * 0.012))
    boxes = [
        (0, panel_top, sample, panel_top + sample),
        (width - sample, panel_top, width, panel_top + sample),
        (0, height - sample, sample, height),
        (width - sample, height - sample, width, height),
    ]
    reference = Image.new("RGB", (sample, sample), ivory)
    errors = [mean_error(image.crop(box), reference) for box in boxes]
    return sorted(errors)[1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--ratio", type=parse_ratio, default=parse_ratio("9:16"))
    parser.add_argument("--ratio-tolerance", type=float, default=0.001)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--photo-share", type=float)
    parser.add_argument("--focus-x", type=float, default=0.5)
    parser.add_argument("--focus-y", type=float, default=0.5)
    parser.add_argument("--fidelity-tolerance", type=float, default=1.5)
    parser.add_argument("--ivory", type=parse_hex, default=parse_hex("#F3F0E8"))
    parser.add_argument("--corner-tolerance", type=float, default=18.0)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    with Image.open(args.input) as result_file:
        result = ImageOps.exif_transpose(result_file).convert("RGB")

    actual_ratio = result.width / result.height
    ratio_error = abs(actual_ratio - args.ratio)
    share = args.photo_share
    fidelity_error = None
    if args.source:
        with Image.open(args.source) as source_file:
            source = ImageOps.exif_transpose(source_file).convert("RGB")
        share = share if share is not None else auto_photo_share(source)
        photo_height = round(result.height * share)
        expected = cover(source, (result.width, photo_height), (args.focus_x, args.focus_y))
        fidelity_error = mean_error(result.crop((0, 0, result.width, photo_height)), expected)
    elif share is None:
        share = 0.55

    panel_top = round(result.height * share)
    ivory_error = corner_error(result, panel_top, args.ivory)
    checks = {
        "ratio": ratio_error <= args.ratio_tolerance,
        "photo_fidelity": fidelity_error is None or fidelity_error <= args.fidelity_tolerance,
        "clean_panel_corners": ivory_error <= args.corner_tolerance,
    }
    report = {
        "input": str(args.input.resolve()),
        "size": [result.width, result.height],
        "actual_ratio": round(actual_ratio, 6),
        "ratio_error": round(ratio_error, 6),
        "photo_fidelity_error": None if fidelity_error is None else round(fidelity_error, 4),
        "panel_corner_error": round(ivory_error, 4),
        "checks": checks,
        "passed": all(checks.values()),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
