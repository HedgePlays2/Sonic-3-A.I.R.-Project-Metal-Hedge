# Project Metal Hedge — Mod Development

## Current safe starter

- `mod.json`: mod metadata.
- `icon.png`: mod icon.
- `scripts/main.lemon`: intentionally no-op script entry point.
- `sprites/`, `rawdata/`, and `audio/`: reserved for runtime assets.
- Root-level approved artwork: `metalhedge.png`.

## Locked design requirements

- Sonic, Tails, and Knuckles all remain playable.
- Keep the original controls and physics.
- Metal Hedge is Eggman's robotic antagonist.
- **Current boss target: Launch Base Zone Act 2.**
- `metalhedge.png` is the approved visual source of truth. Do not substitute the discarded six-pose SVG concept or invent replacement poses.

## Approved Metal Hedge sprite sheet

The approved `metalhedge.png` sheet contains the actual Metal Hedge artwork and animation sequence. Its information panel specifies **16-color, 128×128 pixels per frame**. Preserve the artwork's green armor, yellow reactor, silver mechanical details, red shoes, proportions, silhouettes, and the existing animation poses.

The sheet groups the poses into:
- Idle
- Walk
- Run / dash
- Jump
- Spin attack
- Hit / damage
- Defeat / explode
- Launch Base Zone Act 2 boss-fight sequence

Use the original sheet as the source when extracting frames. Keep it unchanged; put any cropped, cleaned, indexed, or converted working frames in a separate folder under `sprites/`. Do not redraw the character or use the discarded concept.

The sheet's credits panel names **J.I.B.** for the original Metal Sonic artwork and **TannerTH25** for the Metal Sonic (Sonic 3-Style) custom/edited sprite sheet. The project README links to the source listing. Check applicable reuse permissions before redistributing any third-party source artwork; the presence of the reference in this development repository does not itself establish redistribution permission.

## Runtime conversion research

The Sonic 3 & Knuckles disassembly identifies Launch Base boss mapping files:

- `Levels/LBZ/Misc Object Data/Map - Final Boss 1.asm`
- `Levels/LBZ/Misc Object Data/Map - Final Boss 2.asm`

The SonLVL definition `SonLVL INI Files/LBZ/FinalBoss1.xml` identifies the mapped object as **Boss (Knuckles)** and pairs `Levels/LBZ/Nemesis Art/Final Boss 1.nem` with `Levels/LBZ/Misc Object Data/Map - Final Boss 1.asm`. The art is Nemesis-compressed (the `.nem` format). The mapping table contains 44 frame entries; the SonLVL definition uses mapping frames 0, 1, 2, 4, and 10 for its main body, rockets, cockpit, gun, and fire components. The XML uses palette start index 6 for several of those mapped parts. Palette leads include `Levels/LBZ/Palettes/Final Boss 1.bin` and `Levels/LBZ/Palettes/End Boss.bin`.

The disassembly also defines separate LBZ boss art entries: `Final Boss 2.kosm` is Kosinski-M compressed, not Nemesis-compressed. This means the fight's related boss components are not necessarily one interchangeable sprite file. The exact Act 2 runtime use of each object/art set, tile layout, palette compatibility, and ROM injection offset still require verification. The GameBanana boss-sprite tutorial describes using Flex 2 with the correct compressed art type, mappings, and palette to export/import mapped sprites.

Sonic 3 A.I.R. raw-data mods place binary files under `rawdata/` and describe them in JSON using `File` and `RomInject`. The injection address must be verified against the exact source ROM/disassembly. **Never guess a ROM offset**: an incorrect address can overwrite unrelated game data.

## First implementation target: Launch Base Zone Act 2 boss

The goal is to adapt the target boss's appearance to Metal Hedge while preserving the encounter's existing behavior and the rest of the game.

### Before editing runtime assets

1. Obtain the Sonic 3 & Knuckles disassembly and matching Sonic 3 A.I.R. modding documentation.
2. Inspect both Launch Base boss art sets and determine which objects/characters use each one; do not assume the Knuckles-specific `Final Boss 1` definition is the whole Act 2 encounter.
3. Inspect the selected art's compression, mappings, and palette together.
4. Extract the required poses from the approved `metalhedge.png` sheet into separate working files, preserving the original frame artwork and transparency.
5. Use Flex 2 (or a compatible verified toolchain) to match the game's mapped sprite layout and import the Metal Hedge frames.
6. Verify the target boss's ROM injection offset from the exact source ROM/disassembly and document the evidence before creating an injection entry.

### Implementation and test checklist

- [x] Keep the approved `metalhedge.png` source sheet in the repository.
- [x] Record the approved frame categories, dimensions, palette depth, and design constraints.
- [x] Credit J.I.B. and TannerTH25 in the README.
- [ ] Verify permission/terms for redistributing third-party source artwork.
- [ ] Confirm the exact target boss art, compression format, mappings, and palette.
- [ ] Extract the required frames from `metalhedge.png` without redesigning them.
- [ ] Confirm the ROM injection offset from a reliable source.
- [ ] Convert/import the replacement into the required game format.
- [ ] Add the verified replacement binary and `rawdata/rominjections.json`.
- [ ] Install/enable the mod and test the Launch Base Zone Act 2 encounter.
- [ ] Verify the boss renders correctly and its behavior remains functional.
- [ ] Verify Sonic, Tails, and Knuckles are all still playable.
- [ ] Check logs and record the game/mod version tested.

## Testing notes

The GitHub repository is a source project, not an installed mod. To test it, copy the mod folder into the Sonic 3 A.I.R. `mods` directory (or package it with the mod folder at the archive root), enable it in the game's Mods menu, and launch the game.

The current starter has not yet been tested as a boss replacement. Do not describe the Launch Base boss as changed until the actual runtime asset/data override has been implemented and verified in-game.
