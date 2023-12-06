#!/usr/bin/python3
import dis
import sys
import types


def print_hidden_discovery():
    with open("hidden_4.pyc", "rb") as file:
        code = compile(file.read(), "hidden_4.pyc", "exec")

    for name, obj in code.co_names:
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    print_hidden_discovery()
