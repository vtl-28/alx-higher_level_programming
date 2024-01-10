#!/usr/bin/python3

def square(elements):
    new_list = []
    for i in elements:
        new_list.append(i * i)

    return (new_list)


def square_matrix_simple(matrix=[]):
    new_list = []

    if len(matrix) < 1:
        return (None)

    for i in matrix:
        new_list.append(square(i))

    return (new_list)
