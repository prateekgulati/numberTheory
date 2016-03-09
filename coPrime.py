__author__ = 'Prateek'
from sympy import gcd


def coPrime(n):
    num = set()
    for i in range(1, n):
        if (gcd(i, n) == 1):
            num.add(i)
    return num


#if __author__ == 'Prateek':
#    print coPrime(8)
