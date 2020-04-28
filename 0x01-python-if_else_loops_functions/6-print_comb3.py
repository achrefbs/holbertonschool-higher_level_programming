#!/usr/bin/python3
n = 1
for i in range(9):
    for j in range(n, 10):
        if n != 9:
            print('{:d}{:d}, '.format(i, j), end="")
        else:
            print('{:d}{:d}'.format(i, j))
    n += 1
