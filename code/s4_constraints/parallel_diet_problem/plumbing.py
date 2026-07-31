"""S4 parallel domain -- the classic diet problem. Data only.

Pick quantities of foods to meet minimum nutrient requirements within a budget.
"""

# (food_name, cost_per_unit, calories_per_unit, protein_per_unit)
FOODS = [
    ("bread", 1.5, 250, 8),
    ("rice", 0.8, 200, 4),
    ("beans", 1.2, 150, 10),
    ("eggs", 2.0, 140, 12),
    ("milk", 1.0, 120, 8),
]

MIN_CALORIES = 2000
MIN_PROTEIN = 60
BUDGET = 15.0


def print_diet(quantities: dict) -> None:
    print(f"{'food':8} {'units':>8}")
    for name, qty in quantities.items():
        print(f"{name:8} {qty:8.2f}")
