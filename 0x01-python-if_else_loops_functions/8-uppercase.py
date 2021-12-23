#!/usr/bin/python3
def uppercase(str):

    idx = ''
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            idx += chr(ord(letter) - 32)
        else:
            idx += letter
    print("{}".format(idx))
