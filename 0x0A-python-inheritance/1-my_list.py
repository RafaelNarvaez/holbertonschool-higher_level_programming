#!/usr/bin/python3
''' Inherits List '''


class MyList(list):
    ''' Prints a list in ascending order '''

    def print_sorted(self):
        ''' Prints a sorted list '''
        print(sorted(self))
