# Time Estimates

Rough wall-clock estimates, assuming you write every `task.py` yourself (per the CLAUDE.md
contract) rather than reading a finished solution. Actual time depends heavily on how much
you stop to read gurobipy docs or re-derive math on paper — these are planning numbers, not
targets. Update this table (or just your own notes) once `log-lesson-time` gives you real
data; see `../.claude/skills/log-lesson-time/SKILL.md`.

| Session | Focus | Placement task | Parallel task | Total estimate |
|---|---|---|---|---|
| S0 | Orientation & setup | — | — | 0.5 h |
| S1 | Optimizer theory (pure Python) | — | — | 2.5–3.5 h (theory + 2 brute-force implementations) |
| S2 | gurobipy introduction | — | — | 1–1.5 h |
| S3 | Model & decision variables | 0.5–0.75 h | 0.5–0.75 h | 1–1.5 h |
| S4 | Linear constraints | 0.5–0.75 h | 0.5–0.75 h | 1–1.5 h |
| S5 | The objective (HPWL linearization) | 0.75–1 h | 0.5–0.75 h | 1.5–2 h |
| S6 | Non-overlap (big-M, the hardest concept) | 1–1.5 h | 1–1.5 h | 2–3 h |
| S7 | Symmetry & matching | 0.75–1 h | 0.75–1 h | 1.5–2 h |
| S8 | Orientation, spacing, alignment | 1–1.25 h | 1–1.25 h | 2–2.5 h |
| S9 | Solver parameters & tuning | 1 h | 1 h | +1 h for `Model.tune()` → 2–3 h |
| S10 | Read my existing project | — | — | 1.5–2 h |
| S11 | Debugging & experiments | 0.5–0.75 h | 0.5–0.75 h | 1–1.5 h |
| **Total** | | | | **~18–26 h** |

Biggest time sinks to expect: S1 (new theory + two from-scratch implementations), S6
(big-M is the conceptual crux of the whole course), and S9 (parameter sweeps take real
solver wall-clock time on top of your own thinking time).
