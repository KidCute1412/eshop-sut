#!/usr/bin/env python3
"""Create a complete Task 2 usability-evaluation workspace atomically."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _table_utils import ensure_utf8_stdio

TOP_LEVEL_FILES = {
    "usability-plan.md": "usability-plan-template.md",
    "participants.md": "participant-table-template.md",
    "sus-scoring.md": "sus-scoring-template.md",
    "findings.md": "findings-severity-template.md",
    "bug-report.md": "bug-report-template.md",
}

SESSION_IDS = ("PILOT", "P01", "P02", "P03", "P04", "P05", "P06", "P07")


def non_empty(value: str) -> str:
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("value cannot be empty")
    return value


def render(text: str, flow_name: str, session_id: str = "") -> str:
    return text.replace("{{FLOW_NAME}}", flow_name).replace("{{SESSION_ID}}", session_id).replace(
        "{{SOURCE_LABEL}}", f"Usability Evaluation ({flow_name})"
    ).replace("{{SOURCE_COMPACT}}", "USE")


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Create a Task 2 usability-evaluation workspace.")
    parser.add_argument("--flow-name", required=True, type=non_empty, help="The single end-to-end flow selected for Task 2.")
    parser.add_argument("--output", required=True, type=non_empty, help="Output root directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    assets = Path(__file__).resolve().parents[1] / "assets"
    session_template = assets / "session-notes-template.md"

    missing = [str(assets / template) for template in TOP_LEVEL_FILES.values() if not (assets / template).is_file()]
    if not session_template.is_file():
        missing.append(str(session_template))
    if missing:
        print("ERROR: required templates are missing; no output was written:", file=sys.stderr)
        for item in missing:
            print(f"  - {item}", file=sys.stderr)
        return 3

    out_dir = Path(args.output) / "usability-evaluation"
    rendered_top = {
        relative: render((assets / template).read_text(encoding="utf-8"), args.flow_name)
        for relative, template in TOP_LEVEL_FILES.items()
    }
    session_content = session_template.read_text(encoding="utf-8")
    rendered_sessions = {
        f"session-notes/{session_id}.md": render(session_content, args.flow_name, session_id)
        for session_id in SESSION_IDS
    }

    created: list[str] = []
    skipped: list[str] = []
    for relative, content in {**rendered_top, **rendered_sessions}.items():
        target = out_dir / relative
        if target.exists() and not args.force:
            skipped.append(str(target))
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        created.append(str(target))
    (out_dir / "evidence").mkdir(parents=True, exist_ok=True)

    print(f"Workspace: {out_dir}")
    print(f"Created/updated: {len(created)}")
    for item in created:
        print(f"  - {item}")
    print(f"Skipped existing: {len(skipped)}")
    for item in skipped:
        print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
