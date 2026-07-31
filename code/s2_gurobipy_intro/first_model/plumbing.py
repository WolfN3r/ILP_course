"""S2 -- plumbing: re-exposes S1's tiny LP and MILP problem data so you can rebuild them in
gurobipy without retyping the raw numbers, and a tiny timing helper.
"""
import sys
import time
from pathlib import Path
from contextlib import contextmanager

# Reuse the exact same problem data as S1, so the comparison is apples-to-apples.
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "s1_optimizer_theory" / "lp_bruteforce"))
from plumbing import OBJECTIVE_COEFFS as LP_OBJECTIVE_COEFFS, KNOWN_OPTIMUM as LP_KNOWN_OPTIMUM  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "s1_optimizer_theory" / "milp_bruteforce"))
from plumbing import ITEMS as KNAPSACK_ITEMS, CAPACITY as KNAPSACK_CAPACITY  # noqa: E402


@contextmanager
def timed(label: str):
    start = time.perf_counter()
    yield
    print(f"{label}: {time.perf_counter() - start:.4f}s")
