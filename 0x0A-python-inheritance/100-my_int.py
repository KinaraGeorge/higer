#!/usr/bin/python3


class MyInt(int):

    def __init__(self, myint):
        self.myint = myint

    def __eq__(int1, int2):
        return int1.myint != int2

    def __ne__(int1, int2):
        return int1.myint == int2
