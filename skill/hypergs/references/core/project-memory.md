# Project Memory

## Contents

- Directory contract
- Source of truth
- Update policy
- Evidence policy

## Directory contract

Maintain durable project context under `.hypergs/`:

```text
.hypergs/
|-- state.json
|-- studio-profile.json          # optional project-level name override
|-- docs/
|   |-- GAME.md
|   |-- GDD.md
|   |-- TECH.md
|   |-- UIUX.md
|   |-- ART.md
|   |-- VISUAL_BENCHMARK.md
|   |-- MOTION.md
|   |-- PRESENTATION_BEATS.md
|   |-- ASSET_MANIFEST.json
|   |-- ANIMATION_EVENTS.json
|   |-- MARKET.md
|   |-- ANALYTICS.md
|   |-- ROADMAP.md
|   |-- DECISIONS.md
|   `-- CHANGELOG.md
|-- evidence/
`-- reports/
```

## Source of truth

Use `state.json` as the only machine-readable source for project identity, engine, platform, current phase, gate status, and phase history. Markdown documents explain decisions and designs but must not independently control phase state.

## Update policy

- Update only documents affected by the current run.
- Preserve human-authored content and add concise sections or entries.
- Date meaningful decisions and record their owner, rationale, alternatives, and consequences.
- Keep the roadmap ordered by outcome rather than by department.
- Add changelog entries for user-visible or production-relevant changes, not every formatting edit.

## Evidence policy

Evidence may include test output, screenshots, build logs, profiling summaries, review checklists, and analytics query results. Store only durable, useful evidence. Link it from the run report or decision record. Do not store secrets, credentials, personal data, generated dependency trees, or large build artifacts in `.hypergs`.
