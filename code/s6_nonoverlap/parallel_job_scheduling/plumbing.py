"""S6 parallel domain -- single-machine job scheduling. Same disjunction pattern as
placement non-overlap, but on one axis (time) instead of two (x, y), and with only two
outcomes per pair instead of four (job A before B, or B before A -- no "above/below" axis).
"""
from itertools import combinations

# (job_name, duration)
JOBS = [
    ("job_0", 3.0),
    ("job_1", 2.0),
    ("job_2", 4.0),
    ("job_3", 1.5),
]

HORIZON = sum(d for _, d in JOBS)  # a valid, meaningful big-M: total time if run back-to-back
JOB_PAIRS = list(combinations([j[0] for j in JOBS], 2))


def print_schedule(start_times: dict) -> None:
    durations = {j[0]: j[1] for j in JOBS}
    print(f"{'job':8} {'start':>8} {'end':>8}")
    for job, start in sorted(start_times.items(), key=lambda kv: kv[1]):
        print(f"{job:8} {start:8.2f} {start + durations[job]:8.2f}")


def check_no_overlap(start_times: dict) -> list:
    durations = {j[0]: j[1] for j in JOBS}
    overlaps = []
    for a, b in JOB_PAIRS:
        a_start, a_end = start_times[a], start_times[a] + durations[a]
        b_start, b_end = start_times[b], start_times[b] + durations[b]
        separated = a_end <= b_start or b_end <= a_start
        if not separated:
            overlaps.append((a, b))
    return overlaps
