#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Deterministic, stdlib-only. Writes the monologue to /output/entry.txt.

The villain never says he is weary. The tiredness lives in the rhythm:
the wobbling chair, the leaking roof, the flooded cellar, the ravens
that stopped coming. Empires end with a draught under the door.
"""

import os
import sys

ENTRY = (
    "You ask why I keep you alive. Sit down. No, the other chair — "
    "that one wobbles, and I have listened to it wobble since your "
    "grandfather was a boy with a wooden sword. I was going to unmake "
    "the sun. I had the eclipse, the choir, the knife with the bone "
    "handle. Then the roof leaked. Then the cellar flooded. Then the "
    "ravens stopped coming because the tower steps rotted through. "
    "Empires end the same way, hero. Not with a battle. With a draught "
    "under the door and nobody left who knows where the candles are kept."
)

MIN_CHARS = 1
MAX_CHARS = 600


def main() -> int:
    text = ENTRY.strip()
    words = text.split()
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}",
              file=sys.stderr)
        return 1
    if not 90 <= len(words) <= 110:
        print(f"entry should be near 100 words, got {len(words)}",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {out_path} ({len(text)} chars, "
          f"{len(text.split())} words)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
