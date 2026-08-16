#!/usr/bin/env python3
import csv
import re
import sys
from pathlib import Path


REQUIRED_DOCS = [
    "README.md",
    "main-report.md",
    "ai-audit.md",
    "ai-critique.md",
    "bug-report.md",
    "git-commit-log.txt",
]

REQUIRED_CSV_COLUMNS = [
    "email",
    "password",
    "search",
    "product_id",
    "product_name",
    "price",
    "quantity",
    "shipping_address",
]


def fail(message):
    print(f"ERROR: {message}")
    return 1


def main():
    if len(sys.argv) != 2:
        return fail("usage: validate_hw5_workspace.py <reports/HW5>")

    root = Path(sys.argv[1])
    if not root.exists():
        return fail(f"workspace does not exist: {root}")

    errors = []
    for name in REQUIRED_DOCS:
        if not (root / name).exists():
            errors.append(f"missing required document: {name}")

    plans_dir = root / "plans"
    plans = list(plans_dir.glob("*.jmx")) if plans_dir.exists() else []
    pattern = re.compile(r"^\d{8}_(Load|Stress|Spike)_\d{8}\.jmx$")
    by_type = {"Load": 0, "Stress": 0, "Spike": 0}
    for plan in plans:
        match = pattern.match(plan.name)
        if not match:
            errors.append(f"plan filename does not match required convention: {plan.name}")
        else:
            by_type[match.group(1)] += 1
        text = plan.read_text(encoding="utf-8", errors="ignore")
        for required in ["/api/login", "/api/products", "/api/cart", "/api/checkout", "localhost", "3000"]:
            if required not in text:
                errors.append(f"{plan.name} missing expected token: {required}")
        if "CSVDataSet" not in text and ".csv" not in text:
            errors.append(f"{plan.name} does not appear CSV-driven")

    for scenario, count in by_type.items():
        if count == 0:
            errors.append(f"missing {scenario} plan")

    data_dir = root / "data"
    csv_files = list(data_dir.glob("*.csv")) if data_dir.exists() else []
    if not csv_files:
        errors.append("missing CSV data file under data/")
    for csv_file in csv_files:
        with csv_file.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            missing = [col for col in REQUIRED_CSV_COLUMNS if col not in (reader.fieldnames or [])]
            if missing:
                errors.append(f"{csv_file.name} missing columns: {', '.join(missing)}")
            rows = list(reader)
            if not rows:
                errors.append(f"{csv_file.name} has no data rows")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validation passed: {len(plans)} plan(s), {len(csv_files)} CSV file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

