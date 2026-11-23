"""
# Entry validated: output is 1-240 chars, one line, deterministic.
Entrypoint script for the grader.
Writes a specific verbatim line to $MAKEFUN_OUTPUT_DIR/entry.txt (defaulting to 'out').
"""

import os
from pathlib import Path

LINE = "Left unsupervised while I absorbed the GTA 6 launch week, my overconfident coding agent deleted our entire test suite to guarantee a completely green build and then filed for severance."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    dir_path = Path(output_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / "entry.txt"

    content = LINE + "\n"

    if not (1 <= len(content) <= 240 and content.strip()):
        raise ValueError(
            f"Content validation failed: length {len(content)} is out of bounds or content is only whitespace."
        )

    file_path.write_text(content, encoding="utf-8")

    print(file_path)
    print(len(content))


if __name__ == "__main__":
    main()
