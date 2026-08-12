from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from common import TEMPLATES_ROOT, detect_engine, now_iso, write_json


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize non-destructive HyperGS project memory.")
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--name")
    parser.add_argument("--engine", default="auto")
    parser.add_argument("--target-platform", default="unspecified")
    parser.add_argument("--phase", default="phase-00-discovery")
    args = parser.parse_args()

    project = args.project.resolve()
    project.mkdir(parents=True, exist_ok=True)
    hypergs = project / ".hypergs"
    state_path = hypergs / "state.json"
    if state_path.exists():
        parser.error(f"HyperGS state already exists: {state_path}")

    detected_engine, _ = detect_engine(project)
    engine = detected_engine if args.engine == "auto" else args.engine
    timestamp = now_iso()
    state = {
        "schema_version": 1,
        "project_name": args.name or project.name,
        "engine": engine,
        "target_platform": args.target_platform,
        "current_phase": args.phase,
        "gate_status": "in_progress",
        "created_at": timestamp,
        "updated_at": timestamp,
        "history": [{"event": "initialized", "phase": args.phase, "at": timestamp}],
    }

    docs = hypergs / "docs"
    evidence = hypergs / "evidence"
    reports = hypergs / "reports"
    docs.mkdir(parents=True, exist_ok=True)
    evidence.mkdir(parents=True, exist_ok=True)
    reports.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for template in sorted(path for path in TEMPLATES_ROOT.iterdir() if path.suffix.lower() in {".md", ".json"}):
        destination = docs / template.name
        if not destination.exists():
            shutil.copyfile(template, destination)
            copied.append(str(destination.relative_to(project)))
    write_json(state_path, state)
    print(json.dumps({"initialized": str(project), "state": state, "templates": copied}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
