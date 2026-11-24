#!/usr/bin/env python3
"""make.fun entry — Seventeen Syllables of Debugging.

Competition: u-irvan-motion-seventeen-syllables-of-debugging-d194b605.

The entry is a haiku about debugging: three lines in the 5-7-5 syllable
shape, at most 200 characters total, written to /output/entry.txt as
UTF-8. Each line is a concrete image; the last line turns on the first two.
"""
import os

# The haiku, three lines, 5-7-5 syllables.
#   line 1 (5): breakpoint at 3am
#   line 2 (7): I step through the code at dawn
#   line 3 (5): the bug is in me
HAIKU = (
    "breakpoint at 3am\n"
    "I step through the code at dawn\n"
    "the bug is in me"
)


def write_entry() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = HAIKU
    if len(text) > 200:
        raise ValueError(f"haiku is {len(text)} chars (max 200)")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    write_entry()
