"""Writes the make.fun bounty entry text to entry.txt."""

import os
import sys
from pathlib import Path

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I "
    "respect her. All my mail is being held at the post office, and by the wasp."
)


ENV_VARS = ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR")
DEFAULT_DIR = "/output"


def output_dir() -> Path:
    """First set folder from ENV_VARS, else DEFAULT_DIR."""
    for name in ENV_VARS:
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path(DEFAULT_DIR)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
