"""One Word for Your Wi-Fi — entry program.

Writes a single word describing my Wi-Fi to /output/entry.txt.
The word: haunted — the signal vanishes like a ghost right when
you need it most, then comes back on its own as if nothing happened.
"""

import os

WORD = "haunted"

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Read back and verify the exact bytes we meant to write.
    # Explicit comparison (not a bare check that disappears under python -O):
    # if the file on disk differs from WORD, fail loudly with a non-zero exit.
    with open(OUTPUT_PATH, "rb") as f:
        actual_bytes = f.read()
    expected_bytes = WORD.encode("utf-8")
    if actual_bytes != expected_bytes:
        raise SystemExit(
            "entry.txt mismatch: read back "
            f"{actual_bytes!r}, expected {expected_bytes!r} (word={WORD!r})"
        )


if __name__ == "__main__":
    main()
