from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

INIT_WORKSPACE = SCRIPTS / "init_feature_workspace.py"
VALIDATE_DATA = SCRIPTS / "validate_test_data.py"
VALIDATE_HTML = SCRIPTS / "validate_html_report.py"
CHECK_COMMIT_RULE = SCRIPTS / "check_commit_rule.py"
APPEND_AUDIT = SCRIPTS / "append_ai_audit.py"
COMPUTE_SUMMARY = SCRIPTS / "compute_test_summary.py"


def run(script: Path, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args], text=True, capture_output=True, check=False, cwd=cwd,
    )


def run_git(args: list[str], cwd: Path, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=cwd, text=True, capture_output=True, check=False, env=env)


class InitFeatureWorkspaceTests(unittest.TestCase):
    def test_creates_templated_files_and_subdirs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "reports" / "HW4"
            result = run(
                INIT_WORKSPACE,
                "--feature-id", "FR-01",
                "--feature-name", "Account registration",
                "--output", str(out),
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            feature_dir = out / "FR-01"
            for name in ("test-cases.md", "ai-gap-analysis.md", "bug-report.md"):
                self.assertTrue((feature_dir / name).is_file(), name)
            for sub in ("tests", "data", "reports"):
                self.assertTrue((feature_dir / sub).is_dir(), sub)
            text = (feature_dir / "test-cases.md").read_text(encoding="utf-8")
            self.assertIn("FR-01", text)
            self.assertIn("Account registration", text)
            self.assertNotIn("{{FEATURE_ID}}", text)

    def test_skips_existing_without_force(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "reports" / "HW4"
            run(INIT_WORKSPACE, "--feature-id", "FR-07", "--feature-name", "Shopping cart", "--output", str(out))
            marker = out / "FR-07" / "test-cases.md"
            marker.write_text("CUSTOM CONTENT", encoding="utf-8")
            result = run(INIT_WORKSPACE, "--feature-id", "FR-07", "--feature-name", "Shopping cart", "--output", str(out))
            self.assertEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(encoding="utf-8"), "CUSTOM CONTENT")


class ValidateTestDataTests(unittest.TestCase):
    def _make_feature(self, tmp: str) -> Path:
        feature_dir = Path(tmp) / "FR-01"
        (feature_dir / "tests").mkdir(parents=True)
        (feature_dir / "data").mkdir(parents=True)
        return feature_dir

    def test_passes_with_external_data_and_no_inline_literal(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            feature_dir = self._make_feature(tmp)
            (feature_dir / "data" / "cases.json").write_text("[]", encoding="utf-8")
            (feature_dir / "tests" / "register.spec.ts").write_text(
                "import cases from '../data/cases.json';\n"
                "for (const c of cases) { test(c.id, async ({ page }) => {}); }\n",
                encoding="utf-8",
            )
            result = run(VALIDATE_DATA, str(feature_dir))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_fails_when_no_data_file_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            feature_dir = self._make_feature(tmp)
            (feature_dir / "tests" / "register.spec.ts").write_text("test('x', async () => {});\n", encoding="utf-8")
            result = run(VALIDATE_DATA, str(feature_dir))
            self.assertEqual(result.returncode, 1)
            self.assertIn("no external", result.stdout)

    def test_fails_on_hardcoded_inline_array_of_objects(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            feature_dir = self._make_feature(tmp)
            (feature_dir / "data" / "cases.json").write_text("[]", encoding="utf-8")
            (feature_dir / "tests" / "register.spec.ts").write_text(
                "const testCases = [\n"
                "  { name: 'A', email: 'a@test.com' },\n"
                "  { name: 'B', email: 'b@test.com' },\n"
                "];\n"
                "for (const c of testCases) { test(c.name, async () => {}); }\n",
                encoding="utf-8",
            )
            result = run(VALIDATE_DATA, str(feature_dir))
            self.assertEqual(result.returncode, 1)
            self.assertIn("hardcoded inline", result.stdout)


class ValidateHtmlReportTests(unittest.TestCase):
    def test_passes_with_run_by_tag_and_iso_timestamp(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "index.html"
            report.write_text(
                "<html><body><div>Run by: 23127539 - 2026-08-03T09:15:00.123Z</div></body></html>",
                encoding="utf-8",
            )
            result = run(VALIDATE_HTML, str(report), "--student-id", "23127539")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_fails_when_run_by_tag_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "index.html"
            report.write_text("<html><body>No tag here</body></html>", encoding="utf-8")
            result = run(VALIDATE_HTML, str(report))
            self.assertEqual(result.returncode, 1)

    def test_fails_when_student_id_does_not_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "index.html"
            report.write_text(
                "<html><body>Run by: 99999999 - 2026-08-03T09:15:00Z</body></html>", encoding="utf-8",
            )
            result = run(VALIDATE_HTML, str(report), "--student-id", "23127539")
            self.assertEqual(result.returncode, 1)
            self.assertIn("student ID", result.stdout)

    def test_fails_when_timestamp_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "index.html"
            report.write_text("<html><body>Run by: 23127539</body></html>", encoding="utf-8")
            result = run(VALIDATE_HTML, str(report))
            self.assertEqual(result.returncode, 1)
            self.assertIn("timestamp", result.stdout)


class AppendAiAuditTests(unittest.TestCase):
    def test_appends_and_preserves_prior_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            audit_file = Path(tmp) / "ai-audit.md"
            result1 = run(
                APPEND_AUDIT,
                "--audit-file", str(audit_file),
                "--ai-tool", "Claude",
                "--feature-id", "FR-01",
                "--task", "Convert positive cases",
                "--prompt", "Convert these 4 positive registration cases to Playwright specs.",
                "--output-refs", "https://example.com/output-1",
                "--human-review", "Reviewed line by line.",
                "--human-corrections", "Fixed one selector.",
            )
            self.assertEqual(result1.returncode, 0, result1.stderr)
            result2 = run(
                APPEND_AUDIT,
                "--audit-file", str(audit_file),
                "--ai-tool", "Claude",
                "--feature-id", "FR-01",
                "--task", "Convert negative cases",
                "--prompt", "Convert these 3 negative registration cases to Playwright specs.",
                "--output-refs", "https://example.com/output-2",
                "--human-review", "Reviewed line by line.",
                "--human-corrections", "None needed.",
            )
            self.assertEqual(result2.returncode, 0, result2.stderr)
            text = audit_file.read_text(encoding="utf-8")
            self.assertIn("Convert positive cases", text)
            self.assertIn("Convert negative cases", text)
            self.assertEqual(text.count("## AI Interaction"), 2)

    def test_rejects_bad_feature_id(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            audit_file = Path(tmp) / "ai-audit.md"
            result = run(
                APPEND_AUDIT,
                "--audit-file", str(audit_file),
                "--ai-tool", "Claude",
                "--feature-id", "not-a-feature",
                "--task", "x",
                "--prompt", "x",
                "--output-refs", "https://example.com",
                "--human-review", "x",
                "--human-corrections", "x",
            )
            self.assertEqual(result.returncode, 2)


class ComputeTestSummaryTests(unittest.TestCase):
    def test_counts_automated_cases_bugs_and_browser_runs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            feature_dir = Path(tmp) / "FR-01"
            (feature_dir / "reports" / "chromium").mkdir(parents=True)
            (feature_dir / "reports" / "firefox").mkdir(parents=True)

            (feature_dir / "test-cases.md").write_text(
                "| ID | Type | Steps | Data | Expected | Assertions | Automatable | Spec File |\n"
                "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
                "| TC-01 | Positive | s | d | e | a | Yes | x.spec.ts |\n"
                "| TC-02 | Negative | s | d | e | a | Yes | x.spec.ts |\n"
                "| TC-03 | Edge | s | d | e | a | No | |\n"
                "\n## Not Automated\n\n| ID | Reason |\n| --- | --- |\n| TC-03 | needs manual inbox check |\n",
                encoding="utf-8",
            )
            (feature_dir / "bug-report.md").write_text(
                "# Bug Report\n\n## BUG-AUTO-FR-01-001: Something\n\ndetails\n\n"
                "## BUG-AUTO-FR-01-002: Something else\n\ndetails\n",
                encoding="utf-8",
            )
            (feature_dir / "reports" / "chromium" / "results.json").write_text(
                json.dumps({"stats": {"expected": 10, "unexpected": 2, "flaky": 0, "skipped": 0}}),
                encoding="utf-8",
            )
            (feature_dir / "reports" / "firefox" / "results.json").write_text(
                json.dumps({"stats": {"expected": 9, "unexpected": 3, "flaky": 0, "skipped": 0}}),
                encoding="utf-8",
            )

            result = run(COMPUTE_SUMMARY, "--feature-dir", str(feature_dir))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Test cases automated: 2", result.stdout)
            self.assertIn("Bugs confirmed: 2", result.stdout)
            self.assertIn("Browser runs (JSON reports found): 2", result.stdout)
            self.assertIn("Test cases passed: 19", result.stdout)
            self.assertIn("Test cases failed: 5", result.stdout)


class CheckCommitRuleTests(unittest.TestCase):
    def _init_repo(self, path: Path) -> None:
        run_git(["init", "-q"], cwd=path)
        run_git(["config", "user.email", "test@example.com"], cwd=path)
        run_git(["config", "user.name", "Test User"], cwd=path)

    def _commit(self, path: Path, filename: str, date_iso: str) -> None:
        target = path / filename
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(f"// {filename} at {date_iso}\n", encoding="utf-8")
        run_git(["add", filename], cwd=path)
        env = {
            "GIT_AUTHOR_DATE": date_iso,
            "GIT_COMMITTER_DATE": date_iso,
            "GIT_AUTHOR_NAME": "Test User",
            "GIT_AUTHOR_EMAIL": "test@example.com",
            "GIT_COMMITTER_NAME": "Test User",
            "GIT_COMMITTER_EMAIL": "test@example.com",
        }
        import os
        full_env = {**os.environ, **env}
        run_git(["commit", "-q", "-m", f"update {filename}"], cwd=path, env=full_env)

    def test_passes_with_8_spec_commits_over_4_days(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self._init_repo(repo)
            dates = [
                "2026-07-01T10:00:00", "2026-07-01T11:00:00",
                "2026-07-02T10:00:00", "2026-07-02T11:00:00",
                "2026-07-03T10:00:00", "2026-07-03T11:00:00",
                "2026-07-04T10:00:00", "2026-07-04T11:00:00",
            ]
            for i, date in enumerate(dates):
                self._commit(repo, f"tests/fr-01-register.spec.ts", date)
            result = run(CHECK_COMMIT_RULE, str(repo))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Validation passed", result.stdout)

    def test_fails_when_non_spec_commits_dont_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self._init_repo(repo)
            # 8 commits, but only touching README -- none should count.
            for i in range(8):
                self._commit(repo, "README.md", f"2026-07-0{(i % 4) + 1}T10:00:00")
            result = run(CHECK_COMMIT_RULE, str(repo))
            self.assertEqual(result.returncode, 1)
            self.assertIn("Commits touching a test-script file: 0", result.stdout)

    def test_fails_when_fewer_than_4_distinct_days(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            self._init_repo(repo)
            for i in range(8):
                self._commit(repo, f"tests/f{i}.spec.ts", "2026-07-01T10:00:00")
            result = run(CHECK_COMMIT_RULE, str(repo))
            self.assertEqual(result.returncode, 1)
            self.assertIn("expected >= 4 distinct days", result.stdout)


if __name__ == "__main__":
    unittest.main()
