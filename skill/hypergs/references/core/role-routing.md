# Role Routing

## Contents

- Stable identity model
- Routing matrix
- Display rules
- Support responsibilities

## Stable identity model

Use immutable `role_id` values for files, automation, routing, and decisions. Use configurable `display_name` values only in user-facing prose. Never derive a path, command, permission, or state key from a display name.

Resolve names using this precedence:

1. `<project>/.hypergs/studio-profile.json`
2. `<CODEX_HOME>/hypergs/studio-profile.json`
3. `assets/profiles/default-studio-profile.json`

## Routing matrix

| Work type | Lead | Typical support |
|---|---|---|
| Project scope or phase | `producer` | All affected roles |
| New mechanic | `game_designer` | Client, UI/UX, data |
| Client feature | `client_engineer` | Design, UI/UX, art |
| Online or persistence feature | `server_engineer` | Client, data |
| Screen or player journey | `uiux_designer` | Client, design, art |
| Art direction | `art_director` | UI/UX, client |
| Product positioning | `market_analyst` | Producer, design |
| Balance or measurement | `data_analyst` | Design, server |
| Quality review | `producer` | Every affected specialist |

## Display rules

Render a role as `display name (localized role title)`. If a profile uses title mode, avoid duplicated output such as `Producer (Producer)` and show the title once.

Accept Unicode display names. Trim whitespace, limit names to 40 characters, reject control characters, and warn about duplicates without using them as identifiers.

## Support responsibilities

Quality assurance is a mandatory cross-functional responsibility: the producer owns the test plan, the implementing engineer owns automated checks, and the relevant design specialist owns behavioral acceptance.

Audio, localization, accessibility, security, deployment, community, and live operations are support functions. Route them to the closest core role until a future extension adds dedicated stable role IDs. Never silently omit a support function that affects the current phase gate.
