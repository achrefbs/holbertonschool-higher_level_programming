#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """
    writes a string to a text file
    return: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
