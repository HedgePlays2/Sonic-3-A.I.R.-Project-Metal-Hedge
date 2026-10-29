# Sprite Mod Assets

## Original Metal Hedge concept

- `metal-hedge-concept.svg` — original editable concept strip with six small poses. It is authored for this project and does not reuse the credited Metal Sonic sprite sheet.
- The SVG is **source artwork only**. It is not yet a Sonic 3 A.I.R. replacement: the game's exact tile dimensions, palette restrictions, mappings, compression, and injection method still need to be confirmed.
- The existing root-level Metal Sonic sprite sheet is a separate reference and is not used by this new concept.

## Conversion checklist

- [x] Add an original green Metal Hedge concept asset.
- [ ] Redraw/refine the poses as pixel-perfect frames at the target game's native sprite scale.
- [ ] Export transparent PNG frames and convert them to the game's expected graphics format.
- [ ] Match the correct Launch Base boss mappings and palette.
- [ ] Verify the correct ROM injection location before writing any raw-data override.
- [ ] Test the replacement in-game before claiming the boss has changed.

Do not treat the SVG as a drop-in runtime replacement. The script entry point intentionally remains safe/no-op until the supported LemonScript API and exact asset-loading mechanism are verified.