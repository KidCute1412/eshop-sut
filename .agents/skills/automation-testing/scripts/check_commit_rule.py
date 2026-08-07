#!/usr/bin/env python3
"""Check the assignment's specific Git Commit Log rule: at least 8 commits that touch a test-script
file (.spec.js/.spec.ts or an equivalent pattern), spanning at least 4 distinct calendar days.
Commits that only touch README/PDF/other non-test documents do not count."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from _common import ensure_utf8_stdio

DEFAULT_SPEC_SUFFIXES = (".spec.js", ".spec.ts", ".spec.jsx", ".spec.tsx", "test.py", "Test.java")


def run_git(args: list[str], cwd: Path) -> str:
    result = subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def touches_spec_file(files: list[str], suffixes: tuple[str, ...]) -> bool:
    return any(f.endswith(suffixes) for f in files)


def main() -> int:
    ensure_utf8_stdio()
    parser = argparse.ArgumentParser(description="Check the >=8 spec-touching commits over >=4 days rule.")
    parser.add_argument("repo", nargs="?", default=".", help="Path to the git repository (default: current directory).")
    parser.add_argument("--suffix", action="append", dest="suffixes",
                         help="Additional filename suffix that counts as a test-script file (repeatable). "
                              "Defaults: " + ", ".join(DEFAULT_SPEC_SUFFIXES))
    args = parser.parse_args()

    repo = Path(args.repo)
    if not (repo / ".git").exists():
        print(f"ERROR: not a git repository: {repo}", file=sys.stderr)
        return 2

    suffixes = tuple(DEFAULT_SPEC_SUFFIXES) + tuple(args.suffixes or ())

    try:
        log_output = run_git(
            ["log", "--pretty=format:%H|%ad", "--date=short", "--name-only"], cwd=repo,
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 3

    # Parse the interleaved "hash|date" header lines and following file-name blocks.
    commits: list[tuple[str, str, list[str]]] = []
    current_hash = None
    current_date = None
    current_files: list[str] = []
    for line in log_output.splitlines():
        if "|" in line and len(line.split("|", 1)[0]) == 40:
            if current_hash is not None:
                commits.append((current_hash, current_date, current_files))
            current_hash, current_date = line.split("|", 1)
            current_files = []
        elif line.strip():
            current_files.append(line.strip())
    if current_hash is not None:
        commits.append((current_hash, current_date, current_files))

    spec_commits = [(h, d) for h, d, files in commits if touches_spec_file(files, suffixes)]
    distinct_days = sorted(set(d for _, d in spec_commits))

    print(f"Total commits in repo: {len(commits)}")
    print(f"Commits touching a test-script file: {len(spec_commits)}")
    print(f"Distinct days among those commits: {len(distinct_days)} ({', '.join(distinct_days)})")

    errors = []
    if len(spec_commits) < 8:
        errors.append(f"expected >= 8 spec-touching commits, found {len(spec_commits)}")
    if len(distinct_days) < 4:
        errors.append(f"expected >= 4 distinct days, found {len(distinct_days)}")

    if errors:
        print("\nValidation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nValidation passed: the Git Commit Log rule is satisfied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
