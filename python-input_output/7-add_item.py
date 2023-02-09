#!/usr/bin/python3
""" main """


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

""" main """



filename = "add_item.json"
args = sys.argv[1:]
""" main """


try:
    with open(filename, 'a+', encoding="utf-8") as f:
        my_list = load_from_json_file(filename)

except FileNotFoundError:
    my_list = []
my_list.extend(args)
save_to_json_file(my_list, filename)
