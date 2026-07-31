"""S5 parallel domain -- YOUR task: set the objective to maximize total value.

Contrast with the placement task: here it's a plain linear MAXIMIZE over binary variables,
no linearization trick needed -- a good baseline before HPWL's max/min helper variables.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import ITEMS, CAPACITY, print_selection


def build_model() -> tuple:
    """TODO:
    1. Binary variable per item (Model.addVars(..., vtype=GRB.BINARY)).
    2. Capacity constraint: sum(weight_i * x_i) <= CAPACITY.
    3. Objective: maximize sum(value_i * x_i) via Model.setObjective(..., GRB.MAXIMIZE).
    Return (model, {item_name: binary_var}).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, variables = build_model()
    m.optimize()
    selection = {name: v.X for name, v in variables.items()}
    print_selection(selection)
    print(f"Total value: {m.ObjVal:.2f}")
