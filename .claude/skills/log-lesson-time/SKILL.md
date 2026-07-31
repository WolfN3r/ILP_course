---
name: log-lesson-time
description: Log how long the current session's lesson took, at the end of an ILP course session. Use this during the "Wrap up" step described in CLAUDE.md section 3 (after filling in a topic file's "What we achieved" section), or whenever the user asks to log/record session time, e.g. "log the time for this session", "how long did S6 take", "wrap up S3". Reads the worklog CSV that the UserPromptSubmit/Stop hooks maintain and writes a line into the topic's .md file plus a row into .claude/workProgress/lesson_log.csv.
---

# Log lesson time

At the end of a session, once the topic file's "What we achieved" section is filled in,
run this to record how long the session actually took (measured from the hook-maintained
worklog, not a guess):

```bash
python .claude/skills/log-lesson-time/log_lesson_time.py <lesson_id> <topic_md_path>
```

Example, at the end of an S6 session:

```bash
python .claude/skills/log-lesson-time/log_lesson_time.py S6 topics/S6_nonoverlap.md
```

This:
1. Finds the current month's raw log in `.claude/workProgress/YYYY-MM.csv`.
2. Identifies the most recently active `session_id` (the one this conversation is running
   in) and computes elapsed time from its first prompt to its last stop.
3. Appends a row to `.claude/workProgress/lesson_log.csv` (`date, session_id, lesson,
   minutes`) — this is what `workProgress/lesson_time_graph.py` reads to plot the graph.
4. Appends a line under a `## Time tracking` section in the given topic `.md` file (creating
   the section if it doesn't exist yet).

If the user names a lesson that spans multiple chat sessions (e.g. they closed and reopened
the terminal partway through S6), just run this once per session — multiple lines will
accumulate under the same topic file's "Time tracking" section and as separate rows in
`lesson_log.csv`, and the graph script sums per-day/per-lesson correctly either way.

Don't run this speculatively mid-session — only when the user is actually wrapping up a
lesson, since it stamps "now" as the session's end time.
