"""S7 -- YOUR task: add symmetry constraints about a shared vertical axis.

For a mirrored pair (a, b): their y's match, and their x's are mirrored around the axis:
  x_a + x_a_width == 2 * axis_x - (x_b - x_b)  -- work out the exact equality yourself,
  it's simpler than it looks once you draw it (mirrored means a's right edge and b's left
  edge are symmetric distances from the axis).
For a self-symmetric device: it must be centered exactly on the axis.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import DEVICES, CHIP_WIDTH, CHIP_HEIGHT, SYMMETRY_PAIRS, SELF_SYMMETRIC, \
    DEVICE_DIMS, print_positions_with_axis


def build_model() -> tuple:
    """TODO:
    1. Position variables + boundary constraints (from S4). Add non-overlap too if you want
       a fully realistic model, or skip it to isolate the symmetry logic -- your call.
    2. An axis_x variable (fixed value or decision variable -- try fixed first).
    3. Equality constraints for each pair in SYMMETRY_PAIRS.
    4. Equality constraints for each device in SELF_SYMMETRIC.
    Return (model, {device_id: (x_var, y_var)}, axis_x_var_or_value).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, variables, axis_x = build_model()
    m.optimize()
    positions = {dev_id: (xv.X, yv.X) for dev_id, (xv, yv) in variables.items()}
    axis_value = axis_x.X if hasattr(axis_x, "X") else axis_x
    print_positions_with_axis(positions, axis_value)
