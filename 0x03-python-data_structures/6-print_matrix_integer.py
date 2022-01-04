#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx in row:
            if idx is not row[len(row) - 1]:
                print("{:d}".format(idx), end=" ")
            else:
                print("{:d}".format(idx), end="")
        print()
