"""S1 -- YOUR task: brute-force the tiny 0/1 knapsack defined in plumbing.py.

Write everything below yourself. See topics/S1_optimizer_theory.md for the concept.
"""
import time

from plumbing import ITEMS, CAPACITY, all_binary_combinations


def total_weight(selection: tuple) -> int:
    """TODO: sum the weight of every item where selection[i] == 1."""
    raise NotImplementedError


def total_value(selection: tuple) -> int:
    """TODO: sum the value of every item where selection[i] == 1."""
    raise NotImplementedError


def brute_force_knapsack() -> dict:
    """TODO: try every combination from all_binary_combinations(len(ITEMS)), skip
    infeasible ones (total_weight > CAPACITY), keep the best feasible by total_value.
    Return {"selection": ..., "weight": ..., "value": ...}.
    """
    raise NotImplementedError


if __name__ == "__main__":
    start = time.perf_counter()
    result = brute_force_knapsack()
    elapsed = time.perf_counter() - start
    print(f"Best selection: {result}")
    print(f"Brute force took {elapsed:.4f}s for {len(ITEMS)} items "
          f"(2^{len(ITEMS)} = {2 ** len(ITEMS)} combinations)")
    print("Try bumping len(ITEMS) in plumbing.py to 20, 30... and watch this number explode.")
