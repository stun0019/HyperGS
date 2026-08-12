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
STILL_CAPTURE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
MOTION_CAPTURE_EXTENSIONS = {".gif", ".mp4", ".webm"}
ASSET_TYPES = {"character", "environment", "ui", "vfx", "audio", "font", "animation", "other"}
ASSET_SOURCES = {"authored", "generated", "licensed", "placeholder"}
LICENSE_STATUSES = {"verified", "pending", "restricted", "not_applicable"}
ASSET_STATUSES = {"planned", "prototype", "approved", "rejected"}
PRESENTATION_BEATS = {"anticipation", "action", "impact", "resolution", "recovery"}
PRESENTATION_CHANNELS = {"animation", "vfx", "camera", "ui", "audio", "haptics", "gameplay"}


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


def validate_presentation_specs(docs_root: Path, require_approved: bool = False) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    manifest_path = docs_root / "ASSET_MANIFEST.json"
    events_path = docs_root / "ANIMATION_EVENTS.json"
    if not manifest_path.is_file() or not events_path.is_file():
        return problems
    try:
        manifest = load_json(manifest_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"invalid_json: {error}"})
        manifest = {}
    try:
        events_spec = load_json(events_path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        problems.append({"kind": "specification", "name": events_path.name, "reason": f"invalid_json: {error}"})
        events_spec = {}

    asset_ids: set[str] = set()
    assets = manifest.get("assets")
    if manifest.get("schema_version") != 1:
        problems.append({"kind": "specification", "name": manifest_path.name, "reason": "schema_version_must_be_1"})
    if not isinstance(assets, list):
        problems.append({"kind": "specification", "name": manifest_path.name, "reason": "assets_must_be_array"})
    elif isinstance(assets, list):
        if not assets:
            problems.append({"kind": "specification", "name": manifest_path.name, "reason": "assets_empty"})
        for index, asset in enumerate(assets):
            label = f"asset[{index}]"
            if not isinstance(asset, dict):
                problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_must_be_object"})
                continue
            asset_id = str(asset.get("id", "")).strip()
            if not asset_id or asset_id in asset_ids:
                problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_id_missing_or_duplicate"})
            else:
                asset_ids.add(asset_id)
            for field in ("runtime_path", "owner", "version", "provenance", "fallback"):
                if not str(asset.get(field, "")).strip():
                    problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_{field}_missing"})
            if asset.get("type") not in ASSET_TYPES:
                problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_type_invalid"})
            if asset.get("source") not in ASSET_SOURCES:
                problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_source_invalid"})
            if asset.get("license_status") not in LICENSE_STATUSES:
                problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_license_status_invalid"})
            if asset.get("status") not in ASSET_STATUSES:
                problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_status_invalid"})
            if asset.get("source") == "placeholder" and asset.get("status") == "approved":
                problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_placeholder_cannot_be_approved"})
            if asset.get("status") == "approved" and asset.get("license_status") not in {"verified", "not_applicable"}:
                problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_approved_license_unresolved"})
            if require_approved and asset.get("source") == "placeholder":
                problems.append({"kind": "specification", "name": manifest_path.name, "reason": f"{label}_placeholder_blocks_delivery"})
        if require_approved and not any(isinstance(asset, dict) and asset.get("status") == "approved" for asset in assets):
            problems.append({"kind": "specification", "name": manifest_path.name, "reason": "approved_asset_missing"})

    event_ids: set[str] = set()
    events = events_spec.get("events")
    if events_spec.get("schema_version") != 1:
        problems.append({"kind": "specification", "name": events_path.name, "reason": "schema_version_must_be_1"})
    if not isinstance(events, list):
        problems.append({"kind": "specification", "name": events_path.name, "reason": "events_must_be_array"})
    elif isinstance(events, list):
        if not events:
            problems.append({"kind": "specification", "name": events_path.name, "reason": "events_empty"})
        for index, event in enumerate(events):
            label = f"event[{index}]"
            if not isinstance(event, dict):
                problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_must_be_object"})
                continue
            event_id = str(event.get("id", "")).strip()
            if not event_id or event_id in event_ids:
                problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_id_missing_or_duplicate"})
            else:
                event_ids.add(event_id)
            for field in (
                "trigger",
                "completion_signal",
                "intensity",
                "input_policy",
                "interruption_policy",
                "recovery_state",
            ):
                if not str(event.get(field, "")).strip():
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_{field}_missing"})
            for field in ("skippable", "reduced_motion"):
                if not isinstance(event.get(field), bool):
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_{field}_must_be_boolean"})
            budget = event.get("performance_budget")
            if not isinstance(budget, dict):
                problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_performance_budget_missing"})
            else:
                if not isinstance(budget.get("max_duration_ms"), int) or budget["max_duration_ms"] <= 0:
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_max_duration_ms_invalid"})
                for field in ("max_simultaneous_particles", "max_audio_voices"):
                    if not isinstance(budget.get(field), int) or budget[field] < 0:
                        problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_{field}_invalid"})
            beats = event.get("beats")
            if not isinstance(beats, list) or not beats:
                problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_beats_missing"})
                continue
            last_start = -1
            max_end = 0
            phases: set[str] = set()
            for beat_index, beat in enumerate(beats):
                beat_label = f"{label}.beat[{beat_index}]"
                if not isinstance(beat, dict):
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{beat_label}_must_be_object"})
                    continue
                if beat.get("phase") not in PRESENTATION_BEATS:
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{beat_label}_phase_invalid"})
                else:
                    phases.add(str(beat["phase"]))
                start_ms = beat.get("start_ms")
                duration_ms = beat.get("duration_ms")
                if not isinstance(start_ms, int) or start_ms < 0 or start_ms < last_start:
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{beat_label}_start_ms_invalid"})
                else:
                    last_start = start_ms
                if not isinstance(duration_ms, int) or duration_ms <= 0:
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{beat_label}_duration_ms_invalid"})
                elif isinstance(start_ms, int) and start_ms >= 0:
                    max_end = max(max_end, start_ms + duration_ms)
                channels = beat.get("channels")
                if not isinstance(channels, list) or not channels or any(channel not in PRESENTATION_CHANNELS for channel in channels):
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{beat_label}_channels_invalid"})
                references = beat.get("asset_ids", [])
                if not isinstance(references, list):
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{beat_label}_asset_ids_must_be_array"})
                elif asset_ids:
                    unknown = [reference for reference in references if reference not in asset_ids]
                    if unknown:
                        problems.append({"kind": "specification", "name": events_path.name, "reason": f"{beat_label}_unknown_assets"})
                if not str(beat.get("completion_marker", "")).strip():
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{beat_label}_completion_marker_missing"})
            if "recovery" not in phases:
                problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_recovery_beat_missing"})
            if isinstance(budget, dict) and isinstance(budget.get("max_duration_ms"), int):
                if max_end > budget["max_duration_ms"]:
                    problems.append({"kind": "specification", "name": events_path.name, "reason": f"{label}_duration_exceeds_budget"})
    return problems


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
    if phase.get("requires_still_capture"):
        still_captures = [
            path
            for path in evidence_root.rglob("*")
            if path.is_file() and path.suffix.lower() in STILL_CAPTURE_EXTENSIONS
        ] if evidence_root.is_dir() else []
        if not still_captures:
            problems.append({"kind": "evidence", "name": "still-capture", "reason": "missing"})
    if phase.get("requires_motion_capture"):
        motion_captures = [
            path
            for path in evidence_root.rglob("*")
            if path.is_file() and path.suffix.lower() in MOTION_CAPTURE_EXTENSIONS
        ] if evidence_root.is_dir() else []
        if not motion_captures:
            problems.append({"kind": "evidence", "name": "motion-capture", "reason": "missing"})
    if phase.get("requires_presentation_specs"):
        required_specs = ("ASSET_MANIFEST.json", "ANIMATION_EVENTS.json")
        if all(is_substantive_document(docs_root / name)[0] for name in required_specs):
            problems.extend(
                validate_presentation_specs(
                    docs_root,
                    require_approved=phase_id in {"phase-03-first-playable", "phase-04-vertical-slice"},
                )
            )
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
