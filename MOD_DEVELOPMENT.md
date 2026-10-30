# Project Metal Hedge — Mod Development

## Current implementation

- `metalhedge.png` is the approved 1175×790 source sheet.
- `tools/extract_metal_hedge.py` extracts the actual artwork into transparent 128×128 PNG working frames.
- `.github/workflows/extract-sprites.yml` runs the extractor and publishes a downloadable workflow artifact named `metal-hedge-128px-frames`.
- The source sheet remains unchanged; generated working frames are kept out of the source tree.

Run locally with `python -m pip install Pillow` and `python tools/extract_metal_hedge.py`.

## Locked design requirements

- Sonic, Tails, and Knuckles all remain playable.
- Keep the original controls and physics.
- Metal Hedge is Eggman's robotic antagonist.
- Current boss target: Launch Base Zone Act 2.
- `metalhedge.png` is the approved visual source of truth. Do not substitute the discarded six-pose SVG concept.

## Runtime conversion still required

The extracted PNGs are working assets, not a drop-in game replacement. The target boss art, compression, mappings, palette and ROM injection location must be verified against the exact game data. Never guess an injection address. The boss is not considered replaced until the converted assets are installed and tested in-game.

The disassembly research identifies multiple Launch Base boss art sets with different compression formats. The Act 2 use of each set and the exact target data still need confirmation before a raw-data override is created.

## Credits

- J.I.B. — credited for the original Metal Sonic artwork.
- TannerTH25 — uploader of the Metal Sonic (Sonic 3-Style) custom/edited sprite sheet.

Check reuse permissions before redistributing third-party source artwork.
