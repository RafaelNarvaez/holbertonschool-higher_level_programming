#!/usr/bin/python3
'''Module create an Object from JSON def load_from_json_file(filename):'''
import json


def load_from_json_file(filename):
    ''' Loads from JSON file '''
    with open(filename, "r", encoding="utf") as myfile:
        return json.load(myfile)
