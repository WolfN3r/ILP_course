# S2 — gurobipy Introduction

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] Confirm installed `gurobipy` version and license type (academic/WLS) — recap from S0
- [ ] `Model` and `Env` objects; what a "session" with the solver looks like
- [ ] Re-solve S1's tiny LP in gurobipy (`first_model/`) — compare code shape and runtime
      against your brute-force version
- [ ] Re-solve S1's tiny MILP in gurobipy — same comparison
- [ ] Anatomy of a Gurobi program: `Model()` → `addVar`/`addVars` → `addConstr` →
      `setObjective` → `optimize()` → read `.X` / `ObjVal`
- [ ] Solve status basics: `GRB.OPTIMAL`, `GRB.INFEASIBLE`, `GRB.TIME_LIMIT` (just enough to
      recognize them — full debugging is S11)

## Why it matters
This is the bridge session: you already know *what* a solver does from S1 because you built
one. Now you see the real thing, and can directly compare "my grid search took N seconds and
only handled a toy size" against "Gurobi does this instantly and scales."

## Notes
### Concept
_(added live)_

### gurobipy tools seen
- `Model` —
- `Model.addVar` / `addVars` —
- `Model.addConstr` —
- `Model.setObjective` —
- `Model.optimize` —

### Doc links
-

### My questions / sticking points
-

## Task(s) — mine to write
- `code/s2_gurobipy_intro/setup_check/task.py` — quick script confirming `gurobipy` import,
  version, and a trivial solve (this one's nearly all yours to run/read, not much to "write").
- `code/s2_gurobipy_intro/first_model/task.py` — re-implement S1's tiny LP and MILP as
  gurobipy models; time both and compare against your brute-force numbers.

## What we achieved
_(Claude writes at the end)_
