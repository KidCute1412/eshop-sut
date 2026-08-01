#!/usr/bin/env python3
"""Create a Task 1 (baseline) or Task 3 (cross-platform) checklist workspace,
one screen at a time, following the professor's Web GUI checklist Template.xlsx
layout: a shared 'GUI list' index plus one checklist file per GUI ID.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from _table_utils import ensure_utf8_stdio, parse_table, render_table

CHECKLIST_HEADER = [
    "No.", "Type", "Checkpoint", "IA", "Requirement / Heuristic Reference",
    "Platform", "Source", "AI-Miss Reason", "Yes", "No", "Remarks", "Evidence", "Bug ID",
]

GUI_LIST_HEADER = ["ID", "GUI name", "GUI detail", "Remark"]

SHARED_FILES = {
    "ai-gap-analysis.md": "ai-gap-analysis-template.md",
    "bug-report.md": "bug-report-template.md",
}


def non_empty(value: str) -> str:
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("value cannot be empty")
    return value


def render(text: str, gui_id: str, gui_name: str, gui_detail: str, platform: str) -> str:
    return (
        text.replace("{{GUI_ID}}", gui_id)
        .replace("{{GUI_NAME}}", gui_name)
        .replace("{{GUI_DETAIL}}", gui_detail or "N/A")
        .replace("{{PLATFORM}}", platform)
        .replace("{{SOURCE_LABEL}}", "GUI Checklist (All Screens)")
        .replace("{{SOURCE_COMPACT}}", "GUI")
    )


def upsert_gui_list(gui_list_path: Path, assets: Path, gui_id: str, gui_name: str, gui_detail: str) -> None:
    if gui_list_path.is_file():
        text = gui_list_path.read_text(encoding="utf-8")
        rows = parse_table(text, GUI_LIST_HEADER)
        prefix = text.split("| " + " | ".join(GUI_LIST_HEADER) + " |")[0]
    else:
        template = assets / "gui-list-template.md"
        text = template.read_text(encoding="utf-8")
        rows = []
        prefix = text.split("| " + " | ".join(GUI_LIST_HEADER) + " |")[0]

    updated = False
    for row in rows:
        if row.get("ID") == gui_id:
            row["GUI name"] = gui_name
            row["GUI detail"] = gui_detail or row.get("GUI detail", "")
            updated = True
            break
    if not updated:
        rows.append({"ID": gui_id, "GUI name": gui_name, "GUI detail": gui_detail or "", "Remark": ""})

    table = render_table(GUI_LIST_HEADER, rows)
    gui_list_path.parent.mkdir(parents=True, exist_ok=True)
    gui_list_path.write_text(prefix + table + "\n", encoding="utf-8")


def seed_platform_checklist(seed_from: Path, platform: str) -> str:
    """Build a fresh per-platform checklist.md from an approved baseline checklist,
    preserving items but resetting execution state for the new platform."""
    text = seed_from.read_text(encoding="utf-8")
    rows = parse_table(text, CHECKLIST_HEADER)
    if not rows:
        raise ValueError(f"no checklist rows found in seed file: {seed_from}")
    header_lines = text.split("| " + " | ".join(CHECKLIST_HEADER) + " |")[0]
    reset_rows = []
    for row in rows:
        new_row = dict(row)
        if new_row.get("Type") == "Item":
            new_row["Platform"] = platform
            new_row["Yes"] = ""
            new_row["No"] = ""
            new_row["Remarks"] = ""
            new_row["Evidence"] = ""
            new_row["Bug ID"] = ""
        reset_rows.append(new_row)
    table = render_table(CHECKLIST_HEADER, reset_rows)
    return (
        f"{header_lines}"
        f"Re-executed on platform: {platform}. Seeded from `{seed_from}`.\n\n"
        f"{table}\n\n"
        "## Human Review\n\n"
        "- Reviewer: TODO\n"
        "- Review Date and Time: TODO\n"
        f"- Review Scope: Cross-Platform Execution on {platform}\n"
        "- Status: Pending\n"
        "- Approved for Test Execution: No\n"
    )


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Create a GUI-checklist workspace (baseline or per-platform) for one screen.")
    parser.add_argument("--gui-id", required=True, type=non_empty, help="Screen ID matching the GUI list, e.g. '01'.")
    parser.add_argument("--gui-name", required=True, type=non_empty, help="Screen name, e.g. 'Trang chu (Home)'.")
    parser.add_argument("--gui-detail", default="", help="Optional extra context for this screen.")
    parser.add_argument("--output", required=True, type=non_empty, help="Output root directory.")
    parser.add_argument("--platform", help="If set, create a Task 3 cross-platform workspace for this platform instead of the Task 1 baseline.")
    parser.add_argument("--seed-from", help="Existing baseline checklist.md to seed a --platform workspace from.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing checklist.md.")
    args = parser.parse_args()

    if args.seed_from and not args.platform:
        print("ERROR: --seed-from requires --platform.", file=sys.stderr)
        return 2

    assets = Path(__file__).resolve().parents[1] / "assets"
    gui_dir_name = f"GUI-{args.gui_id}"

    if args.platform:
        platform_slug = args.platform.strip().lower().replace(" ", "-")
        out_dir = Path(args.output) / "cross-platform" / platform_slug / gui_dir_name
        checklist_target = out_dir / "checklist.md"
        if checklist_target.exists() and not args.force:
            print(f"Skipped existing: {checklist_target}")
            (out_dir / "evidence").mkdir(parents=True, exist_ok=True)
            return 0
        try:
            if args.seed_from:
                content = seed_platform_checklist(Path(args.seed_from), args.platform)
            else:
                template = assets / "checklist-template.md"
                if not template.is_file():
                    print(f"ERROR: missing template {template}", file=sys.stderr)
                    return 3
                content = render(template.read_text(encoding="utf-8"), args.gui_id, args.gui_name, args.gui_detail, args.platform)
        except (OSError, ValueError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 3
        out_dir.mkdir(parents=True, exist_ok=True)
        checklist_target.write_text(content, encoding="utf-8")
        (out_dir / "evidence").mkdir(parents=True, exist_ok=True)
        print(f"Workspace: {out_dir}")
        print(f"Created/updated: {checklist_target}")
        return 0

    checklist_template = assets / "checklist-template.md"
    missing = [str(assets / t) for t in ({"checklist.md": "checklist-template.md", **SHARED_FILES}).values() if not (assets / t).is_file()]
    if not (assets / "gui-list-template.md").is_file():
        missing.append(str(assets / "gui-list-template.md"))
    if missing:
        print("ERROR: required templates are missing; no output was written:", file=sys.stderr)
        for item in missing:
            print(f"  - {item}", file=sys.stderr)
        return 3

    root = Path(args.output) / "gui-checklist"
    gui_out_dir = root / gui_dir_name
    checklist_target = gui_out_dir / "checklist.md"

    created: list[str] = []
    skipped: list[str] = []
    if checklist_target.exists() and not args.force:
        skipped.append(str(checklist_target))
    else:
        content = render(checklist_template.read_text(encoding="utf-8"), args.gui_id, args.gui_name, args.gui_detail, "Baseline")
        gui_out_dir.mkdir(parents=True, exist_ok=True)
        checklist_target.write_text(content, encoding="utf-8")
        created.append(str(checklist_target))
    (gui_out_dir / "evidence").mkdir(parents=True, exist_ok=True)

    for relative, template_name in SHARED_FILES.items():
        target = root / relative
        if target.exists() and not args.force:
            skipped.append(str(target))
            continue
        content = render((assets / template_name).read_text(encoding="utf-8"), args.gui_id, args.gui_name, args.gui_detail, "Baseline")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        created.append(str(target))

    upsert_gui_list(root / "gui-list.md", assets, args.gui_id, args.gui_name, args.gui_detail)

    print(f"Workspace: {root}")
    print(f"Created/updated: {len(created)}")
    for item in created:
        print(f"  - {item}")
    print(f"Skipped existing: {len(skipped)}")
    for item in skipped:
        print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
