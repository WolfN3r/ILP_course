#!/usr/bin/env python3
"""
Plot time spent per day, colored by lesson, from lesson_log.csv (written by the
`log-lesson-time` skill -- see ../skills/log-lesson-time/SKILL.md).

Usage:  python lesson_time_graph.py
Reads:  lesson_log.csv (date, session_id, lesson, minutes) in this same directory
Writes: lesson_time.png in this same directory
"""
import csv
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

COLOR_BG = "#0d1117"
COLOR_GRID_LINE = "#21262d"
COLOR_TEXT = "#8b949e"
COLOR_TITLE = "#c9d1d9"
BAR_WIDTH = 0.65
DPI = 150
FIG_WIDTH_PER_DAY = 0.75
FIG_WIDTH_MIN = 10
FIG_HEIGHT = 6


def date_range_inclusive(start: date, end: date) -> list:
    return [start + timedelta(days=i) for i in range((end - start).days + 1)]


def main() -> None:
    here = Path(__file__).parent
    csv_path = here / "lesson_log.csv"
    if not csv_path.exists():
        print(f"No {csv_path} yet -- run the log-lesson-time skill after a session first.")
        sys.exit(1)

    rows = list(csv.DictReader(csv_path.open(newline="", encoding="utf-8")))
    if not rows:
        print(f"{csv_path} is empty.")
        sys.exit(1)

    # minutes[date][lesson] = total minutes
    minutes: dict = defaultdict(lambda: defaultdict(float))
    lessons_seen = []
    for r in rows:
        d = date.fromisoformat(r["date"])
        lesson = r["lesson"]
        minutes[d][lesson] += float(r["minutes"])
        if lesson not in lessons_seen:
            lessons_seen.append(lesson)

    all_dates = date_range_inclusive(min(minutes), max(minutes))
    date_labels = [d.strftime("%b %d") for d in all_dates]
    n = len(all_dates)

    cmap = cm.get_cmap("tab20", max(len(lessons_seen), 1))
    lesson_colors = {lesson: cmap(i) for i, lesson in enumerate(lessons_seen)}

    fig_w = max(FIG_WIDTH_MIN, n * FIG_WIDTH_PER_DAY)
    fig, ax = plt.subplots(figsize=(fig_w, FIG_HEIGHT))
    fig.patch.set_facecolor(COLOR_BG)
    ax.set_facecolor(COLOR_BG)
    ax.tick_params(colors=COLOR_TEXT)
    for sp in ax.spines.values():
        sp.set_color(COLOR_GRID_LINE)

    x = np.arange(n)
    bottoms = np.zeros(n)
    for lesson in lessons_seen:
        heights = np.array([minutes[d].get(lesson, 0.0) / 60.0 for d in all_dates])
        ax.bar(x, heights, bottom=bottoms, width=BAR_WIDTH,
               color=lesson_colors[lesson], label=lesson)
        bottoms += heights

    ax.set_xticks(x)
    ax.set_xticklabels(date_labels, rotation=45, ha="right", color=COLOR_TEXT, fontsize=8)
    ax.set_ylabel("Hours", color=COLOR_TEXT, fontsize=9)
    ax.set_title("Time Spent per Day, by Lesson", color=COLOR_TITLE, fontsize=12, pad=8)
    ax.yaxis.grid(True, color=COLOR_GRID_LINE, linestyle="--", alpha=0.7)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(facecolor=COLOR_BG, labelcolor=COLOR_TITLE, framealpha=0.9,
              edgecolor=COLOR_GRID_LINE, fontsize=8, ncol=min(len(lessons_seen), 6),
              loc="upper left", bbox_to_anchor=(0, -0.25))

    out_path = here / "lesson_time.png"
    plt.savefig(out_path, dpi=DPI, bbox_inches="tight", facecolor=COLOR_BG)
    print(out_path)


if __name__ == "__main__":
    main()
