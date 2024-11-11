#!/usr/bin/python3
"""module that has a script that adds all arguments to a Python list,
 and then save them to a file:"""


import sys


from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file


filename = "add_item.json"

"""Try to load the existing list from the file, or start with an
empty list if the file doesn't exist"""
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []
"""Add all command-line arguments (excluding the script name itself)"""
items.extend(sys.argv[1:])
"""Save the updated list back to the file"""
save_to_json_file(items, filename)
