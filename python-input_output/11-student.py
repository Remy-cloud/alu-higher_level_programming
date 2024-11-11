#!/usr/bin/python3
"""class creation"""


class Student:
    """defines a student by first name, last name, and age."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only those attributes will be included.
        Otherwise, all attributes will be included.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for
                                           attr in attrs):
            return {key: getattr(self, key) for
                    key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
