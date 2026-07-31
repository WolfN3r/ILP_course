"""S9 -- YOUR task: run Gurobi's built-in Model.tune() and judge whether it's worth it.

Use the same model as the other two S9 tasks. Compare tune()'s suggested parameter set
against your own manual conclusions from speed_only_params/ and solution_changing_params/.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def build_model():
    """TODO: same as in the other S9 tasks -- reuse one of your completed models."""
    raise NotImplementedError


def run_tuning():
    """TODO:
    1. Build the model.
    2. Set Model.Params.TuneTimeLimit (a few seconds is enough for a small model).
    3. Call Model.tune().
    4. Inspect Model.tuneResultCount and Model.getTuneResult(i) for the best result(s).
    5. Apply the best tuned parameters and re-solve; compare runtime/quality against your
       manual best guess from the earlier two tasks.
    """
    raise NotImplementedError


if __name__ == "__main__":
    run_tuning()
