#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1

    if a == 0:
        print("{:d} arguments.".format(a))
    elif a == 1:
        print("{:d} argument:".format(a))
        print("{:d}: {:s}".format(1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(a))
        for i in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(i, sys.argv[i]))
