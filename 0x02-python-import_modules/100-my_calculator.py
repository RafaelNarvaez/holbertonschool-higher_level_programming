#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()
argc = len(argv) - 1
if argc != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)

a = int(argv[1])
b = int(argv[3])

elif argv[2] == '+':
    func = add(a, b)
    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, func)
elif argv[2] == '-':
    func = sub(a, b)
    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, func)
elif argv[2] == '*':
    func = mul(a, b)
    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, func)
elif argv[2] == '/':
    func = div(a, b)
    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, func)
else:
    print("Unknown operator. Available operators: +, -, *, and /")
    exit(1)
