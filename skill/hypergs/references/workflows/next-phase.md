# Next Phase Workflow

## Trigger

Use when the user asks what to do next, requests the next phase, or asks HyperGS to advance development.

## Procedure

1. Read state, roadmap, decisions, and evidence.
2. Run `phase_check.py` against the current phase.
3. If the gate fails, convert missing requirements into a minimal recovery backlog and execute only what the request authorizes.
4. If the gate passes, summarize the evidence and run `phase_advance.py`.
5. Read the next phase reference and define its first measurable objective.

## Completion

Report whether the phase stayed in place or advanced, why, which evidence supports the decision, and the first objective for the active phase. Never treat "next phase" as permission to bypass a gate.
