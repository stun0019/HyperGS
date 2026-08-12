# HyperGS

HyperGS turns Codex into a structured virtual game studio. It coordinates production, game design, client and server engineering, UI/UX, art direction, market analysis, and data analysis across a gated game-development lifecycle.

Instead of returning an isolated code fragment, HyperGS maintains project memory, selects the relevant studio roles, implements a thin end-to-end slice, verifies the result, and recommends the next production action.

## Status

This repository contains a functional skill architecture, deterministic project-memory tools, strict First Playable gates, and a motion-presentation production pipeline. HTML5, Unity, Godot, and Unreal project adapters are documented; actual build capability depends on the tools installed in the target workspace.

## Install in three steps

1. Copy `skill/hypergs` to your Codex skills directory as `hypergs`.
   - Windows default: `%USERPROFILE%\.codex\skills\hypergs`
   - macOS/Linux default: `~/.codex/skills/hypergs`
2. Restart Codex.
3. Enter `HyperGS` or invoke `$hypergs` with a request.

Example:

```text
HyperGS, plan and execute the next phase of an HTML5 mobile game that combines LF2-style combat with lightweight MMORPG progression.
```

On first use, HyperGS offers three role-naming modes: the original default roster, role titles, or custom names. Display names can be changed later without changing role responsibilities or project state.

## Repository layout

- `skill/hypergs/` — the installable Codex skill
- `docs/` — architecture, workflow, installation, usage, and development documentation
- `examples/` — realistic prompts and expected behavior
- `tests/` — deterministic script tests

## Core principles

- Stable role IDs, configurable display names
- Evidence-based phase gates
- Project-local durable memory under `.hypergs/`
- Thin playable slices before broad production
- Honest validation: planned or unrun work is never reported as complete
- Event-driven motion, VFX, camera, UI, and audio presentation with video evidence
- Machine-readable asset provenance and animation-event contracts
- Engine-native conventions and preservation of existing user work

## Documentation

- [Installation](docs/installation.md)
- [Usage](docs/usage.md)
- [Architecture](docs/architecture.md)
- [Workflow](docs/workflow.md)
- [Development](docs/development.md)

## License

No open-source license has been selected yet. See `LICENSE`.
