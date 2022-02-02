#!/usr/bin/python3
'''Module Read UTF8 File'''


def read_file(filename=""):
    ''' read a file '''
    with open(filename, "r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
