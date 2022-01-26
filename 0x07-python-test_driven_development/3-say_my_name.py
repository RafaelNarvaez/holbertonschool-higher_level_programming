#!/usr/bin/python3
""" Test-driven development
   say_my_name - Arg:
        fist_name: str
        last_name: str
"""


def say_my_name(first_name, last_name=""):
    """
    Print my first and last name
    """
    if type(first_name) is str:
        if type(last_name) is str:
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")
