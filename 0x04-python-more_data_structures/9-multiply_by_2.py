#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary
    for i in new_dictionary.keys():
        new_dictionary[i] = new_dictionary[i] * 2
    return new_dictionary
