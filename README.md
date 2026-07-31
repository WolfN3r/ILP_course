# ILP / gurobipy Course

A self-paced, project-grounded course on mathematical optimization (LP/MILP) and Gurobi's
Python API (`gurobipy`), built around a real project — an analog IC placement optimizer
(`../ALDA_placementOptimizer`) — and a set of classic ILP problems from other domains
(scheduling, knapsack, assignment, bin packing, diet problem) so the skills generalize
beyond chip placement.

This repo is the curriculum + code scaffolding for that course. It's meant to be worked
through with an AI tutor (Claude Code) following the contract in [`CLAUDE.md`](CLAUDE.md):
**the student writes every line of modeling logic**; the assistant only prepares plumbing
(data, helpers) and skeletons (TODOs, signatures, no implementation).

## Structure

```
CLAUDE.md                 tutor contract: how sessions run, what Claude may/may not write
requirements.txt          gurobipy + matplotlib
topics/                   one .md per session (S0-S11) -- subtopics, notes, tasks, time log
  _TEMPLATE.md
  _TIME_ESTIMATES.md      planning estimates per session
  S0_orientation.md ... S11_debugging.md
code/                     per-session code scaffolding
  s0_orientation/ ... s11_debugging/
    <subtask>/
      plumbing.py         written ahead of time (imports, data, helpers)
      task.py             TODO skeleton -- the student's work
.claude/
  settings.json           hooks wiring (see below)
  hooks/worklog.py         logs every prompt/stop to a monthly CSV
  skills/log-lesson-time/  turns that raw log into a per-lesson time entry
  workProgress/            generated logs + graphs (gitignored: only *.png)
```

## Curriculum

| # | Session |
|---|---|
| S0 | Orientation & environment setup |
| S1 | Optimizer theory in pure Python (LP vs MILP, brute-force solvers) |
| S2 | gurobipy introduction (`Model`, `Env`, anatomy of a solve) |
| S3 | Model & decision variables |
| S4 | Linear constraints |
| S5 | The objective (HPWL, linearizing max/min) |
| S6 | Non-overlap (disjunctions, binaries, big-M) |
| S7 | Symmetry & matching |
| S8 | Orientation, spacing, alignment |
| S9 | Solver parameters & tuning (benchmark harness, `Model.tune()`) |
| S10 | Reading the real ALDA placement project |
| S11 | Debugging (`computeIIS`, status codes) |

S3-S8 each pair a placement-specific task with a structurally-analogous task from another
domain (production planning, diet problem, knapsack, job-shop scheduling, assignment,
bin packing). See [`topics/_TIME_ESTIMATES.md`](topics/_TIME_ESTIMATES.md) for rough
per-session time budgets (~18-26 hours total).

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python code/s0_orientation/check_environment.py
```

Requires a working Gurobi license (academic licenses are free — see gurobi.com). The check
script confirms the `gurobipy` version and that the license solves a trivial model.

## How a session works

Open the relevant `topics/SN_*.md` file and follow the flow described in `CLAUDE.md`
section 3: concept → gurobipy tools named (not written) → task(s) in `code/sN_.../` →
checkpoint questions → wrap-up. Every `task.py` is yours to implement; `plumbing.py` files
are provided so you spend your time on the concept, not boilerplate.

## Time tracking

Two hooks (`UserPromptSubmit`, `Stop`, wired in `.claude/settings.json`) log every prompt
and response to `.claude/workProgress/YYYY-MM.csv` automatically — no action needed.

At the end of a session, the `log-lesson-time` skill turns that raw log into a per-lesson
entry:

```bash
python .claude/skills/log-lesson-time/log_lesson_time.py S6 topics/S6_nonoverlap.md
```

This appends to `.claude/workProgress/lesson_log.csv` and to the topic file's own
`## Time tracking` section. To see time spent per day, colored by lesson:

```bash
python .claude/workProgress/lesson_time_graph.py
```

This writes `.claude/workProgress/lesson_time.png` (gitignored — regenerate any time).
