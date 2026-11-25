#!/usr/bin/env python3
"""One Line, One Laugh — a single hilarious line, written to /output/entry.txt.

The line is the whole entry: one original joke, at most 200 characters,
built to land on a first read. The turn: "the cloud" starts as the tech
everyone stores their work in, and ends as the literal sky — which has
just eaten the homework, the way every schoolkid once blamed on the dog.
"""

import os

LINE = "The cloud crashed today, which is the first time the sky has ever eaten my homework."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
