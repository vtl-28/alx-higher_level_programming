#!/usr/bin/python3

"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def check_nested_list_type(nested_list):
    """
    Check the type of a nested list and the types of its elements.

    Parameters:
        nested_list (list): Nested list to be checked.

    Raises:
        TypeError: If any element in the nested list is not an integer, float

    Returns:
        None
    """
    for elem in nested_list:
        if isinstance(elem, list):
            check_nested_list_type(elem)

        elif not isinstance(elem, (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


def matrix_divided(matrix, div):
    check_nested_list_type(matrix)

    first_list_length = len(matrix[0]) if matrix else 0

    for elem in matrix:
        if len(elem) != first_list_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in l] for l in matrix]
