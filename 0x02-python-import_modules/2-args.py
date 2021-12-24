#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    str = "argument"
    if argc == 0:
        print("0 {}s.".format(str))
    else:
        if argc > 1:
            str += "s"
        str += ":"
        print(argc, str)
        for idx in range(1, argc+1):
            print("{}:".format(idx), sys.argv[idx])
