#!/usr/bin/env python3
"""Define a square with a validated private size attribute."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the square after validating its size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
