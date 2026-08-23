#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


REQUIRED_DOCS = [
    "README.md",
    "main-report.md",
    "ai-audit.md",
    "ai-critique.md",
    "bug-report.md",
    "ci-cd-report.md",
    "generator-design.md",
    "git-commit-log.txt",
]


def fail(message):
    print(f"ERROR: {message}")
    return 1


def read_text(path):
    return path.read_text(encoding="utf-8", errors="ignore")


def count_rows_with_prefix(text, prefix):
    return len(re.findall(rf"\|\s*{re.escape(prefix)}[-A-Z0-9]*-API-\d+\s*\|", text))


def main():
    if len(sys.argv) != 2:
        return fail("usage: validate_hw6_workspace.py <reports/HW6>")

    root = Path(sys.argv[1])
    if not root.exists():
        return fail(f"workspace does not exist: {root}")

    errors = []
    for name in REQUIRED_DOCS:
        if not (root / name).exists():
            errors.append(f"missing required document: {name}")

    api_dirs = [p for p in root.iterdir() if p.is_dir() and re.match(r"^(FR-\d{2}|API-\d+|[A-Za-z0-9_-]+)$", p.name)]
    api_dirs = [p for p in api_dirs if (p / "test-cases.md").exists()]
    if len(api_dirs) < 3:
        errors.append("expected at least 3 API workspaces with test-cases.md")

    for api_dir in api_dirs:
        test_file = api_dir / "test-cases.md"
        text = read_text(test_file)
        case_rows = len(re.findall(r"\|\s*[^|\s]+-API-\d+\s*\|", text))
        if case_rows < 40:
            errors.append(f"{test_file} has {case_rows} case rows; expected at least 40 including human-added cases")
        for label in ["VALID", "INVALID", "INCOMPLETE"]:
            if label not in text:
                errors.append(f"{test_file} missing AI review label: {label}")
        human_added = len(re.findall(r"\|\s*Human-Added\s*\|", text))
        if human_added < 5:
            errors.append(f"{test_file} has {human_added} Human-Added rows; expected at least 5")
        if "Not Executed" in text and "newman" in read_text(root / "main-report.md") if (root / "main-report.md").exists() else False:
            errors.append(f"{test_file} still contains Not Executed while main report appears to claim Newman execution")

    postman_dir = root / "postman"
    collection_files = list(postman_dir.glob("*.json")) if postman_dir.exists() else []
    collection_candidates = []
    for file in collection_files:
        try:
            data = json.loads(read_text(file))
        except json.JSONDecodeError:
            continue
        if "item" in data:
            collection_candidates.append((file, data))
    if not collection_candidates:
        errors.append("missing Postman collection JSON under postman/")
    for file, data in collection_candidates:
        text = json.dumps(data)
        if "X-Student-Id" not in text:
            errors.append(f"{file} does not contain X-Student-Id")
        if "/api/" not in text:
            errors.append(f"{file} does not appear to contain EShop API requests")

    newman_dir = root / "newman"
    if not newman_dir.exists():
        errors.append("missing newman/ directory")
    else:
        if not list(newman_dir.glob("*.html")):
            errors.append("missing Newman HTML report under newman/")
        if not list(newman_dir.glob("*.txt")):
            errors.append("missing Newman CLI output .txt under newman/")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validation passed: {len(api_dirs)} API workspace(s), {len(collection_candidates)} collection(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
