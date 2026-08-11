# Architecture

## Package boundary

The repository contains public documentation and tests, while `skill/hypergs` is the only installable package. This keeps development material out of the Codex skill context.

## Progressive disclosure

`SKILL.md` contains the operating contract, request router, and execution loop. It links directly to detailed role, workflow, phase, engine, and quality references. Codex loads only the references required by the active request.

Templates that become project output live under `assets/project-templates`, not `references`.

## Identity model

HyperGS routes work with immutable role IDs. A studio profile maps each role ID to a user-facing display name. Names may contain Unicode and may change without affecting file paths, state, decisions, or workflow ownership.

Profile precedence is:

```text
project profile > user profile > built-in profile
```

## State model

Each game project has one canonical `.hypergs/state.json`. It contains the current phase, gate state, engine, target platform, and history. Markdown documents explain product and production decisions but do not independently control the lifecycle.

## Lifecycle

```text
Discovery -> Concept -> Pre-production -> First Playable -> Vertical Slice
          -> Production -> Alpha -> Beta -> Polish -> Release -> Live Operations
```

Advancement requires structural gate checks plus substantive producer review. File presence alone cannot prove quality or playability.

## Execution model

One coordinated execution is the default. Only roles with a concrete deliverable or review responsibility participate. Optional parallel agents may be used when supported and explicitly requested, but their results must be reconciled before integration.
