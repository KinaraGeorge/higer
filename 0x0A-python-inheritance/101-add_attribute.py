#!/usr/bin/python3


def add_attribute(obj, name, value):
    if type(name) is not str:
        raise TypeError("can't add new attribute")
    try:
        exec("obj.{} = value".format(name))
    except:
        raise TypeError("can't add new attribute")
