from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import get_phase, load_json, project_profile_path, validate_profile


REQUIRED_STATE_FIELDS = (
    "schema_version",
    "project_name",
    "engine",
    "target_platform",
    "current_phase",
    "gate_status",
    "created_at",
    "updated_at",
    "history",
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate HyperGS project-memory structure.")
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    project = args.project.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    state_path = project / ".hypergs" / "state.json"
    docs = project / ".hypergs" / "docs"

    if not state_path.is_file():
        errors.append(f"Missing state file: {state_path}")
    else:
        try:
            state = load_json(state_path)
            for field in REQUIRED_STATE_FIELDS:
                if field not in state:
                    errors.append(f"Missing state field: {field}")
            if state.get("schema_version") != 1:
                errors.append("state.schema_version must be 1")
            if state.get("gate_status") not in {"not_started", "in_progress", "passed", "blocked"}:
                errors.append("state.gate_status is invalid")
            if "current_phase" in state:
                get_phase(str(state["current_phase"]))
            if not isinstance(state.get("history"), list):
                errors.append("state.history must be an array")
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(str(error))

    if not docs.is_dir():
        errors.append(f"Missing docs directory: {docs}")
    profile_path = project_profile_path(project)
    if profile_path.exists():
        try:
            errors.extend(f"studio profile: {error}" for error in validate_profile(load_json(profile_path)))
        except (OSError, ValueError, json.JSONDecodeError) as error:
            errors.append(f"Invalid studio profile: {error}")
    if (project / ".hypergs" / "reports").exists() is False:
        warnings.append("Missing reports directory")
    if (project / ".hypergs" / "evidence").exists() is False:
        warnings.append("Missing evidence directory")

    result = {"valid": not errors, "project": str(project), "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"HyperGS project: {'VALID' if result['valid'] else 'INVALID'}")
        for error in errors:
            print(f"ERROR: {error}")
        for warning in warnings:
            print(f"WARNING: {warning}")
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
