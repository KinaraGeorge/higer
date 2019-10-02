#!/usr/bin/python3
class Square:
    """empty class Square that defines a square"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Defines the area of a square'''
        return self.__size * self.__size

    @property
    def size(self):
        """Return size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
