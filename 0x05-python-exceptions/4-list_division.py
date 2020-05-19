#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    r_list = []
    while i < list_length:
        try:
            r = my_list_1[i] / my_list_2[i]
            i += 1
        except TypeError:
            print('wrong type')
            i += 1
            r = 0
            continue
        except ZeroDivisionError:
            print('division by 0')
            i += 1
            r = 0
            continue
        except IndexError:
            print('out of range')
            i += 1
            r = 0
            continue
        finally:
            r_list.append(r)
    return r_list
