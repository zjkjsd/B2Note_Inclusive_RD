#!/usr/bin/env python3
"""Enforce the provenance convention described in AGENTS.md.

Every ``figure`` and ``table`` environment in the note must be preceded by a
PROVENANCE comment block, either immediately above it or once at the top of
the section file it lives in.  Exit status is non-zero if any is missing or
incomplete, so this can be used as a pre-commit or CI check.

Usage:  python3 scripts/check_provenance.py [root]
"""
from __future__ import annotations

import pathlib
import re
import sys

REQUIRED_KEYS = ("status", "produced-by", "commit")
ENV_RE = re.compile(r"\\begin\{(figure|table)\*?\}")
BLOCK_RE = re.compile(r"^\s*%\s*PROVENANCE\b", re.IGNORECASE)
KEY_RE = re.compile(r"^\s*%\s*([A-Za-z-]+)\s*:")
# A float carrying only placeholder macros has nothing to attribute yet.
PLACEHOLDER_RE = re.compile(r"\\(AnalysisTBD|Superseded)\b")


def block_keys(lines: list[str], start: int) -> set[str]:
    """Collect the keys of the comment block that begins at ``start``."""
    keys: set[str] = set()
    for line in lines[start + 1:]:
        if not line.lstrip().startswith("%"):
            break
        match = KEY_RE.match(line)
        if match:
            keys.add(match.group(1).lower())
    return keys


def file_level_keys(lines: list[str]) -> set[str]:
    """Keys of a section-level block in the first comment run of the file."""
    for index, line in enumerate(lines[:15]):
        if BLOCK_RE.match(line):
            return block_keys(lines, index)
    return set()


def environment_body(lines: list[str], start: int) -> str:
    depth = 0
    body: list[str] = []
    for line in lines[start:]:
        depth += line.count(r"\begin{")
        depth -= line.count(r"\end{")
        body.append(line)
        if depth <= 0:
            break
    return "".join(body)


def check_file(path: pathlib.Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    section_keys = file_level_keys(lines)
    problems: list[str] = []

    for index, line in enumerate(lines):
        if not ENV_RE.search(line):
            continue
        if PLACEHOLDER_RE.search(environment_body(lines, index)):
            continue

        keys = set(section_keys)
        # Walk upwards over blank lines and the comment run directly above.
        cursor = index - 1
        while cursor >= 0 and not lines[cursor].strip():
            cursor -= 1
        run_start = None
        while cursor >= 0 and lines[cursor].lstrip().startswith("%"):
            if BLOCK_RE.match(lines[cursor]):
                run_start = cursor
                break
            cursor -= 1
        if run_start is not None:
            keys |= block_keys(lines, run_start)

        missing = [key for key in REQUIRED_KEYS if key not in keys]
        if missing:
            problems.append(
                f"{path}:{index + 1}: {line.strip()} "
                f"is missing provenance key(s): {', '.join(missing)}"
            )
    return problems


def main(argv: list[str]) -> int:
    root = pathlib.Path(argv[1] if len(argv) > 1 else ".")
    targets = sorted(root.glob("sections/*.tex")) + sorted(root.glob("*.tex"))
    problems: list[str] = []
    for path in targets:
        problems.extend(check_file(path))

    if problems:
        print("Provenance check FAILED:\n")
        for problem in problems:
            print(f"  {problem}")
        print(
            "\nAdd a PROVENANCE block above each float, or a section-level "
            "block at the top of the file.  See AGENTS.md."
        )
        return 1

    print(f"Provenance check passed ({len(targets)} files).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
