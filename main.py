#!/usr/bin/env python3
"""One-Liner Laughs entry: writes a single original funny line to /output/entry.txt.

The joke: a smoke detector with a secret social life. Setup promises a fire
warning; the twist reframes the 3 a.m. beep as loneliness, not danger.
"""

import os

JOKE = (
    "My smoke detector only beeps at 3 a.m. \u2014 I've decided it's not "
    "warning me about a fire, it's just lonely and checking I'm still alive."
)


def check_gate(text: str) -> None:
    """Enforce the bounty gate rules on the joke text."""
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert text.strip(), "joke must not be only whitespace"
    assert 1 <= len(text) <= 200, (
        f"joke must be 1-200 characters, got {len(text)}"
    )


def main() -> None:
    check_gate(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    # Read-back check: what landed on disk must be exactly the joke.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == JOKE, "read-back mismatch: entry.txt differs from joke"
    print(f"Gate passed: {len(JOKE)} characters, single line, no newline.")
    print(JOKE)


if __name__ == "__main__":
    main()
