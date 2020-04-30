#!/usr/bin/python3
import hidden_4


def main():
    ls = dir(hidden_4)
    for i in range(len(ls)):
        if(ls[i][0] != '_'):
            print("{}".format(ls[i]))

if __name__ == "__main__":
    main()
