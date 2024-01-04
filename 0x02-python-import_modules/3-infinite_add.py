#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    length_of_args = len(args)
    sum_of = 0

    for i in range(0, length_of_args):
        sum_of += int(args[i])

    print(sum_of)
