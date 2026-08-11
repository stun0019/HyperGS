from __future__ import annotations

import json
import os
import tempfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSETS_ROOT = SKILL_ROOT / "assets"
DEFAULT_PROFILE_PATH = ASSETS_ROOT / "profiles" / "default-studio-profile.json"
PHASE_CATALOG_PATH = ASSETS_ROOT / "schemas" / "phase-catalog.json"
TEMPLATES_ROOT = ASSETS_ROOT / "project-templates"

ROLE_IDS = (
    "producer",
    "game_designer",
    "client_engineer",
    "server_engineer",
    "uiux_designer",
    "art_director",
    "market_analyst",
    "data_analyst",
)

RUNTIME_CAPTURE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".webm"}


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(payload)
        os.replace(temporary_path, path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def codex_home() -> Path:
    configured = os.environ.get("CODEX_HOME")
    return Path(configured).expanduser().resolve() if configured else Path.home() / ".codex"


def user_profile_path() -> Path:
    return codex_home() / "hypergs" / "studio-profile.json"


def project_profile_path(project: Path) -> Path:
    return project.resolve() / ".hypergs" / "studio-profile.json"


def default_profile() -> dict[str, Any]:
    return deepcopy(load_json(DEFAULT_PROFILE_PATH))


def validate_display_name(value: str) -> str:
    name = value.strip()
    if not name:
        raise ValueError("Display names cannot be empty")
    if len(name) > 40:
        raise ValueError("Display names cannot exceed 40 characters")
    if any(ord(character) < 32 or ord(character) == 127 for character in name):
        raise ValueError("Display names cannot contain control characters")
    return name


def validate_profile(profile: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if profile.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if profile.get("preset") not in {"default", "titles", "custom"}:
        errors.append("preset must be default, titles, or custom")
    roles = profile.get("roles")
    if not isinstance(roles, dict):
        return errors + ["roles must be an object"]
    missing = [role_id for role_id in ROLE_IDS if role_id not in roles]
    unknown = [role_id for role_id in roles if role_id not in ROLE_IDS]
    if missing:
        errors.append(f"missing roles: {', '.join(missing)}")
    if unknown:
        errors.append(f"unknown roles: {', '.join(unknown)}")
    for role_id in ROLE_IDS:
        role = roles.get(role_id)
        if not isinstance(role, dict):
            continue
        try:
            validate_display_name(str(role.get("display_name", "")))
        except ValueError as error:
            errors.append(f"{role_id}: {error}")
    return errors


def build_profile(
    preset: str,
    overrides: dict[str, str] | None = None,
    locale: str = "zh-TW",
    profile_name: str | None = None,
) -> dict[str, Any]:
    if preset not in {"default", "titles", "custom"}:
        raise ValueError(f"Unknown preset: {preset}")
    profile = default_profile()
    profile["preset"] = preset
    profile["locale"] = locale
    profile["profile_name"] = profile_name or (
        "Role Titles" if preset == "titles" else "HyperGS Originals"
    )
    if preset == "titles":
        title_key = "title_zh_tw" if locale.lower().startswith("zh") else "title_en"
        for role in profile["roles"].values():
            role["display_name"] = role[title_key]
    for role_id, display_name in (overrides or {}).items():
        if role_id not in ROLE_IDS:
            raise ValueError(f"Unknown role ID: {role_id}")
        profile["roles"][role_id]["display_name"] = validate_display_name(display_name)
        profile["preset"] = "custom"
    errors = validate_profile(profile)
    if errors:
        raise ValueError("; ".join(errors))
    return profile


def resolve_profile(project: Path | None = None) -> tuple[dict[str, Any], str, Path]:
    if project is not None:
        candidate = project_profile_path(project)
        if candidate.exists():
            return load_json(candidate), "project", candidate
    candidate = user_profile_path()
    if candidate.exists():
        return load_json(candidate), "user", candidate
    return default_profile(), "built_in", DEFAULT_PROFILE_PATH


def load_phase_catalog() -> list[dict[str, Any]]:
    value = load_json(PHASE_CATALOG_PATH).get("phases")
    if not isinstance(value, list):
        raise ValueError("Phase catalog must contain a phases array")
    return value


def get_phase(phase_id: str) -> dict[str, Any]:
    for phase in load_phase_catalog():
        if phase.get("id") == phase_id:
            return phase
    raise ValueError(f"Unknown phase: {phase_id}")


def detect_engine(project: Path) -> tuple[str, list[str]]:
    markers: list[str] = []
    if (project / "Assets").is_dir() and (project / "ProjectSettings" / "ProjectVersion.txt").is_file():
        markers.extend(["Assets/", "ProjectSettings/ProjectVersion.txt"])
        return "unity", markers
    if (project / "project.godot").is_file():
        return "godot", ["project.godot"]
    unreal_projects = sorted(project.glob("*.uproject"))
    if unreal_projects:
        return "unreal", [item.name for item in unreal_projects]
    html_markers = [name for name in ("index.html", "package.json", "vite.config.js", "vite.config.ts") if (project / name).is_file()]
    if html_markers:
        return "html5", html_markers
    return "unknown", markers


def is_substantive_document(path: Path) -> tuple[bool, str | None]:
    if not path.is_file():
        return False, "missing"
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return False, "empty"
    template = TEMPLATES_ROOT / path.name
    if template.is_file() and content == template.read_text(encoding="utf-8").strip():
        return False, "template_only"
    return True, None


def assess_phase(project: Path, phase_id: str) -> dict[str, Any]:
    phase = get_phase(phase_id)
    docs_root = project / ".hypergs" / "docs"
    evidence_root = project / ".hypergs" / "evidence" / phase_id
    problems: list[dict[str, str]] = []
    for name in phase.get("required_docs", []):
        valid, reason = is_substantive_document(docs_root / name)
        if not valid:
            problems.append({"kind": "document", "name": name, "reason": reason or "invalid"})
    for name in phase.get("required_evidence", []):
        valid, reason = is_substantive_document(evidence_root / name)
        if not valid:
            problems.append({"kind": "evidence", "name": name, "reason": reason or "invalid"})
    if phase.get("requires_runtime_capture"):
        captures = [
            path
            for path in evidence_root.rglob("*")
            if path.is_file() and path.suffix.lower() in RUNTIME_CAPTURE_EXTENSIONS
        ] if evidence_root.is_dir() else []
        if not captures:
            problems.append({"kind": "evidence", "name": "runtime-capture", "reason": "missing"})
    for name in phase.get("required_pass_reviews", []):
        review_path = evidence_root / name
        if not review_path.is_file():
            continue
        content = review_path.read_text(encoding="utf-8").upper()
        has_pass = "PASS" in content
        has_fail = "FAIL" in content
        if not has_pass or has_fail:
            problems.append({"kind": "review", "name": name, "reason": "missing_unambiguous_pass"})
    return {
        "phase": phase_id,
        "phase_name": phase["name"],
        "passed": not problems,
        "problems": problems,
        "next_phase": phase.get("next"),
    }
