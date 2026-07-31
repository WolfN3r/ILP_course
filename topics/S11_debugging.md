# S11 — Debugging & Experiments

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] Solve status codes (`OPTIMAL`, `INFEASIBLE`, `INF_OR_UNBD`, `TIME_LIMIT`, ...)
- [ ] `computeIIS()` to find why a model is infeasible; reading the IIS output
- [ ] `Model.write("model.lp")` to inspect the actual model Gurobi sees
- [ ] Placement: deliberately over-constrain a small placement model (e.g. impossible
      spacing) and diagnose it
- [ ] Parallel domain: deliberately over-constrain a small scheduling model (e.g. more jobs
      than time slots on a machine) and diagnose it
- [ ] Running controlled parameter experiments; runtime vs quality trade-offs, recap of S9

## Why it matters
Real models go infeasible or slow, and the diagnostic toolkit (`computeIIS`, `.lp` export,
status codes) is domain-independent — the same three tools debug a placement model or a
scheduling model.

## Notes
### Concept
_(added live)_

### gurobipy tools seen
- `Model.computeIIS` —
- `Model.write` —
- `Model.Status` —

### Doc links
-

### My questions / sticking points
-

## Task(s) — mine to write
- Placement: `code/s11_debugging/placement_infeasible/task.py` — build the deliberately
  infeasible placement model, run `computeIIS()`, identify the conflicting constraints.
- Parallel (scheduling): `code/s11_debugging/parallel_infeasible/task.py` — same exercise for
  an over-constrained scheduling model.

## What we achieved
_(Claude writes at the end)_
