"""Museum of the Year 3000 -- make.fun bounty entry.

Writes one museum label (one line, at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Python 3.13, standard library only, deterministic: the same bytes on
every run.
"""

import os

# The label, exactly as the year-3000 curator would print it beside the
# exhibit: a sticky note holding the password to the machine it was
# stuck to. The twist lands in the last words.
LINE = "Sticky note, 2024. It guarded the machine it was stuck to. The password was 'password'."


def main():
    """Write the label to $MAKEFUN_OUTPUT_DIR/entry.txt."""
    # Gate guard: the sealed scorer accepts UTF-8 text of 1 to 200
    # characters, not only white space. Refuse to write anything else.
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("entry must not be only white space")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
