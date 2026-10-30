#!/usr/bin/env python3
"""Extract the approved Metal Hedge sprite sheet into 128x128 PNG frames.

The source sheet stays untouched. Each frame is cropped from its labeled
animation panel, made transparent, centered, and reduced to the 16 colors
shown in the sheet's palette strip. This creates PNG working assets only;
it does NOT create Sonic 3 A.I.R. ROM injections or prove runtime compatibility.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "metalhedge.png"
OUT = ROOT / "build" / "metal-hedge-frames"
CANVAS = 128
MAX_SPRITE = 112

# Coordinates refer to the 1175x790 approved reference sheet.
# Each panel is split into equal frame slots; the panel headings are excluded.
PANELS = [
    ("idle",       (20, 103, 562, 181), 10),
    ("walk",       (565, 103, 1018, 181), 9),
    ("run_dash",   (20, 207, 662, 294), 11),
    ("jump",       (666, 207, 1018, 294), 6),
    ("spin_attack",(20, 309, 408, 406), 6),
    ("hit_damage", (412, 309, 757, 406), 5),
    ("defeat",     (761, 309, 1157, 406), 5),
    ("boss",       (20, 428, 1157, 571), 8),
]


def sample_palette(sheet: Image.Image) -> Image.Image:
    """Build a 16-color Pillow palette from the palette strip in the source."""
    rgb = sheet.convert("RGB")
    colors = []
    # The 16 swatches run horizontally from x=29 to x=319 at y=610.
    for i in range(16):
        x = round(29 + (i + 0.5) * (290 / 16))
        colors.append(rgb.getpixel((x, 610)))
    pal = Image.new("P", (1, 1))
    flat = []
    for color in colors:
        flat.extend(color)
    flat.extend([0] * (768 - len(flat)))
    pal.putpalette(flat)
    return pal


def extract_slot(sheet: Image.Image, box, palette: Image.Image):
    x1, y1, x2, y2 = box
    crop = sheet.crop((x1, y1, x2, y2)).convert("RGBA")
    px = crop.load()
    # The sheet background is black. Keep every non-black sprite pixel,
    # including dark outlines and anti-aliased edges.
    mask = Image.new("L", crop.size, 0)
    mp = mask.load()
    for y in range(crop.height):
        for x in range(crop.width):
            r, g, b, _ = px[x, y]
            if max(r, g, b) > 8:
                mp[x, y] = 255

    bbox = mask.getbbox()
    if not bbox:
        return None

    # Expand the detected bounds slightly so edge pixels aren't shaved off.
    left, top, right, bottom = bbox
    left = max(0, left - 2)
    top = max(0, top - 2)
    right = min(crop.width, right + 2)
    bottom = min(crop.height, bottom + 2)
    crop = crop.crop((left, top, right, bottom))
    mask = mask.crop((left, top, right, bottom))

    # Convert the crop to the source's 16-color swatch palette.
    rgb = crop.convert("RGB")
    indexed = rgb.quantize(palette=palette, dither=Image.Dither.NONE).convert("RGB")
    indexed.putalpha(mask)

    # Fit without changing proportions; nearest-neighbor keeps pixel edges crisp.
    scale = min(MAX_SPRITE / indexed.width, MAX_SPRITE / indexed.height)
    size = (max(1, round(indexed.width * scale)),
            max(1, round(indexed.height * scale)))
    sprite = indexed.resize(size, Image.Resampling.NEAREST)
    frame = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    frame.alpha_composite(sprite, ((CANVAS - size[0]) // 2,
                                   (CANVAS - size[1]) // 2))
    return frame


def main():
    if not SOURCE.exists():
        raise SystemExit(f"Missing approved source sheet: {SOURCE}")
    sheet = Image.open(SOURCE).convert("RGBA")
    if sheet.size != (1175, 790):
        raise SystemExit(f"Unexpected source dimensions {sheet.size}; expected 1175x790")

    OUT.mkdir(parents=True, exist_ok=True)
    palette = sample_palette(sheet)
    manifest = {
        "name": "Metal Hedge extracted frames",
        "source": "metalhedge.png",
        "canvas": {"width": CANVAS, "height": CANVAS},
        "paletteColors": 16,
        "groups": {}
    }

    for group, (x1, y1, x2, y2), count in PANELS:
        group_dir = OUT / group
        group_dir.mkdir(parents=True, exist_ok=True)
        slot_width = (x2 - x1) / count
        names = []
        for index in range(count):
            sx1 = round(x1 + index * slot_width)
            sx2 = round(x1 + (index + 1) * slot_width)
            frame = extract_slot(sheet, (sx1, y1, sx2, y2), palette)
            if frame is None:
                print(f"WARNING: empty slot {group}/{index:02d}")
                continue
            filename = f"{index:02d}.png"
            frame.save(group_dir / filename, optimize=True)
            names.append(filename)
        manifest["groups"][group] = {
            "frameCountExpected": count,
            "framesExtracted": len(names),
            "files": names
        }

    import json
    (OUT / "atlas.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Extracted working frames to {OUT}")
    for group, data in manifest["groups"].items():
        print(f"  {group}: {data['framesExtracted']}/{data['frameCountExpected']} frames")


if __name__ == "__main__":
    main()
