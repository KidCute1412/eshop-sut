"""Shared, dependency-free Markdown pipe-table and bullet-field helpers.

Used by the gui-usability skill scripts. Not a standalone entry point.
"""
from __future__ import annotations

import re
import sys


def ensure_utf8_stdio() -> None:
    """Force UTF-8 stdout/stderr so Vietnamese checklist text prints correctly
    even on a Windows console defaulting to a legacy codepage (e.g. cp1252).
    Call this once at the top of a script's main()."""
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (OSError, ValueError):
                pass

SEPARATOR_RE = re.compile(r"^\s*\|?(\s*:?-{2,}:?\s*\|)*\s*:?-{2,}:?\s*\|?\s*$")
FIELD_RE = re.compile(r"^\s*-\s*([^:\n]+):\s*(.*)$")

PLACEHOLDER_RE = re.compile(r"\b(?:TODO|TBD|PLACEHOLDER)\b", re.IGNORECASE)
EMPTY_VALUES = {"", "todo", "tbd", "n/a", "none"}


def split_row(line: str) -> list[str]:
    """Split one Markdown table line into trimmed cell strings."""
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def find_header(lines: list[str], header_cells: list[str]) -> int | None:
    """Return the line index of the first row matching header_cells exactly, with a
    valid separator line immediately after it. None if not found."""
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = split_row(line)
        if cells == header_cells and i + 1 < len(lines) and SEPARATOR_RE.match(lines[i + 1]):
            return i
    return None


def parse_table(text: str, header_cells: list[str]) -> list[dict[str, str]]:
    """Parse all data rows of the first table whose header matches header_cells."""
    lines = text.splitlines()
    header_index = find_header(lines, header_cells)
    if header_index is None:
        return []
    rows: list[dict[str, str]] = []
    for line in lines[header_index + 2:]:
        if not line.strip().startswith("|"):
            break
        cells = split_row(line)
        if len(cells) != len(header_cells):
            break
        rows.append(dict(zip(header_cells, cells)))
    return rows


def render_table(header_cells: list[str], rows: list[dict[str, str]]) -> str:
    """Render a Markdown pipe table from a header and a list of row dicts."""
    header = "| " + " | ".join(header_cells) + " |"
    separator = "| " + " | ".join("---" for _ in header_cells) + " |"
    body_lines = [
        "| " + " | ".join(row.get(col, "") for col in header_cells) + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body_lines])


def parse_fields(text: str) -> dict[str, str]:
    """Parse '- Field: value' bullet lines anywhere in the text, including simple
    multi-line continuations. Later duplicate keys overwrite earlier ones."""
    fields: dict[str, str] = {}
    current: str | None = None
    for line in text.splitlines():
        match = FIELD_RE.match(line)
        if match:
            current = match.group(1).strip()
            fields[current] = match.group(2).strip()
            continue
        if current and line.strip() and not line.startswith("#") and not line.strip().startswith("|"):
            fields[current] += "\n" + line.strip()
    return fields


def is_empty_or_placeholder(value: str | None) -> bool:
    """Return True when a value is missing, blank, or still literal TODO/TBD/N/A text."""
    if value is None:
        return True
    if value.strip().lower() in EMPTY_VALUES:
        return True
    return bool(PLACEHOLDER_RE.search(value))
