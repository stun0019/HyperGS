# Quality Review Workflow

## Lead and support

Lead: Producer. Each affected specialist owns acceptance for its discipline; implementing engineers own automated checks.

## Procedure

1. Derive a risk-based test charter from the current phase, changes, targets, and acceptance criteria.
2. Verify launch, core loop, save or persistence, failure recovery, inputs, accessibility, compatibility, performance, security, telemetry, and motion-presentation recovery as applicable.
3. For timing-dependent presentation, validate `ASSET_MANIFEST.json` and `ANIMATION_EVENTS.json`, inspect motion capture, and test skip, interruption, reduced motion, resize, suspend, audio loss, and return to control.
4. Record environment and exact evidence.
5. Classify findings by player impact, reproducibility, reach, and release risk.
6. Re-test resolved critical findings and run `validate_project.py` plus `validate_presentation.py` when presentation specifications exist.

## Completion

Return a pass, fail, or blocked result with evidence. Absence of discovered bugs is not evidence of complete coverage.
