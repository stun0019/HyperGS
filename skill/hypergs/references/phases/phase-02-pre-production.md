# Phase 02 — Pre-production

## Objective

Design the production approach and remove the largest technical, usability, and visual unknowns before broad implementation.

## Lead and support

Lead: Producer. Support: Game Designer, Client Engineer, Server Engineer when needed, UI/UX Designer, and Art Director.

## Required outcomes

- Implementable core rules and system boundaries
- Engine, platform, input, build, data, performance, and asset-pipeline decisions
- Primary player flow, visual benchmark plan, milestone roadmap, and acceptance criteria
- Separate Gameplay Prototype and Visual Prototype checks at target device scale; neither may be reported as a First Playable
- Architecture and test paths for persistence, networking, shared state, social presence, or other systems implied by the public genre label
- A locked representative art benchmark that proves player, enemy, environment, animation, VFX, and UI can coexist under one producible visual grammar
- Gin and Forza approval that the art and VFX direction is grounded in user intent plus current, sourced, relevant gameplay references
- A production animation plan proving that real-time player and enemy actors will not ship as static cutouts
- A motion presentation plan covering event beats, intensity tiers, camera, UI, VFX, audio, accessibility, interruption, and recovery
- Machine-readable asset provenance and animation-event specifications validated before broad implementation

## Exit gate

Pass when `GDD.md`, `TECH.md`, `UIUX.md`, `ART.md`, `VISUAL_BENCHMARK.md`, `MOTION.md`, `PRESENTATION_BEATS.md`, `ASSET_MANIFEST.json`, `ANIMATION_EVENTS.json`, and `ROADMAP.md` define one thin first-playable slice with owned risks and test steps. The Gameplay Prototype must prove the core rules and input-to-outcome loop. The Visual Prototype must prove gameplay scale, UI hierarchy, animated player and enemy states, impact language, environment depth, visual coherence, and at least one complete presentation event in the runtime. Genre-system prototypes must prove the riskiest persistence, networking, simulation, or social claim where applicable. Do not advance merely because static images, debug controls, placeholder geometry, genre-themed UI, generic tweens, or one impressive unsourced image are operable.
