#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for idx in set(my_list):
        total += idx
    return(total)
