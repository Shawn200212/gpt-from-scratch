"""Create small UTF-8 text samples from local tar-format corpus archives."""

from __future__ import annotations

import argparse
import tarfile
from pathlib import Path


def create_sample(source: Path, destination: Path, max_bytes: int) -> None:
    """Write up to ``max_bytes`` of article text from a tar archive."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    remaining = max_bytes

    with tarfile.open(source, mode="r:*") as archive, destination.open(
        "w", encoding="utf-8", newline="\n"
    ) as output:
        for member in archive:
            if remaining <= 0:
                break
            if not member.isfile():
                continue

            extracted = archive.extractfile(member)
            if extracted is None:
                continue

            raw = extracted.read(remaining)
            if not raw:
                continue

            text = raw.decode("utf-8", errors="replace")
            header = f"\n\n--- source: {member.name} ---\n\n"
            output.write(header)
            output.write(text)
            remaining -= len(raw)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Path to a local tar-format corpus archive")
    parser.add_argument("destination", type=Path, help="Destination UTF-8 text file")
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=512 * 1024,
        help="Maximum corpus bytes to include (default: 524288)",
    )
    args = parser.parse_args()
    create_sample(args.source, args.destination, args.max_bytes)


if __name__ == "__main__":
    main()
