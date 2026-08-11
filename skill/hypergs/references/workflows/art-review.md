# Art Review Workflow

## Lead and support

Lead: Art Director. Support: UI/UX Designer, Client Engineer, Game Designer, and Market Analyst when positioning is affected.

## Procedure

1. Read `market-visual-benchmark.md` and `art-style-system.md`.
2. Verify that `VISUAL_BENCHMARK.md` uses user direction plus current, dated popularity evidence and direct gameplay captures from relevant 2D, 3D, or mixed-pipeline comparables.
3. Compare the runtime against both the market synthesis and the locked camera, scale, perspective, shape, palette, value, lighting, material, edge, animation, VFX, and UI grammar in `ART.md`.
4. Review VFX in motion by effect family, timing, intensity hierarchy, readability, accessibility, and performance; do not approve timing claims from a still image.
5. Inspect every gameplay character and representative enemy in motion. For real-time character-driven games, require authored idle, locomotion, action, recovery, hit, and defeat states through sprite sheets, Spine or equivalent skeletal animation, or 3D rig animation.
6. Verify animation events align hitboxes, projectiles, VFX, audio, hit stop, camera response, and state changes.
7. Inspect provenance and production repeatability; distinguish a coherent asset family from unrelated polished outputs.
8. Separate objective grammar violations and readability defects from taste preferences.
9. Prioritize changes that improve player comprehension or establish a reusable asset rule.
10. Validate a representative player, enemy, environment, action VFX, and HUD benchmark together in the runtime.
11. For a First Playable, reject static cutout gameplay actors, debug-scale characters, absent action or reaction animation, flat or empty staging, primitive placeholder effects, incompatible perspective or lighting, mismatched rendering finish, and UI/gameplay style mismatch.

## Completion

Produce specific, bounded review findings, updated art rules where needed, runtime evidence for material changes, and an explicit `PASS` or `FAIL` verdict. A First Playable art review must cite actual runtime capture and address every Runtime Review category from `art-style-system.md`; `market-visual-review.md` records Gin and Forza verdicts on sources and synthesis, while `animation-review.md` records motion coverage and runtime synchronization.
