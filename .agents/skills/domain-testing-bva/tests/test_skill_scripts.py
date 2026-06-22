from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CREATE = ROOT / "scripts" / "create_feature_workspace.py"
VALIDATE = ROOT / "scripts" / "validate_test_cases.py"
AUDIT = ROOT / "scripts" / "append_ai_audit.py"


def run(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True, check=False)


def case(case_id: str, technique: str, coverage: str, *, status: str = "Not Executed",
         actual: str = "Not Executed", evidence: str = "None", extra: str = "") -> str:
    return f"""## {case_id}

- Test Case ID: {case_id}
- Technique: {technique}
- Objective: Verify documented input classification
- Requirement or Rule Reference: RULE-01
- Preconditions: Public interface is available
- Test Data: representative-value-{case_id}
- Steps: Submit the representative value through the public interface
- Expected Result: The documented response is observable
- Actual Result: {actual}
- Status: {status}
- Evidence: {evidence}
- Partition or Boundary Covered: {coverage}
- Test Basis Reference: README.md RULE-01
- Notes and Assumptions: No assumptions
{extra}
"""


class SkillScriptsTests(unittest.TestCase):
    def test_help_and_python_entry_points(self) -> None:
        for script in (CREATE, VALIDATE, AUDIT):
            result = run(script, "--help")
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_workspace_supports_fr_and_mobile_and_preserves_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            for feature, pool in (("FR-01", "A"), ("D-01", "D")):
                result = run(CREATE, "--feature-id", feature, "--feature-name", "Feature", "--pool", pool, "--output", temp)
                self.assertEqual(result.returncode, 0, result.stderr)
                workspace = Path(temp) / feature
                self.assertTrue((workspace / "execution-summary.md").is_file())
                self.assertTrue((workspace / "bug-report.md").is_file())
                self.assertTrue((workspace / "evidence" / "evidence-index.md").is_file())
            marker = Path(temp) / "FR-01" / "test-cases.md"
            marker.write_text("preserve me", encoding="utf-8")
            result = run(CREATE, "--feature-id", "FR-01", "--feature-name", "Feature", "--pool", "A", "--output", temp)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(encoding="utf-8"), "preserve me")
            result = run(CREATE, "--feature-id", "FR-01", "--feature-name", "Feature", "--pool", "A", "--output", temp, "--force")
            self.assertEqual(result.returncode, 0)
            self.assertNotEqual(marker.read_text(encoding="utf-8"), "preserve me")

    def test_workspace_rejects_invalid_input(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            for feature, name, pool in (("X-01", "Feature", "A"), ("FR-1", "Feature", "A"), ("FR-01", " ", "A"), ("FR-01", "Feature", "Z")):
                result = run(CREATE, "--feature-id", feature, "--feature-name", name, "--pool", pool, "--output", temp)
                self.assertNotEqual(result.returncode, 0)

    def test_missing_template_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            copied = Path(temp) / "skill"
            (copied / "scripts").mkdir(parents=True)
            (copied / "assets").mkdir()
            (copied / "scripts" / CREATE.name).write_text(CREATE.read_text(encoding="utf-8"), encoding="utf-8")
            for asset in (ROOT / "assets").iterdir():
                if asset.name != "bug-report-template.md" and asset.is_file():
                    (copied / "assets" / asset.name).write_text(asset.read_text(encoding="utf-8"), encoding="utf-8")
            output = Path(temp) / "output"
            result = run(copied / "scripts" / CREATE.name, "--feature-id", "FR-01", "--feature-name", "Feature", "--pool", "A", "--output", str(output))
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())

    def test_validator_valid_fr_and_mobile(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            for feature, compact in (("FR-01", "FR01"), ("D-01", "D01")):
                folder = Path(temp) / feature
                folder.mkdir()
                content = case(f"{compact}-DT-001", "Domain Testing", "PARTITION-P01")
                content += "\n" + case(f"{compact}-BVA-001", "Boundary Value Analysis", "BOUNDARY-B01")
                target = folder / "test-cases.md"
                target.write_text(content, encoding="utf-8")
                before = target.read_bytes()
                result = run(VALIDATE, str(folder))
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(target.read_bytes(), before, "validator must not modify reports")

    def test_validator_failure_modes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.assertNotEqual(run(VALIDATE, str(root)).returncode, 0)  # zero files
            folder = root / "FR-01"
            folder.mkdir()
            target = folder / "test-cases.md"
            target.write_text("# no cases", encoding="utf-8")
            self.assertNotEqual(run(VALIDATE, str(folder)).returncode, 0)  # zero parsed

            valid = case("FR01-DT-001", "Domain Testing", "PARTITION-P01")
            variants = {
                "duplicate": valid + "\n" + valid,
                "missing field": valid.replace("- Test Basis Reference: README.md RULE-01\n", ""),
                "Pass without evidence": valid.replace("- Status: Not Executed", "- Status: Pass").replace("- Actual Result: Not Executed", "- Actual Result: observed"),
                "Blocked without reason": valid.replace("- Status: Not Executed", "- Status: Blocked").replace("- Actual Result: Not Executed", "- Actual Result: blocked"),
                "Not Executed with evidence": valid.replace("- Evidence: None", "- Evidence: evidence/file.png"),
                "wrong feature": valid.replace("FR01-DT-001", "D01-DT-001"),
            }
            for label, content in variants.items():
                with self.subTest(label=label):
                    target.write_text(content, encoding="utf-8")
                    self.assertNotEqual(run(VALIDATE, str(folder)).returncode, 0)

    def test_ai_audit_appends_and_validates_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            prompt = root / "prompt.txt"
            output = root / "result.md"
            audit = root / "audit.md"
            prompt.write_text("line one\nline two\n", encoding="utf-8")
            output.write_text("AI output", encoding="utf-8")
            args = ("--audit-file", str(audit), "--ai-tool", "Codex", "--task", "Design",
                    "--feature-id", "D-01", "--prompt-file", str(prompt), "--output-refs", str(output),
                    "--human-review", "Reviewed", "--human-corrections", "Added one case")
            self.assertEqual(run(AUDIT, *args).returncode, 0)
            first = audit.read_text(encoding="utf-8")
            self.assertIn("line one\nline two\n", first)
            self.assertEqual(run(AUDIT, *args).returncode, 0)
            second = audit.read_text(encoding="utf-8")
            self.assertTrue(second.startswith(first))
            bad_args = list(args)
            bad_args[bad_args.index(str(output))] = str(root / "missing.md")
            self.assertNotEqual(run(AUDIT, *bad_args).returncode, 0)


if __name__ == "__main__":
    unittest.main()
