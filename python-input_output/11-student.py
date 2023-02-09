#!/usr/bin/python3
""" main """


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_list = {}
            for i in attrs:
                if hasattr(self, i):
                    new_list[i] = getattr(self, i)
            return new_list

    def reload_from_json(self, json):
        self.__dict__ = json