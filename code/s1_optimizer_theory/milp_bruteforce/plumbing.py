"""S1 -- plumbing for the MILP brute-force exercise (0/1 knapsack). Data + generic utility
only -- the search is yours to write.

8 items, each either taken (1) or not (0). Capacity limits total weight.
Small enough (2**8 = 256 combos) to brute force in a fraction of a second, but already
shows how fast this blows up as items grow.
"""
from itertools import product
from typing import Iterator

ITEMS = [
    # (name, weight, value)
    ("item_0", 3, 4),
    ("item_1", 4, 5),
    ("item_2", 2, 3),
    ("item_3", 5, 8),
    ("item_4", 1, 1),
    ("item_5", 6, 9),
    ("item_6", 2, 2),
    ("item_7", 3, 5),
]
CAPACITY = 12


def all_binary_combinations(n: int) -> Iterator[tuple]:
    """Yield every length-n tuple of 0/1 -- i.e. every possible subset selection."""
    return product((0, 1), repeat=n)
