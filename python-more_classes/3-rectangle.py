#!/usr/bin/python3
"""A class that defines a rectangle by width and height"""


class Rectangle:
    """A class that defines a rectangle by width and height"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Return a string representation of the rectangle object"""
        return f"Rectangle({self.width}, {self.height})"
