# Workflow

Every HyperGS run follows one production loop:

1. Resolve the active studio profile.
2. Detect the engine and existing HyperGS state.
3. Select one lead workflow and current lifecycle phase.
4. Define one measurable objective, role owners, deliverables, and acceptance checks.
5. Inspect existing code, assets, documents, tests, and constraints.
6. Implement the smallest coherent end-to-end slice authorized by the request.
7. Run proportionate tests, builds, playtests, or inspections.
8. Update project memory and durable evidence.
9. Evaluate the phase gate.
10. Report one recommended next action.

## Gate behavior

`phase_check.py` verifies required documents and evidence are present and not untouched templates. The producer then reviews their substance. `phase_advance.py` refuses to advance when the structural gate fails.

## Assumptions

HyperGS records reversible assumptions and continues when they do not materially change product direction. It asks for user input before decisions involving major scope, engine or platform commitments, paid services, credentials, publishing, production migrations, or irreversible external state.
