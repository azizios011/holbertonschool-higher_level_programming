#!/usr/bin/python3
""" the 'Student' class that defines a student with
the specified attributes and a 'to_json' method to retrieve
a dictionary representation of a 'Student' instance"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        """The 'to_json' method now takes an optional 'attrs'
        parameter, which is a list of attribute names to be included
        in the JSON representation. If 'attrs' is 'None', all attributes
        are retrieved. Otherwise, only the attributes specified in
        the 'attrs' list are included."""

    def to_json(self, attrs=None):

        """Inside the method, we check if 'attrs' is 'None'.
        If it is, we return the '__dict__' attribute of the instance,
        which contains a dictionary representation of all the attributes."""

        if attrs is None:
            return self.__dict__

            """If 'attrs' is not 'None', we create a new dictionary
            comprehension. For each attribute in 'attrs', we check if
            the instance has the attribute using 'hasattr'. If it does,
            we retrieve the attribute value using 'getattr' and include
            it in the dictionary."""

        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
