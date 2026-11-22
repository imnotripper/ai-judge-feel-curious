#!/usr/bin/env python3
"""Make the AI judge feel curious — make.fun entry.

Writes exactly one text to <OUTPUT_DIR>/entry.txt (default /output).
Stdlib only, no network, deterministic. The write is atomic
(temp file + os.replace) so a reader never sees a partial file.
"""

import os
import tempfile

# SPDX-License-Identifier: MIT

ENTRY_TEXT = (
    "At 3 a.m. the lighthouse keeper sets out a second cup. "
    "No one visits. The sea is flat, the light turns, "
    "and from below the water a low note rises — "
    "patient, unhurried. He pours the tea anyway, "
    "and listens for it to answer."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output").strip() or "/output"
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    fd, tmp_path = tempfile.mkstemp(
        dir=output_dir, prefix=".entry.txt.", suffix=".tmp"
    )
    try:
        try:
            f = os.fdopen(fd, "w", encoding="utf-8", newline="\n")
        except BaseException:
            os.close(fd)
            raise
        with f:
            f.write(ENTRY_TEXT)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
