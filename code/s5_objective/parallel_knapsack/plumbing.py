"""S5 parallel domain -- 0/1 knapsack, but framed around setting an objective (S1's version
was about the search loop; this one is about setObjective + MAXIMIZE).
"""

# (item_name, weight, value) -- camping-gear flavored, distinct from S1's dataset
ITEMS = [
    ("tent", 4.0, 10.0),
    ("stove", 2.0, 6.0),
    ("sleeping_bag", 3.0, 8.0),
    ("first_aid_kit", 1.0, 5.0),
    ("water_filter", 1.5, 7.0),
    ("extra_food", 2.5, 4.0),
]

CAPACITY = 8.0


def print_selection(selection: dict) -> None:
    print(f"{'item':14} {'selected':>8}")
    for name, chosen in selection.items():
        print(f"{name:14} {chosen:8.0f}")
