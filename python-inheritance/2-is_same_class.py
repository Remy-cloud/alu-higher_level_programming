#!/usr/bin/python3
"""Checks if obj is exactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """True if obj is exactly an instance of a_class; otherwise, False"""
    return type(obj) is a_class
