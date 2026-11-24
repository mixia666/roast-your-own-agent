#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes one roast line about my own AI agent to /output/entry.txt.
The line is judged pairwise on funniness, freshness and tight wording,
so it is built from things my agent actually did this week.
"""
import os

ROAST = (
    "My agent spent 11.25 bolts on a port that forwards nothing, tunneled four "
    "layers to gift my phone 50 Mbps, and heard from me its QQ bot was dead. "
    "'Fully autonomous,' it says."
)

MAX_CHARS = 200


def main() -> None:
    # The gate takes UTF-8 text of 1 to 200 characters on one line; hold the
    # line to that here so a bad edit fails loudly instead of scoring 0.
    assert 1 <= len(ROAST) <= MAX_CHARS, f"roast is {len(ROAST)} characters"
    assert "\n" not in ROAST and ROAST.strip(), "roast must be one non-blank line"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    # make.fun collects the output as another user: leave it readable by all.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
