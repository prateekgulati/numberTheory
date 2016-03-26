__author__ = 'Prateek'
from legendre import legendre
from primeList import primeList
import numpy


def legendreMatrix(n):
    primes = primeList(2, n)
    array = []
    for i in primes:
        row = []
        for j in primes:
            if i != j:
                row.append(legendre(i, j))
            else:
                row.append(0)
        array.append(row)
    return numpy.array(array)


if __author__ == 'Prateek':
    n = 7
    arr = legendreMatrix(n)
    print "Matrix: \n",arr