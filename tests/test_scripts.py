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


if __name__ == "__main__":
    unittest.main()
