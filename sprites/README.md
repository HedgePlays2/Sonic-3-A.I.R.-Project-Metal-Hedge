# Metal Hedge sprite assets

## Approved source

`../metalhedge.png` is the approved 1175×790 reference sheet. It is the source of truth for the design and poses. Do not substitute the discarded SVG concept.

## Frame extraction

Run:

```bash
python -m pip install Pillow
python tools/extract_metal_hedge.py
```

The script writes transparent 128×128 PNG working frames to
`build/metal-hedge-frames/`, grouped into idle, walk, run/dash, jump,
spin attack, hit/damage, defeat, and boss sequence. It samples the 16-color
swatch strip printed on the reference sheet and nearest-neighbor scales.

A GitHub Actions workflow also runs this extractor when the source sheet or
extractor changes and publishes the output as the
`metal-hedge-128px-frames` workflow artifact.

## Important runtime limitation

These PNGs are extracted working assets, **not yet a Sonic 3 A.I.R. runtime
sprite replacement**. The Launch Base Zone Act 2 boss uses game-specific
compressed art, mappings, palette and ROM injection data. Those must be
verified against the exact target game data before creating any injection.
Never guess a ROM offset or claim the boss has changed until tested in-game.
