#!/usr/bin/python3
'''Module save JSON to an Object '''
import json


def save_to_json_file(my_obj, filename):
    ''' Writes and save a JSON file '''
    with open(filename, "w", encoding="utf") as myfile:
        json.dump(my_obj, myfile)
