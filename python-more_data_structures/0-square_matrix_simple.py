#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for r in matrix:
        m.append([x ** 2 for c in r])
    return m

