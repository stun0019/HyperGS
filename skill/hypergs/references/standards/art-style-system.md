# Art Style System

## Contents

- Style intent
- Visual grammar
- Style benchmark
- Asset production
- Runtime review

## Style intent

Read `market-visual-benchmark.md`. Derive art direction from user intent, sourced current-market gameplay evidence, game fantasy, genre promise, target audience, platform, camera, input, readability, performance budget, team capacity, and content volume. Do not select a style only because one image looks impressive or a reference game is popular.

Record in `ART.md`:

- a one-sentence visual thesis;
- three to five target qualities and three anti-target qualities;
- reference observations separated into composition, palette, shape, material, camera, animation, VFX, and UI lessons;
- an original synthesis that does not copy protected characters, assets, maps, logos, or distinctive expression;
- production cost, reuse strategy, and known style risks.

## Visual grammar

Specify implementable rules rather than mood adjectives:

- camera projection, framing, horizon, play-plane depth, and parallax;
- player, enemy, prop, architecture, and UI scale relationships;
- anatomy or proportion system, silhouette families, shape language, and detail density;
- perspective consistency, grounding, contact shadows, and overlap rules;
- palette roles, value groups, saturation hierarchy, light direction, temperature, contrast, and atmosphere;
- material vocabulary, texture density, brush or pixel treatment, edge hardness, outlines, and rendering finish;
- animation timing, pose exaggeration, smear or trail language, hit reactions, and motion readability;
- VFX geometry, color ownership, blend behavior, lifetime, intensity hierarchy, and combat readability;
- UI typography, icon geometry, borders, surface treatment, spacing, motion, and relationship to the world art.

Use explicit tokens, ranges, annotated examples, or do/don't pairs wherever practical. Avoid vague directions such as `dark`, `epic`, `anime`, or `high quality` without production rules.

For real-time character-driven games, define an authored animation pipeline. Use sprite sheets, Spine or an equivalent skeletal system, or 3D rigs as appropriate. Require at least idle or breathing, locomotion, primary action anticipation and execution, recovery, hit reaction, and defeat for the player and representative enemies. Add skills, cast, block, dodge, crowd-control, and interaction states when present in the First Playable loop. Static character cutouts fail unless the product is intentionally static and the user explicitly approves that presentation.

Synchronize hitboxes, projectiles, footsteps, VFX, audio, hit stop, camera response, and state transitions with animation clips or authored event markers. Record blend or mix rules, interruption behavior, facing, pivots, root motion, frame rate, and fallback states.

## Style benchmark

Before broad asset production, build one representative runtime benchmark containing:

- one player character at target scale;
- one representative enemy or interactable;
- one playable environment segment with foreground, play plane, midground, and background;
- one primary action and reaction animation;
- one impact VFX and one persistent gameplay effect if applicable;
- one representative HUD panel and action control or interaction prompt.

Review the benchmark as one composition at target resolution and in motion. Lock the visual grammar only when these elements appear intentionally authored for the same game. A beautiful background with characters or UI that use incompatible perspective, lighting, outline, texture density, or rendering finish fails style lock.

## Asset production

For authored, sourced, or generated assets:

- record provenance, license or usage status, intended role, version, and approval state;
- maintain a compact prompt or production bible for generated variants, including camera, proportions, palette, lighting, material, edge treatment, and exclusions;
- generate or commission coherent sets rather than selecting unrelated impressive outputs;
- verify sprite sheets, animation frames, cutouts, pivots, collision silhouettes, resolution, compression, and runtime performance;
- reject assets that require the rest of the game to change styles merely to accommodate them.

Do not treat upscaling, filters, color grading, or shared darkness as a substitute for structural consistency.

## Runtime review

Read `motion-presentation-system.md` when animation, VFX, camera, UI transitions, reward sequences, cinematics, or audio-reactive feedback materially affect the player experience. Keep visual grammar in `ART.md` and event execution rules in `MOTION.md`, `PRESENTATION_BEATS.md`, and `ANIMATION_EVENTS.json`.

Open original-resolution captures and inspect motion where timing matters. Record an explicit `PASS` or `FAIL` in `art-review.md` for:

- camera and perspective compatibility;
- proportions and gameplay scale;
- grounding and spatial depth;
- silhouette and action readability;
- palette, value, lighting, and material consistency;
- detail-density and edge-treatment consistency;
- animation and VFX integration;
- UI/world relationship;
- provenance and production repeatability;
- target-device performance and clarity.

List concrete mismatches and the smallest rule-level correction. Do not pass by averaging strengths: one spectacular environment does not cancel incompatible characters, effects, or UI.
