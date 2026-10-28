# Sonic 3 A.I.R. — Project Metal Hedge

A fan-made **Sonic 3 A.I.R. mod** featuring **Metal Hedge**, a green robotic hedgehog created by Dr. Eggman.

## Story

Dr. Eggman has created Metal Hedge, a machine designed to imitate Sonic's speed and stop him. Eggman sends his new creation to Angel Island, where Sonic begins to uncover the secret project.

## Core goals

- Keep **Sonic, Tails, and Knuckles** playable.
- Keep the original controls, physics, and normal gameplay wherever possible.
- Make Metal Hedge Eggman's robotic antagonist—not a replacement for Sonic as the protagonist.
- First planned boss target: **Launch Base Zone Act 2**. The goal is to give the boss a Metal Hedge-themed replacement; the exact asset/data method must be confirmed before implementing it.
- Build and test in small steps so the original game remains playable.

## Development roadmap

### Starter
- [x] Create the project repository and initial documentation.
- [x] Add initial mod metadata and a no-op script entry point.
- [x] Record the planned boss target and playable-character requirements.
- [ ] Verify metadata and folder structure against current Sonic 3 A.I.R. mod documentation.

### First playable change
- [ ] Inspect the target game's Launch Base Zone Act 2 boss assets and replacement format.
- [ ] Create a Metal Hedge-inspired boss sprite/asset replacement that fits the game's existing dimensions and format.
- [ ] Add the replacement at the correct mod-relative paths.
- [ ] Test that the boss replacement works and Sonic, Tails, and Knuckles remain playable.

### Later
- [ ] Add story scenes and clues about Eggman's project.
- [ ] Develop a custom Metal Hedge boss fight if asset replacement alone is not enough.
- [ ] Test, fix bugs, document compatibility, and package a release.

## Current status

**Starter framework only.** The repository includes `scripts/main.lemon` as a no-op entry point and documented `sprites/`, `rawdata/`, and `audio/` folders. The mod currently does **not** replace the Launch Base Zone Act 2 boss or add Metal Hedge in-game.

## Project structure

- `mod.json` — mod metadata
- `icon.png` — mod icon
- `scripts/main.lemon` — script entry point (currently no-op)
- `sprites/` — reserved for sprite replacements and matching definition files
- `rawdata/` — reserved for future level/data edits
- `audio/` — reserved for future audio overrides
- `MOD_DEVELOPMENT.md` — implementation and testing checklist

## Requirements and compatibility

- **Game:** Sonic 3 A.I.R.
- **Game data:** A legally obtained, compatible Sonic 3 & Knuckles ROM is required by the game.
- **Compatibility:** The starter framework and metadata still need testing against the target game version.

## Credits and disclaimer

This is a fan project and is not an official SEGA release. Sonic and related official characters and assets belong to their respective rights holders. Original Metal Hedge artwork, writing, and project-created assets will be credited as they are added.
