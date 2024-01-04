#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

length_of_args = len(sys.argv[1:])
args = sys.argv[1:]

if __name__ == "__main__":
    if length_of_args < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    first_arg = int(args[0])
    operand = args[1]
    second_arg = int(args[2])

    if operand == '+':
        print("{} + {} = {}".format(first_arg, second_arg, add(first_arg, second_arg)))
        sys.exit(0)
    elif operand == '-':
        print("{} - {} = {}".format(first_arg, second_arg, sub(first_arg, second_arg)))
        sys.exit(0)
    elif operand == '*':
        print("{} * {} = {}".format(first_arg, second_arg, mul(first_arg, second_arg)))
        sys.exit(0)
    elif operand == '*':
        print("{} / {} = {}".format(first_arg, second_arg, div(first_arg, second_arg)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
