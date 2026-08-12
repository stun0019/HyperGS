from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import is_substantive_document, validate_presentation_specs


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate HyperGS motion-presentation specifications.")
    parser.add_argument("project", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--require-approved", action="store_true")
    args = parser.parse_args()

    project = args.project.resolve()
    docs = project / ".hypergs" / "docs"
    problems: list[dict[str, str]] = []
    for name in ("MOTION.md", "PRESENTATION_BEATS.md", "ASSET_MANIFEST.json", "ANIMATION_EVENTS.json"):
        valid, reason = is_substantive_document(docs / name)
        if not valid:
            problems.append({"kind": "document", "name": name, "reason": reason or "invalid"})
    if not problems:
        problems.extend(validate_presentation_specs(docs, require_approved=args.require_approved))

    result = {"valid": not problems, "project": str(project), "problems": problems}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Motion presentation: {'VALID' if result['valid'] else 'INVALID'}")
        for problem in problems:
            print(f"- {problem['kind']}: {problem['name']} ({problem['reason']})")
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
