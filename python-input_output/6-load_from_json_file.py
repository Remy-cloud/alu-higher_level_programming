#!/usr/bin/python3
"""module that has a function that creates an Object from a “JSON file”:"""


import json


def load_from_json_file(filename):
    """creates an obj from json file"""
    with open(filename, "r", encoding="utf_8") as file:
        return json.load(file)
