# Workflow

Every HyperGS run follows one production loop:

1. Resolve the active studio profile.
2. Detect the engine and existing HyperGS state.
3. Check for newly required project templates and add only missing files when changes are authorized.
4. Select one lead workflow and current lifecycle phase.
5. Define one measurable objective, role owners, deliverables, and acceptance checks.
6. Inspect existing code, assets, documents, tests, and constraints.
7. Implement the smallest coherent end-to-end slice authorized by the request.
8. Run proportionate tests, builds, playtests, or inspections.
9. For player-facing presentation, validate asset and animation-event specifications and capture representative motion from anticipation through recovery.
10. Update project memory and durable evidence.
11. Evaluate the phase gate.
12. Report one recommended next action.

## Gate behavior

`phase_check.py` verifies required documents and evidence are present and not untouched templates. It also validates presentation specifications and requires motion capture for First Playable and Vertical Slice. `validate_presentation.py` provides a focused specification check. The producer then reviews substance, and `phase_advance.py` refuses to advance when the gate fails.

`sync_project_templates.py` migrates existing HyperGS projects by copying only missing templates. Use `--check` for a read-only audit. It never overwrites existing project documents.

## Assumptions

HyperGS records reversible assumptions and continues when they do not materially change product direction. It asks for user input before decisions involving major scope, engine or platform commitments, paid services, credentials, publishing, production migrations, or irreversible external state.
