#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for idx in dir(hidden_4):
        if not idx.startswith("__"):
            print("{:s}".format(idx))
