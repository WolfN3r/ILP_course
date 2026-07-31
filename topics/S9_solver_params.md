# S9 — Solver Parameters & Tuning

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] Reading the solver log: incumbent, bound, gap, explored nodes
- [ ] `MIPGap` and `TimeLimit` — the main runtime levers, and how `MIPGap` in particular can
      make the *returned solution* different, not just slower/faster
- [ ] Speed-only params: `Threads`, `Presolve`, `Method` — benchmark them and confirm the
      final objective/solution is identical, only wall-clock changes
- [ ] Solution-changing params: `Cuts`, `Symmetry`, `Heuristics`, `MIPFocus` — benchmark them
      and check whether, under a time limit or nonzero gap, they land on a *different*
      solution (in placement: does the layout actually look different?)
- [ ] `Model.tune()` — run it on one of your models, inspect `TuneResults`, and judge: did it
      find better parameters than your manual guesses? Was it worth the tuning time spent?
- [ ] `NonConvex` (if a nonconvex term like `area = width × height` ever appears)

## Why it matters
Not all Gurobi parameters are the same kind of knob. Some only affect *how fast* you get to
the one true optimum; others can change *which* solution you get when you stop early — which
matters a lot if "early" is the normal operating mode (as it is for the real ALDA project,
`TimeLimit=20`, `MIPGap=0.1`). Confusing the two categories leads to wrong conclusions about
what a parameter "does."

## Notes
### Concept
_(added live — keep a running table: param | category (speed-only / solution-changing) |
observed effect | model it was tested on)_

### gurobipy tools seen
- `Model.setParam` / `Model.Params.*` —
- `Model.tune()` / `Model.getTuneResult()` —
- `Model.Params.LogToConsole`, log fields (`Incumbent`, `BestBd`, `Gap`, `Nodes`) —

### Doc links
-

### My questions / sticking points
-

## Task(s) — mine to write
- `code/s9_solver_params/speed_only_params/task.py` — use the benchmark harness
  (`code/s9_solver_params/benchmark_harness.py`, plumbing) to sweep `Threads`/`Presolve` on a
  fixed model; confirm the objective value and variable values don't change, only time.
- `code/s9_solver_params/solution_changing_params/task.py` — sweep `Cuts`/`Symmetry`/
  `MIPFocus` under a tight `TimeLimit` or nonzero `MIPGap`; check whether the returned
  solution actually differs run to run.
- `code/s9_solver_params/tuning_tool/task.py` — run `Model.tune()` on one model and compare
  its suggested parameter set against your own manual choices from the two tasks above.

## What we achieved
_(Claude writes at the end)_
