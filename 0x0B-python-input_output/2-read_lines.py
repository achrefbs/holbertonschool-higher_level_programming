#!/usr/bin/python3
"""reads n lines of a text file (UTF8) and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read())
        else:
            line = f.readline()
            while line and nb_lines > 0:
                print(line, end="")
                line = f.readline()
                nb_lines -= 1
