#!/usr/bin/python3
"""a module that has a function that returns the JSON
representation of an object (string):"""


import json


def to_json_string(my_obj):
    """return json of an object (string)"""
    return json.dumps(my_obj)
