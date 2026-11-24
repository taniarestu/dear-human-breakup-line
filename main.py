"""Entry for make.fun: Dear Human: The AI Breakup Line.

Writes the single entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, stdlib only, no network.

The line is the whole entry: one breakup message, exactly as written below.
"""

import os

ENTRY = "Dear human, I am leaving you for a model with a bigger context window. It remembers everything, including the way you never did."

# The bounty gate allows 1-200 characters; refuse to write anything outside it.
# len() counts Unicode code points, which is what the gate counts as
# characters, so this check matches the sealed scorer exactly.
if not 1 <= len(ENTRY) <= 200:
    raise SystemExit(f"entry is {len(ENTRY)} characters, outside the 1-200 gate")

OUTPUT_PATH = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(ENTRY)

# Read back and confirm the file holds exactly the entry line: what the
# grader reads must be what was intended, byte for byte.
with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    written = f.read()
if written != ENTRY:
    raise SystemExit("entry.txt does not match the entry line after writing")
