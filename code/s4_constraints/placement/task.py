"""S4 -- YOUR task: add boundary constraints so every device stays inside the chip.

No overlap handling yet (that's S6) -- devices may still overlap each other here.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import DEVICES, CHIP_WIDTH, CHIP_HEIGHT, print_positions


def build_model() -> tuple:
    """TODO:
    1. Create the Model and, for each device, x/y variables (as in S3).
    2. Add boundary constraints: x + width <= CHIP_WIDTH, y + height <= CHIP_HEIGHT
       (and x, y >= 0 via variable lower bounds).
    3. No objective yet -- any feasible point is fine for this task.
    Return (model, {device_id: (x_var, y_var)}).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, variables = build_model()
    m.optimize()
    positions = {dev_id: (xv.X, yv.X) for dev_id, (xv, yv) in variables.items()}
    print_positions(positions)
