#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for a in range(1, len(sys.argv)):
        result += int(sys.argv[a])
    print("{:d}".format(result))
