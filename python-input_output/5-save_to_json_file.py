#!/usr/bin/python3
"""  main """

import json


def save_to_json_file(my_obj, filename):
    """ json func """
    with open(filename) as f:
        return f.write(json.dumps(my_obj))
