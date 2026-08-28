#!/usr/bin/env python3
"""Report LaTeX build problems from note.log.

Written after a hand-rolled grep silently matched nothing for several
commits and reported a clean build that was not clean.  This script asserts
that its own patterns match the log format before trusting a zero count.

Usage:  python3 scripts/check_build.py [note.log]
"""
from __future__ import annotations

import pathlib
import re
import sys

PATTERNS = {
    "overfull hbox": re.compile(r"^Overfull \\hbox \(([\d.]+)pt", re.M),
    "underfull vbox": re.compile(r"^Underfull \\vbox", re.M),
    "undefined reference": re.compile(r"^LaTeX Warning: Reference .* undefined", re.M),
    "undefined citation": re.compile(r"^LaTeX Warning: Citation .* undefined", re.M),
    "rerun needed": re.compile(r"^LaTeX Warning: Label\(s\) may have changed", re.M),
}
# A line that must exist in any real log.  If it does not match, the log is
# not in the format these patterns assume and a zero count means nothing.
SANITY = re.compile(r"^(This is pdfTeX|Output written on)", re.M)


def main(argv: list[str]) -> int:
    log = pathlib.Path(argv[1] if len(argv) > 1 else "note.log")
    if not log.exists():
        print(f"FAIL  {log} does not exist; the document did not build.")
        return 2
    text = log.read_text(errors="replace")

    if not SANITY.search(text):
        print(f"FAIL  {log} does not look like a pdfTeX log; counts below "
              "would be meaningless.")
        return 2

    total = 0
    for label, pattern in PATTERNS.items():
        hits = pattern.findall(text)
        total += len(hits)
        if label == "overfull hbox" and hits:
            worst = max(float(h) for h in hits)
            print(f"  {len(hits):3d}  {label} (worst {worst:.1f}pt)")
        else:
            print(f"  {len(hits):3d}  {label}")

    print(f"\n{'PASS' if total == 0 else 'PROBLEMS FOUND'}: {total} issue(s).")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
