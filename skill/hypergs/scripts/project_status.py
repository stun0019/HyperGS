from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import detect_engine, load_json, resolve_profile, validate_profile


def main() -> int:
    parser = argparse.ArgumentParser(description="Report HyperGS project and studio status.")
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    project = args.project.resolve()
    state_path = project / ".hypergs" / "state.json"
    engine, markers = detect_engine(project)
    profile, profile_source, profile_path = resolve_profile(project)
    profile_errors = validate_profile(profile)
    state = load_json(state_path) if state_path.is_file() else None
    result = {
        "project": str(project),
        "detected_engine": engine,
        "engine_markers": markers,
        "initialized": state is not None,
        "state": state,
        "studio_profile": {
            "source": profile_source,
            "path": str(profile_path),
            "valid": not profile_errors,
            "errors": profile_errors,
            "profile_name": profile.get("profile_name"),
            "roles": {
                role_id: role.get("display_name")
                for role_id, role in profile.get("roles", {}).items()
                if isinstance(role, dict)
            },
        },
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Project: {project}")
        print(f"Detected engine: {engine}")
        if state:
            print(f"Phase: {state.get('current_phase', 'unknown')}")
            print(f"Gate: {state.get('gate_status', 'unknown')}")
        else:
            print("Phase: not initialized")
        print(f"Studio profile: {profile.get('profile_name')} ({profile_source})")
    return 0 if not profile_errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
