#!/usr/bin/env python3
"""Compose an untouched source photo and a generated abstract panel."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageOps


def parse_size(value: str) -> tuple[int, int]:
    normalized = value.lower().replace("×", "x")
    try:
        width, height = (int(part) for part in normalized.split("x", 1))
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("size must look like 1080x1920") from exc
    if width < 64 or height < 64:
        raise argparse.ArgumentTypeError("width and height must be at least 64 pixels")
    return width, height


def auto_photo_share(image: Image.Image) -> float:
    ratio = image.width / image.height
    if ratio >= 1.2:
        return 0.48
    if ratio <= 0.8:
        return 0.62
    return 0.55


def cover(image: Image.Image, size: tuple[int, int], focus: tuple[float, float]) -> Image.Image:
    return ImageOps.fit(
        image,
        size,
        method=Image.Resampling.LANCZOS,
        centering=focus,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="original user photograph")
    parser.add_argument("panel", type=Path, help="generated panel without title")
    parser.add_argument("output", type=Path, help="output PNG or JPEG")
    parser.add_argument("--size", type=parse_size, default=(1080, 1920))
    parser.add_argument(
        "--photo-share",
        type=float,
        help="photo height divided by canvas height; inferred when omitted",
    )
    parser.add_argument("--focus-x", type=float, default=0.5)
    parser.add_argument("--focus-y", type=float, default=0.5)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not args.source.is_file() or not args.panel.is_file():
        raise SystemExit("source and panel must be readable image files")
    if not 0.0 <= args.focus_x <= 1.0 or not 0.0 <= args.focus_y <= 1.0:
        raise SystemExit("focus coordinates must stay between 0 and 1")

    with Image.open(args.source) as source_file:
        source = ImageOps.exif_transpose(source_file).convert("RGB")
    with Image.open(args.panel) as panel_file:
        panel = ImageOps.exif_transpose(panel_file).convert("RGB")

    share = args.photo_share if args.photo_share is not None else auto_photo_share(source)
    if not 0.30 <= share <= 0.72:
        raise SystemExit("photo-share must stay between 0.30 and 0.72")

    width, height = args.size
    photo_height = round(height * share)
    panel_height = height - photo_height
    focus = (args.focus_x, args.focus_y)

    photo_region = cover(source, (width, photo_height), focus)
    panel_region = cover(panel, (width, panel_height), (0.5, 0.5))
    canvas = Image.new("RGB", (width, height), "#F3F0E8")
    canvas.paste(photo_region, (0, 0))
    canvas.paste(panel_region, (0, photo_height))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    save_kwargs = {"quality": 95, "subsampling": 0} if args.output.suffix.lower() in {".jpg", ".jpeg"} else {}
    canvas.save(args.output, **save_kwargs)
    print(
        json.dumps(
            {
                "output": str(args.output.resolve()),
                "size": [width, height],
                "photo_share": share,
                "panel_start": photo_height,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
