#!/usr/bin/python3
"""  main """


def append_write(filename="", text=""):
    """ read_file func """
    with open(filename, 'a') as f:
        new_line = f.write(text)
        return new_line
