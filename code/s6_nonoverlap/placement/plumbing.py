"""S6 -- plumbing: devices, chip, and a sensible big-M per axis (the chip dimension itself
is a valid, meaningful M here -- no device pair can be farther apart than the chip is wide).
"""
from itertools import combinations

DEVICES = [
    ("M1", 4.0, 2.0),
    ("M2", 4.0, 2.0),
    ("M3", 3.0, 3.0),
    ("M4", 2.0, 5.0),
    ("M5", 6.0, 1.5),
]

CHIP_WIDTH = 20.0
CHIP_HEIGHT = 12.0

BIG_M_X = CHIP_WIDTH
BIG_M_Y = CHIP_HEIGHT

DEVICE_PAIRS = list(combinations([d[0] for d in DEVICES], 2))


def print_positions(positions: dict) -> None:
    dims = {d[0]: (d[1], d[2]) for d in DEVICES}
    print(f"{'device':6} {'x':>8} {'y':>8} {'x+w':>8} {'y+h':>8}")
    for dev_id, (x, y) in positions.items():
        w, h = dims[dev_id]
        print(f"{dev_id:6} {x:8.2f} {y:8.2f} {x + w:8.2f} {y + h:8.2f}")


def check_no_overlap(positions: dict) -> list:
    """Returns a list of overlapping pairs found -- a plain geometric check, useful to
    sanity-check your model's output independently of the model itself.
    """
    dims = {d[0]: (d[1], d[2]) for d in DEVICES}
    overlaps = []
    for a, b in DEVICE_PAIRS:
        ax, ay = positions[a]
        aw, ah = dims[a]
        bx, by = positions[b]
        bw, bh = dims[b]
        separated = (ax + aw <= bx or bx + bw <= ax or ay + ah <= by or by + bh <= ay)
        if not separated:
            overlaps.append((a, b))
    return overlaps
