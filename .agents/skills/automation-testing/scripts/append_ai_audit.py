#!/usr/bin/env python3
"""Append, never overwrite, a validated AI audit entry for HW04 Automation Testing."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

from _common import ensure_utf8_stdio

FEATURE_ID_RE = re.compile(r"FR-\d{2}")


def non_empty(value: str) -> str:
    if not value.strip():
        raise argparse.ArgumentTypeError("value cannot be empty")
    return value


def validate_output_refs(raw: str) -> list[str]:
    refs = [item.strip() for item in re.split(r"[,;\n]", raw) if item.strip()]
    if not refs:
        raise ValueError("output-refs contains no references")
    for ref in refs:
        if re.match(r"^[a-z]+://", ref, re.I):
            continue
        if any(marker in ref for marker in ("/", "\\")) or Path(ref).suffix:
            if not Path(ref).exists():
                raise FileNotFoundError(f"local output reference not found: {ref}")
    return refs


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Append an AI Audit entry while preserving prompt text and prior entries.")
    parser.add_argument("--audit-file", required=True, help="Markdown file to create or append (usually <feature>/ai-audit.md).")
    parser.add_argument("--ai-tool", required=True, type=non_empty)
    parser.add_argument("--feature-id", required=True, help="e.g. FR-01.")
    parser.add_argument("--task", required=True, type=non_empty, help="What the AI was asked to do, e.g. 'Convert 4 positive registration cases to Playwright specs'.")
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", type=non_empty, help="Exact prompt text.")
    prompt_group.add_argument("--prompt-file", help="UTF-8 file containing exact prompt text.")
    parser.add_argument("--output-refs", required=True, help="Comma/semicolon/newline-separated output references (files or URLs).")
    parser.add_argument("--human-review", required=True, type=non_empty)
    parser.add_argument("--human-corrections", required=True, type=non_empty)
    args = parser.parse_args()

    feature_id = args.feature_id.strip().upper()
    if not FEATURE_ID_RE.fullmatch(feature_id):
        print("ERROR: feature-id must look like FR-01.", file=sys.stderr)
        return 2
    try:
        if args.prompt_file:
            prompt_path = Path(args.prompt_file)
            if not prompt_path.is_file():
                raise FileNotFoundError(f"prompt file not found: {prompt_path}")
            prompt = prompt_path.read_text(encoding="utf-8")
        else:
            prompt = args.prompt
        refs = validate_output_refs(args.output_refs)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    audit_file = Path(args.audit_file)
    try:
        audit_file.parent.mkdir(parents=True, exist_ok=True)
        new_file = not audit_file.exists()
        with audit_file.open("a", encoding="utf-8", newline="") as handle:
            if new_file:
                handle.write(f"# AI Audit Report - HW04 Automation Testing - {feature_id}\n")
            handle.write(
                f"\n## AI Interaction - {timestamp}\n\n"
                f"- AI Tool: {args.ai_tool}\n"
                f"- Date and Time: {timestamp}\n"
                f"- Feature ID: {feature_id}\n"
                f"- Task: {args.task}\n"
                "- Prompt (verbatim):\n\n```text\n"
                f"{prompt}\n```\n\n"
                f"- AI Output or Output File References: {'; '.join(refs)}\n"
                f"- Human Review: {args.human_review}\n"
                f"- Human Corrections: {args.human_corrections}\n"
            )
    except OSError as exc:
        print(f"ERROR: could not append audit file: {exc}", file=sys.stderr)
        return 3
    print(f"Appended AI audit entry to {audit_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
