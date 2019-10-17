#!/usr/bin/python3


def pascal_triangle(n):

    a = []
    if n <= 0:
        return a

    for i in range(n):
        b = [1]
        if a:
            for j in range(i):
                b.append(sum(a[-1][j:j+2]))
        a.append(b)
    return a
