#!/usr/bin/python3
import importlib

# Only execute the following when the script is run directly
if __name__ == "__main__":
    # Import the hidden_4 module
    hidden_4 = importlib.import_module('hidden_4')

    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter names that do not start with '__' and sort them
    valid_names = sorted(name for name in names if not name.startswith("__"))

    # Print each name on a new line
    for name in valid_names:
        print(name)
