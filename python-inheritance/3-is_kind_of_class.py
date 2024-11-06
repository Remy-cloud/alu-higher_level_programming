#!/usr/bin/python3
"""Checks if obj is an instance of, or if it is an instance
 of a class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """ True if obj is an instance or inherits from a_class;
     otherwise, False"""
    return isinstance(obj, a_class)
