#!/usr/bin/python3
"""a module that has a function that writes an Object
 to a text file, using a JSON representation:"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using
     a JSON representation"""
    with open(filename, "w", encoding="utf_8") as file:
        return json.dump(my_obj, file)
