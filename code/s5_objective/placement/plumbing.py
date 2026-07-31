"""S5 -- plumbing: devices, chip, and nets. A net connects several devices (by center point)
and its HPWL is the half-perimeter of the bounding box around those centers.
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

# Each net lists the device ids whose centers it connects.
NETS = [
    ("net_0", ["M1", "M2"]),
    ("net_1", ["M2", "M3", "M4"]),
    ("net_2", ["M4", "M5"]),
]

DEVICE_DIMS = {d[0]: (d[1], d[2]) for d in DEVICES}


def print_result(positions: dict, hpwl_total: float) -> None:
    print(f"{'device':6} {'x':>8} {'y':>8}")
    for dev_id, (x, y) in positions.items():
        print(f"{dev_id:6} {x:8.2f} {y:8.2f}")
    print(f"Total HPWL: {hpwl_total:.2f}")
