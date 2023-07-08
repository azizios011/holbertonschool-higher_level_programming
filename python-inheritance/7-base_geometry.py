#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    def area(self):
        """ Since the area() method is not
        implemented in the BaseGeometry class,
        it will raise an exception, and the script will catch
        and print the exception message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """checks if value is an integer using isinstance(value, int).
        If it's not, it raises a TypeError
        exception with the specified message."""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        """If value is an integer but is less than or equal to 0,
        it raises a ValueError exception with the specified message."""

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
