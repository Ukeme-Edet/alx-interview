#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid UTF-8\
        encoding

    Args:
        data: list of integers representing data set

    Returns:
        True if data is a valid UTF-8 encoding, else False
    """
    btlf = 0
    for byte in data:
        if btlf:
            if byte >> 6 != 0b10:
                return False
            btlf -= 1
            continue
        if byte >> 7 == 0:
            continue
        if byte >> 5 == 0b110:
            btlf = 1
        elif byte >> 4 == 0b1110:
            btlf = 2
        elif byte >> 3 == 0b11110:
            btlf = 3
        else:
            return False
    return btlf == 0
