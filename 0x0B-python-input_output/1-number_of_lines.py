#!/usr/bin/python3
"""a function that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """a function that returns the number of lines of a text file"""
    count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            count += 1
    return count
