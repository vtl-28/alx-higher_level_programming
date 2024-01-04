#!/usr/bin/python3
import sys

length_of_args = len(sys.argv[1:])
args = sys.argv[1:]

if length_of_args < 1:
    print("0 arguments.")
else:
    if length_of_args == 1:
        print("{} argument:".format(length_of_args))
    else:
        print("{} arguments:".format(length_of_args))
    for arg in range(0, length_of_args):
        print("{}: {}".format(arg + 1, args[arg]))
