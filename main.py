"""One word for the boss: Reply-all.

Prints the word to stdout and writes the exact same word, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the word is a constant in this file,
and the checks enforce the competition's one-word, 30-character gate.
"""

import os
import sys

WORD = "Reply-all"


def main() -> int:
    if not 1 <= len(WORD) <= 30:
        print(f"error: word is {len(WORD)} chars, must be 1-30",
              file=sys.stderr)
        return 1
    if " " in WORD or "\n" in WORD:
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
