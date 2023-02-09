#!/usr/bin/python3
"""  main """


def write_file(filename="", text=""):
    """ read_file func """
    with open(filename, 'w') as f:
        new_line = f.write(text)
        return new_line
