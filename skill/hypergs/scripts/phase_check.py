from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import assess_phase, load_json


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the structural gate for a HyperGS phase.")
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--phase")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    project = args.project.resolve()
    state_path = project / ".hypergs" / "state.json"
    if not state_path.is_file() and not args.phase:
        parser.error(f"Missing state file: {state_path}")
    try:
        phase_id = args.phase or str(load_json(state_path)["current_phase"])
        result = assess_phase(project, phase_id)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        parser.error(str(error))

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Phase: {result['phase']} ({result['phase_name']})")
        print(f"Structural gate: {'PASS' if result['passed'] else 'FAIL'}")
        for problem in result["problems"]:
            print(f"- {problem['kind']}: {problem['name']} ({problem['reason']})")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
