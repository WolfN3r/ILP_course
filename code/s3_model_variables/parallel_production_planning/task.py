"""S3 parallel domain -- YOUR task: declare decision variables for production quantities.

Same idea as the placement task, different physical meaning: continuous quantity variables
bounded by demand, instead of position variables bounded by chip size.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import PRODUCTS, TOTAL_RESOURCE_UNITS, print_plan


def build_variables(m: gp.Model) -> dict:
    """TODO: for each product in PRODUCTS, add a quantity variable bounded by
    [0, max_demand]. Return {product_name: quantity_var}.
    """
    raise NotImplementedError


if __name__ == "__main__":
    m = gp.Model("s3_production_variables")
    variables = build_variables(m)
    m.optimize()
    quantities = {name: v.X for name, v in variables.items()}
    print_plan(quantities)
