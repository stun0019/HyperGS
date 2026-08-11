# Godot Adapter

## Detect

Confirm `project.godot` and identify the engine version, renderer, main scene, input map, autoloads, and export presets.

## Architecture

Prefer small scenes with explicit signals and ownership. Keep reusable gameplay rules separate from presentation nodes where practical. Avoid fragile absolute node paths and broad autoload state.

## Verify

Run the pinned Godot binary headlessly for parse or test checks when possible, then run the project or exported build. Inspect errors, input actions, scene transitions, persistence, resize behavior, and target performance.

Do not modify engine-version metadata merely to satisfy the local installation.
