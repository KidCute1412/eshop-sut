#!/usr/bin/env python3
import csv
import json
import sys
from pathlib import Path


def percentile(values, pct):
    if not values:
        return 0
    idx = max(0, min(len(values) - 1, int((pct / 100) * len(values) + 0.999999) - 1))
    return values[idx]


def main():
    if len(sys.argv) != 2:
        print("usage: summarize_jtl.py <file.jtl>")
        return 1

    path = Path(sys.argv[1])
    rows = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(row)

    elapsed = sorted(int(float(row.get("elapsed", 0) or 0)) for row in rows)
    successes = [str(row.get("success", "")).lower() == "true" for row in rows]
    passed = sum(1 for ok in successes if ok)
    failed = len(rows) - passed
    by_label = {}
    for row in rows:
        label = row.get("label", "(unknown)")
        by_label.setdefault(label, {"samples": 0, "failed": 0, "elapsed": []})
        by_label[label]["samples"] += 1
        by_label[label]["failed"] += 0 if str(row.get("success", "")).lower() == "true" else 1
        by_label[label]["elapsed"].append(int(float(row.get("elapsed", 0) or 0)))

    summary = {
        "file": str(path),
        "samples": len(rows),
        "passed": passed,
        "failed": failed,
        "error_rate_percent": round((failed / len(rows) * 100) if rows else 0, 2),
        "avg_ms": round(sum(elapsed) / len(elapsed), 2) if elapsed else 0,
        "min_ms": elapsed[0] if elapsed else 0,
        "max_ms": elapsed[-1] if elapsed else 0,
        "p90_ms": percentile(elapsed, 90),
        "p95_ms": percentile(elapsed, 95),
        "p99_ms": percentile(elapsed, 99),
        "by_label": {
            label: {
                "samples": data["samples"],
                "failed": data["failed"],
                "avg_ms": round(sum(data["elapsed"]) / len(data["elapsed"]), 2) if data["elapsed"] else 0,
                "p95_ms": percentile(sorted(data["elapsed"]), 95),
            }
            for label, data in by_label.items()
        },
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

