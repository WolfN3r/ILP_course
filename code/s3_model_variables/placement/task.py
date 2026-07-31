"""S3 -- YOUR task: declare decision variables describing each device's position.

No constraints or objective yet -- just build the Model and the variables, then solve a
model with no constraints/objective to confirm the variables exist and .X reads back.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import DEVICES, CHIP_WIDTH, CHIP_HEIGHT, print_positions


def build_variables(m: gp.Model) -> dict:
    """TODO: for each device in DEVICES, add an x and y variable (bottom-left corner of the
    device) with sensible bounds so the device could plausibly fit on the chip.
    Use Model.addVar with vtype=GRB.CONTINUOUS, lb=..., ub=....
    Return {device_id: (x_var, y_var)}.
    """
    raise NotImplementedError


if __name__ == "__main__":
    m = gp.Model("s3_placement_variables")
    variables = build_variables(m)
    m.optimize()
    positions = {dev_id: (xv.X, yv.X) for dev_id, (xv, yv) in variables.items()}
    print_positions(positions)
