#!/usr/bin/env python3
"""One Line, Big Laugh entry (make.fun).

Writes exactly one joke line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python stdlib only, no dependencies.

The joke: a hotel minibar overcharge drives the guest to petty revenge
-- drinking the free shampoo on principle -- and the punch lands on
the smell of a refund. Setup, escalation, and a sudden turn in one line.
"""

import os

JOKE = "The hotel charged me $40 for the minibar, so I drank the shampoo out of principle and now I smell like a refund."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Gate: exactly one line, 1-200 chars, no trailing newline.
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip() == JOKE, "joke must not start or end with whitespace"
    assert 1 <= len(JOKE) <= 200, f"joke length {len(JOKE)} out of gate range"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Read-back check: the file on disk must be byte-identical to JOKE.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == JOKE, "written entry does not match JOKE"
    print(f"Wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
