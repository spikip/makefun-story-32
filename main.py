"""Entry for the make.fun bounty "Tell a Whole Story in 32 Characters".

The program writes a single Wi-Fi network name to /output/entry.txt.
The name implies a whole story in a glance at a phone's network list:
the Wi-Fi died with Grandma, so whoever named the network is still
grieving, and still online — the whole story is the tension
between the death in the name and the living network behind it.
The gate allows 1 to 32 characters of UTF-8 text, so the name is
checked against that cap before it is written.
"""

import os

ENTRY = "The WiFi Died With Grandma"

MAX_CHARS = 32
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
