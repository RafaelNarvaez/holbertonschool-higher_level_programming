#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

ld = "Last digit of"

if number < 0:
    Num = number % -10

else:
    Num = number % 10

if Num > 5:
    print("{} {} is {} and is greater than 5".format(ld, number, Num))

elif Num == 0:
    print("{} {} is {} and is 0".format(ld, number, number % 10))

else:
    print("{} {} is {} and is less than 6 and not 0".format(ld, number, Num))
