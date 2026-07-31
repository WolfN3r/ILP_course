"""S5 -- YOUR task: minimize total HPWL over the nets.

For each net, HPWL = (max_x - min_x) + (max_y - min_y) over the centers of the devices on
that net. max/min aren't linear directly -- you need helper variables + constraints to
linearize them (a hi variable that is >= every center x on the net, a lo variable that is
<= every center x on the net; hi - lo becomes part of the objective).
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import DEVICES, CHIP_WIDTH, CHIP_HEIGHT, NETS, DEVICE_DIMS, print_result


def build_model() -> tuple:
    """TODO:
    1. Position variables x, y (bottom-left corner) per device, bounded to the chip
       (reuse your S4 boundary constraints).
    2. Center-point expressions: cx = x + width/2, cy = y + height/2 per device.
    3. Per net: x_lo/x_hi/y_lo/y_hi helper variables with
       x_lo <= cx_i <= x_hi (and same for y) for every device i on the net.
    4. Objective: minimize sum over nets of (x_hi - x_lo) + (y_hi - y_lo).
    Use Model.setObjective with GRB.MINIMIZE.
    Return (model, {device_id: (x_var, y_var)}, hpwl_total_expression_or_value_getter).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, variables, get_hpwl_total = build_model()
    m.optimize()
    positions = {dev_id: (xv.X, yv.X) for dev_id, (xv, yv) in variables.items()}
    print_result(positions, get_hpwl_total())
