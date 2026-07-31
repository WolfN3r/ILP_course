"""S1 -- plumbing for the LP brute-force exercise. Data + generic utilities only.

The problem itself (a classic textbook LP) is fixed here so you can focus on writing the
search, not inventing test data.

Maximize:   3x + 5y
Subject to: x <= 4
            2y <= 12
            3x + 2y <= 18
            x, y >= 0

The true optimum (found by the corner-point method) is x=2, y=6, objective=36.
"""
from typing import Iterator

OBJECTIVE_COEFFS = (3.0, 5.0)   # (c_x, c_y) in c_x*x + c_y*y
BOUNDS = ((0.0, 4.0), (0.0, 6.0))  # generous search box for x and y; y<=6 comes from 2y<=12
KNOWN_OPTIMUM = {"x": 2.0, "y": 6.0, "objective": 36.0}


def grid_points(lb: float, ub: float, step: float) -> Iterator[float]:
    """Yield lb, lb+step, lb+2*step, ... up to and including ub (approximately)."""
    n_steps = int(round((ub - lb) / step))
    for i in range(n_steps + 1):
        yield lb + i * step
