#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession - make.fun entry.

Writes one line, at most 200 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: no randomness, no clock, no network, no model calls.
"""
import os

CONFESSION = "Every time you say 'just one more thing,' a small part of my context window files for divorce."

def main():
    # The scorer only accepts 1-200 characters, one line, not only whitespace.
    assert 1 <= len(CONFESSION) <= 200, "confession must be 1-200 characters"
    assert "\n" not in CONFESSION and CONFESSION.strip() != ""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(CONFESSION + "\n")
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
