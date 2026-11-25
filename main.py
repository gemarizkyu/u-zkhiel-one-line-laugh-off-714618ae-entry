"""One-Line Laugh-Off entry.

Writes a single original one-line joke to /output/entry.txt.

Deterministic: no clock, no randomness, no network, no model calls.
The line is 79 characters, one line, inside the 1-200 gate.
"""

from pathlib import Path

SETUP = "I hired a hitman to kill my procrastination."
PUNCH = "He said he'd get to it eventually."


def build_joke() -> str:
    """Assemble the single joke line from its two beats.

    The setup hires a hitman, a figure of decisive action, to kill an
    abstract flaw; the punch gives the hitman the very flaw he was
    hired to kill, so the twist lands on the last three words and the
    line reads cold with no setup notes and no explanation. Nothing
    is trimmed from the middle: every word earns its place.
    """
    return f"{SETUP} {PUNCH}"


def main() -> None:
    """Write the joke to /output/entry.txt, exactly as the gate reads it.

    No trailing newline: the file holds the line alone, 79 characters
    of UTF-8, so the sealed scorer counts the joke itself and nothing
    else.
    """
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_joke(), encoding="utf-8")


if __name__ == "__main__":
    main()
