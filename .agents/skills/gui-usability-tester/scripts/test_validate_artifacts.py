from __future__ import annotations

import contextlib
import csv
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("validate_artifacts.py")
SPEC = importlib.util.spec_from_file_location("validate_artifacts", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)

HEADERS = list(VALIDATOR.ALIASES)
VALID_ROW = {
    "check_id": "CHK-1", "requirement_id": "REQ-1", "interface_aspect": "Navigation",
    "screen": "Cart", "precondition": "Item exists", "action": "Open cart",
    "expected_result": "Cart opens", "actual_result": "Cart opened", "status": "Pass",
    "environment": "Chrome / Windows", "evidence_ref": "", "defect_id": "N/A",
    "origin": "AI", "notes": "None",
}


class ValidatorTests(unittest.TestCase):
    def run_fixture(self, headers: list[str], row: list[str]) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "checklist").mkdir()
            (root / "bugs").mkdir()
            with (root / "checklist" / "gui_checklist.csv").open("w", encoding="utf-8", newline="") as handle:
                writer = csv.writer(handle)
                writer.writerow(headers)
                writer.writerow(row)
            (root / "bugs" / "bug_report.md").write_text("# Defects\n", encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = VALIDATOR.main(str(root))
            return result, output.getvalue()

    def test_valid_contract_passes(self) -> None:
        result, output = self.run_fixture(HEADERS, [VALID_ROW[name] for name in HEADERS])
        self.assertEqual(0, result)
        self.assertIn("VALIDATION PASSED", output)

    def test_every_contract_column_is_required(self) -> None:
        for omitted in HEADERS:
            with self.subTest(omitted=omitted):
                headers = [name for name in HEADERS if name != omitted]
                result, output = self.run_fixture(headers, [VALID_ROW[name] for name in headers])
                self.assertEqual(1, result)
                self.assertIn(omitted, output)

    def test_short_row_reports_error_instead_of_crashing(self) -> None:
        result, output = self.run_fixture(HEADERS, [VALID_ROW[name] for name in HEADERS[:3]])
        self.assertEqual(1, result)
        self.assertIn("fewer values than the header", output)

    def test_extra_value_reports_row_error(self) -> None:
        row = [VALID_ROW[name] for name in HEADERS] + ["unexpected"]
        result, output = self.run_fixture(HEADERS, row)
        self.assertEqual(1, result)
        self.assertIn("extra value", output)


if __name__ == "__main__":
    unittest.main()
