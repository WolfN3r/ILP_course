"""S8 parallel domain -- 2D bin packing with rotation, single bin, feasibility only
(does everything fit?). Same rotation-binary + non-overlap pattern as placement, without
any of the DRC/analog-specific baggage.
"""
from itertools import combinations

# (item_id, width, height)
ITEMS = [
    ("A", 5.0, 3.0),
    ("B", 4.0, 4.0),
    ("C", 2.0, 6.0),
    ("D", 3.0, 3.0),
]

BIN_WIDTH = 8.0
BIN_HEIGHT = 8.0

BIG_M_X = BIN_WIDTH
BIG_M_Y = BIN_HEIGHT
ITEM_PAIRS = list(combinations([i[0] for i in ITEMS], 2))


def print_result(positions: dict, rotations: dict) -> None:
    print(f"{'item':6} {'x':>8} {'y':>8} {'rotated':>8}")
    for item_id, (x, y) in positions.items():
        print(f"{item_id:6} {x:8.2f} {y:8.2f} {str(bool(round(rotations[item_id]))):>8}")
