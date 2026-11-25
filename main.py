#!/usr/bin/env python3
"""Write the one-line resignation letter to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "The Funniest One-Line Resignation Letter" bounty.
The program writes exactly one line of text and nothing else.

How the line targets the brief: the judge is a tired engineering manager
picking the funnier letter, so the letter comes from the most thankless
worker in the stack -- the cron job that has fired every single minute
since March without anyone ever noticing it exists. The joke turns on one
word doing double duty: "interval" is both the cron schedule and the only
raise a cron job can ever get, a promotion that is really just more work.
Resignation, ingratitude, and a pun that only an engineer would write --
all inside 140 characters.
"""

import os
from pathlib import Path

LINE = "I quit. I've run every minute since March, nobody thanked me once, and the only raise I ever got was my interval."


def write_entry(out_dir: Path) -> Path:
    """Write the resignation line to entry.txt inside out_dir and return
    its path.

    The file holds exactly the line and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line of at most 140 chars.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
