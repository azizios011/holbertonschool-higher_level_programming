#!/usr/bin/python3
""" the 'Student' class that defines a student with
the specified attributes and a 'to_json' method to retrieve
a dictionary representation of a 'Student' instance"""


class Student:

    """The 'Student' class has three public instance attributes:
    'first_name', 'last_name', and 'age'. These attributes are
    initialized through the '__init__' method when
    a 'Student' object is created."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """The 'to_json' method returns a dictionary representation
        of the 'Student' instance, where the keys are the attribute
        names and the values are the corresponding attribute values."""

        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
