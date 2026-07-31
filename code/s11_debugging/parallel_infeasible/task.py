"""S11 parallel domain -- YOUR task: same diagnostic workflow, applied to an over-constrained
schedule instead of an over-constrained layout.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import JOBS, HORIZON


def build_model() -> gp.Model:
    """TODO: build the same single-machine non-overlap schedule model as S6's parallel task,
    using JOBS/HORIZON from plumbing.py. Should come out infeasible.
    """
    raise NotImplementedError


def diagnose(m: gp.Model) -> None:
    """TODO: same as placement_infeasible/task.py -- computeIIS(), print IIS constraints."""
    raise NotImplementedError


if __name__ == "__main__":
    m = build_model()
    m.optimize()
    print(f"Status: {m.Status} (INFEASIBLE == {GRB.INFEASIBLE})")
    diagnose(m)
