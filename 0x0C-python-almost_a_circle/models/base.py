#!/usr/bin/python3
''' Module Base Class '''
import json


class Base:
    ''' Class Base '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' define attributes '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        dictionary = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            if list_objs:
                for objects in list_objs:
                    dictionary.append(objects.to_dictionary())
            file.write(cls.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_rect = cls(1, 1)
        if cls.__name__ == "Square":
            new_rect = cls(1)
        new_rect.update(**dictionary)
        return(new_rect)

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + "json", "r") as file:
                return[cls.create(**dictionary) for dictionary
                       in cls.from_json_string(file.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def reset_nb_objects():
        Base._Base__nb_objects = 0
