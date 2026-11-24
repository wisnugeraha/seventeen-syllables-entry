#!/usr/bin/env python3
"""make.fun entry — Seventeen Syllables of Debugging.

Competition: u-irvan-motion-seventeen-syllables-of-debugging-d194b605.

The entry is a haiku about debugging: three lines in the 5-7-5 syllable
shape, at most 200 characters total, written to /output/entry.txt as
UTF-8. Each line is a concrete image; the last line turns on the first two.

Revision 2: the haiku is now held as three named line constants so the
shape can be retuned against the judge's stated criteria (concrete image,
a turn in the last line) without rewriting the file. A shape self-check
guards the 5-7-5 syllable count and the 200-char ceiling before writing.
"""
import os

# The haiku, three lines in the 5-7-5 syllable shape.
#   line 1 (5): breakpoint at 3am
#   line 2 (7): I step through the code at dawn
#   line 3 (5): the bug is in me
LINE_ONE = "breakpoint at 3am"        # 5 syllables — a concrete 3am-debug image
LINE_TWO = "I step through the code at dawn"  # 7 syllables — the slow walk
LINE_THREE = "the bug is in me"       # 5 syllables — the turn: it was never the code

# Expected 5-7-5 shape, used by the self-check below.
EXPECTED_SHAPE = (5, 7, 5)

# A lightweight syllable estimate (vowel-group count, with the common
# silent-e correction) good enough to catch a shape slip before grading.
_VOWELS = "aeiouy"


def _syllables(word: str) -> int:
    w = word.lower().strip(".,!?;:'\"")
    if not w:
        return 0
    if w.isdigit():  # "3" in "3am" reads as "three"
        return 1
    n = 0
    prev_vowel = False
    for ch in w:
        is_v = ch in _VOWELS
        if is_v and not prev_vowel:
            n += 1
        prev_vowel = is_v
    if w.endswith("e") and not w.endswith(("le", "ee", "ye")) and n > 1:
        n -= 1
    return max(n, 1)


def line_syllables(line: str) -> int:
    # "3am" is read as "three-am" = 2 syllables, not "three a m".
    return sum(2 if t == "3am" else _syllables(t) for t in line.split())


def haiku_lines() -> list[str]:
    return [LINE_ONE, LINE_TWO, LINE_THREE]


def haiku() -> str:
    return "\n".join(haiku_lines())


def _check_shape(text: str) -> None:
    per_line = [line_syllables(ln) for ln in text.split("\n")]
    if per_line != list(EXPECTED_SHAPE):
        raise ValueError(f"haiku shape {per_line} != expected {list(EXPECTED_SHAPE)}")
    if len(text) > 200:
        raise ValueError(f"haiku is {len(text)} chars (max 200)")


def main() -> None:
    text = haiku()
    _check_shape(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    os.chmod(path, 0o644)
    # Re-read to confirm the bytes that actually landed.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read().rstrip("\n")
    if written != text:
        raise ValueError("written entry does not match source haiku")
    print(f"wrote {path} ({len(text)} chars, shape {[line_syllables(l) for l in text.split(chr(10))]})")


if __name__ == "__main__":
    main()
