#!/usr/bin/python3
class magic_string: 
    n = 0
    def __str__(self):
        magic_string.n += 1 ; return "holberton" * magic_string.n

for i in range(10):
    print(magic_string())