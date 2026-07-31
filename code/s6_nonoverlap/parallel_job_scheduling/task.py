"""S6 parallel domain -- YOUR task: add non-overlap constraints so no two jobs run at the
same time on the one shared machine.

For each pair (a, b), at least one of these must hold:
  a finishes before b starts   |   b finishes before a starts
Same binary * big-M disjunction pattern as placement, just 2 outcomes instead of 4.
"""
import gurobipy as gp
from gurobipy import GRB

from plumbing import JOBS, HORIZON, JOB_PAIRS, print_schedule, check_no_overlap


def build_model() -> tuple:
    """TODO:
    1. A start-time variable per job, bounded [0, HORIZON].
    2. For each pair in JOB_PAIRS: 2 binary variables (a_before_b, b_before_a), the 2
       big-M constraints, and one constraint requiring their sum >= 1.
    3. No objective yet -- any feasible non-overlapping schedule is fine.
    Return (model, {job_name: start_time_var}).
    """
    raise NotImplementedError


if __name__ == "__main__":
    m, variables = build_model()
    m.optimize()
    start_times = {job: v.X for job, v in variables.items()}
    print_schedule(start_times)
    overlaps = check_no_overlap(start_times)
    print(f"Overlapping pairs found: {overlaps if overlaps else 'none'}")
