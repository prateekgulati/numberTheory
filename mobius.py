__author__ = 'Prateek'
from sympy.ntheory import factorint


def mobius(n):
    primeNos = 0
    if n < 1:
        return "Invalid"
    if n == 1:
        return 1
    for prime, exp in factorint(n).items():
        if exp >= 2:
            return 0
        primeNos = primeNos + 1
    if primeNos % 2 == 0:
        return 1
    else:
        return -1


if __author__ == 'Prateek':
    for i in range(1, 31):
        print mobius(i),
