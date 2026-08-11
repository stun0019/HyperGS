# Development

## Validate the skill

Run the official skill validator against the installable package:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "skill\hypergs"
```

## Run tests

```powershell
python -m unittest discover -s tests -v
```

## Design rules

- Write all Markdown files in English.
- Keep `SKILL.md` concise and route detailed knowledge to direct references.
- Keep reusable output templates under `assets`.
- Use Python's standard library in bundled scripts unless a dependency is essential and documented.
- Do not identify roles by display name.
- Do not duplicate canonical phase state across Markdown files.
- Add or change a gate only with matching tests and documentation.
- Test scripts by executing them against temporary projects.

## Adding an engine adapter

Add a direct reference under `skill/hypergs/references/engines`, link it from `SKILL.md`, and specify detection markers, architectural constraints, and honest verification steps. Do not claim support that cannot be tested with the available toolchain.
