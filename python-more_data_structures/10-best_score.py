#!/usr/bin/python3
def best_score(a_dictionary):
    return max(a_dictionary, key=lambda x: a_dictionary[x]) if a_dictionary else None
