from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import detect_engine


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect a game project and its HyperGS state.")
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    project = args.project.resolve()
    if not project.is_dir():
        parser.error(f"Project directory does not exist: {project}")
    engine, markers = detect_engine(project)
    result = {
        "project": str(project),
        "engine": engine,
        "markers": markers,
        "has_hypergs": (project / ".hypergs" / "state.json").is_file(),
        "is_empty": not any(project.iterdir()),
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Project: {project}")
        print(f"Engine: {engine}")
        print(f"HyperGS state: {'present' if result['has_hypergs'] else 'absent'}")
        print(f"Markers: {', '.join(markers) if markers else 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
