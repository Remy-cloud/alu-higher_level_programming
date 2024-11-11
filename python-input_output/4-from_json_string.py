#!/usr/bin/python3
"""a module that has a function that returns an object
 (Python data structure) represented by a JSON string:"""


import json


def from_json_string(my_str):
    """ returns an object represented by a json string """
    return json.loads(my_str)
