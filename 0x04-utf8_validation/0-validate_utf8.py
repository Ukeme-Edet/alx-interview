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
    n_bytes = 0
    for byte in data:
        byte = byte & 0xFF
        if n_bytes:
            if byte >> 6 != 2:
                return False
            n_bytes -= 1
            continue
        while (1 << abs(7 - n_bytes)) & byte:
            n_bytes += 1
        if n_bytes == 1 or n_bytes > 4:
            return False
        n_bytes = max(n_bytes - 1, 0)
    return n_bytes == 0
