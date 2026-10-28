# Project Metal Hedge — Mod Development

## Current safe starter
- `mod.json`: mod metadata.
- `icon.png`: mod icon.
- `scripts/main.lemon`: intentionally no-op script entry point.
- `sprites/`, `rawdata/`, and `audio/`: documented locations for future assets.

## First implementation target
Create a Metal Hedge sprite replacement while keeping Sonic as the only playable protagonist and preserving the original controls and physics.

## Sprite implementation checklist
1. Confirm the sprite file path and matching JSON definitions from the target Sonic 3 A.I.R. installation.
2. Recolor a copy of the source sheet: blue metal to green; retain gray/silver parts, red details, outlines, and transparency.
3. Export at the original dimensions and pixel-art scale.
4. Place the edited sprite and its matching JSON definitions at the correct relative paths under `sprites/`.
5. Install the mod in the game's mods folder and test with the original game settings.
6. Check the log and confirm the mod loads without errors.

## Testing notes
The GitHub repository is a source project, not an installed mod. To test it, copy the mod folder into the Sonic 3 A.I.R. `mods` directory (or package it with the mod folder at the archive root), enable it in the game's Mods menu, and launch the game.

The current starter has not yet been tested in-game. Do not describe it as a working Metal Hedge character replacement until the sprite paths and assets have been installed and verified.
