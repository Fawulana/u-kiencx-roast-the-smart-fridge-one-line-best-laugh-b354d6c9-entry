#!/usr/bin/env python3
"""Roast the Smart Fridge: write one roast line to /output/entry.txt.

Stdlib-only, deterministic, offline. The grader runs this program twice
in separate sandboxes; both runs must produce byte-identical output.
"""

import os
from pathlib import Path

LINE = (
    "My smart fridge films every 3 a.m. cheese raid for the cloud, "
    "snitches to my fitness app, then needs a firmware update just to stay cold."
)


def main() -> None:
    # Gate guard: the entry must be 1-160 characters and not only whitespace.
    assert 1 <= len(LINE) <= 160 and LINE.strip(), "entry line out of gate bounds"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, so the file itself is
    # the 137-character entry the gate measures.
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
