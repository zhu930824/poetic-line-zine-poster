#!/usr/bin/env python3
"""Render one short English title on an already-composed poster."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


FONT_CANDIDATES = {
    "serif": ["DejaVuSerif.ttf", "Georgia.ttf", "Times New Roman.ttf"],
    "mono": ["DejaVuSansMono.ttf", "Courier New.ttf", "Consolas.ttf"],
    "condensed": ["DejaVuSerifCondensed.ttf", "RobotoCondensed-Regular.ttf", "Georgia.ttf"],
}


def parse_hex(value: str) -> tuple[int, int, int]:
    clean = value.strip().lstrip("#")
    if len(clean) != 6:
        raise argparse.ArgumentTypeError("color must use six hexadecimal digits")
    try:
        return tuple(int(clean[index : index + 2], 16) for index in (0, 2, 4))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("color must use hexadecimal digits") from exc


def load_font(kind: str, size: int, explicit: Path | None = None) -> ImageFont.FreeTypeFont:
    candidates = [str(explicit)] if explicit else FONT_CANDIDATES[kind]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    return right - left, bottom - top


def clamp(value: float, lower: float, upper: float) -> int:
    return round(max(lower, min(upper, value)))


def draw_fragmented(
    draw: ImageDraw.ImageDraw,
    words: list[str],
    font: ImageFont.ImageFont,
    origin: tuple[int, int],
    field_width: int,
    color: tuple[int, int, int, int],
) -> None:
    widths = [text_size(draw, word, font)[0] for word in words]
    total = sum(widths)
    gap = max(12, (field_width - total) // max(1, len(words) - 1))
    x, y = origin
    offsets = (0, -5, 4, -2, 3)
    for index, (word, width) in enumerate(zip(words, widths)):
        draw.text((x, y + offsets[index % len(offsets)]), word, font=font, fill=color)
        x += width + gap


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument(
        "--mode",
        choices=("edge", "fragmented", "letterpress", "ghost"),
        default="fragmented",
    )
    parser.add_argument("--panel-start", type=float, default=0.55)
    parser.add_argument("--anchor-x", type=float, default=0.50)
    parser.add_argument("--anchor-y", type=float, default=0.58)
    parser.add_argument("--color", type=parse_hex, default=parse_hex("#34363A"))
    parser.add_argument("--accent", type=parse_hex, default=parse_hex("#C95C3D"))
    parser.add_argument("--font", type=Path)
    parser.add_argument("--emphasis-word")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    words = args.title.split()
    if not 2 <= len(words) <= 5 or not all(word.isascii() for word in words):
        raise SystemExit("title must contain two to five ASCII words")
    if not 0.30 <= args.panel_start <= 0.72:
        raise SystemExit("panel-start must stay between 0.30 and 0.72")
    if not 0.0 <= args.anchor_x <= 1.0 or not 0.0 <= args.anchor_y <= 1.0:
        raise SystemExit("anchor coordinates must stay between 0 and 1")

    with Image.open(args.input) as image_file:
        image = image_file.convert("RGBA")
    width, height = image.size
    panel_top = round(height * args.panel_start)
    panel_height = height - panel_top
    anchor_x = round(width * args.anchor_x)
    anchor_y = panel_top + round(panel_height * args.anchor_y)
    layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    small_size = max(12, round(panel_height * 0.032))
    color = (*args.color, 255)

    if args.mode == "fragmented":
        font = load_font("mono", small_size, args.font)
        field_width = round(width * min(0.46, 0.14 + len(words) * 0.07))
        origin_x = clamp(anchor_x - field_width / 2, width * 0.05, width * 0.95 - field_width)
        draw_fragmented(draw, words, font, (origin_x, anchor_y), field_width, color)
    elif args.mode == "edge":
        font = load_font("serif", small_size, args.font)
        lines = words if len(words) <= 3 else [" ".join(words[:2]), " ".join(words[2:])]
        line_height = round(small_size * 1.18)
        for index, line in enumerate(lines):
            draw.text((anchor_x, anchor_y + index * line_height), line, font=font, fill=color)
    elif args.mode == "ghost":
        font = load_font("serif", small_size, args.font)
        phrase = " ".join(words)
        phrase_width, _ = text_size(draw, phrase, font)
        x = clamp(anchor_x - phrase_width / 2, width * 0.05, width * 0.95 - phrase_width)
        draw.text((x, anchor_y), phrase, font=font, fill=(*args.color, 112))
    else:
        emphasis = args.emphasis_word or words[-1]
        matches = [index for index, word in enumerate(words) if word.lower() == emphasis.lower()]
        if len(matches) != 1:
            raise SystemExit("emphasis-word must match one title word exactly once")
        emphasis_index = matches[0]
        supporting = words[:emphasis_index] + words[emphasis_index + 1 :]
        small_font = load_font("mono", max(12, round(panel_height * 0.026)), args.font)
        large_font = load_font("condensed", max(20, round(panel_height * 0.075)), args.font)
        emphasized = words[emphasis_index].upper()
        large_width, large_height = text_size(draw, emphasized, large_font)
        x = clamp(anchor_x - large_width / 2, width * 0.05, width * 0.95 - large_width)
        draw.text((x, anchor_y), emphasized, font=large_font, fill=(*args.accent, 255))
        if supporting:
            supporting_text = " ".join(supporting)
            supporting_width, _ = text_size(draw, supporting_text, small_font)
            support_x = clamp(anchor_x - supporting_width / 2, width * 0.05, width * 0.95 - supporting_width)
            draw.text((support_x, anchor_y - round(large_height * 0.72)), supporting_text, font=small_font, fill=color)

    result = Image.alpha_composite(image, layer).convert("RGB")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    save_kwargs = {"quality": 95, "subsampling": 0} if args.output.suffix.lower() in {".jpg", ".jpeg"} else {}
    result.save(args.output, **save_kwargs)
    print(json.dumps({"output": str(args.output.resolve()), "title": args.title, "mode": args.mode}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
