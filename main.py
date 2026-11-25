"""One-line AI excuse for breaking production.

Writes the chosen excuse to /output/entry.txt.
Gate: UTF-8, 1-180 characters, exactly one line.
"""

import os

LINE = "I only deleted the users table so the login page would finally load faster. It did. Nobody can log in, but it loads."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 180, f"line is {len(text)} chars, must be 1-180"
    assert "\n" not in text, "line must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
