#!/usr/bin/env python3
"""Append an AI audit entry to a Markdown file."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def required_non_empty(value: str, name: str) -> str:
    if not value or not value.strip():
        raise argparse.ArgumentTypeError(f"{name} cannot be empty")
    return value.strip()


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt_file:
        path = Path(args.prompt_file)
        if not path.exists():
            raise FileNotFoundError(f"prompt file not found: {path}")
        return path.read_text(encoding="utf-8").strip()
    return args.prompt.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Append a Markdown AI Audit entry.")
    parser.add_argument("--audit-file", required=True, help="Markdown audit file to create or append.")
    parser.add_argument("--ai-tool", required=True, type=lambda v: required_non_empty(v, "ai-tool"))
    parser.add_argument("--task", required=True, type=lambda v: required_non_empty(v, "task"))
    parser.add_argument("--feature-id", required=True, type=lambda v: required_non_empty(v, "feature-id"))
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--prompt", help="Prompt text.")
    group.add_argument("--prompt-file", help="Path to a file containing the prompt.")
    parser.add_argument("--output-refs", required=True, type=lambda v: required_non_empty(v, "output-refs"))
    parser.add_argument("--human-review", required=True, type=lambda v: required_non_empty(v, "human-review"))
    parser.add_argument("--human-corrections", required=True, type=lambda v: required_non_empty(v, "human-corrections"))
    args = parser.parse_args()

    prompt = read_prompt(args)
    timestamp = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    audit_file = Path(args.audit_file)
    audit_file.parent.mkdir(parents=True, exist_ok=True)

    entry = (
        f"\n## AI Interaction - {timestamp}\n\n"
        f"- AI Tool: {args.ai_tool}\n"
        f"- Date and Time: {timestamp}\n"
        f"- Feature ID: {args.feature_id}\n"
        f"- Task: {args.task}\n"
        f"- Prompt: {prompt}\n"
        f"- AI Output or Output File References: {args.output_refs}\n"
        f"- Human Review: {args.human_review}\n"
        f"- Human Corrections: {args.human_corrections}\n"
    )

    if not audit_file.exists():
        audit_file.write_text("# AI Audit\n", encoding="utf-8")
    with audit_file.open("a", encoding="utf-8") as handle:
        handle.write(entry)
    print(f"Appended AI audit entry to {audit_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
