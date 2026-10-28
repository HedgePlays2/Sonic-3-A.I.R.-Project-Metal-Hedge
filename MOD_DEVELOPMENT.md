# Project Metal Hedge — Mod Development

## Current safe starter

- `mod.json`: mod metadata.
- `icon.png`: mod icon.
- `scripts/main.lemon`: intentionally no-op script entry point.
- `sprites/`, `rawdata/`, and `audio/`: reserved for future assets.
- Root-level reference image: `Custom _ Edited - Sonic the Hedgehog Customs - Metal Sonic - Metal Sonic (Sonic 3-Style).png`.

## Design requirements

- Sonic, Tails, and Knuckles all remain playable.
- Keep the original controls and physics.
- Metal Hedge is Eggman's robotic antagonist.
- **Current boss target: Launch Base Zone Act 2.**

## Sprite reference and credits

The repository now contains the Metal Sonic (Sonic 3-Style) sprite sheet as a **reference image** for planning the boss appearance. The image's own credits panel names J.I.B and Tanner; the project README credits both and links to the source listing on The Spriters Resource.

This PNG is not yet a game-ready replacement. It must not be treated as if it already has the game's exact tile data, mappings, palette format, or compression. Before redistributing the sprite sheet with a public mod release, verify the original artwork's reuse permissions.

## Research so far

The Sonic 3 & Knuckles disassembly identifies Launch Base's boss mapping files as:

- `Levels/LBZ/Misc Object Data/Map - Final Boss 1.asm`
- `Levels/LBZ/Misc Object Data/Map - Final Boss 2.asm`

The disassembly's SonLVL project identifies the mapped boss artwork as `Levels/LBZ/Nemesis Art/Final Boss 1.nem`, paired with `Levels/LBZ/Misc Object Data/Map - Final Boss 1.asm` (the project uses this pair for multiple frames). Palette leads include `Levels/LBZ/Palettes/Final Boss 1.bin` and `Levels/LBZ/Palettes/End Boss.bin`. This confirms a source art filename and mapping relationship, but not a ready-to-inject A.I.R. replacement: the exact binary format/compression, the boss's runtime use in Act 2, and the ROM injection offset still need verification.

Sonic 3 A.I.R. raw-data mods use binary files under `rawdata/` plus a JSON entry containing a `File` and a `RomInject` address. A wrong offset can overwrite unrelated ROM data, so do not guess the address. The GameBanana boss-sprite tutorial recommends extracting/editing the boss art with Flex 2 using the matching mapping and palette, then injecting the edited binary.

## First implementation target: Launch Base Zone Act 2 boss

The goal is to replace or adapt the target boss's appearance so it becomes Metal Hedge-themed, without breaking the encounter or other playable characters.

### Before editing assets

1. Obtain the Sonic 3 & Knuckles disassembly and the matching Sonic 3 A.I.R. modding documentation.
2. Inspect the Launch Base boss art, mappings, compression format, and palette together.
3. Make a green Metal Hedge art draft from the credited sprite reference, while preserving individual animation frames and transparent pixels. Keep this as a separate working asset; do not overwrite the original reference.
4. Use a compatible editor such as Flex 2 to export the mapped in-game boss sprite, create/import the Metal Hedge version, and preserve the expected layout.
5. Verify the correct ROM injection offset from the exact source ROM/disassembly and document the source of that offset.

### Implementation and test checklist

- [x] Locate and retain the credited Metal Sonic (Sonic 3-Style) reference sheet in the repository.
- [x] Add J.I.B and TannerTH25 attribution to the README.
- [ ] Verify permission/terms for redistributing the reference artwork.
- [ ] Confirm the exact target boss art file, compression format, and matching mappings.
- [ ] Create a green Metal Hedge sprite draft that preserves the reference sheet's frame layout.
- [ ] Confirm the ROM injection offset from a reliable source.
- [ ] Convert/import the replacement into the required game format.
- [ ] Add the replacement binary and `rawdata/rominjections.json`.
- [ ] Install/enable the mod and test the Launch Base Zone Act 2 encounter.
- [ ] Verify the boss renders correctly and its behavior remains functional.
- [ ] Verify Sonic, Tails, and Knuckles are all still playable.
- [ ] Check logs and record the game/mod version tested.

## Testing notes

The GitHub repository is a source project, not an installed mod. To test it, copy the mod folder into the Sonic 3 A.I.R. `mods` directory (or package it with the mod folder at the archive root), enable it in the game's Mods menu, and launch the game.

The current starter has not yet been tested as a boss replacement. Do not describe the Launch Base boss as changed until the actual asset/data override has been implemented and verified in-game.
