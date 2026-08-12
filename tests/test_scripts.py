from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skill" / "hypergs" / "scripts"


def run_script(name: str, *arguments: str, environment: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPTS / name), *arguments],
        text=True,
        capture_output=True,
        env=environment,
        check=False,
    )


def write_valid_presentation_specs(project: Path) -> tuple[Path, dict[str, object]]:
    docs = project / ".hypergs" / "docs"
    for name in ("MOTION.md", "PRESENTATION_BEATS.md"):
        (docs / name).write_text(f"# {name}\n\nProject-specific presentation content.\n", encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "assets": [
            {
                "id": "vfx.hit.gold",
                "type": "vfx",
                "source": "authored",
                "provenance": "Created in the project source-art pipeline.",
                "license_status": "not_applicable",
                "runtime_path": "assets/vfx/hit-gold.webp",
                "version": "1.0.0",
                "owner": "art_director",
                "status": "approved",
                "fallback": "Use the low-particle impact flash.",
            }
        ],
    }
    events: dict[str, object] = {
        "schema_version": 1,
        "events": [
            {
                "id": "combat.primary-hit",
                "trigger": "combat.hit.resolved",
                "completion_signal": "presentation.combat.primary-hit.complete",
                "intensity": "routine",
                "input_policy": "Movement remains active while attack input waits for recovery.",
                "interruption_policy": "Defeat cancels the event and forces combat.defeated.",
                "skippable": False,
                "reduced_motion": True,
                "recovery_state": "combat.ready",
                "performance_budget": {
                    "max_duration_ms": 300,
                    "max_simultaneous_particles": 24,
                    "max_audio_voices": 2,
                },
                "beats": [
                    {
                        "phase": "impact",
                        "start_ms": 0,
                        "duration_ms": 120,
                        "channels": ["animation", "vfx", "audio"],
                        "asset_ids": ["vfx.hit.gold"],
                        "completion_marker": "impact.complete",
                    },
                    {
                        "phase": "recovery",
                        "start_ms": 120,
                        "duration_ms": 100,
                        "channels": ["animation", "gameplay"],
                        "asset_ids": [],
                        "completion_marker": "recovery.complete",
                    },
                ],
            }
        ],
    }
    (docs / "ASSET_MANIFEST.json").write_text(json.dumps(manifest), encoding="utf-8")
    events_path = docs / "ANIMATION_EVENTS.json"
    events_path.write_text(json.dumps(events), encoding="utf-8")
    return events_path, events


