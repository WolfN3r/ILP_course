# S8 — Orientation, Spacing, Alignment

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] Rotation / flip modeled with binary variables (width/height swap)
- [ ] Minimum spacing / DRC margins between devices
- [ ] Alignment and abutment constraints
- [ ] Fixed grid vs continuous coordinates
- [ ] Parallel domain — 2D bin packing with rotation: same width/height-swap binaries, same
      spacing idea (here: no gap requirement, but items *can* rotate 90°)

## Why it matters
This session adds "extra" binary decisions (does the piece rotate?) on top of the non-overlap
skeleton from S6. Bin packing is the textbook version of exactly this pattern without any
of analog design's domain baggage.

## Notes
### Concept
_(added live)_

### gurobipy tools seen
-

### Doc links
-

### My questions / sticking points
-

## Task(s) — mine to write
- Placement: `code/s8_orientation_spacing/placement/task.py` — add rotation binaries and
  minimum-spacing margins to the non-overlap model from S6.
- Parallel (bin packing): `code/s8_orientation_spacing/parallel_bin_packing/task.py` — add
  rotation binaries to a 2D bin-packing model (fit items into the fewest/smallest bins).

## What we achieved
_(Claude writes at the end)_
