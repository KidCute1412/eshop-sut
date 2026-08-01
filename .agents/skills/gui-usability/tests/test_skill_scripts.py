from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from _table_utils import render_table  # noqa: E402

CREATE_CHECKLIST = SCRIPTS / "create_checklist_workspace.py"
CREATE_USABILITY = SCRIPTS / "create_usability_workspace.py"
VALIDATE_CHECKLIST = SCRIPTS / "validate_checklist.py"
VALIDATE_SESSION = SCRIPTS / "validate_usability_session.py"
COMPUTE_SUS = SCRIPTS / "compute_sus_score.py"
CHECKLIST_TO_CSV = SCRIPTS / "checklist_to_csv.py"
AUDIT = SCRIPTS / "append_ai_audit.py"

CHECKLIST_HEADER = [
    "No.", "Type", "Checkpoint", "IA", "Requirement / Heuristic Reference",
    "Platform", "Source", "AI-Miss Reason", "Yes", "No", "Remarks", "Evidence", "Bug ID",
]

PARTICIPANT_HEADER = [
    "#", "Name", "Contact (Zalo/Email/Phone, masked)", "Profile Notes",
    "Confirmed Outside Class", "Session Date", "Session Type", "Consent to Record",
]


def run(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(script), *args], text=True, capture_output=True, check=False)


def make_item_row(no: str, ia: str = "IA-01", source: str = "Template-Provided",
                   ai_miss_reason: str = "N/A", yes: str = "", no_mark: str = "",
                   remarks: str = "", evidence: str = "", requirement: str = "README.md FR-21") -> dict[str, str]:
    return {
        "No.": no,
        "Type": "Item",
        "Checkpoint": f"Checkpoint for {no}",
        "IA": ia,
        "Requirement / Heuristic Reference": requirement,
        "Platform": "Baseline",
        "Source": source,
        "AI-Miss Reason": ai_miss_reason,
        "Yes": yes,
        "No": no_mark,
        "Remarks": remarks,
        "Evidence": evidence,
        "Bug ID": "",
    }


def make_section_row(no: str, ia: str = "IA-01") -> dict[str, str]:
    return {
        "No.": no,
        "Type": "Section",
        "Checkpoint": f"Section {no}",
        "IA": ia,
        "Requirement / Heuristic Reference": "N/A",
        "Platform": "N/A",
        "Source": "Template-Provided",
        "AI-Miss Reason": "N/A",
        "Yes": "",
        "No": "",
        "Remarks": "",
        "Evidence": "",
        "Bug ID": "",
    }


def build_valid_checklist(count: int = 41) -> str:
    ia_cycle = ["IA-01", "IA-02", "IA-03", "IA-04"]
    rows = [make_section_row("9", "Mixed")]
    for i in range(count):
        ia = ia_cycle[i % 4]
        rows.append(make_item_row(f"9.{i + 1}", ia=ia))
    table = render_table(CHECKLIST_HEADER, rows)
    return f"# GUI Checklist - GUI-01 Home\n\n{table}\n"


def build_valid_participants() -> str:
    rows = []
    rows.append({
        "#": "1", "Name": "Nguyen Van Pilot", "Contact (Zalo/Email/Phone, masked)": "090****678",
        "Profile Notes": "Pilot", "Confirmed Outside Class": "Yes", "Session Date": "2026-07-20",
        "Session Type": "Pilot", "Consent to Record": "Yes",
    })
    for i in range(1, 8):
        rows.append({
            "#": str(i + 1), "Name": f"Participant {i}",
            "Contact (Zalo/Email/Phone, masked)": f"091****00{i}",
            "Profile Notes": "Non-IT", "Confirmed Outside Class": "Yes",
            "Session Date": "2026-07-21", "Session Type": "Real Session", "Consent to Record": "Yes",
        })
    table = render_table(PARTICIPANT_HEADER, rows)
    return f"# Usability Evaluation Participants\n\n{table}\n"


