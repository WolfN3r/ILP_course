#!/usr/bin/env python3
"""
Log how long the current session's lesson took.

Reads the raw hook log (.claude/workProgress/YYYY-MM.csv, written by
.claude/hooks/worklog.py on every prompt/stop), finds the most recently active session_id,
computes elapsed wall-clock time (first prompt -> last stop) for it, appends a row to
.claude/workProgress/lesson_log.csv, and appends a line to the given topic file's
"## Time tracking" section (created if missing).

Usage:
    python log_lesson_time.py <lesson_id> <topic_md_path>
    e.g. python log_lesson_time.py S6 topics/S6_nonoverlap.md
"""
import csv
import sys
import datetime
from pathlib import Path


def find_project_root(start: Path) -> Path:
    """Walk up until a .claude directory is found."""
    for p in [start, *start.parents]:
        if (p / ".claude").is_dir():
            return p
    return start


def latest_month_csv(work_progress_dir: Path) -> Path:
    month_files = sorted(work_progress_dir.glob("[0-9][0-9][0-9][0-9]-[0-9][0-9].csv"))
    if not month_files:
        raise SystemExit(f"No worklog CSV found in {work_progress_dir}. "
                          f"Has the Stop hook fired at least once yet?")
    return month_files[-1]


def current_session_span(csv_path: Path) -> tuple[str, datetime.datetime, datetime.datetime]:
    """Return (session_id, first_timestamp, last_timestamp) for whichever session_id has
    the most recent activity in the log -- that's the session this skill is running in.
    """
    rows = list(csv.DictReader(csv_path.open(newline="", encoding="utf-8")))
    if not rows:
        raise SystemExit(f"{csv_path} is empty.")

    latest_ts = max(datetime.datetime.fromisoformat(r["timestamp"]) for r in rows)
    latest_session = next(r["session_id"] for r in rows
                           if datetime.datetime.fromisoformat(r["timestamp"]) == latest_ts)

    session_rows = [r for r in rows if r["session_id"] == latest_session]
    timestamps = [datetime.datetime.fromisoformat(r["timestamp"]) for r in session_rows]
    return latest_session, min(timestamps), max(timestamps)


def append_lesson_log(work_progress_dir: Path, date: datetime.date, session_id: str,
                       lesson: str, minutes: int) -> None:
    log_path = work_progress_dir / "lesson_log.csv"
    is_new = not log_path.exists()
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["date", "session_id", "lesson", "minutes"])
        w.writerow([date.isoformat(), session_id, lesson, minutes])


def append_to_topic_file(topic_path: Path, date: datetime.date, session_id: str,
                          minutes: int) -> None:
    text = topic_path.read_text(encoding="utf-8") if topic_path.exists() else ""
    marker = "## Time tracking"
    line = f"- {date.isoformat()} — {minutes} min (session `{session_id[:8]}`)\n"

    if marker in text:
        idx = text.index(marker) + len(marker)
        rest = text[idx:]
        insert_at = idx + (rest.find("\n") + 1 if "\n" in rest else len(rest))
        text = text[:insert_at] + line + text[insert_at:]
    else:
        text = text.rstrip("\n") + f"\n\n{marker}\n{line}"

    topic_path.write_text(text, encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: log_lesson_time.py <lesson_id> <topic_md_path>")
    lesson_id, topic_arg = sys.argv[1], sys.argv[2]

    root = find_project_root(Path(__file__).resolve())
    work_progress_dir = root / ".claude" / "workProgress"
    csv_path = latest_month_csv(work_progress_dir)

    session_id, start, end = current_session_span(csv_path)
    minutes = max(1, round((end - start).total_seconds() / 60))

    append_lesson_log(work_progress_dir, end.date(), session_id, lesson_id, minutes)

    topic_path = Path(topic_arg)
    if not topic_path.is_absolute():
        topic_path = root / topic_path
    append_to_topic_file(topic_path, end.date(), session_id, minutes)

    print(f"Logged {minutes} min for {lesson_id} on {end.date().isoformat()} "
          f"(session {session_id[:8]}) -> {topic_path}")


if __name__ == "__main__":
    main()
