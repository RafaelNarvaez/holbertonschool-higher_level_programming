#!/usr/bin/python3
''' Class Student '''


class Student:
    """ Define Student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' student representation of the Stident instance '''
        return self.__dict__

        new = {}
        for attributes in attrs:
            if attributes in self.__dict__:
                new[attributes] = self.__dict__[attributes]
        return new
