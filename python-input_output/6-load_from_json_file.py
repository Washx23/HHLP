#!/usr/bin/python3
"""  main """

import json


def load_from_json_file(filename):
    """ load_from_json func """
    with open(filename, 'r') as f:
        new_line = json.load(f)
        return new_line
