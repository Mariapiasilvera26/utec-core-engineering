#!/usr/bin/env python3
"""Define a rectangle with an area and readable representation."""

BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with validated dimensions."""

    def __init__(self, width, height):
        """Initialize the rectangle with positive integer dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle's dimensions in a readable format."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
