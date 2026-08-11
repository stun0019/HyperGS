from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import (
    ROLE_IDS,
    build_profile,
    project_profile_path,
    resolve_profile,
    user_profile_path,
    validate_profile,
    write_json,
)


def parse_overrides(values: list[str]) -> dict[str, str]:
    overrides: dict[str, str] = {}
    for value in values:
        if "=" not in value:
            raise ValueError(f"Expected role_id=name, received: {value}")
        role_id, display_name = value.split("=", 1)
        role_id = role_id.strip()
        if role_id not in ROLE_IDS:
            raise ValueError(f"Unknown role ID: {role_id}")
        overrides[role_id] = display_name
    return overrides


def main() -> int:
    parser = argparse.ArgumentParser(description="Show or configure HyperGS role display names.")
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--scope", choices=("user", "project"), default="user")
    parser.add_argument("--preset", choices=("default", "titles", "custom"))
    parser.add_argument("--set", dest="overrides", action="append", default=[], metavar="ROLE_ID=NAME")
    parser.add_argument("--locale", default="zh-TW")
    parser.add_argument("--profile-name")
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()

    try:
        target = user_profile_path() if args.scope == "user" else project_profile_path(args.project)
        if args.reset:
            if target.exists():
                target.unlink()
            profile, source, path = resolve_profile(args.project)
            print(json.dumps({"reset": str(target), "source": source, "path": str(path), "profile": profile}, ensure_ascii=False, indent=2))
            return 0

        if args.show or (args.preset is None and not args.overrides):
            profile, source, path = resolve_profile(args.project)
            errors = validate_profile(profile)
            print(json.dumps({"source": source, "path": str(path), "valid": not errors, "errors": errors, "profile": profile}, ensure_ascii=False, indent=2))
            return 0 if not errors else 1

        overrides = parse_overrides(args.overrides)
        profile = build_profile(args.preset or "custom", overrides, args.locale, args.profile_name)
        write_json(target, profile)
        print(json.dumps({"saved": str(target), "profile": profile}, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
