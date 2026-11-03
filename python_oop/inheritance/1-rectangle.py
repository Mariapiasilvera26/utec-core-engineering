#!/usr/bin/env python3
"""Define a rectangle that inherits geometry validation."""

from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with validated dimensions."""

    def __init__(self, width, height):
        """Initialize the rectangle with positive integer dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
