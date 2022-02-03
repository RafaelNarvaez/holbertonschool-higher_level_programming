#!/usr/bin/python3
''' Module Boolean '''


def inherits_from(obj, a_class):
    ''' Identifies an instance '''
    return type(obj,) != a_class and isinstance(obj, a_class)
