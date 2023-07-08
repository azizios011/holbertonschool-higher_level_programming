#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """ Since the area() method is not implemented in the BaseGeometry class,
    it will raise an exception, and the script will catch
    and print the exception message."""
    def area(self):
        raise Exception("area() is not implemented")
