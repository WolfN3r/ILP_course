"""S6 -- YOUR task: add non-overlap constraints between every pair of devices.

For each pair (a, b), at least one of these must hold:
  a is left of b   |  a is right of b   |  a is below b   |  a is above b
Encode each as a binary * big-M relationship, and require the sum of the 4 binaries for a
pair to be >= 1 (the disjunction).
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import DEVICES, CHIP_WIDTH, CHIP_HEIGHT, BIG_M_X, BIG_M_Y, DEVICE_PAIRS, \
    print_positions, check_no_overlap


def build_model() -> tuple:
    """TODO:
    1. Position variables + boundary constraints (from S4).
    2. For each pair in DEVICE_PAIRS: 4 binary variables (left/right/below/above), the 4
       big-M constraints, and one constraint requiring their sum >= 1.
    3. No objective yet -- any feasible non-overlapping layout is fine.
    Return (model, {device_id: (x_var, y_var)}).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, variables = build_model()
    m.optimize()
    positions = {dev_id: (xv.X, yv.X) for dev_id, (xv, yv) in variables.items()}
    print_positions(positions)
    overlaps = check_no_overlap(positions)
    print(f"Overlapping pairs found: {overlaps if overlaps else 'none'}")