def build_valid_session(session_id: str) -> str:
    sus_rows = [{"#": str(i), "Statement": f"Statement {i}", "Score (1-5)": "3"} for i in range(1, 11)]
    sus_table = render_table(["#", "Statement", "Score (1-5)"], sus_rows)
    obs_rows = [{"Timestamp": "00:01:00", "Observation (friction, error, hesitation, verbalized frustration/quote)": "Hesitated at coupon field", "Screen/Step": "Checkout"}]
    obs_table = render_table(
        ["Timestamp", "Observation (friction, error, hesitation, verbalized frustration/quote)", "Screen/Step"],
        obs_rows,
    )
    return f"""# Usability Session Notes - {session_id}

- Session ID: {session_id}
- Date and Time: 2026-07-21 10:00
- Environment: Windows 11, Chrome
- Completed: Yes

## Observation Log

{obs_table}

## SUS Responses

{sus_table}

## Probe Question Answers

- Clarity: It was clear
- Error recovery: Recovered fine
- Speed: Reasonably fast
- Trust: Felt confident
"""


class ChecklistScriptsTests(unittest.TestCase):
    def test_help_entry_points(self) -> None:
        for script in (CREATE_CHECKLIST, CREATE_USABILITY, VALIDATE_CHECKLIST, VALIDATE_SESSION, COMPUTE_SUS, CHECKLIST_TO_CSV, AUDIT):
            result = run(script, "--help")
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_create_baseline_checklist_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = run(CREATE_CHECKLIST, "--gui-id", "01", "--gui-name", "Trang chu (Home)", "--output", temp)
            self.assertEqual(result.returncode, 0, result.stderr)
            root = Path(temp) / "gui-checklist"
            self.assertTrue((root / "GUI-01" / "checklist.md").is_file())
            self.assertTrue((root / "ai-gap-analysis.md").is_file())
            self.assertTrue((root / "bug-report.md").is_file())
            self.assertTrue((root / "gui-list.md").is_file())
            self.assertTrue((root / "GUI-01" / "evidence").is_dir())
            gui_list = (root / "gui-list.md").read_text(encoding="utf-8")
            self.assertIn("Trang chu (Home)", gui_list)

            marker = root / "GUI-01" / "checklist.md"
            marker.write_text("preserve me", encoding="utf-8")
            result = run(CREATE_CHECKLIST, "--gui-id", "01", "--gui-name", "Trang chu (Home)", "--output", temp)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(encoding="utf-8"), "preserve me")
            result = run(CREATE_CHECKLIST, "--gui-id", "01", "--gui-name", "Trang chu (Home)", "--output", temp, "--force")
            self.assertEqual(result.returncode, 0)
            self.assertNotEqual(marker.read_text(encoding="utf-8"), "preserve me")

    def test_create_second_screen_appends_to_gui_list(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            run(CREATE_CHECKLIST, "--gui-id", "01", "--gui-name", "Home", "--output", temp)
            result = run(CREATE_CHECKLIST, "--gui-id", "02", "--gui-name", "Cart", "--output", temp)
            self.assertEqual(result.returncode, 0, result.stderr)
            gui_list = (Path(temp) / "gui-checklist" / "gui-list.md").read_text(encoding="utf-8")
            self.assertIn("Home", gui_list)
            self.assertIn("Cart", gui_list)
            self.assertTrue((Path(temp) / "gui-checklist" / "GUI-02" / "checklist.md").is_file())

    def test_create_platform_checklist_seeded_from_baseline(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            baseline = Path(temp) / "checklist.md"
            baseline.write_text(build_valid_checklist(41), encoding="utf-8")
            result = run(CREATE_CHECKLIST, "--gui-id", "01", "--gui-name", "Home", "--output", temp, "--platform", "Firefox", "--seed-from", str(baseline))
            self.assertEqual(result.returncode, 0, result.stderr)
            target = Path(temp) / "cross-platform" / "firefox" / "GUI-01" / "checklist.md"
            self.assertTrue(target.is_file())
            content = target.read_text(encoding="utf-8")
            self.assertIn("Firefox", content)
            validate_result = run(VALIDATE_CHECKLIST, str(target))
            self.assertEqual(validate_result.returncode, 0, validate_result.stdout + validate_result.stderr)

    def test_validate_checklist_accepts_valid_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "checklist.md"
            path.write_text(build_valid_checklist(41), encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_validate_checklist_rejects_too_few_items(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "checklist.md"
            path.write_text(build_valid_checklist(20), encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("more than 40", result.stdout)

    def test_validate_checklist_combined_total_across_two_screens(self) -> None:
        # Neither file alone exceeds 40, but validating them together should
        # pass: the >40 minimum is a combined-checklist total, not per-screen.
        with tempfile.TemporaryDirectory() as temp:
            gui01 = Path(temp) / "gui01.md"
            gui02 = Path(temp) / "gui02.md"
            gui01.write_text(build_valid_checklist(21), encoding="utf-8")
            gui02.write_text(build_valid_checklist(21), encoding="utf-8")
            result_alone = run(VALIDATE_CHECKLIST, str(gui01))
            self.assertNotEqual(result_alone.returncode, 0)
            result_combined = run(VALIDATE_CHECKLIST, str(gui01), str(gui02))
            self.assertEqual(result_combined.returncode, 0, result_combined.stdout + result_combined.stderr)
            self.assertIn("42 total Item row(s)", result_combined.stdout)

    def test_validate_checklist_no_min_items_check_bypasses_combined_total(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "checklist.md"
            path.write_text(build_valid_checklist(20), encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path), "--no-min-items-check")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_validate_checklist_accepts_markdown_link_evidence_pointing_to_real_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            evidence_dir = Path(temp) / "evidence"
            evidence_dir.mkdir()
            (evidence_dir / "9.999.png").write_bytes(b"fake-png")
            ia_cycle = ["IA-01", "IA-02", "IA-03", "IA-04"]
            rows = [make_item_row(f"9.{i}", ia=ia_cycle[i % 4]) for i in range(40)]
            rows.append(make_item_row(
                "9.999", ia="IA-01", no_mark="X", remarks="Broken button",
                evidence="[9.999.png](evidence/9.999.png)",
            ))
            table = render_table(CHECKLIST_HEADER, rows)
            path = Path(temp) / "checklist.md"
            path.write_text(f"# Checklist\n\n{table}\n", encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_validate_checklist_rejects_markdown_link_evidence_pointing_to_missing_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            ia_cycle = ["IA-01", "IA-02", "IA-03", "IA-04"]
            rows = [make_item_row(f"9.{i}", ia=ia_cycle[i % 4]) for i in range(40)]
            rows.append(make_item_row(
                "9.999", ia="IA-01", no_mark="X", remarks="Broken button",
                evidence="[9.999.png](evidence/9.999.png)",
            ))
            table = render_table(CHECKLIST_HEADER, rows)
            path = Path(temp) / "checklist.md"
            path.write_text(f"# Checklist\n\n{table}\n", encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("evidence file does not exist", result.stdout)

    def test_validate_checklist_rejects_missing_ia_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            rows = [make_item_row(f"9.{i}", ia="IA-01") for i in range(1, 42)]
            table = render_table(CHECKLIST_HEADER, rows)
            path = Path(temp) / "checklist.md"
            path.write_text(f"# Checklist\n\n{table}\n", encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("IA-02", result.stdout)

    def test_validate_checklist_requires_ai_miss_reason_for_human_added(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            ia_cycle = ["IA-01", "IA-02", "IA-03", "IA-04"]
            rows = [make_item_row(f"9.{i}", ia=ia_cycle[i % 4]) for i in range(40)]
            rows.append(make_item_row("9.999", ia="IA-01", source="Human-Added", ai_miss_reason=""))
            table = render_table(CHECKLIST_HEADER, rows)
            path = Path(temp) / "checklist.md"
            path.write_text(f"# Checklist\n\n{table}\n", encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("AI-Miss Reason", result.stdout)

    def test_validate_checklist_requires_evidence_when_marked_no(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            ia_cycle = ["IA-01", "IA-02", "IA-03", "IA-04"]
            rows = [make_item_row(f"9.{i}", ia=ia_cycle[i % 4]) for i in range(40)]
            rows.append(make_item_row("9.999", ia="IA-01", no_mark="X", remarks="Broken button", evidence=""))
            table = render_table(CHECKLIST_HEADER, rows)
            path = Path(temp) / "checklist.md"
            path.write_text(f"# Checklist\n\n{table}\n", encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Evidence", result.stdout)

    def test_validate_checklist_accepts_no_with_real_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            evidence_dir = Path(temp) / "evidence"
            evidence_dir.mkdir()
            (evidence_dir / "9.999.png").write_bytes(b"fake")
            ia_cycle = ["IA-01", "IA-02", "IA-03", "IA-04"]
            rows = [make_item_row(f"9.{i}", ia=ia_cycle[i % 4]) for i in range(40)]
            rows.append(make_item_row("9.999", ia="IA-01", no_mark="X", remarks="Broken button", evidence="evidence/9.999.png"))
            table = render_table(CHECKLIST_HEADER, rows)
            path = Path(temp) / "checklist.md"
            path.write_text(f"# Checklist\n\n{table}\n", encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_validate_checklist_rejects_both_yes_and_no_marked(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            ia_cycle = ["IA-01", "IA-02", "IA-03", "IA-04"]
            rows = [make_item_row(f"9.{i}", ia=ia_cycle[i % 4]) for i in range(40)]
            rows.append(make_item_row("9.999", ia="IA-01", yes="X", no_mark="X", remarks="x", evidence="x"))
            table = render_table(CHECKLIST_HEADER, rows)
            path = Path(temp) / "checklist.md"
            path.write_text(f"# Checklist\n\n{table}\n", encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("cannot both be marked", result.stdout)

    def test_validate_checklist_rejects_todo_placeholder_checkpoint(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            ia_cycle = ["IA-01", "IA-02", "IA-03", "IA-04"]
            rows = [make_item_row(f"9.{i}", ia=ia_cycle[i % 4]) for i in range(41)]
            rows[0]["Checkpoint"] = "TODO -- generate via AI"
            table = render_table(CHECKLIST_HEADER, rows)
            path = Path(temp) / "checklist.md"
            path.write_text(f"# Checklist\n\n{table}\n", encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("placeholder", result.stdout)

    def test_validate_checklist_accepts_section_rows_without_execution(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            ia_cycle = ["IA-01", "IA-02", "IA-03", "IA-04"]
            rows = [make_section_row("9")]
            rows += [make_item_row(f"9.{i}", ia=ia_cycle[i % 4]) for i in range(41)]
            table = render_table(CHECKLIST_HEADER, rows)
            path = Path(temp) / "checklist.md"
            path.write_text(f"# Checklist\n\n{table}\n", encoding="utf-8")
            result = run(VALIDATE_CHECKLIST, str(path))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_checklist_to_csv(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "checklist.md"
            path.write_text(build_valid_checklist(41), encoding="utf-8")
            out_csv = Path(temp) / "checklist.csv"
            result = run(CHECKLIST_TO_CSV, "--input", str(path), "--output", str(out_csv))
            self.assertEqual(result.returncode, 0, result.stderr)
            with out_csv.open(newline="", encoding="utf-8-sig") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 42)  # 1 Section row + 41 Item rows
            self.assertEqual(rows[0]["No."], "9")
            self.assertEqual(rows[0]["Type"], "Section")


class UsabilityScriptsTests(unittest.TestCase):
    def test_create_usability_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = run(CREATE_USABILITY, "--flow-name", "Signup to Checkout", "--output", temp)
            self.assertEqual(result.returncode, 0, result.stderr)
            out_dir = Path(temp) / "usability-evaluation"
            self.assertTrue((out_dir / "usability-plan.md").is_file())
            self.assertTrue((out_dir / "participants.md").is_file())
            self.assertTrue((out_dir / "sus-scoring.md").is_file())
            self.assertTrue((out_dir / "findings.md").is_file())
            self.assertTrue((out_dir / "bug-report.md").is_file())
            for session_id in ("PILOT", "P01", "P02", "P03", "P04", "P05", "P06", "P07"):
                self.assertTrue((out_dir / "session-notes" / f"{session_id}.md").is_file())
            self.assertTrue((out_dir / "evidence").is_dir())

    def test_validate_usability_session_accepts_complete_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "participants.md").write_text(build_valid_participants(), encoding="utf-8")
            session_dir = root / "session-notes"
            session_dir.mkdir()
            for session_id in ("P01", "P02", "P03", "P04", "P05", "P06", "P07"):
                (session_dir / f"{session_id}.md").write_text(build_valid_session(session_id), encoding="utf-8")
            result = run(VALIDATE_SESSION, str(root))
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_validate_usability_session_rejects_unmasked_phone(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            bad_participants = build_valid_participants().replace("091****001", "0911234001")
            (root / "participants.md").write_text(bad_participants, encoding="utf-8")
            session_dir = root / "session-notes"
            session_dir.mkdir()
            for session_id in ("P01", "P02", "P03", "P04", "P05", "P06", "P07"):
                (session_dir / f"{session_id}.md").write_text(build_valid_session(session_id), encoding="utf-8")
            result = run(VALIDATE_SESSION, str(root))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("mask", result.stdout)

    def test_validate_usability_session_rejects_missing_probe_answer(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "participants.md").write_text(build_valid_participants(), encoding="utf-8")
            session_dir = root / "session-notes"
            session_dir.mkdir()
            for session_id in ("P01", "P02", "P03", "P04", "P05", "P06", "P07"):
                content = build_valid_session(session_id)
                if session_id == "P01":
                    content = content.replace("- Trust: Felt confident", "- Trust: TODO")
                (session_dir / f"{session_id}.md").write_text(content, encoding="utf-8")
            result = run(VALIDATE_SESSION, str(root))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Trust", result.stdout)

    def test_compute_sus_score(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            csv_path = Path(temp) / "scores.csv"
            with csv_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["Participant"] + [f"Q{i}" for i in range(1, 11)])
                for i in range(1, 8):
                    writer.writerow([f"P0{i}"] + ["3"] * 10)
            result = run(COMPUTE_SUS, "--input", str(csv_path))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("SUS = 50.0", result.stdout)
            self.assertIn("Mean SUS across 7 participant(s): 50.0", result.stdout)

    def test_compute_sus_score_rejects_wrong_participant_count(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            csv_path = Path(temp) / "scores.csv"
            with csv_path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(["Participant"] + [f"Q{i}" for i in range(1, 11)])
                writer.writerow(["P01"] + ["3"] * 10)
            result = run(COMPUTE_SUS, "--input", str(csv_path))
            self.assertNotEqual(result.returncode, 0)
            result_bypass = run(COMPUTE_SUS, "--input", str(csv_path), "--allow-any-count")
            self.assertEqual(result_bypass.returncode, 0)


class AuditScriptTests(unittest.TestCase):
    def test_ai_audit_appends_and_validates_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            prompt = root / "prompt.txt"
            output = root / "result.md"
            audit = root / "audit.md"
            prompt.write_text("line one\nline two\n", encoding="utf-8")
            output.write_text("AI output", encoding="utf-8")
            args = (
                "--audit-file", str(audit), "--ai-tool", "Claude", "--task-id", "TASK1-CHECKLIST",
                "--task", "Generate initial GUI checklist", "--prompt-file", str(prompt),
                "--output-refs", str(output), "--human-review", "Reviewed", "--human-corrections", "Added 5 items",
            )
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
