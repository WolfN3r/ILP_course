# S3 — Model & Decision Variables

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] `addVar` vs `addVars`; vtype `CONTINUOUS` / `BINARY` / `INTEGER`
- [ ] Variable bounds (`lb`, `ub`) and names
- [ ] Placement: which variables describe a device's position (corner vs center; x, y)
- [ ] Parallel domain — production planning: which variables describe "how much to produce
      of each product"
- [ ] Reading results: `var.X` and `Model.ObjVal`

## Why it matters
Choosing decision variables is the first modeling decision, and it constrains everything
downstream. Seeing the same variable-design question asked twice — once for physical
positions, once for production quantities — shows what's placement-specific vs universal.

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
- Placement: `code/s3_model_variables/placement/task.py` — declare position variables for a
  small set of devices from `plumbing.py`'s device list.
- Parallel (production planning): `code/s3_model_variables/parallel_production_planning/task.py`
  — declare quantity variables for a small set of products with capacity bounds.

## What we achieved
_(Claude writes at the end)_
