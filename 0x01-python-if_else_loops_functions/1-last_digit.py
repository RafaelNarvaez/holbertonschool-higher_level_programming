#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

newNumber = abs(number) % 10

if newNumber < 0:
    newNumber = -newNumber
    print("Last digit of {} is {} and is ".format(number, newNumber), end="")

if newNumber > 5:
    print("greater than 5")

elif newNumber == 0:
    print("0")

else:
    print("less than 6 and not 0")
