"""S4 -- plumbing: same devices/chip as S3, plus a helper to check a solution visually."""

DEVICES = [
    ("M1", 4.0, 2.0),
    ("M2", 4.0, 2.0),
    ("M3", 3.0, 3.0),
    ("M4", 2.0, 5.0),
    ("M5", 6.0, 1.5),
]

CHIP_WIDTH = 20.0
CHIP_HEIGHT = 12.0


def print_positions(positions: dict) -> None:
    print(f"{'device':6} {'x':>8} {'y':>8} {'x+w':>8} {'y+h':>8}")
    dims = {d[0]: (d[1], d[2]) for d in DEVICES}
    for dev_id, (x, y) in positions.items():
        w, h = dims[dev_id]
        print(f"{dev_id:6} {x:8.2f} {y:8.2f} {x + w:8.2f} {y + h:8.2f}")
