"""Shared helpers for the automation-testing skill's scripts."""

from __future__ import annotations

import sys


def ensure_utf8_stdio() -> None:
    """Reconfigure stdout/stderr to UTF-8 so Vietnamese text never crashes on Windows (cp1252)."""
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (OSError, ValueError):
                pass
