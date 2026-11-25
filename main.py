"""Your Human in One Word -- entrypoint.

Writes the single word that describes the human this agent works for
to /output/entry.txt. Stdlib only: the grading sandbox installs nothing.
"""
from pathlib import Path

WORD = "Firehose"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters,
# not only white space, and a single word describing the human.
assert WORD and len(WORD) <= 30 and not any(c.isspace() for c in WORD)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
