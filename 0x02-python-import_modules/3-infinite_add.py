#!/usr/bin/python3
import sys


def main(*argv):
    sum = 0
    for args in sys.argv:
            if args != sys.argv[0]:
                sum += int(args)
    print("{}".format(sum))
if __name__ == "__main__":
    main()
