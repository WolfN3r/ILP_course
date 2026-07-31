"""S9 -- YOUR task: confirm which params only affect speed, not the answer.

Pick one of your already-working models from an earlier session (e.g. the S6 non-overlap
placement model, or the S7 assignment model -- something with a nontrivial MIP structure).
Sweep Threads and Presolve on it and confirm the solution (variable values, not just the
objective) doesn't change -- only runtime does.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from benchmark_harness import run_param_sweep, print_report, solutions_match


def build_model():
    """TODO: import and call the build_model() from a session you've completed (e.g.
    s6_nonoverlap/placement/task.py), and return the freshly built gurobipy Model.
    (You'll need to add that folder to sys.path the same way benchmark_harness was imported
    above.)
    """
    raise NotImplementedError


if __name__ == "__main__":
    param_grid = [
        {"Threads": 1},
        {"Threads": 2},
        {"Threads": 4},
        {"Presolve": 0},
        {"Presolve": 2},
    ]
    results = run_param_sweep(build_model, param_grid)
    print_report(results)
    print(f"All solutions identical: {solutions_match(results)}")
