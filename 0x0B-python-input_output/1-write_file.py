#!/usr/bin/python3
'''Module Write UTF8 File'''


def write_file(filename="", text=""):
    ''' write into a file '''
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.write(text)
        return len(text)
