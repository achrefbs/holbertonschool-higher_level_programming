#!/usr/bin/python3
"""prints a text with 2 new lines"""


def text_indentation(text):
    """
    a function that prints a text with
    2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in range(len(text)):
        print("{}".format(text[i]), end='')
        if text[i] in('.?:'):
            print()
            i += 1
