#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    big = my_list[0]
    for idx in my_list:
        if idx > big:
            big = idx
    return big
