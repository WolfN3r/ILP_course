# S7 — Symmetry & Matching

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] Why symmetry/matching matters in analog design (matched transistor pairs)
- [ ] Symmetric pair about a vertical axis: the equality constraints
- [ ] Self-symmetric devices centered on the axis
- [ ] Symmetry groups; axis as a fixed value vs a decision variable
- [ ] Parallel domain — an assignment/matching problem: pairing workers to tasks (or
      students to projects) with equality/one-to-one constraints instead of a spatial axis

## Why it matters
Symmetry constraints are just structured equalities — `x_a + x_b == 2·x_axis` isn't
conceptually different from "each worker assigned to exactly one task." Seeing equality
constraints used for a *geometric* relationship vs a *combinatorial* one builds the same
muscle two ways.

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
- Placement: `code/s7_symmetry/placement/task.py` — add symmetry-pair and self-symmetric
  equality constraints about a shared axis.
- Parallel (assignment): `code/s7_symmetry/parallel_assignment/task.py` — add one-to-one
  assignment (each worker exactly one task, each task exactly one worker) equality
  constraints and an objective (e.g. minimize total cost).

## What we achieved
_(Claude writes at the end)_
