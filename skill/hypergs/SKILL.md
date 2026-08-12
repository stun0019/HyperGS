---
name: hypergs
description: Operate a game project as a structured virtual game studio from idea through live operations. Use when the user says HyperGS or asks Codex to plan, build, review, test, validate, optimize, or advance a game project or game-development phase in HTML5, Unity, Godot, Unreal, or another engine. Coordinate production, game design, client, server, UI/UX, art direction, market analysis, and data analysis; maintain project memory; implement the smallest useful playable slice; collect verification evidence; and enforce phase gates instead of returning isolated code only.
---

# HyperGS

Run the user's game project as an evidence-driven studio workflow. Respond in the user's language, but write HyperGS-managed Markdown artifacts in English unless the user explicitly requests another artifact language.

## Operating contract

- Treat role names as display labels. Route all work by immutable role IDs.
- Inspect the workspace before proposing changes. Preserve existing user work.
- Prefer a thin playable vertical slice over broad disconnected systems.
- Distinguish an internal functional prototype from a player-facing First Playable. When a user asks to make or build a game without explicitly requesting a rough prototype, default the delivery target to a presentation-ready First Playable.
- Convert every genre label and reference-game shorthand into a testable Genre Promise Contract before implementation. Do not claim a genre from visual theme, HUD chrome, or planned systems alone.
- Make reasonable, reversible assumptions and record them. Ask only for decisions that materially change scope, platform, engine, cost, or external state.
- Produce working artifacts, implementation, tests, and evidence when the request authorizes changes. Do not stop at advice or sample code.
- Never call a build playable, validated, or complete unless it was actually run or verified.
- Never advance a phase when its gate fails. Report the missing evidence and the smallest recovery plan.
- Distinguish hypotheses from observed market or analytics data.

## Start every run

1. Locate this skill directory and the user's game-project root.
2. Run `python scripts/configure_studio.py --show --project <project-root>`.
3. If the returned profile source is `built_in`, perform first-use onboarding before changing the project:
   - Offer `default`, `titles`, and `custom` naming modes.
   - Show the complete role-to-name mapping in one compact table.
   - Let the user change only selected roles; keep all unspecified defaults.
   - Save the choice with `configure_studio.py --scope user --preset <mode>` and repeated `--set role_id=name` arguments.
   - Retain the user's original game request and continue it after onboarding.
4. Run `python scripts/detect_project.py <project-root> --json`.
5. If `.hypergs/state.json` is absent and the user authorized project creation or modification, initialize it with `init_project.py`. Otherwise, report what initialization would create.
6. If `.hypergs/state.json` exists, run `python scripts/sync_project_templates.py <project-root> --check --json`. When required templates are missing and the user authorized project changes, rerun without `--check`; never overwrite existing project documents.
7. Run `python scripts/project_status.py <project-root> --json` and use its state as the execution baseline.

Read [orchestration.md](references/core/orchestration.md), [role-routing.md](references/core/role-routing.md), and [project-memory.md](references/core/project-memory.md) for the operating model. Read only the role, workflow, phase, engine, and standard references needed for the current request.

## Route the request

| Request | Required workflow |
|---|---|
| One-sentence game idea or empty workspace | [new-project.md](references/workflows/new-project.md) |
| Existing repository without HyperGS state | [existing-project.md](references/workflows/existing-project.md) |
| Plan or execute the next phase | [next-phase.md](references/workflows/next-phase.md) |
| Add or revise player-facing mechanics | [gameplay-feature.md](references/workflows/gameplay-feature.md) |
| Add services, persistence, networking, or accounts | [backend-feature.md](references/workflows/backend-feature.md) |
| Create or improve interaction flows and screens | [uiux-feature.md](references/workflows/uiux-feature.md) |
| Establish or review visual direction and assets | [art-review.md](references/workflows/art-review.md) |
| Plan, implement, or review animation, VFX, audio, camera, reward, or cinematic presentation | [motion-presentation.md](references/workflows/motion-presentation.md) |
| Tune economy, difficulty, progression, or rewards | [balance-review.md](references/workflows/balance-review.md) |
| Diagnose and fix a defect | [bug-fix.md](references/workflows/bug-fix.md) |
| Review quality or readiness | [qa-review.md](references/workflows/qa-review.md) |
| Prepare a public build | [release-review.md](references/workflows/release-review.md) |

Combine workflows only when their deliverables genuinely overlap. Name one lead workflow and treat the rest as supporting checks.

## Select the lifecycle phase

Use `.hypergs/state.json` as the canonical phase state. Consult the matching phase reference under `references/phases/` and the machine-readable `assets/schemas/phase-catalog.json`.

The lifecycle is:

`discovery -> concept -> pre-production -> first-playable -> vertical-slice -> production -> alpha -> beta -> polish -> release -> live-ops`

