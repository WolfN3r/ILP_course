"""S11 parallel domain -- plumbing: an over-constrained single-machine schedule. More total
job duration than the horizon allows -- diagnose it the same way as the placement case.
"""

# (job_name, duration)
JOBS = [
    ("job_0", 5.0),
    ("job_1", 5.0),
    ("job_2", 5.0),
]

HORIZON = 10.0  # too small -- 3 jobs of duration 5 need at least 15
