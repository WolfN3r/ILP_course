"""S1 -- YOUR task: brute-force / grid-search the tiny LP defined in plumbing.py.

Write everything below yourself. See topics/S1_optimizer_theory.md for the concept.
"""
from plumbing import OBJECTIVE_COEFFS, BOUNDS, KNOWN_OPTIMUM, grid_points


def is_feasible(x: float, y: float) -> bool:
    """TODO: check all three constraints (x <= 4, 2y <= 12, 3x + 2y <= 18) plus x,y >= 0."""
    raise NotImplementedError


def objective(x: float, y: float) -> float:
    """TODO: compute 3x + 5y using OBJECTIVE_COEFFS."""
    raise NotImplementedError


def brute_force_search(step: float = 0.1) -> dict:
    """TODO: loop over a grid of (x, y) using grid_points() and BOUNDS, keep the best
    feasible point found. Return {"x": ..., "y": ..., "objective": ...}.
    """
    raise NotImplementedError


if __name__ == "__main__":
    result = brute_force_search(step=0.1)
    print(f"Brute-force result: {result}")
    print(f"Known optimum:      {KNOWN_OPTIMUM}")
