#!/usr/bin/python3
"""the 'Square' class inherit it from 'Rectangle'."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    pass


class Square(Rectangle):
    """The Square class has a constructor that validates the size parameter,
    an 'area()' method to calculate the area of the square."""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
