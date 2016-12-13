__author__ = 'Prateek'

import math
from numpy import matrix, linalg, resize
from itertools import product, combinations


def compound(matrix, k):
    determinant = []
    nCk = combinations(range(len(matrix)), k)
    for index in product(nCk, repeat=2):
        # print index
        minor = []
        for i in index[0]:
            for j in index[1]:
                minor.append(matrix[i, j])
        determinant.append(linalg.det(resize(minor, (k, k))))
    dim = int(math.sqrt(len(determinant)))
    return resize(determinant, (dim, dim))


if __name__ == '__main__':
    A = matrix([[7, 3, 9, 5], [7, 6, 5, 9], [9, 7, 6, 3], [8, 1, 2, 6]],dtype=int)
    # A=numpy.matrix([[2,1,0,0],[1,2,1,0],[0,1,2,1],[0,0,1,2]],dtype=int)
    # A=numpy.matrix([[11,12,13,14],[21,22,23,24],[31,32,33,34],[41,42,43,44]],dtype=int)
    print A
    k = 3
    matrix=compound(A, k)
    print matrix