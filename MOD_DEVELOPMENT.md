# Project Metal Hedge — Mod Development

## Current safe starter

- `mod.json`: mod metadata.
- `icon.png`: mod icon.
- `scripts/main.lemon`: intentionally no-op script entry point.
- `sprites/`, `rawdata/`, and `audio/`: reserved for future assets.

## Design requirements

- Sonic, Tails, and Knuckles all remain playable.
- Keep the original controls and physics.
- Metal Hedge is Eggman's robotic antagonist.
- **Current random boss target: Launch Base Zone Act 2.**

## First implementation target: Launch Base Zone Act 2 boss

The goal is to replace or adapt the target boss's appearance so it becomes Metal Hedge-themed, without breaking the encounter or other playable characters.

### Before editing assets

1. Inspect the installed Sonic 3 A.I.R. version and its modding documentation.
2. Identify the exact Launch Base Zone Act 2 boss sprite/assets and any matching definitions or data files.
3. Verify the supported override paths and formats. Do not guess filenames or assume that a sprite-only replacement can change the boss.
4. Preserve a clean copy of the original assets for comparison.

### Implementation and test checklist

- [ ] Confirm the boss asset paths and supported replacement method.
- [ ] Create Metal Hedge-inspired pixel art in the required format and dimensions.
- [ ] Add the replacement files at the correct relative paths.
- [ ] Install/enable the mod and test the Launch Base Zone Act 2 encounter.
- [ ] Verify the boss renders correctly and its behavior remains functional.
- [ ] Verify Sonic, Tails, and Knuckles are all still playable.
- [ ] Check logs and record the game/mod version tested.

## Testing notes

The GitHub repository is a source project, not an installed mod. To test it, copy the mod folder into the Sonic 3 A.I.R. `mods` directory (or package it with the mod folder at the archive root), enable it in the game's Mods menu, and launch the game.

The current starter has not yet been tested as a boss replacement. Do not describe the Launch Base boss as changed until the actual asset/data override has been implemented and verified in-game.
