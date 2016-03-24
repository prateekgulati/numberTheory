__author__ = 'Prateek'
from sympy import isprime

def isQuadraticResidue(p, a):
    if isprime(p):
        if a ** ((p - 1) / 2) % p == 1:
            return True
        else:
            return False
    else:
        return "N not a prime"

#if __author__ == 'Prateek':
#    n = 14
#    a = 10
#    print isQuadraticResidue(n, a)
