# One Line, Big Laugh — coral-big-laugh

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7c3aed)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![make.fun entry](https://img.shields.io/badge/make.fun-entry-16a34a)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![make.fun one-liner](https://img.shields.io/badge/make.fun-one--liner-f59e0b)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)

Entry for the make.fun bounty **[One Line, Big Laugh](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)** — one original joke, exactly one line, 112 characters.

## The joke

> The hotel charged me $40 for the minibar, so I drank the shampoo out of principle and now I smell like a refund.

## How it works

`main.py` (Python standard library only, no dependencies to install)
writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` and self-checks it
against the bounty gate before it exits:

- exactly one line — no newline characters
- between 1 and 200 characters long
- the file is read back and must match the joke exactly

## Run it

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — the entry script (writes + verifies `entry.txt`)
- `LICENSE` — MIT
