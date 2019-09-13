#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    z = sys.argv

    if len(z) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(z[1])
    b = int(z[3])

    if z[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif z[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif z[2] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif z[2] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
