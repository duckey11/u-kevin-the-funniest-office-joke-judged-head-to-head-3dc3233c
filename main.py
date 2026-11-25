#!/usr/bin/env python3
"""Write one office joke, one line, to /output/entry.txt.

Stdlib only, no network, deterministic: the same fixed text every run.
"""

import os

JOKE = (
    "Our office printer finally got a promotion: it now jams "
    "in management meetings too."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
