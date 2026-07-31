"""S8 parallel domain -- YOUR task: fit all items into one bin, allowing 90-degree rotation.

Identical structure to the placement task: rotation binary -> effective width/height ->
boundary constraints -> non-overlap disjunction. No spacing margin needed here.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import ITEMS, BIN_WIDTH, BIN_HEIGHT, BIG_M_X, BIG_M_Y, ITEM_PAIRS, print_result


def build_model() -> tuple:
    """TODO: same shape as s8_orientation_spacing/placement/task.py, applied to ITEMS and
    the single BIN_WIDTH x BIN_HEIGHT bin, with MIN_SPACING = 0 (items may touch).
    Return (model, {item_id: (x_var, y_var)}, {item_id: rotation_var}).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, positions_vars, rotation_vars = build_model()
    m.optimize()
    if m.Status == GRB.OPTIMAL:
        positions = {item_id: (xv.X, yv.X) for item_id, (xv, yv) in positions_vars.items()}
        rotations = {item_id: rv.X for item_id, rv in rotation_vars.items()}
        print_result(positions, rotations)
    else:
        print(f"No feasible packing found (status {m.Status}) -- try a bigger bin.")
