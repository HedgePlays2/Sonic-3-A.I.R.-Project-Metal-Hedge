# Sonic 3 A.I.R. — Project Metal Hedge

A fan-made **Sonic 3 A.I.R. mod** featuring **Metal Hedge**, Eggman's green robotic hedgehog.

## Current progress

<badge>Sprite extraction pipeline working</badge>

- The approved `metalhedge.png` reference sheet is the source of truth.
- A Python extractor now produces transparent 128×128 PNG working frames in the 16-color palette shown on the sheet.
- The first GitHub Actions extraction completed successfully: **60 frames extracted** across Idle (10), Walk (9), Run/Dash (11), Jump (6), Spin Attack (6), Hit/Damage (5), Defeat/Explode (5), and the boss sequence (8).
- [Download the extracted frame pack](https://github.com/HedgePlays2/Sonic-3-A.I.R.-Project-Metal-Hedge/actions/runs/41146761900/artifacts/13021072015) (GitHub Actions artifact; available for 30 days from the run).
- The original reference sheet remains unchanged.

Run the extractor locally with `python -m pip install Pillow` and `python tools/extract_metal_hedge.py`.

## Story

Dr. Eggman has created Metal Hedge, a machine designed to imitate Sonic's speed and stop him. Eggman sends his new creation to Angel Island, where Sonic begins to uncover the secret project.

## Core goals

- Keep **Sonic, Tails, and Knuckles** playable.
- Keep the original controls, physics, and normal gameplay wherever possible.
- Make Metal Hedge Eggman's robotic antagonist—not a replacement for Sonic as the protagonist.
- First planned boss target: **Launch Base Zone Act 2**.
- Build and test in small steps so the original game remains playable.

## Next implementation steps

1. Visually review the extracted frame crops and correct any panel-slot boundaries that need adjustment.
2. Verify the exact Launch Base Zone Act 2 boss art, compression format, mappings, and palette.
3. Convert the reviewed frames into the format expected by the target boss.
4. Verify the ROM injection location against the exact source game data; never guess an offset.
5. Install and test the replacement in Sonic 3 A.I.R., confirming the boss behavior and all playable characters remain intact.

## Project structure

- `mod.json` — mod metadata
- `icon.png` — mod icon
- `metalhedge.png` — approved original reference sheet (preserved unchanged)
- `tools/extract_metal_hedge.py` — sprite extraction tool
- `.github/workflows/extract-sprites.yml` — automatic frame extraction and artifact publishing
- `sprites/` — extraction manifest and sprite documentation
- `rawdata/` — reserved for verified future data overrides
- `audio/` — reserved for future audio overrides
- `MOD_DEVELOPMENT.md` — implementation and testing checklist

## Credits

- **J.I.B** — credited for the original Metal Sonic artwork.
- **TannerTH25** — uploader of the *Metal Sonic (Sonic 3-Style)* custom/edited sprite sheet on The Spriters Resource: https://www.spriters-resource.com/custom_edited/sonicthehedgehogcustoms/asset/237787/
- **SEGA and the original Sonic 3 & Knuckles / Sonic 3 A.I.R. creators** — the original game characters, assets, and engine belong to their respective rights holders.

The Metal Sonic sprite sheet is third-party artwork and is not claimed as original work by HedgePlays2. Credit is provided for attribution; permission and applicable reuse terms must be checked before redistributing the artwork with the mod.

## Disclaimer

This is a fan project and is not an official SEGA release. Sonic and related official characters and assets belong to their respective rights holders.
