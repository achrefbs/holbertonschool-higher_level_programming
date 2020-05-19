#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        r = None
    return r
