#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    print("{:d} argument{}{}".format(
        argc, "" if argc == 1 else "s", ":" if argc > 0 else "."))

    for i in range(1, argc + 1):
        print("{:d}: {}".format(i, argv[i]))
