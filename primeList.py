__author__ = 'Prateek'
from sympy import prime

def primeList(beg, n):
    primeList = list()
    for i in range(beg,n+beg):
        primeList.append(prime(i))
    return primeList

#if __author__ == 'Prateek':
#    n = 7
#    beg = 3
#    print primeList(beg,n)

