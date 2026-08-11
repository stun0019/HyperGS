# Quality Review Workflow

## Lead and support

Lead: Producer. Each affected specialist owns acceptance for its discipline; implementing engineers own automated checks.

## Procedure

1. Derive a risk-based test charter from the current phase, changes, targets, and acceptance criteria.
2. Verify launch, core loop, save or persistence, failure recovery, inputs, accessibility, compatibility, performance, security, and telemetry as applicable.
3. Record environment and exact evidence.
4. Classify findings by player impact, reproducibility, reach, and release risk.
5. Re-test resolved critical findings and run `validate_project.py`.

## Completion

Return a pass, fail, or blocked result with evidence. Absence of discovered bugs is not evidence of complete coverage.