class HyperGSScriptTests(unittest.TestCase):
    def test_configure_studio_supports_defaults_titles_and_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temp = Path(temporary)
            environment = os.environ.copy()
            environment["CODEX_HOME"] = str(temp / "codex")

            initial = run_script("configure_studio.py", "--show", "--project", str(temp), environment=environment)
            self.assertEqual(initial.returncode, 0, initial.stderr)
            self.assertEqual(json.loads(initial.stdout)["source"], "built_in")

            configured = run_script(
                "configure_studio.py",
                "--scope",
                "user",
                "--preset",
                "titles",
                "--set",
                "producer=Adam",
                environment=environment,
            )
            self.assertEqual(configured.returncode, 0, configured.stderr)
            saved = json.loads(configured.stdout)["profile"]
            self.assertEqual(saved["preset"], "custom")
            self.assertEqual(saved["roles"]["producer"]["display_name"], "Adam")
            self.assertEqual(saved["roles"]["game_designer"]["display_name"], "遊戲企劃")

    def test_initialize_detect_validate_and_block_empty_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "game"
            project.mkdir()
            (project / "index.html").write_text("<!doctype html><title>Game</title>", encoding="utf-8")

            detected = run_script("detect_project.py", str(project), "--json")
            self.assertEqual(detected.returncode, 0, detected.stderr)
            self.assertEqual(json.loads(detected.stdout)["engine"], "html5")

            initialized = run_script(
                "init_project.py",
                str(project),
                "--name",
                "Test Game",
                "--target-platform",
                "mobile-web",
            )
            self.assertEqual(initialized.returncode, 0, initialized.stderr)
            state = json.loads((project / ".hypergs" / "state.json").read_text(encoding="utf-8"))
            self.assertEqual(state["engine"], "html5")
            self.assertTrue((project / ".hypergs" / "docs" / "ASSET_MANIFEST.json").is_file())
            self.assertTrue((project / ".hypergs" / "docs" / "ANIMATION_EVENTS.json").is_file())

            validated = run_script("validate_project.py", str(project), "--json")
            self.assertEqual(validated.returncode, 0, validated.stderr)
            self.assertTrue(json.loads(validated.stdout)["valid"])

            blocked = run_script("phase_check.py", str(project), "--json")
            self.assertEqual(blocked.returncode, 1)
            result = json.loads(blocked.stdout)
            self.assertFalse(result["passed"])
            self.assertEqual(result["problems"][0]["reason"], "template_only")

    def test_phase_advances_only_after_gate_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "game"
            project.mkdir()
            initialized = run_script("init_project.py", str(project))
            self.assertEqual(initialized.returncode, 0, initialized.stderr)

            blocked = run_script("phase_advance.py", str(project))
            self.assertEqual(blocked.returncode, 1)

            game_brief = project / ".hypergs" / "docs" / "GAME.md"
            game_brief.write_text("# Game Brief\n\nA bounded and testable game vision.\n", encoding="utf-8")
            advanced = run_script("phase_advance.py", str(project))
            self.assertEqual(advanced.returncode, 0, advanced.stderr)
            result = json.loads(advanced.stdout)
            self.assertEqual(result["to"], "phase-01-concept")

    def test_template_sync_migrates_without_overwriting_existing_docs(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "game"
            project.mkdir()
            initialized = run_script("init_project.py", str(project))
            self.assertEqual(initialized.returncode, 0, initialized.stderr)

            motion_path = project / ".hypergs" / "docs" / "MOTION.md"
            motion_path.unlink()
            art_path = project / ".hypergs" / "docs" / "ART.md"
            art_path.write_text("# Art Direction\n\nUser-authored content.\n", encoding="utf-8")

            check = run_script("sync_project_templates.py", str(project), "--check", "--json")
            self.assertEqual(check.returncode, 1)
            self.assertIn("MOTION.md", json.loads(check.stdout)["missing"])

            synced = run_script("sync_project_templates.py", str(project), "--json")
            self.assertEqual(synced.returncode, 0, synced.stderr)
            self.assertTrue(motion_path.is_file())
            self.assertEqual(art_path.read_text(encoding="utf-8"), "# Art Direction\n\nUser-authored content.\n")

    def test_presentation_validator_rejects_placeholders_and_invalid_events(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "game"
            project.mkdir()
            initialized = run_script("init_project.py", str(project))
            self.assertEqual(initialized.returncode, 0, initialized.stderr)
            events_path, events = write_valid_presentation_specs(project)

            valid = run_script("validate_presentation.py", str(project), "--json")
            self.assertEqual(valid.returncode, 0, valid.stdout)

            manifest_path = project / ".hypergs" / "docs" / "ASSET_MANIFEST.json"
            placeholder_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            placeholder_manifest["assets"][0]["source"] = "placeholder"
            placeholder_manifest["assets"][0]["status"] = "planned"
            placeholder_manifest["assets"][0]["license_status"] = "pending"
            manifest_path.write_text(json.dumps(placeholder_manifest), encoding="utf-8")
            placeholder_blocked = run_script(
                "validate_presentation.py", str(project), "--json", "--require-approved"
            )
            self.assertEqual(placeholder_blocked.returncode, 1)
            placeholder_reasons = [
                problem["reason"] for problem in json.loads(placeholder_blocked.stdout)["problems"]
            ]
            self.assertTrue(any("placeholder_blocks_delivery" in reason for reason in placeholder_reasons))

            events["events"][0]["beats"][0]["start_ms"] = -1  # type: ignore[index]
            events_path.write_text(json.dumps(events), encoding="utf-8")
            invalid = run_script("validate_presentation.py", str(project), "--json")
            self.assertEqual(invalid.returncode, 1)
            reasons = [problem["reason"] for problem in json.loads(invalid.stdout)["problems"]]
            self.assertTrue(any("start_ms_invalid" in reason for reason in reasons))

    def test_first_playable_requires_still_motion_specs_and_pass_reviews(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "game"
            project.mkdir()
            initialized = run_script("init_project.py", str(project), "--phase", "phase-03-first-playable")
            self.assertEqual(initialized.returncode, 0, initialized.stderr)

            for name in ("GDD.md", "TECH.md", "UIUX.md", "ART.md", "VISUAL_BENCHMARK.md", "ROADMAP.md"):
                (project / ".hypergs" / "docs" / name).write_text(
                    f"# {name}\n\nProject-specific acceptance content.\n", encoding="utf-8"
                )
            events_path, events = write_valid_presentation_specs(project)

            evidence = project / ".hypergs" / "evidence" / "phase-03-first-playable"
            evidence.mkdir(parents=True)
            for name in ("build.md", "playtest.md"):
                (evidence / name).write_text(f"# {name}\n\nObserved runtime evidence.\n", encoding="utf-8")
            reviews = (
                "gameplay-review.md",
                "genre-review.md",
                "market-visual-review.md",
                "animation-review.md",
                "motion-presentation-review.md",
                "uiux-review.md",
                "art-review.md",
                "producer-review.md",
            )
            for name in reviews:
                (evidence / name).write_text("# Review\n\nPASS - observed in runtime capture.\n", encoding="utf-8")

            no_capture = run_script("phase_check.py", str(project), "--json")
            self.assertEqual(no_capture.returncode, 1)
            no_capture_names = [problem["name"] for problem in json.loads(no_capture.stdout)["problems"]]
            self.assertIn("runtime-capture", no_capture_names)
            self.assertIn("still-capture", no_capture_names)
            self.assertIn("motion-capture", no_capture_names)

            (evidence / "gameplay.png").write_bytes(b"representative-runtime-capture")
            no_motion = run_script("phase_check.py", str(project), "--json")
            self.assertEqual(no_motion.returncode, 1)
            self.assertIn("motion-capture", [problem["name"] for problem in json.loads(no_motion.stdout)["problems"]])

            (evidence / "gameplay.mp4").write_bytes(b"representative-motion-capture")
            passed = run_script("phase_check.py", str(project), "--json")
            self.assertEqual(passed.returncode, 0, passed.stdout)

            events["events"][0]["beats"][0]["start_ms"] = -1  # type: ignore[index]
            events_path.write_text(json.dumps(events), encoding="utf-8")
            invalid_presentation = run_script("phase_check.py", str(project), "--json")
            self.assertEqual(invalid_presentation.returncode, 1)
            self.assertIn(
                "ANIMATION_EVENTS.json",
                [problem["name"] for problem in json.loads(invalid_presentation.stdout)["problems"]],
            )
            events["events"][0]["beats"][0]["start_ms"] = 0  # type: ignore[index]
            events_path.write_text(json.dumps(events), encoding="utf-8")

            (evidence / "motion-presentation-review.md").write_text(
                "# Motion Presentation Review\n\nFAIL - presentation is a generic tween sequence.\n",
                encoding="utf-8",
            )
            rejected = run_script("phase_check.py", str(project), "--json")
            self.assertEqual(rejected.returncode, 1)
            self.assertIn(
                "motion-presentation-review.md",
                [problem["name"] for problem in json.loads(rejected.stdout)["problems"]],
            )


if __name__ == "__main__":
    unittest.main()
