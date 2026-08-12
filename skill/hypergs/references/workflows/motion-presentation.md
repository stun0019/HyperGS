# Motion Presentation Workflow

## Lead and support

Lead: Art Director for direction and presentation hierarchy; Client Engineer for runtime orchestration and synchronization. Support: Game Designer, UI/UX Designer, Producer, and Market Analyst when a commercial benchmark is required.

## Procedure

1. Read `motion-presentation-system.md`, `art-style-system.md`, `prototype-quality.md`, and the relevant engine adapter.
2. Identify the smallest set of representative player-facing events. Separate routine, elevated, feature, jackpot or climax, failure, and recovery tiers as applicable.
3. Record the presentation contract in `MOTION.md` and event timing in `PRESENTATION_BEATS.md`.
4. Register required runtime assets, provenance, licensing, approval, and fallbacks in `ASSET_MANIFEST.json`.
5. Define triggers, beats, channels, markers, interruption, reduced motion, recovery, and budgets in `ANIMATION_EVENTS.json`.
6. Run `python scripts/validate_presentation.py <project-root> --json`. Add `--require-approved` for First Playable or later. Fix specification errors before implementation.
7. Implement one complete representative event from anticipation through recovery. Keep gameplay results authoritative and presentation cancellable.
8. Capture the event in motion at the target viewport. Inspect animation, VFX, camera, UI, audio synchronization, frame pacing, reduced motion, skip, interruption, and return to control.
9. Produce `motion-presentation-review.md` with an explicit `PASS` or `FAIL`, observed evidence, blocking defects, and the smallest correction.
10. Expand to additional events only after the representative event passes.

## Completion

Complete when specifications validate, required assets have acceptable provenance, one representative event runs through every required beat, motion evidence exists, the target-device budget is met, and the review passes without placeholder or generic-effect substitution.
