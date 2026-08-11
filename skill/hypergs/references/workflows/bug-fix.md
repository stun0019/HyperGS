# Bug Fix Workflow

## Lead and support

Lead: the specialist owning the failing component. Producer coordinates cross-system or release-blocking defects.

## Procedure

1. Capture expected behavior, actual behavior, environment, frequency, and minimum reproduction.
2. Reproduce before changing code when possible.
3. Trace the failure to a cause; distinguish cause from visible symptom.
4. Add a regression test or deterministic check when proportionate.
5. Apply the smallest maintainable fix and run focused plus relevant broader checks.
6. Update changelog or decisions only when the impact warrants it.

## Completion

Provide reproduction evidence, cause, changed files, verification, and residual risk. If reproduction is impossible, label the result as mitigation or diagnosis rather than a confirmed fix.
