#!/usr/bin/env python3
"""One Line, Big Laugh -- coral-big-laugh entry.

Writes a single original one-liner joke to the output directory that
make.fun expects, then self-checks it against the bounty gate rules:

  * exactly one line (no newline characters anywhere in the text)
  * length between 1 and 200 characters, inclusive
  * the bytes written to disk read back identical to the joke

Only the Python standard library is used, so the script runs anywhere
with a plain `python3` install.
"""

import os
import sys

# The joke itself. One line, one laugh, no room for a second take.
JOKE = (
    "The hotel charged me $40 for the minibar, so I drank the shampoo "
    "out of principle and now I smell like a refund."
)


def output_path() -> str:
    """Resolve the file the entry must be written to.

    make.fun hands us the output directory through the
    MAKEFUN_OUTPUT_DIR environment variable.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit(
            "MAKEFUN_OUTPUT_DIR is not set; "
            "run with e.g. MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py"
        )
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def check_gate(text: str) -> None:
    """Enforce the bounty gate rules on the joke text.

    Raises AssertionError with a human-readable reason if any rule
    fails, so a bad entry can never be written silently.
    """
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert 1 <= len(text) <= 200, (
        f"joke must be 1-200 characters, got {len(text)}"
    )


def main() -> int:
    check_gate(JOKE)

    path = output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)

    # Read the file back and make sure what landed on disk is exactly
    # the joke we meant to submit -- no trailing newline, no drift.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == JOKE, "read-back mismatch: entry.txt differs from joke"
    assert "\n" not in written, "entry.txt must contain no newline"

    print(f"Gate passed: {len(JOKE)} characters, single line, no newline.")
    print(f"Wrote one-liner to {path}")
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
