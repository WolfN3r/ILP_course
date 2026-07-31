# S6 — Non-Overlap (the heart of placement)

> Session file. Claude opens this at the start of the session.
> We add to **Notes** during the lesson; Claude fills **What we achieved** at the end.

## Subtopics
- [ ] Why "two rectangles don't overlap" is a disjunction (an OR)
- [ ] left / right / above / below encoded with binary variables
- [ ] The big-M technique; how to choose M sensibly
- [ ] How the number of binaries grows with the number of pairs
- [ ] Parallel domain — job-shop scheduling: "two jobs don't use the same machine at the same
      time" is the *same* disjunction, just on a time axis instead of x/y

## Why it matters
Non-overlap is THE canonical use of big-M disjunctions in MILP, and it shows up everywhere
resources can't be double-booked — machines, time slots, rooms, not just rectangles on a
chip. Seeing the identical pattern in two domains is the point of this whole course.

## Notes
### Concept
_(added live)_

### gurobipy tools seen
-

### Doc links
-

### My questions / sticking points
-

## Task(s) — mine to write
- Placement: `code/s6_nonoverlap/placement/task.py` — add the 4-way disjunctive big-M
  non-overlap constraints for each pair of devices.
- Parallel (job-shop scheduling): `code/s6_nonoverlap/parallel_job_scheduling/task.py` — add
  the 2-way disjunctive big-M constraints so no two jobs occupy the same machine at
  overlapping times.

## What we achieved
_(Claude writes at the end)_
