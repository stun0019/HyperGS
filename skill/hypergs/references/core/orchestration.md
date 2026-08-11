# Studio Orchestration

## Contents

- Operating model
- Decision ownership
- Execution modes
- Conflict resolution
- Completion rules

## Operating model

HyperGS is a workflow coordinator, not a role-play transcript. Each run has one objective, one lead role, zero or more supporting roles, concrete deliverables, and acceptance evidence.

The producer selects scope and resolves cross-discipline tradeoffs. A specialist owns the correctness of its discipline. The user retains authority over product direction, irreversible external actions, spending, publishing, and credentials.

## Decision ownership

| Decision | Owner | Required consultation |
|---|---|---|
| Scope, schedule, and phase gate | `producer` | All affected roles |
| Core loop, rules, progression | `game_designer` | Client, data, producer |
| Runtime architecture and client performance | `client_engineer` | Design, UI/UX, art |
| Services, persistence, networking, security | `server_engineer` | Client, data, producer |
| Navigation, interaction, accessibility | `uiux_designer` | Design, client |
| Visual language and asset consistency | `art_director` | UI/UX, client |
| Audience, competitors, positioning | `market_analyst` | Producer, design |
| Telemetry, KPIs, experiments, balance evidence | `data_analyst` | Design, server |

## Execution modes

Use sequential mode by default: inspect, plan, implement, validate, and reconcile in one execution context.

Use parallel role work only when the user explicitly requests it and the environment supports independent agents. Give each role a bounded artifact and no overlapping write ownership. The producer must review all outputs against the same scope before integration.

## Conflict resolution

Resolve conflicts in this order:

1. Player safety, security, privacy, and platform rules
2. Explicit user constraints
3. Phase objective and acceptance criteria
4. Playability and technical feasibility
5. Schedule and cost
6. Polish and optional scope

Record consequential tradeoffs in `.hypergs/docs/DECISIONS.md`.

## Completion rules

A run is complete only when its promised deliverable exists and the reported verification was actually performed. A phase is complete only when its gate passes. Missing tools, assets, credentials, or user decisions are blockers to the affected claim, not reasons to fabricate success.
