#!/usr/bin/env python3
"""Extract Metal Hedge frames without recoloring or slicing through poses.

The source sheet is kept untouched. Each animation panel is split at the
lowest-ink vertical gaps near expected frame boundaries, then each frame is
cropped to its actual non-background bounds and placed on a transparent canvas.
"""
from pathlib import Path
import json
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "metalhedge.png"
OUT = ROOT / "build" / "metal-hedge-frames"
CANVAS = 128
MAX_SPRITE = 112
BACKGROUND_THRESHOLD = 8

# Tight vertical crops exclude the panel labels and borders.
PANELS = [
    ("idle",        (20, 108, 562, 181), 10),
    ("walk",        (565, 108, 1018, 181), 9),
    ("run_dash",    (20, 216, 662, 294), 11),
    ("jump",        (666, 216, 1018, 294), 6),
    ("spin_attack", (20, 333, 408, 406), 6),
    ("hit_damage",  (412, 333, 757, 406), 5),
    ("defeat",      (761, 333, 1157, 406), 5),
    ("boss",        (20, 438, 1157, 571), 8),
]


def foreground_mask(image):
    rgb = image.convert("RGB")
    return rgb.point(lambda value: 255 if value > BACKGROUND_THRESHOLD else 0)


def find_boundaries(panel, count):
    """Find low-ink vertical seams near each expected frame boundary."""
    mask = foreground_mask(panel)
    width, height = mask.size
    pixels = mask.load()
    projection = [
        sum(1 for y in range(height) if pixels[x, y] != 0)
        for x in range(width)
    ]
    boundaries = [0]
    for index in range(1, count):
        expected = round(index * width / count)
        radius = max(8, round(width / count * 0.32))
        lo = max(boundaries[-1] + 12, expected - radius)
        hi = min(width - (count - index) * 12, expected + radius)
        if lo >= hi:
            raise RuntimeError(f"Cannot safely locate seam {index}/{count}")
        seam = min(range(lo, hi), key=lambda x: (projection[x], abs(x - expected)))
        boundaries.append(seam)
    boundaries.append(width)
    return boundaries


def extract_frame(sheet, bounds):
    crop = sheet.crop(bounds).convert("RGBA")
    mask = Image.new("L", crop.size, 0)
    src = crop.load()
    dst = mask.load()
    for y in range(crop.height):
        for x in range(crop.width):
            r, g, b, _ = src[x, y]
            if max(r, g, b) > BACKGROUND_THRESHOLD:
                dst[x, y] = 255

    bbox = mask.getbbox()
    if bbox is None:
        return None
    left, top, right, bottom = bbox
    # Small padding protects antialiased edges without importing adjacent poses.
    left = max(0, left - 2)
    top = max(0, top - 2)
    right = min(crop.width, right + 2)
    bottom = min(crop.height, bottom + 2)
    crop = crop.crop((left, top, right, bottom))
    mask = mask.crop((left, top, right, bottom))
    crop.putalpha(mask)

    scale = min(MAX_SPRITE / crop.width, MAX_SPRITE / crop.height)
    size = (max(1, round(crop.width * scale)),
            max(1, round(crop.height * scale)))
    sprite = crop.resize(size, Image.Resampling.NEAREST)
    frame = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    frame.alpha_composite(sprite, ((CANVAS - size[0]) // 2,
                                   (CANVAS - size[1]) // 2))
    return frame


def main():
    if not SOURCE.exists():
        raise SystemExit(f"Missing source sheet: {SOURCE}")
    sheet = Image.open(SOURCE).convert("RGBA")
    if sheet.size != (1175, 790):
        raise SystemExit(f"Unexpected source dimensions {sheet.size}; expected 1175x790")

    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "name": "Metal Hedge extracted frames",
        "source": "metalhedge.png",
        "canvas": {"width": CANVAS, "height": CANVAS},
        "sourceColorsPreserved": True,
        "groups": {},
    }

    for group, (x1, y1, x2, y2), count in PANELS:
        panel = sheet.crop((x1, y1, x2, y2))
        seams = find_boundaries(panel, count)
        group_dir = OUT / group
        group_dir.mkdir(parents=True, exist_ok=True)
        files = []
        for index in range(count):
            sx1, sx2 = seams[index], seams[index + 1]
            frame = extract_frame(sheet, (x1 + sx1, y1, x1 + sx2, y2))
            if frame is None:
                raise RuntimeError(f"Empty frame: {group}/{index:02d}")
            filename = f"{index:02d}.png"
            frame.save(group_dir / filename, optimize=True)
            files.append(filename)
        manifest["groups"][group] = {
            "frameCountExpected": count,
            "framesExtracted": len(files),
            "files": files,
            "verticalSeams": [x1 + seam for seam in seams],
        }

    (OUT / "atlas.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Extracted {sum(len(v['files']) for v in manifest['groups'].values())} frames to {OUT}")
    for group, data in manifest["groups"].items():
        print(f"  {group}: {data['framesExtracted']}/{data['frameCountExpected']}")


if __name__ == "__main__":
    main()
