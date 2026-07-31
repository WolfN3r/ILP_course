"""S11 -- plumbing: a deliberately infeasible placement setup. Two devices, a chip too small
for them to both fit with the required spacing -- diagnose it with computeIIS().
"""

DEVICES = [
    ("M1", 8.0, 8.0),
    ("M2", 8.0, 8.0),
]

CHIP_WIDTH = 10.0   # too small -- can't fit two 8-wide devices side by side
CHIP_HEIGHT = 10.0
MIN_SPACING = 1.0

BIG_M_X = CHIP_WIDTH
BIG_M_Y = CHIP_HEIGHT
