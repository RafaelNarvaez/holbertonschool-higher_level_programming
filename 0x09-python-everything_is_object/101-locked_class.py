#!/usr/bin/python3
"""Define LockedClass"""


class LockedClass():
    """Empty class that prevents new instance attributes
       except if the new instance attribute is called first_name
    """
    __slots__ = ["first_name"]
