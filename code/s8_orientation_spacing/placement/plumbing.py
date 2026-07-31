"""S8 -- plumbing: devices that may rotate 90 degrees, plus a minimum spacing margin."""
from itertools import combinations

# (device_id, width, height) -- as originally oriented; rotation swaps these
DEVICES = [
    ("M1", 4.0, 2.0),
    ("M2", 4.0, 2.0),
    ("M3", 3.0, 3.0),
    ("M4", 2.0, 5.0),
    ("M5", 6.0, 1.5),
]

CHIP_WIDTH = 22.0
CHIP_HEIGHT = 14.0
MIN_SPACING = 0.5  # required gap between any two devices (DRC margin)

BIG_M_X = CHIP_WIDTH
BIG_M_Y = CHIP_HEIGHT
DEVICE_PAIRS = list(combinations([d[0] for d in DEVICES], 2))


def print_result(positions: dict, rotations: dict) -> None:
    print(f"{'device':6} {'x':>8} {'y':>8} {'rotated':>8}")
    for dev_id, (x, y) in positions.items():
        print(f"{dev_id:6} {x:8.2f} {y:8.2f} {str(bool(round(rotations[dev_id]))):>8}")
