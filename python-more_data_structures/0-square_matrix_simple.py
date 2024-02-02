#!/usr/bin/python3
def square_matrix_simply(matrix=[]):
    m = []
    for r in matrix:
        m[r] = matrix[r] ** 2
    return m
