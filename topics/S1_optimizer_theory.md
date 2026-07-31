# S1 — Optimizer Theory (pure Python)

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] What an optimization problem is: decision variables, constraints, objective
      (plain-language example first, then notation)
- [ ] What "linear" means; LP vs MILP vs other families (NLP, CP, heuristics/metaheuristics
      like simulated annealing/genetic algorithms) — a comparison: what each is good/bad for
- [ ] Continuous vs discrete decisions; why non-overlap needs binary/integer variables
- [ ] Build a brute-force / grid-search optimizer in pure Python for a tiny LP
      (`lp_bruteforce/`)
- [ ] Build a brute-force / grid-search optimizer in pure Python for a tiny MILP
      (`milp_bruteforce/`)
- [ ] Where brute force breaks down: combinatorial explosion as variables/binaries grow —
      this motivates why real solvers (branch-and-bound, cutting planes) exist

## Why it matters
Before learning gurobipy's API, you should understand *what a solver is actually doing* —
searching a space of candidate solutions for the best feasible one. Writing the dumbest
possible version of that yourself makes every later Gurobi feature legible instead of magic.

## Notes
### Concept
_(added live — LP vs MILP definitions, complexity intuition, comparison table go here)_

### gurobipy tools seen
- _(none yet — pure Python this session)_

### Doc links
-

### My questions / sticking points
-

## Task(s) — mine to write
- `code/s1_optimizer_theory/lp_bruteforce/task.py` — grid-search a tiny 2-variable LP
  (continuous), compare your found optimum against the true corner-point optimum.
- `code/s1_optimizer_theory/milp_bruteforce/task.py` — enumerate a tiny knapsack-style MILP
  (small number of binary items), find the best feasible combination by brute force.

## What we achieved
_(Claude writes at the end)_
