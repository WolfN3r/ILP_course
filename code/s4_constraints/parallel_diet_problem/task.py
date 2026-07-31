"""S4 parallel domain -- YOUR task: add budget and minimum-nutrient constraints.

Same pattern as the placement boundary constraints -- linear inequalities bounding a
weighted sum -- applied to cost and nutrients instead of x/y coordinates.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import FOODS, MIN_CALORIES, MIN_PROTEIN, BUDGET, print_diet


def build_model() -> tuple:
    """TODO:
    1. Create the Model and a quantity variable (>= 0) per food.
    2. Add: sum(cost_i * qty_i) <= BUDGET
    3. Add: sum(calories_i * qty_i) >= MIN_CALORIES
    4. Add: sum(protein_i * qty_i) >= MIN_PROTEIN
    Use gp.quicksum. No objective yet.
    Return (model, {food_name: quantity_var}).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, variables = build_model()
    m.optimize()
    quantities = {name: v.X for name, v in variables.items()}
    print_diet(quantities)
