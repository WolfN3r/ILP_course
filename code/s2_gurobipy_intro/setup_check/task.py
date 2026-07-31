"""S2 -- YOUR task: confirm gurobipy + license work, in your own words this time.

(code/s0_orientation/check_environment.py already did this for you once -- this is about
writing the four or five lines yourself so `Model()` / `addVar` / `optimize()` stop feeling
unfamiliar.)
"""


def confirm_setup() -> None:
    """TODO:
    1. import gurobipy as gp, from gurobipy import GRB
    2. print gp.gurobi.version()
    3. build a trivial Model, add one variable, one constraint, an objective
    4. call optimize() and print m.Status and the optimal value
    """
    raise NotImplementedError


if __name__ == "__main__":
    confirm_setup()
