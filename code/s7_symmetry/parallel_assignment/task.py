"""S7 parallel domain -- YOUR task: one-to-one assignment with equality constraints.

For each worker: sum of their assignment binaries across all tasks == 1.
For each task: sum of its assignment binaries across all workers == 1.
Minimize total cost.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import WORKERS, TASKS, COST, print_assignment


def build_model() -> tuple:
    """TODO:
    1. Binary variable x[w, t] for every (worker, task) pair.
    2. For each worker: sum_t x[w, t] == 1.
    3. For each task: sum_w x[w, t] == 1.
    4. Objective: minimize sum(COST[w][t] * x[w, t]).
    Return (model, {(worker, task): binary_var}).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, variables = build_model()
    m.optimize()
    assignment = {w: t for (w, t), v in variables.items() if v.X > 0.5}
    print_assignment(assignment)
    print(f"Total cost: {m.ObjVal:.2f}")
