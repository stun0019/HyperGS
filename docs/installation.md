# Installation

## Requirements

- Codex with local skill support
- Python 3.10 or newer for the bundled deterministic tools
- The toolchain required by the target game engine

## Install

Copy only the installable package directory:

```text
HyperGS/skill/hypergs
```

Place it at:

```text
%USERPROFILE%\.codex\skills\hypergs
```

On macOS or Linux, use:

```text
~/.codex/skills/hypergs
```

Restart Codex after installing or updating the skill.

## Verify

Invoke the skill explicitly:

```text
$hypergs, show my studio team.
```

Natural invocation is also supported:

```text
HyperGS, inspect this game project and recommend the next phase.
```

If no user profile exists, HyperGS starts the naming setup before continuing the retained game request.

## Update

Replace the installed `hypergs` skill directory and restart Codex. Studio names are stored outside the installed package, so a normal update does not overwrite them.