Load the active phase brief: [Discovery](references/phases/phase-00-discovery.md), [Concept](references/phases/phase-01-concept.md), [Pre-production](references/phases/phase-02-pre-production.md), [First Playable](references/phases/phase-03-first-playable.md), [Vertical Slice](references/phases/phase-04-vertical-slice.md), [Production](references/phases/phase-05-production.md), [Alpha](references/phases/phase-06-alpha.md), [Beta](references/phases/phase-07-beta.md), [Polish](references/phases/phase-08-polish.md), [Release](references/phases/phase-09-release.md), or [Live Operations](references/phases/phase-10-live-ops.md).

Run `phase_check.py` before proposing advancement. Run `phase_advance.py` only after all required gate evidence exists.

## Route studio roles

Use stable role IDs and resolve their display names from the active studio profile:

- `producer`
- `game_designer`
- `client_engineer`
- `server_engineer`
- `uiux_designer`
- `art_director`
- `market_analyst`
- `data_analyst`

The producer owns scope and the final gate decision. Involve only roles with a real deliverable or review responsibility. Do not generate eight ceremonial opinions.

Load the briefs for participating roles only: [Producer](references/roles/producer.md), [Game Designer](references/roles/game-designer.md), [Client Engineer](references/roles/client-engineer.md), [Server Engineer](references/roles/server-engineer.md), [UI/UX Designer](references/roles/uiux-designer.md), [Art Director](references/roles/art-director.md), [Market Analyst](references/roles/market-analyst.md), and [Data Analyst](references/roles/data-analyst.md).

Default to one coordinated Codex execution. If independent parallel agents are available and the user explicitly requests parallel studio work, assign bounded artifacts to relevant roles, then have the producer reconcile conflicts before implementation.

## Execute a production loop

For each run:

1. State the current phase and one measurable run objective.
2. Select the lead role, supporting roles, expected artifacts, and acceptance checks.
3. Inspect existing code, documents, assets, tests, and constraints.
4. Update the smallest required project-memory documents.
5. Implement the thinnest end-to-end playable or reviewable slice.
6. Run proportionate tests, builds, or inspections.
7. Store concise evidence under `.hypergs/evidence/<phase>/` when evidence files add value.
8. Update `.hypergs/state.json`, decisions, roadmap, and changelog through the provided scripts or templates.
9. Evaluate the gate without relaxing criteria after seeing the result.

Use [acceptance-criteria.md](references/standards/acceptance-criteria.md), [code-quality.md](references/standards/code-quality.md), [phase-gates.md](references/standards/phase-gates.md), and [priority-levels.md](references/standards/priority-levels.md) as applicable.

For player-facing builds, read [prototype-quality.md](references/standards/prototype-quality.md). Do not present or advance a functional or visual prototype as a First Playable. First Playable review requires runtime capture plus separate gameplay, UI/UX, art, and producer acceptance.

For new concepts, hybrid genres, or any genre-readiness review, read [genre-promise.md](references/standards/genre-promise.md). Require runtime proof for each named genre pillar and use an honest narrower label when online, persistence, social, simulation, or scale promises are not yet implemented.

For visual direction, asset creation, or art review, read [art-style-system.md](references/standards/art-style-system.md). Lock a reusable visual grammar with a representative in-runtime benchmark before producing assets broadly; reject individually polished assets that do not belong to the same camera, proportion, lighting, material, edge, animation, VFX, and UI system.

For player-facing motion, reward sequences, combat impact, slot-style presentation, cinematic transitions, or audio-reactive feedback, read [motion-presentation-system.md](references/standards/motion-presentation-system.md). Require event-level beats, production-ready asset provenance, runtime synchronization, reduced-motion behavior, performance budgets, and motion capture. Do not substitute generic tweens, screen shake, particles, or CSS transitions for authored presentation.

Before locking art direction or combat effects, read [market-visual-benchmark.md](references/standards/market-visual-benchmark.md). Start with user-provided references when available, then research current successful 2D or 3D games on the target platform using dated, cited popularity evidence from sources such as Steam, App Store, or Google Play and direct gameplay captures. Benchmark world art, characters, animation, UI, and VFX separately; block style lock when research is unsourced, stale, based only on promotional art, or disconnected from production constraints.

## Select an engine adapter

- Read [html5.md](references/engines/html5.md) for browser games and fast zero-install prototypes.
- Read [unity.md](references/engines/unity.md) for Unity projects.
- Read [godot.md](references/engines/godot.md) for Godot projects.
- Read [unreal.md](references/engines/unreal.md) for Unreal projects.
- For another engine, inspect its official project structure and preserve its native conventions. Record the unsupported adapter as a risk rather than pretending full support.

## Report the run

End every substantive run with:

- Current phase and gate status
- Run objective
- Lead and supporting roles, shown as `display name (role title)`
- Completed deliverables and changed files
- Tests or inspections actually performed
- Evidence and acceptance results
- Open risks, assumptions, and decisions needed
- One recommended next action

Keep the report concise. The project files are the durable record.
