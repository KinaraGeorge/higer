#!/usr/bin/python3


class Student:

    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self):

        retdict = {}
        objdict = self.__dict__
        for ele in objdict:
            if type(objdict[ele]) in [list, dict, str, int, bool]:
                retdict[ele] = objdict[ele]
        return retdict
