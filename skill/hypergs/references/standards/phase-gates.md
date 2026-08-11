# Phase Gates

A phase gate is an evidence review, not a calendar milestone.

## Gate result

- `passed`: Every mandatory artifact and evidence item exists, is current, and supports the phase objective.
- `blocked`: A required external decision, tool, asset, credential, environment, or authority is unavailable.
- `in_progress`: Work remains that can be completed within the current scope.

## Review method

1. Run `phase_check.py` for structural requirements.
2. Inspect the substance of required documents and evidence.
3. Verify critical claims independently when practical.
4. Record exceptions as explicit producer decisions; never silently waive them.
5. Advance with `phase_advance.py` only after a pass.

For First Playable, structural passage additionally requires a runtime capture and four discipline reviews. Open the capture and inspect it at the original target aspect ratio; file presence alone is not evidence of visual quality. Require video, an image sequence, or direct runtime observation for animation and impact-timing claims. Treat any `FAIL` verdict from gameplay, UI/UX, art, or producer review as a failed gate until the defect is fixed and retested.

Structural scripts can prove presence and non-empty content. They cannot prove game quality, fun, correctness, or production readiness by themselves.
