#!/usr/bin/python3
''' Module Append UTF8 File '''


def append_write(filename="", text=""):
    ''' appends a file '''
    with open(filename, "a", encoding="utf-8") as myfile:
        myfile.write(text)
        return len(text)
