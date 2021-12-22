#!/usr/bin/python3

for idx in range(10):
    for idy in range(idx+1, 10):
        if idx != 8 and idx != 9:
            print("{}{}, ".format(idx, idy), end="")
        else:
            print("{}{}".format(idx, idy))
