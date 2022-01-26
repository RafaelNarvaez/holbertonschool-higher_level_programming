#!/usr/bin/python3
"""
Test-driven development
    text_indentation - Arg:
        text: str
"""


def text_indentation(text):
    """
    Put double \n after :, ?, .
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = True
    for c in text:
        if c == " " and flag:
            continue
        elif flag:
            flag = False
        if c not in [".", ":", "?"]:
            print(c, end="")
            continue
        elif not flag:
            print(c, end="\n\n")
            flag = True
