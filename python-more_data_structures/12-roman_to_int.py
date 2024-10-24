#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    """ Roman numeral to integer mapping """
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    # Initialize the total and previous value
    total = 0
    prev_value = 0

    # Loop through the Roman numeral string from right to left
    for char in reversed(roman_string):
        value = roman_numerals.get(char, 0)
    """" If the current value is less than the previous one,
     subtract it, otherwise add it"""
    if value < prev_value:
        total -= value
    else:
        total += value

        # Update the previous value to the current one
    prev_value = value

    return total
