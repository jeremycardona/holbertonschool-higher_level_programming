#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m = []
    for row in matrix:
        m.append([column ** 2 for column in row])
    return m
