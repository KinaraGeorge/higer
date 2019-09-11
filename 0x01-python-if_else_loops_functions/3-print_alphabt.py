#!/usr/bin/python3
for lowercase_letter in range(97, 123):
    if lowercase_letter != 101 and lowercase_letter != 113:
        print("{:c}".format(lowercase_letter),  end="")
