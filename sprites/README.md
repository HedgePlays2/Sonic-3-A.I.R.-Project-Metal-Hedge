# Sprite Mod Assets

## Original Metal Hedge concept

- `metal-hedge-concept.svg` — original editable concept strip with six small poses.
- `metal-hedge-sprite-atlas-draft.png` — first transparent pixel-art draft atlas, 384×64 overall with six 64×64 cells (idle, walk, quill pose, raised quills, arm pose, and damage flash).
- The root-level `metalhedge.png` is the approved visual/reference sheet showing the intended character, animation groups, and boss sequence. Use it as the appearance guide when refining the draft atlas.
- The separate root-level Metal Sonic sprite sheet is a credited reference and is not the approved Metal Hedge design.

## Important status

The new PNG is a **rough sprite draft**, not a drop-in Sonic 3 A.I.R. runtime replacement. It has not yet been matched to the game's native tile dimensions, palette encoding, mappings, compression, or injection method. The reference sheet shows a more detailed 128×128-per-frame target; the draft atlas needs another pixel-art pass to match that detail and scale.

## Conversion checklist

- [x] Add an original green Metal Hedge concept asset.
- [x] Add a first transparent pixel-art atlas draft.
- [ ] Refine the frames to match the approved `metalhedge.png` reference at the correct native scale.
- [ ] Export frames in the game's expected graphics format and palette.
- [ ] Match the correct Launch Base boss mappings.
- [ ] Verify the correct ROM injection location before writing any raw-data override.
- [ ] Test the replacement in-game before claiming the boss has changed.

Do not treat the SVG or draft PNG as a drop-in runtime replacement. The script entry point intentionally remains safe/no-op until the supported LemonScript API and exact asset-loading mechanism are verified.
