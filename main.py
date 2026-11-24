#!/usr/bin/env python3
"""One-line office joke entry for make.fun's
"One-Line Office Joke: 24-Hour Sprint" bounty.

Writes a single original one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: the same line every run.
"""

import os

LINE = "The office printer is the only honest coworker here \u2014 it says it is out of paper, and it actually is."

# The gate only accepts 1-200 characters: refuse to write anything outside it.
assert 1 <= len(LINE) <= 200, "joke must be 1-200 characters"
assert "\n" not in LINE, "joke must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
