#!/usr/bin/env python3
"""The Houseplant Out-of-Office — entry program.

Writes one line to /output/entry.txt: an out-of-office auto-reply in
the voice of a houseplant that answers only on its own schedule and
redirects all urgent matters to the reader's own photosynthesis.
One line of UTF-8 text inside the gate of 1 to 120 characters, with
no trailing newline.
"""

import os
from pathlib import Path

REPLY = (
    "I will respond when I've been watered. For urgent matters, "
    "please photosynthesize amongst yourselves."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_file = out_dir / "entry.txt"
    # No trailing newline is appended, so the reply's characters are
    # the whole file the sealed scorer measures.
    entry_file.write_text(REPLY, encoding="utf-8")


if __name__ == "__main__":
    main()
