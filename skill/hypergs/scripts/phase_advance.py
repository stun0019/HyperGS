from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import assess_phase, load_json, now_iso, write_json


def main() -> int:
    parser = argparse.ArgumentParser(description="Advance a HyperGS project after its structural gate passes.")
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()

    project = args.project.resolve()
    state_path = project / ".hypergs" / "state.json"
    if not state_path.is_file():
        parser.error(f"Missing state file: {state_path}")
    try:
        state = load_json(state_path)
        current = str(state["current_phase"])
        assessment = assess_phase(project, current)
        if not assessment["passed"]:
            print(json.dumps({"advanced": False, "reason": "gate_failed", "assessment": assessment}, ensure_ascii=False, indent=2))
            return 1
        next_phase = assessment["next_phase"]
        if not next_phase:
            print(json.dumps({"advanced": False, "reason": "terminal_phase", "assessment": assessment}, ensure_ascii=False, indent=2))
            return 1
        timestamp = now_iso()
        state.setdefault("history", []).append({"event": "phase_advanced", "from": current, "to": next_phase, "at": timestamp})
        state["current_phase"] = next_phase
        state["gate_status"] = "in_progress"
        state["updated_at"] = timestamp
        write_json(state_path, state)
        print(json.dumps({"advanced": True, "from": current, "to": next_phase, "state": state}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as error:
        parser.error(str(error))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
