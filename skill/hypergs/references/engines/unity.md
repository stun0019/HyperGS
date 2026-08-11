# Unity Adapter

## Detect

Confirm `Assets/`, `Packages/manifest.json`, and `ProjectSettings/ProjectVersion.txt`. Preserve the recorded editor version and package-lock behavior.

## Architecture

Keep domain rules testable outside `MonoBehaviour` when practical. Separate scenes, prefabs, data assets, presentation, input, networking, and persistence. Avoid unnecessary global singletons and hidden scene dependencies.

## Verify

Use the project-pinned Unity version. Run Edit Mode and Play Mode tests as available, inspect console errors, verify required scenes and build settings, and produce a target build only when the editor and modules are present.

Record missing editor licenses, platform modules, or proprietary assets as blockers rather than fabricating build success.
