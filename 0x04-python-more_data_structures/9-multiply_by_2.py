#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for idx in a_dictionary:
        new[idx] = a_dictionary[idx] * 2
    return(new)
