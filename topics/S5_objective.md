# S5 — The Objective

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] `setObjective`; `MINIMIZE` vs `MAXIMIZE`
- [ ] Placement: Half-Perimeter Wirelength (HPWL) — per-net bounding box, linearizing
      max/min over pins with helper variables
- [ ] Parallel domain — knapsack: maximizing total value under a weight/capacity constraint
- [ ] Weighted objectives (e.g. `α·wirelength + β·area`) and how trade-offs shift results

## Why it matters
The objective is where "what do I actually want" gets encoded. HPWL minimization and
knapsack value-maximization are structurally different (min vs max, and the linearization
trick for HPWL is specific to bounding boxes) — contrasting them sharpens both.

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
- Placement: `code/s5_objective/placement/task.py` — add HPWL helper variables and set the
  objective to minimize total wirelength over the nets in `plumbing.py`.
- Parallel (knapsack): `code/s5_objective/parallel_knapsack/task.py` — set the objective to
  maximize total value of selected items under the capacity constraint.

## What we achieved
_(Claude writes at the end)_
