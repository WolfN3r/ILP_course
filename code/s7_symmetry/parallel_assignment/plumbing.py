"""S7 parallel domain -- assignment problem. Data only.

Assign each worker to exactly one task (and vice versa) minimizing total cost. The
"exactly one" constraints are equalities, same family as the symmetry equalities in
placement, just combinatorial instead of geometric.
"""

WORKERS = ["alice", "bob", "carol"]
TASKS = ["task_x", "task_y", "task_z"]

# cost[worker][task]
COST = {
    "alice": {"task_x": 9, "task_y": 2, "task_z": 7},
    "bob": {"task_x": 6, "task_y": 4, "task_z": 3},
    "carol": {"task_x": 5, "task_y": 8, "task_z": 1},
}


def print_assignment(assignment: dict) -> None:
    print(f"{'worker':8} {'task':8}")
    for worker, task in assignment.items():
        print(f"{worker:8} {task:8}")
