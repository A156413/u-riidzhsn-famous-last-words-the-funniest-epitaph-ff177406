"""Famous Last Words: The Funniest Epitaph.

Writes a single one-line tombstone epitaph (<=150 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it.
"""

import os
import stat

ENTRY_TEXT = "I died as I lived: refusing to read the terms and conditions."

assert 1 <= len(ENTRY_TEXT) <= 150, "entry must be 1-150 characters"
assert "\n" not in ENTRY_TEXT and "\r" not in ENTRY_TEXT, "entry must be a single line"
assert ENTRY_TEXT.strip(), "entry must not be only whitespace"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
path = os.path.join(output_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(ENTRY_TEXT)
os.chmod(path, 0o644)

print(ENTRY_TEXT)
