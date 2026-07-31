"""S3 parallel domain -- production planning. Data only.

A small factory can make a few products. Each product uses some amount of a shared resource
(e.g. machine-hours) per unit, and has a max market demand.
"""

# (product_name, resource_units_per_unit, max_demand, profit_per_unit)
PRODUCTS = [
    ("widget_a", 2.0, 40, 12.0),
    ("widget_b", 3.0, 30, 18.0),
    ("widget_c", 1.0, 60, 7.0),
]

TOTAL_RESOURCE_UNITS = 100.0


def print_plan(quantities: dict) -> None:
    print(f"{'product':10} {'units':>8}")
    for name, qty in quantities.items():
        print(f"{name:10} {qty:8.2f}")
