#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    c = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            c += 1
            i += 1
        except (ValueError, TypeError):
            i += 1
            continue

    print()
    return c
