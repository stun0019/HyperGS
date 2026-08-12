# Motion Presentation System

## Contents

- Presentation contract
- Event architecture
- Beat design
- Asset and runtime pipeline
- Audio and device feedback
- Accessibility and interruption
- Performance and evidence

## Presentation contract

Define presentation as a gameplay communication system, not decoration. Record the player event, information revealed, intended emotion, target duration, intensity tier, input lock, skip behavior, and recovery state before implementation.

Use three delivery levels:

- `prototype_motion`: timing blocks may use controlled placeholders, but event ordering and recovery must work.
- `first_playable_motion`: representative events use authored animation, VFX, UI, camera, and audio that belong to the locked visual system.
- `vertical_slice_motion`: representative events reach near-target production quality through a repeatable asset and integration pipeline.

Do not describe generic fades, scale tweens, shake, particles, or CSS transitions as premium presentation without event-specific timing, art direction, sound, hierarchy, and runtime proof.

## Event architecture

Maintain `ANIMATION_EVENTS.json` as the machine-readable contract between gameplay and presentation. Give every event a stable ID and trigger. Keep gameplay outcomes authoritative; presentation observes or acknowledges resolved state and must not determine rewards, damage, random outcomes, inventory, or persistence.

For each event define:

- trigger and completion signal;
- intensity tier and priority;
- input, skip, queue, replace, and interruption policy;
- reduced-motion behavior;
- ordered beats and active channels;
- referenced assets and authored event markers;
- duration, concurrency, particle, filter, audio-voice, and memory budgets;
- safe final state after completion, skip, error, resize, suspend, or reconnect.

Use one event timeline or orchestrator per sequence. Avoid unrelated component timeouts that cannot be cancelled, inspected, or replayed deterministically.

## Beat design

Compose each meaningful event from the applicable beats:

1. `anticipation`: direct attention and forecast the action.
2. `action`: execute the player or system action.
3. `impact`: mark contact, result, or peak energy.
4. `resolution`: reveal the outcome and update readable state.
5. `recovery`: restore control, hierarchy, camera, audio, and loop readiness.

Not every event needs every beat, but every omitted beat must preserve comprehension. Record start time, duration, active channels, assets, and completion markers in `PRESENTATION_BEATS.md` and `ANIMATION_EVENTS.json`.

Define an intensity ladder. Keep routine actions brief and restrained; reserve longer holds, stronger camera response, denser VFX, larger UI, richer audio, and device feedback for rarer outcomes. Never make every event maximal.

## Asset and runtime pipeline

Maintain `ASSET_MANIFEST.json` for every runtime art, animation, VFX, UI, font, and audio dependency used by representative presentation. Record source, provenance, license state, runtime path, version, owner, approval state, and fallback.

Use authored sprite sheets, skeletal animation, rigs, particles, meshes, shaders, video, or procedural effects appropriate to the engine and style. Generate coherent source sets, then clean, cut, rig, compress, atlas, integrate, and review them. A generated still image is source material, not a completed runtime sequence.

Synchronize hitboxes, reel stops, symbol landings, rewards, counters, projectiles, VFX, UI, camera, audio, haptics, and state transitions with named event markers. Define pivots, blend rules, interruption, layering, masks, z-order, and fallback assets.

## Audio and device feedback

Specify audio by functional layer:

- input confirmation;
- mechanical or movement loop;
- anticipation and escalation;
- action or impact transient;
- reward count-up and reveal;
- ambience and music state;
- voice or character reaction;
- failure, skip, and recovery.

Define ducking, voice limits, loop points, fades, latency tolerance, mobile unlock behavior, and missing-audio fallback. Align important transients to authored markers rather than arbitrary delays. Use haptics only when supported, user-appropriate, and subordinate to accessibility settings.

## Accessibility and interruption

Provide reduced-motion behavior for camera movement, flashing, parallax, zoom, shake, and large spatial transitions. Preserve information through opacity, outline, sound, text, or restrained motion. Define limits for flash frequency, contrast, color dependence, repeated shake, autoplay sound, and prolonged input lock.

Every sequence must recover correctly after skip, rapid repeated input, scene change, resize, orientation change, tab suspension, audio interruption, asset failure, and low-performance fallback. Return gameplay, UI, camera, audio, and input to a named stable state.

## Performance and evidence

Set target-device budgets before polish. Measure frame pacing, CPU and GPU time where available, draw calls, overdraw, texture memory, atlas count, simultaneous particles, active filters, audio voices, startup size, and peak allocation appropriate to the engine.

For a First Playable, store `motion-presentation-review.md` and at least one `.gif`, `.mp4`, or `.webm` capture under `.hypergs/evidence/phase-03-first-playable/`. The capture must show a representative event from anticipation through recovery at the target viewport. A still image cannot prove motion, synchronization, audio, interruption, or frame pacing.

Record `PASS` or `FAIL` for:

- event-specific beat structure and hierarchy;
- animation, VFX, UI, camera, audio, and gameplay synchronization;
- readable outcome and return to control;
- asset provenance and production repeatability;
- interruption, skip, reduced-motion, and fallback behavior;
- target-device clarity and performance;
- delivery-level match without placeholder substitution.

Fail when the review relies on source art or screenshots, presentation is a generic effect applied to every event, critical assets are placeholders or unlicensed, outcome logic depends on animation timing, a sequence can strand input or UI, or measured performance misses the recorded budget.
