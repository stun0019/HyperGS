# Genre Promise

## Contents

- Contract
- Hybrid genres
- Online RPG naming
- Evidence review

## Contract

Translate each genre label, reference title, and audience promise into a Genre Promise Contract before implementation. Record it in `GAME.md` and refine it in `GDD.md`.

For every named pillar, define:

- player fantasy and target audience expectation;
- player-visible verbs and repeatable loop;
- required systems and state ownership;
- visible runtime signals;
- First Playable proof;
- deferred scope and the honest interim label.

Treat reference games as design shorthand, not permission to copy protected assets, characters, names, maps, audio, or distinctive expression.

Visual theme is not genre proof. A fantasy background, health bars, level labels, inventory button, quest text, or skill icons do not prove RPG progression, online play, shared state, persistence, or an MMO.

## Hybrid genres

Identify one primary interaction genre and one or more supporting system genres. A hybrid First Playable must contain a short playable loop from every genre named in the product promise. UI references or future plans do not satisfy a missing pillar.

For an `LF2-style brawler + MMORPG progression` concept, require representative evidence such as:

- brawler pillar: directional or lane-aware movement, responsive normal attack or combo, multiple-threat handling, hit reactions, knockback or crowd control, and clear encounter resolution;
- RPG pillar: persistent avatar identity, level or build choice, equipment or loot with a gameplay effect, quest or progression reward, and visible before/after state;
- online/shared-world pillar when claimed: two authenticated or otherwise distinct clients in the same authoritative space, synchronized relevant state, player presence or party interaction, disconnect/rejoin behavior, and persisted progress.

If only the brawler pillar exists, label the build an `action brawler prototype`. If progression is local or simulated without online shared state, use `action RPG with MMO-inspired progression`. If only small-session networking is proven, use `online co-op action RPG` rather than `MMORPG`.

## Online RPG naming

Use the narrowest label supported by observed evidence:

| Label | Minimum supported promise |
|---|---|
| `action RPG with MMO-inspired progression` | Persistent or simulated character growth and loot/progression loops; no claim of a live shared world |
| `online co-op action RPG` | Real networked sessions for a bounded party, authoritative or reconciled shared gameplay state, and reconnect/error behavior |
| `MMORPG First Playable` | Server-backed player identity and durable character state; at least two distinct simultaneous clients sharing a zone or equivalent authoritative world instance; synchronized player-relevant state; a persisted quest, loot, or progression outcome; visible social or party presence; and reconnect recovery |

An MMORPG First Playable does not need production population scale, a complete open world, guilds, trading, monetization, or final operations infrastructure. It must prove the architecture and player experience behind the word `multiplayer`, `persistent`, and `role-playing`. Record concurrency scale as unproven until measured.

## Evidence review

Create `.hypergs/evidence/phase-03-first-playable/genre-review.md` with:

- claimed public label and narrower fallback label;
- contract table for every named genre pillar;
- links to runtime capture, build, playtest, save/persistence test, and network evidence as applicable;
- observed proof versus planned work;
- explicit `PASS` or `FAIL` verdict from Game Design;
- label correction required when a pillar fails.

For hybrid concepts, `PASS` requires all named pillars to be observable in one coherent build. A visually polished arena fight fails an MMORPG claim when the build shows no persistent character outcome, shared player presence, synchronized state, or social/world loop. Do not allow the producer to override missing genre evidence with presentation quality.
