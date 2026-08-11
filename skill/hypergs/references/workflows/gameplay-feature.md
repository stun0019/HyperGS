# Gameplay Feature Workflow

## Lead and support

Lead: Game Designer. Support: Client Engineer, UI/UX Designer, Data Analyst, and Server Engineer when authoritative state is required.

## Procedure

1. Define the player problem, player verb, state transitions, feedback, failure, recovery, rewards, and non-goals.
2. Identify interactions with existing progression, economy, save data, networking, controls, and accessibility.
3. Recheck the Genre Promise Contract. Identify which named pillar the feature proves and reject decorative UI as substitute evidence.
4. Write acceptance examples and tunable variables before implementation.
5. Classify the target as a Gameplay Prototype, Visual Prototype, First Playable, or Vertical Slice using `prototype-quality.md`.
6. Implement a thin end-to-end path behind an appropriate seam or flag.
7. For action mechanics, verify anticipation, active hit logic, reaction, recovery, impact timing, VFX, state or damage feedback, camera response, and enemy readability as applicable.
8. Test rules, edge cases, player feedback, target-device controls, presentation scale, genre-pillar evidence, and regressions.
9. Update GDD, technical notes, analytics questions, and changelog only where affected.

## Completion

Provide a runnable behavior, verified acceptance cases, known balance assumptions, an explicit maturity label, and no unowned integration risk. Do not call the behavior First Playable when only its functional mechanics pass.
