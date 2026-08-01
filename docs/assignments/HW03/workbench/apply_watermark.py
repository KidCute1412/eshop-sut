"""Apply the required student identity overlay to authentic evidence images."""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


IDENTITY = "23127404@hcmus.edu.vn"
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg"}


def apply_watermark(path: Path) -> None:
    with Image.open(path).convert("RGBA") as image:
        overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)
        font = ImageFont.load_default()
        padding = 10
        bbox = draw.textbbox((0, 0), IDENTITY, font=font)
        width = bbox[2] - bbox[0] + (2 * padding)
        height = bbox[3] - bbox[1] + (2 * padding)
        x = max(0, image.width - width)
        y = max(0, image.height - height)
        draw.rectangle((x, y, image.width, image.height), fill=(15, 23, 42, 220))
        draw.text((x + padding, y + padding), IDENTITY, fill="white", font=font)
        Image.alpha_composite(image, overlay).convert("RGB").save(path)
    print(f"Watermarked: {path}")


def main(directory: Path) -> None:
    if not directory.is_dir():
        raise SystemExit(f"Directory not found: {directory}")
    for path in sorted(directory.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            apply_watermark(path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python apply_watermark.py <evidence-directory>")
    main(Path(sys.argv[1]).resolve())

