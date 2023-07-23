#!/usr/bin/python3
""" an empty class BaseGeometry """


class BaseGeometry:
    """ Function that raises an error message """

    def area(self):
        """Public instance method that raises an error message """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that is in charge of validating the received value

        Args:
            name (str): name
            value (int): value to be evaluated

        Return:
            error messages for each case
        """

        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
