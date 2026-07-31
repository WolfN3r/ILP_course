"""S11 -- YOUR task: build the infeasible model, confirm it's infeasible, then diagnose it.

Reuse your S6/S8 non-overlap + boundary + spacing logic against the plumbing.py data here,
which is deliberately too tight to satisfy.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import DEVICES, CHIP_WIDTH, CHIP_HEIGHT, MIN_SPACING, BIG_M_X, BIG_M_Y


def build_model() -> gp.Model:
    """TODO: build the same boundary + non-overlap + spacing model as S6/S8, using the
    DEVICES/CHIP_WIDTH/CHIP_HEIGHT/MIN_SPACING from plumbing.py. Should come out infeasible.
    """
    raise NotImplementedError


def diagnose(m: gp.Model) -> None:
    """TODO:
    1. Check m.Status == GRB.INFEASIBLE (or INF_OR_UNBD -- if so, set m.Params.DualReductions
       = 0 and re-optimize to disambiguate).
    2. Call m.computeIIS().
    3. Print the names of every constraint where constr.IISConstr is True.
    4. Optionally m.write("infeasible_model.ilp") to save the IIS for inspection.
    """
    raise NotImplementedError


if __name__ == "__main__":
    m = build_model()
    m.optimize()
    print(f"Status: {m.Status} (INFEASIBLE == {GRB.INFEASIBLE})")
    diagnose(m)
