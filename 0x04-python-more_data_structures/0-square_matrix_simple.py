#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_matrix = []
    for i in matrix:
        n_i = []
        for j in i:
            n_i.append(j ** 2)
        n_matrix.append(n_i)
    return (n_matrix)
