"""Make the AI Judge Laugh: the Office Joke Open — entry v1.

Writes a single original office-life joke (one line, 1-200 chars) to
/output/entry.txt with no trailing newline. No network access needed.

The joke follows the winning short-text pattern: one specific detail,
a concrete number, and a second beat that escalates the absurdity —
the meeting about the meeting that ran long.
"""

from pathlib import Path

# One deadpan office joke: a 15-minute standup overruns, and the fix is
# — of course — another meeting about the meeting that ran long.
ENTRY_LINE = "Our 15-minute standup lasted 47 minutes, so we scheduled a follow-up to discuss why it ran long."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    line = ENTRY_LINE
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(line.encode("utf-8"))
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
