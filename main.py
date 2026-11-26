"""What the Elevator Would Say - make.fun entry.

Writes the funniest one line a talking elevator could say to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

# One line, 100 characters. The gate (RULES.txt) allows 1-120.
LINE = "You hit all twelve buttons, then sigh when I stop at every floor. Buddy, I am not the slow one here."

# Enforce the gate locally: a line outside 1-120 characters is refused.
assert 1 <= len(LINE) <= 120, "entry must be 1-120 characters"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
