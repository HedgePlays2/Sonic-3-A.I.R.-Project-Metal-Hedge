# Sprite Mod Assets

## Approved Metal Hedge artwork

- `../metalhedge.png` is the approved Metal Hedge sprite/reference sheet and the source of truth for the character's design, animation poses, colors, proportions, and boss sequence.
- Use the actual artwork in `metalhedge.png` when preparing game assets. Do not substitute the older six-pose SVG concept or invent a different design.
- `metal-hedge-concept.svg` is an early discarded concept and is not the sprite source for the mod.

## Runtime conversion checklist

- [x] Approved full Metal Hedge reference sheet is present at the repository root.
- [ ] Extract the actual animation frames from `metalhedge.png` without redesigning them.
- [ ] Preserve each frame's original pose, silhouette, colors, and proportions while cleaning transparency/cropping only as needed.
- [ ] Determine the exact Launch Base boss tile dimensions, palette encoding, mappings, and compression.
- [ ] Convert the extracted frames to the format expected by Sonic 3 A.I.R.
- [ ] Verify the ROM injection location before adding any raw-data override.
- [ ] Test the replacement in-game before claiming the boss has changed.

The reference sheet is artwork documentation, not itself a drop-in runtime replacement. Do not create replacement sprites from the old SVG concept.
