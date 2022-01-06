#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new = []
        for idx in matrix:
            new.append(list(map(lambda x: x**2, idx)))
        return (new)
    return None
