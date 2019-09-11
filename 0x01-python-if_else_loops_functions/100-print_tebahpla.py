#!/usr/bin/python3
for z in range(90, 64, -1):
    if z % 2 == 0:
        z += 32
    print("{:s}".format(chr(z)), end="")
