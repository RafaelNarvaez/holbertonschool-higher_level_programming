#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    idx = len(argv)
    result = 0
    if idx - 1 ==0:
        print 0
    else:
        for idy in range(1, idx):
            result += int(argv[idy])
            print("{:d}".format(result))
