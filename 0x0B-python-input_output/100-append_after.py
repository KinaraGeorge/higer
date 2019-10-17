#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):

    if None in (search_string, new_string):
        return
    if type(search_string) != str or type(new_string) != str:
        return
    with open(filename, 'r') as f:
        s = f.readlines()

    with open(filename, 'w') as f:
        for i in s:
            if search_string in i:
                i += new_string
            f.write(i)
