#!/usr/bin/env python3
"""Validate a data-driven Playwright suite and optional JSON reports."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


CONFIG_NAMES = (
    "playwright.config.ts",
    "playwright.config.js",
    "playwright.config.mts",
    "playwright.config.mjs",
    "playwright.config.cts",
    "playwright.config.cjs",
)
DATA_DIR_NAMES = {"test-data", "testdata", "data", "fixtures"}
CASE_ID_KEYS = ("caseId", "case_id", "testCaseId", "test_case_id", "id")
PROJECT_RE = re.compile(r"\bname\s*:\s*['\"]([^'\"]+)['\"]")
FIXED_WAIT_RE = re.compile(r"\.waitForTimeout\s*\(")
DATA_LOAD_RE = re.compile(
    r"\breadFile(?:Sync)?\s*\(|\bcreateReadStream\s*\(|"
    r"\bloadCases(?:\s*<[^;()]+>)?\s*\(|"
    r"\bfrom\s+['\"][^'\"]+\.(?:json|csv)['\"]|"
    r"\brequire\s*\(\s*['\"][^'\"]+\.(?:json|csv)['\"]"
)
EXPECT_RE = re.compile(r"\bexpect(?:\.(?:soft|poll))?\s*\(")
ISO_START_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


@dataclass
class Audit:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    facts: dict[str, Any] = field(default_factory=dict)

    def require(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)


def find_config(root: Path) -> Path | None:
    return next((root / name for name in CONFIG_NAMES if (root / name).is_file()), None)


def extract_projects(config_text: str) -> list[str]:
    # Project names are conventionally object `name` fields. Preserve order and
    # remove duplicates so diagnostics remain deterministic.
    return list(dict.fromkeys(PROJECT_RE.findall(config_text)))


def records_from_json(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(payload, dict):
        payload = payload.get("cases", [payload])
    if not isinstance(payload, list) or not all(isinstance(item, dict) for item in payload):
        raise ValueError("expected an object, an array of objects, or an object with a cases array")
    return payload


def records_from_csv(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def case_id(record: dict[str, Any]) -> str | None:
    for key in CASE_ID_KEYS:
        value = record.get(key)
        if isinstance(value, (str, int)) and str(value).strip():
            return str(value).strip()
    return None


def discover_data_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".json", ".csv"}:
            relative_parts = {part.lower() for part in path.relative_to(root).parts[:-1]}
            if relative_parts & DATA_DIR_NAMES:
                files.append(path)
    return sorted(files)


def discover_specs(root: Path) -> list[Path]:
    valid_suffixes = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".mts", ".cts"}
    return sorted(
        path for path in root.rglob("*.spec.*")
        if path.is_file() and path.suffix.lower() in valid_suffixes
    )


def audit_suite(root: Path, expected_projects: list[str], minimum_projects: int) -> Audit:
    audit = Audit()
    audit.require(root.is_dir(), f"suite root is not a directory: {root}")
    if not root.is_dir():
        return audit

    package_path = root / "package.json"
    audit.require(package_path.is_file(), "package.json is missing")
    if package_path.is_file():
        try:
            package = json.loads(package_path.read_text(encoding="utf-8-sig"))
            dependencies = {**package.get("dependencies", {}), **package.get("devDependencies", {})}
            audit.require("@playwright/test" in dependencies, "package.json does not declare @playwright/test")
        except (json.JSONDecodeError, TypeError) as exc:
            audit.errors.append(f"invalid package.json: {exc}")

    config_path = find_config(root)
    audit.require(config_path is not None, "Playwright config is missing")
    projects: list[str] = []
    if config_path:
        config_text = config_path.read_text(encoding="utf-8-sig")
        projects = extract_projects(config_text)
        audit.require(len(projects) >= minimum_projects,
                      f"found {len(projects)} named projects; require at least {minimum_projects}")
        for project in expected_projects:
            audit.require(project in projects, f"expected project is not declared: {project}")
        audit.require("html" in config_text.lower(), "config does not appear to enable an HTML reporter")

    specs = discover_specs(root)
    audit.require(bool(specs), "no Playwright *.spec.* files found")
    bound_specs = 0
    assertion_specs = 0
    for spec in specs:
        source = spec.read_text(encoding="utf-8-sig")
        if DATA_LOAD_RE.search(source):
            bound_specs += 1
        else:
            audit.errors.append(f"spec has no detectable runtime JSON/CSV load: {spec.relative_to(root)}")
        if EXPECT_RE.search(source):
            assertion_specs += 1
        else:
            audit.errors.append(f"spec has no detectable Playwright assertion: {spec.relative_to(root)}")
        if FIXED_WAIT_RE.search(source):
            audit.errors.append(f"spec uses fixed waitForTimeout: {spec.relative_to(root)}")

    data_files = discover_data_files(root)
    audit.require(bool(data_files), "no JSON or CSV files found in a data/fixture directory")
    ids: list[str] = []
    for path in data_files:
        try:
            records = records_from_json(path) if path.suffix.lower() == ".json" else records_from_csv(path)
            audit.require(bool(records), f"data file is empty: {path.relative_to(root)}")
            for index, record in enumerate(records, start=1):
                identifier = case_id(record)
                audit.require(identifier is not None,
                              f"data record lacks a supported case ID at {path.relative_to(root)} row {index}")
                if identifier:
                    ids.append(identifier)
        except (OSError, UnicodeError, json.JSONDecodeError, csv.Error, ValueError) as exc:
            audit.errors.append(f"cannot parse data file {path.relative_to(root)}: {exc}")

    duplicates = sorted({identifier for identifier in ids if ids.count(identifier) > 1})
    audit.require(not duplicates, f"duplicate case IDs: {', '.join(duplicates)}")
    audit.facts.update({
        "suite_root": str(root.resolve()),
        "config": str(config_path.relative_to(root)) if config_path else None,
        "projects": projects,
        "spec_count": len(specs),
        "data_bound_spec_count": bound_specs,
        "assertion_spec_count": assertion_specs,
        "data_file_count": len(data_files),
        "case_ids": sorted(ids),
    })
    return audit


def iter_report_tests(node: Any, titles: tuple[str, ...] = ()) -> Iterable[tuple[str, str, str]]:
    if isinstance(node, dict):
        title = node.get("title")
        next_titles = titles + ((title,) if isinstance(title, str) and title else ())
        project = node.get("projectName")
        if isinstance(project, str):
            status = node.get("status") or node.get("expectedStatus") or "unknown"
            yield (" > ".join(next_titles), project, str(status))
        for key, value in node.items():
            if key != "title":
                yield from iter_report_tests(value, next_titles)
    elif isinstance(node, list):
        for value in node:
            yield from iter_report_tests(value, titles)


def audit_reports(
    paths: list[Path], expected_projects: list[str], case_ids: list[str],
    require_case_matrix: bool, fail_on_unexpected: bool,
) -> Audit:
    audit = Audit()
    observations: list[tuple[str, str, str]] = []
    for path in paths:
        try:
            payload = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            audit.errors.append(f"cannot parse report {path}: {exc}")
            continue
        audit.require(isinstance(payload, dict) and isinstance(payload.get("stats"), dict),
                      f"report lacks Playwright stats: {path}")
        start_time = payload.get("stats", {}).get("startTime") if isinstance(payload, dict) else None
        audit.require(isinstance(start_time, str) and bool(ISO_START_RE.match(start_time)),
                      f"report lacks an ISO-like stats.startTime: {path}")
        observations.extend(iter_report_tests(payload))

    observed_projects = sorted({project for _, project, _ in observations})
    for project in expected_projects:
        audit.require(project in observed_projects, f"no report result found for expected project: {project}")

    missing_cells: list[str] = []
    if require_case_matrix:
        for identifier in case_ids:
            for project in expected_projects:
                if not any(identifier in title and project == observed for title, observed, _ in observations):
                    missing_cells.append(f"{identifier}@{project}")
        audit.require(not missing_cells, f"missing case/project report cells: {', '.join(missing_cells)}")

    bad_statuses = sorted({status for _, _, status in observations
                           if status in {"unexpected", "flaky", "skipped", "failed", "timedOut", "interrupted"}})
    if fail_on_unexpected:
        audit.require(not bad_statuses, f"non-clean report statuses: {', '.join(bad_statuses)}")
    elif bad_statuses:
        audit.warnings.append(f"report contains non-clean statuses: {', '.join(bad_statuses)}")

    audit.facts.update({
        "report_count": len(paths),
        "reported_test_entries": len(observations),
        "reported_projects": observed_projects,
        "missing_case_project_cells": missing_cells,
        "non_clean_statuses": bad_statuses,
    })
    return audit


def merge(target: Audit, source: Audit) -> None:
    target.errors.extend(source.errors)
    target.warnings.extend(source.warnings)
    target.facts.update(source.facts)


def run_self_test() -> int:
    config = "projects: [{ name: 'chromium' }, { name: 'firefox' }, { name: 'webkit' }]"
    assert extract_projects(config) == ["chromium", "firefox", "webkit"]
    assert case_id({"testCaseId": "CASE-1"}) == "CASE-1"
    report = {
        "suites": [{"title": "feature", "specs": [{"title": "CASE-1: works", "tests": [
            {"projectName": "chromium", "status": "expected"}
        ]}]}]
    }
    assert list(iter_report_tests(report)) == [("feature > CASE-1: works", "chromium", "expected")]
    print("Self-test passed: project extraction, case IDs, and report traversal")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite-root", type=Path, default=Path("."))
    parser.add_argument("--expected-project", action="append", default=[])
    parser.add_argument("--minimum-projects", type=int, default=3)
    parser.add_argument("--report", action="append", type=Path, default=[])
    parser.add_argument("--require-case-matrix", action="store_true")
    parser.add_argument("--fail-on-unexpected", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--self-test", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test:
        return run_self_test()
    if args.minimum_projects < 1:
        print("--minimum-projects must be at least 1", file=sys.stderr)
        return 2
    result = audit_suite(args.suite_root, args.expected_project, args.minimum_projects)
    if args.report:
        report_audit = audit_reports(
            args.report,
            args.expected_project or result.facts.get("projects", []),
            result.facts.get("case_ids", []),
            args.require_case_matrix,
            args.fail_on_unexpected,
        )
        merge(result, report_audit)
    elif args.require_case_matrix or args.fail_on_unexpected:
        result.errors.append("report-dependent option used without --report")

    payload = {"ok": not result.errors, "errors": result.errors,
               "warnings": result.warnings, "facts": result.facts}
    if args.as_json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        for message in result.errors:
            print(f"[ERROR] {message}")
        for message in result.warnings:
            print(f"[WARN] {message}")
        print(json.dumps(result.facts, indent=2, sort_keys=True))
        print("Validation passed" if not result.errors else "Validation failed")
    return 0 if not result.errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
