#!/usr/bin/python3
"""the Rectangle class inherit it from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""the Rectangle class inherit it from BaseGeometry."""


class Rectangle(BaseGeometry):
    pass


class Rectangle(BaseGeometry):
    def __init__(self, width, height):

        """validate the 'width' and 'height' parameters using
        the 'integer_validator' method inherited
        from the 'BaseGeometry' class."""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        """ If the validation passes, the 'width' and 'height' are assigned
        to private attributes '__width' and '__height', respectively."""

        self.__width = width
        self.__height = height
