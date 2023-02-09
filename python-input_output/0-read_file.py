#!/usr/bin/python3
"""  main """

def read_file(filename=""):
    """ read_file func """
    with open(filename) as f:
        new_line = f.read()
        print(new_line, end="")
