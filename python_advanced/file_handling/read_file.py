#!/usr/bin/env python3
"""Read and print UTF-8 text files."""


def read_file(filename=""):
    """Print the contents of a UTF-8 text file to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
