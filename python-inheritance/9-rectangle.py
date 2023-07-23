#!/usr/bin/python3
"""Import parent classes from the file 7-base_geometry.py """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a Rectangle class with height and width """

    def __init__(self, width, height):
        """ Init constructor method """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Change to the area method to return area"""

        return self.__width * self.__height

    def __str__(self):
        """ method for printing description """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
