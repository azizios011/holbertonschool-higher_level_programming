#!/usr/bin/python3
"""the 'Student' class that includes the 'reload_from_json'
method to replace all attributes of the 'Student' instance"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):

        """The 'reload_from_json' method takes a dictionary 'json'
        as input. For each key-value pair in the dictionary,
        it sets the corresponding attribute on the 'Student' instance
        using the 'setattr' function."""

        for attr, value in json.items():
            setattr(self, attr, value)
