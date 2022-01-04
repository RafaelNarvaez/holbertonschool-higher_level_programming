#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        valor = False
        if i % 2 == 0:
            valor = True
        new_list.append(valor)

    return new_list
