from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from common import TEMPLATES_ROOT


def main() -> int:
    parser = argparse.ArgumentParser(description="Add missing HyperGS project templates without overwriting project work.")
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    project = args.project.resolve()
    state_path = project / ".hypergs" / "state.json"
    docs = project / ".hypergs" / "docs"
    if not state_path.is_file():
        parser.error(f"Missing state file: {state_path}")

    templates = sorted(path for path in TEMPLATES_ROOT.iterdir() if path.suffix.lower() in {".md", ".json"})
    missing = [template for template in templates if not (docs / template.name).exists()]
    copied: list[str] = []
    if not args.check:
        docs.mkdir(parents=True, exist_ok=True)
        for template in missing:
            destination = docs / template.name
            shutil.copyfile(template, destination)
            copied.append(str(destination.relative_to(project)))

    result = {
        "project": str(project),
        "mode": "check" if args.check else "sync",
        "missing": [template.name for template in missing],
        "copied": copied,
        "up_to_date": not missing,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"HyperGS templates: {'UP TO DATE' if result['up_to_date'] else 'MISSING'}")
        for name in result["missing"]:
            print(f"- missing: {name}")
        for name in copied:
            print(f"- copied: {name}")
    return 0 if not args.check or not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
