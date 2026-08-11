# Market Visual Benchmark

## Contents

- Research scope
- Popularity evidence
- Comparable set
- 2D and 3D analysis
- VFX analysis
- Synthesis and gate

## Research scope

Use user-provided titles and directions as the primary product intent. Expand them with current target-market research before locking a visual direction, redesigning presentation, or approving representative VFX. Use internet research or connected market sources because rankings, player interest, and visual trends change. If current sources cannot be accessed, mark the study `BLOCKED` or explicitly historical; do not invent popularity claims.

Record findings in `.hypergs/docs/VISUAL_BENCHMARK.md`. Keep observed facts, popularity signals, visual interpretation, and recommendations separate.

## Popularity evidence

For every comparable, record:

- game, developer or publisher, release status, platform, region, and research date;
- source links and capture provenance;
- at least one dated popularity signal appropriate to the platform;
- whether the signal represents current momentum, durable popularity, a niche success, or only editorial exposure;
- direct gameplay footage or in-game screenshots at a comparable camera and device context.

Use sources such as Steam store and charts, Steam public player or review data, Apple App Store charts and product pages, Google Play charts and product pages, official publisher gameplay, developer material, and reputable measurement sources. Do not treat search rank, an undated article, a cinematic trailer, key art, or personal familiarity as proof of popularity or runtime style.

Popularity is not automatically design suitability. Explain why each reference matches the target audience, platform, genre promise, camera, session shape, input, readability, performance budget, content volume, and team capacity.

## Comparable set

Use a focused set:

- three to five primary comparables with the closest audience, platform, genre, and camera;
- one or two adjacent successful titles showing a transferable pattern;
- at least one anti-reference showing a popular approach that conflicts with this project's readability, cost, originality, or position.

For each title, record `adopt`, `adapt`, and `avoid` observations. Extract principles, not protected expression. Never request copies of distinctive characters, assets, maps, logos, UI layouts, animation sequences, or a living artist's signature style.

## 2D and 3D analysis

Use only the branch or mixed-pipeline checks relevant to the target project.

For 2D, compare:

- camera, projection, parallax, stage depth, and playable-plane readability;
- character proportions, silhouette size, sprite resolution, frame density, skeletal versus frame animation, pose exaggeration, outlines, edge treatment, and palette discipline;
- environment layering, tile or painted-background strategy, texture density, lighting integration, contact shadows, and grounding;
- UI illustration, typography, icons, surfaces, transitions, and relationship to world art;
- content throughput, variant reuse, memory, atlas, compression, and target-device cost.

Choose a production-capable animation pipeline appropriate to the style. Spine-compatible skeletal animation is preferred when reusable rigs, skins, slot attachments, mesh deformation, animation mixing, and event-timed combat effects materially improve quality and the required editor/runtime license and version compatibility are available. Otherwise use authored sprite sheets, frame animation, another skeletal system, particles, meshes, or shaders with equivalent runtime evidence.

For a Spine pipeline, define source and export ownership, skeleton and bone naming, skins, slots, attachments, mesh weights, constraints, mix durations, events, atlas strategy, runtime version, licensing, fallback assets, and performance budgets. Attach VFX to authored event markers rather than arbitrary timers where practical.

For 3D, compare:

- camera, field of view, projection, framing, world scale, composition, and occlusion;
- character proportions, silhouette, topology or geometric density, rig complexity, animation style, locomotion, and hit reactions;
- materials, PBR or stylized shaders, lighting, shadows, atmosphere, post-processing, color grading, and outlines;
- environment modularity, prop density, terrain, decals, set dressing, LOD, draw calls, overdraw, and target-device cost;
- UI integration, diegetic elements, icons, typography, transitions, and camera-space effects.

For mixed 2D/3D pipelines, explicitly prove perspective, scale, lighting, edge, texture-density, frame-rate, and compositing compatibility. Shared darkness or color grading does not make incompatible assets coherent.

Generic emoji, text glyphs, unstyled lines, geometric primitives, CSS-only flashes, and simplistic one-off SVG must remain internal placeholders unless an intentionally minimal vector language is documented, benchmarked, and approved. They cannot substitute for authored characters, animation, or VFX in a presentation-ready First Playable. SVG remains acceptable when it is a deliberate production format inside the locked visual system rather than a shortcut.

## VFX analysis

Use direct gameplay video, frame sequences, or runtime observation. A single still image cannot prove effect timing or combat feel.

Benchmark applicable effect families:

- basic attack and movement trails;
- hit, block, parry, critical, kill, and damage-state feedback;
- skill cast, projectile, area warning, impact, residue, and cooldown-ready feedback;
- heal, buff, debuff, crowd control, status, loot, progression, and quest feedback;
- environmental ambience, interactables, social or party signals, and UI reinforcement.

For each reference effect, record:

- anticipation, startup, peak, hold, decay, and total duration in frames or milliseconds where measurable;
- screen-space and actor-relative size;
- shape language, directionality, color ownership, value peak, saturation, opacity, blend behavior, and background contrast;
- particles, sprites, skeletal attachments, meshes, trails, distortion, decals, lighting, sound relationship, hit stop, camera shake, and device feedback;
- attack range, target, danger, team, element, rarity, or state communicated;
- simultaneous-effect clutter, photosensitivity, color-vision accessibility, readability, and performance cost.

Do not maximize brightness, particle count, shake, or effect size merely because popular games use spectacle. Define an intensity hierarchy so normal attacks, skills, critical moments, threats, and rewards remain distinguishable.

## Synthesis and gate

Convert the study into an original, producible direction:

- one market-supported visual opportunity and one differentiation thesis;
- visual and VFX rules to adopt, adapt, and avoid;
- separate 2D, 3D, or mixed-pipeline rationale;
- a representative runtime benchmark plan;
- measurable art, animation, VFX, UI, accessibility, and performance criteria;
- unresolved assumptions and the next cheapest validation.

Gin (Market Analyst) owns source quality and popularity interpretation. Forza (Art Director) owns visual analysis, original synthesis, feasibility, and style lock. Both record an explicit `PASS` or `FAIL` in `market-visual-review.md` for a First Playable.

Fail when sources are missing or undated, references do not match the target context, analysis relies on promotional images instead of gameplay, VFX timing is inferred from a still, recommendations merely copy one title, production uses placeholder emoji or primitive effects, or the runtime benchmark does not reflect the documented synthesis.
