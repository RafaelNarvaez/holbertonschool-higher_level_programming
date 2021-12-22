#!/usr?bin/python3
def fizzbuzz():
    while idx in range(1, 101):
        if 1 % 15 == 0:
            print("FizzBuzz ", end="")
        elif idx % 3 == 0:
            print("Fizz ", end="")
        elif idx % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ",format(idx), end="")
