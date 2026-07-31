"""S2 -- YOUR task: rebuild S1's tiny LP and MILP as gurobipy models.

Compare against your S1 brute-force results (both the answer and the runtime).
"""
from plumbing import LP_OBJECTIVE_COEFFS, LP_KNOWN_OPTIMUM, KNAPSACK_ITEMS, KNAPSACK_CAPACITY, timed


def solve_lp_gurobi() -> dict:
    """TODO: same LP as s1_optimizer_theory/lp_bruteforce (max 3x+5y s.t. x<=4, 2y<=12,
    3x+2y<=18, x,y>=0) but built with gurobipy.
    Use: gp.Model, Model.addVar, Model.addConstr, Model.setObjective, Model.optimize.
    Return {"x": ..., "y": ..., "objective": ...}.
    """
    raise NotImplementedError


def solve_knapsack_gurobi() -> dict:
    """TODO: same 0/1 knapsack as s1_optimizer_theory/milp_bruteforce, built with gurobipy.
    Use: Model.addVars(..., vtype=GRB.BINARY), gp.quicksum for the capacity constraint and
    the objective.
    Return {"selection": ..., "value": ...}.
    """
    raise NotImplementedError


if __name__ == "__main__":
    with timed("gurobipy LP solve"):
        lp_result = solve_lp_gurobi()
    print(f"gurobipy LP result: {lp_result}  (known optimum: {LP_KNOWN_OPTIMUM})")

    with timed("gurobipy knapsack solve"):
        knapsack_result = solve_knapsack_gurobi()
    print(f"gurobipy knapsack result: {knapsack_result}")
