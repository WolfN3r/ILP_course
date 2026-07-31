"""S3 -- plumbing: a tiny fixed set of devices and a chip outline. Reused (and grown a
little) across S3-S8's placement tasks so the model builds up session by session, like the
real ALDA project does.
"""

# (device_id, width, height) -- deliberately small and simple, units are arbitrary "microns"
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
    """positions: {device_id: (x, y)} -- prints a simple readable table."""
    print(f"{'device':6} {'x':>8} {'y':>8}")
    for dev_id, (x, y) in positions.items():
        print(f"{dev_id:6} {x:8.2f} {y:8.2f}")
