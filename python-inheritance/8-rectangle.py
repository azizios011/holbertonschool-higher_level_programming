#!/usr/bin/python3
"""import parent classes from the file 7-base_geometry.py """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a Rectangle class with height and width """

    def __init__(self, width, height):
        """ init constructor method """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
