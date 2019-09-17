#!/usr/bin/python3
def no_c(my_string):
    string = my_string.translate({ord('C'): None, ord('c'): None})
    return string
