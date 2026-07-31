# S10 — Read My Existing Project

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.
> No `code/` scaffolding for this session — we read `../ALDA_placementOptimizer` directly.
> We do not modify that project during this course.

## Subtopics
- [ ] Open `ALDA_placementOptimizer/WorkDir/scripts/lib/ilp_optimizer.py` together
- [ ] Map its variables (`W`, `H`, `x`, `y`, `s[bid]`, `rv`, `x_sym`, `x_lo/x_hi/y_lo/y_hi`)
      to S3's variable concepts
- [ ] Map its constraints (boundary, non-overlap disjunctions, symmetry equalities, HPWL
      bounding-box) to S4/S6/S7 concepts
- [ ] Map its objective (weighted HPWL + area/aspect-ratio terms) to S5 concepts
- [ ] Read the `GurobiParams` dataclass and its inline comments — cross-check against your
      S9 findings on speed-only vs solution-changing parameters
- [ ] Identify what's safe to change and experiment with vs what's load-bearing

## Why it matters
This is the payoff session: everything from S1–S9 should now let you read code you didn't
write and understand *why* it's shaped the way it is, not just *that* it works.

## Notes
### Concept
_(added live)_

### gurobipy tools seen
- _(cross-reference to S3–S9 — nothing new in API terms, just seeing it at real-project
  scale)_

### Doc links
-

### My questions / sticking points
-

## What we achieved
_(Claude writes at the end)_
