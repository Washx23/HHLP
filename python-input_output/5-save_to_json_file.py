#!/usr/bin/python3
"""  main """

import json


def save_to_json_file(my_obj, filename):
    """ json func """
    with open(filename, 'w') as f:
        new_line = f.write(json.dumps(my_obj))
        return new_line
