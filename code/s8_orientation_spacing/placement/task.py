"""S8 -- YOUR task: add rotation binaries and minimum spacing to the S6 non-overlap model.

For each device: a binary r (0 = original orientation, 1 = rotated 90 degrees). Its
effective width/height become linear expressions in r:
  eff_width  = width  * (1 - r) + height * r
  eff_height = height * (1 - r) + width  * r
(both terms are constant * binary, so this stays linear -- no products of two variables.)

Then reuse S6's non-overlap disjunction, but with MIN_SPACING added to the big-M
inequalities so devices keep a gap instead of just touching.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import DEVICES, CHIP_WIDTH, CHIP_HEIGHT, MIN_SPACING, BIG_M_X, BIG_M_Y, \
    DEVICE_PAIRS, print_result


def build_model() -> tuple:
    """TODO:
    1. Position variables (from S4) and a rotation binary per device.
    2. Effective width/height linear expressions per device, as described above.
    3. Boundary constraints using effective width/height instead of the fixed ones.
    4. Non-overlap disjunction (from S6) using effective width/height, with MIN_SPACING
       added on the side of each big-M inequality that needs the gap.
    Return (model, {device_id: (x_var, y_var)}, {device_id: rotation_var}).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, positions_vars, rotation_vars = build_model()
    m.optimize()
    positions = {dev_id: (xv.X, yv.X) for dev_id, (xv, yv) in positions_vars.items()}
    rotations = {dev_id: rv.X for dev_id, rv in rotation_vars.items()}
    print_result(positions, rotations)
