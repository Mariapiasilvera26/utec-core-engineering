#!/usr/bin/env python3
"""Write text to UTF-8 files."""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
