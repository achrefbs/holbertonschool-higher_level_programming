#!/usr/bin/python3
def best_score(a_dictionary):
    bestscore = 0
    best_key = ''
    if len(a_dictionary) == 0:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > bestscore:
            bestscore = a_dictionary[i]
            best_key = i
    return best_key
