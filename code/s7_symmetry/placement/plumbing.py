"""S7 -- plumbing: devices, chip, and a symmetry spec.

M1/M2 must be a mirrored pair about a shared vertical axis. M3 is self-symmetric (centered
on that same axis). M4/M5 are unconstrained by symmetry, just for contrast.
"""

DEVICES = [
    ("M1", 4.0, 2.0),
    ("M2", 4.0, 2.0),
    ("M3", 3.0, 3.0),
    ("M4", 2.0, 5.0),
    ("M5", 6.0, 1.5),
]

CHIP_WIDTH = 20.0
CHIP_HEIGHT = 12.0

SYMMETRY_PAIRS = [("M1", "M2")]   # (a, b): mirrored about the shared axis
SELF_SYMMETRIC = ["M3"]           # centered exactly on the shared axis

DEVICE_DIMS = {d[0]: (d[1], d[2]) for d in DEVICES}


def print_positions_with_axis(positions: dict, axis_x: float) -> None:
    print(f"Symmetry axis x = {axis_x:.2f}")
    print(f"{'device':6} {'x':>8} {'y':>8}")
    for dev_id, (x, y) in positions.items():
        print(f"{dev_id:6} {x:8.2f} {y:8.2f}")
