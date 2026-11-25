#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Forecast a city that isn't, for the make.fun commuter bounty."""

import pathlib

FORECAST = "In Drizzleford, rain until nine, then sunshine and a bus that actually comes. Bring an umbrella and low expectations."
TARGET = pathlib.Path("/output/entry.txt")
LIMIT = 140


def validate(text: str) -> str:
    """Return the forecast once it passes the bounty limits."""
    assert text and "\n" not in text and "\r" not in text
    assert len(text) <= LIMIT, "forecast exceeds the 140-character limit"
    return text


def main() -> None:
    text = validate(FORECAST)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
