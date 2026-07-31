# S4 — Linear Constraints

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] Building linear expressions; `quicksum`
- [ ] `addConstr` vs `addConstrs`
- [ ] Placement: boundary constraints — keep each device inside the chip outline
- [ ] Parallel domain — diet problem: budget and nutritional-minimum constraints
- [ ] Naming constraints and inspecting them

## Why it matters
Constraints are where "the problem's rules" live. Boundary-keeping and budget-limiting look
different on the surface but are the same linear-inequality pattern: `expression <= bound`.

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
- Placement: `code/s4_constraints/placement/task.py` — add boundary constraints so every
  device stays inside the chip outline defined in `plumbing.py`.
- Parallel (diet problem): `code/s4_constraints/parallel_diet_problem/task.py` — add budget
  and minimum-nutrient constraints over the food items defined in `plumbing.py`.

## What we achieved
_(Claude writes at the end)_
