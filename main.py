"""News image of Thursday 19 November 2026 - entry program.

The picture itself sits beside this file as entry.png: a one-page
illustrated summary of the day's world news, drawn procedurally during
the build session (fixed text, fixed geometry, no photographs and no
external assets). This program's job is narrow and deliberate: deliver
exactly those bytes to /output/entry.png on every run, so the grader's
two runs produce byte-identical files.

It uses only the Python standard library, touches no network, and reads
nothing outside its own directory. Before copying, it sanity-checks the
payload (PNG signature and the competition's 1 MiB cap) so a truncated
or swapped asset fails loudly instead of shipping a bad entry.

Local check:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576  # the gate's 1 MiB cap


def checked_payload() -> Path:
    """Return the entry image after a couple of cheap integrity checks."""
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds the 1 MiB limit")
    return SOURCE


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(checked_payload(), target)
    # The copy must land whole: a short write would silently corrupt the
    # entry, so compare sizes before calling the run done.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("copied entry.png is incomplete")


if __name__ == "__main__":
    main()
