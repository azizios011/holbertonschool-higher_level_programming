#!/usr/bin/python3
"""the Rectangle class inherit it from BaseGeometry."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    pass


class Square(Rectangle):

    """ The 'self.integer_validator("size", size)' validates
    the size parameter using the 'integer_validator' method
    inherited from the Rectangle class. If the validation passes,
    the size is assigned to the private attribute '__size'."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

        """The 'super().__init__(size, size)' line calls the constructor
        of the Rectangle class with size as the 'width' and 'height'.
        This way, the Square object is treated as a special case of
        a rectangle where the 'width' and 'height' are always the same."""

        super().__init__(size, size)

    """an 'area()' method to calculate the area of the square."""

    def area(self):
        return self.__size ** 2

    """The '__str__' method returns a string representation of
    the Square objectin the format "[Square] size/size"."""

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
