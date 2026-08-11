# Prototype Quality

## Contents

- Delivery intent
- Maturity levels
- First Playable baseline
- Evidence and review

## Delivery intent

Record one delivery intent before implementation:

- `functional_prototype`: internal mechanics test; placeholders and debug UI are allowed.
- `visual_prototype`: runtime test of scale, composition, animation, effects, and UI direction; incomplete game logic is allowed.
- `presentation_ready_first_playable`: coherent player-facing slice suitable for an external review or portfolio capture.

When the user asks to make, build, or create a game without explicitly requesting a rough or internal prototype, use `presentation_ready_first_playable`. Label internal prototypes clearly and do not treat them as the requested final delivery.

## Maturity levels

Validate work in this order without confusing one level for the next:

1. Gameplay Prototype: prove controls, rules, collision, combat state, failure, recovery, and the core outcome.
2. Visual Prototype: prove target gameplay scale, composition, environment depth, animation language, VFX, UI hierarchy, and readability in motion.
3. First Playable: integrate both into a short, stable, comprehensible, and presentable end-to-end loop.
4. Vertical Slice: raise one representative segment to near-target production quality and prove its production pipeline.

Gameplay and visual prototypes are internal readiness milestones inside Pre-production. They are not alternate names for First Playable.

## First Playable baseline

A player-facing action game First Playable must satisfy all applicable criteria below. Replace genre-specific items with equivalent feedback for another genre; never silently omit the underlying player need.

- Player and threats are readable at the target device size and occupy an intentional gameplay scale. Tiny debug-scale actors fail.
- Controls match the target platform. For touch action games, use a movement stick or equivalent directional control and a deliberate action cluster; debug left/right button rows fail unless explicitly approved.
- The primary action has real gameplay resolution: anticipation, active timing or range, hit detection, hit reaction, recovery, and a visible outcome.
- Combat feedback includes suitable animation, impact VFX, hit flash or equivalent confirmation, knockback or reaction, brief impact timing such as hit stop when appropriate, damage or state feedback, and restrained camera response.
- At least idle, locomotion, primary action, and hit/reaction states are visually distinct for the player and representative enemies.
- HUD preserves the gameplay view, establishes hierarchy, and does not dominate the screen. Required combat information is readable without covering the action.
- The environment establishes foreground, play plane, background depth, grounding, and enough landmarks or detail to read the combat space.
- Character, environment, VFX, and UI share a coherent visual language. A styled HUD over placeholder gameplay art fails integration review.
- The loop includes a target or opposition, understandable success or failure, feedback, and restart or continuation.
- The target build launches reproducibly and completes the loop without a severity-1 defect.

Do not prescribe expensive final art when simpler authored assets can establish the intended quality. Placeholder assets are allowed only when they do not undermine scale, readability, feedback, style coherence, or the user's requested presentation level.

## Evidence and review

Store First Playable evidence under `.hypergs/evidence/phase-03-first-playable/`:

- `build.md`: launch path, build identity, target device or viewport, and observed result.
- `playtest.md`: tester, scenario, observations, failures, and retest result.
- At least one runtime capture (`.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.mp4`, or `.webm`) showing the actual gameplay build at target scale.
- `gameplay-review.md`: Game Designer verdict against core loop, controls, combat resolution, and feedback.
- `uiux-review.md`: UI/UX Designer verdict against input, hierarchy, obstruction, readability, and target-device use.
- `art-review.md`: Art Director verdict against scale, animation, effects, environment depth, and visual coherence.
- `producer-review.md`: Producer reconciliation, unresolved defects, delivery-intent match, and final pass or fail.

Each review must say `PASS` or `FAIL`, cite observed runtime evidence, and list blocking defects. Missing, contradictory, screenshot-free, or purely aspirational reviews fail the gate. The producer cannot override a specialist failure without fixing and retesting the defect.

Do not treat capture-file presence as visual proof. Open and inspect every representative capture at its original aspect ratio. Record:

- target viewport and orientation;
- approximate player and enemy height as a percentage of the gameplay viewport;
- approximate HUD and touch-control footprint;
- unobstructed combat-space footprint;
- readable idle, locomotion, attack, and hit states;
- visible attack range or contact, impact VFX, reaction, damage or state feedback, and camera response;
- foreground, play-plane, midground, and background separation;
- style consistency across characters, environment, VFX, and UI.

Compare measurements with the game's recorded genre benchmark and visual target instead of applying one universal ratio. Fail when actors are too small to read, UI dominates the player action, negative space has no gameplay or compositional purpose, the stage lacks depth, or a static capture cannot show the claimed combat feedback. Use video, an image sequence, or direct runtime observation for timing-dependent claims such as animation, hit stop, knockback, combo response, and camera shake.
