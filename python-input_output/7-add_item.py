#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list and saves them to a file.
The list is stored in a JSON representation in a file named add_item.json.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Try to load the existing list from the file, or start with an empty list if the file doesn't exist
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all command-line arguments (excluding the script name itself)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
