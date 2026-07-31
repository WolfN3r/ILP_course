"""S9 -- YOUR task: check whether Cuts/Symmetry/MIPFocus can change the returned solution
when the solver is stopped early (tight TimeLimit or nonzero MIPGap).

Use the same model you used in speed_only_params/task.py, but this time also set a tight
TimeLimit or MIPGap in every param combination in the grid, so the solver is likely to stop
before proving optimality -- that's when these params have the most room to matter.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from benchmark_harness import run_param_sweep, print_report, solutions_match


def build_model():
    """TODO: same as in speed_only_params/task.py -- reuse one of your completed models."""
    raise NotImplementedError


if __name__ == "__main__":
    param_grid = [
        {"TimeLimit": 1.0, "Cuts": 0},
        {"TimeLimit": 1.0, "Cuts": 2},
        {"TimeLimit": 1.0, "Symmetry": 0},
        {"TimeLimit": 1.0, "Symmetry": 2},
        {"TimeLimit": 1.0, "MIPFocus": 1},
        {"TimeLimit": 1.0, "MIPFocus": 3},
    ]
    results = run_param_sweep(build_model, param_grid)
    print_report(results)
    print(f"All solutions identical: {solutions_match(results)}")
    print("If False: which params changed the answer, and does the placement/schedule/"
          "assignment actually look meaningfully different, or just numerically different?")
