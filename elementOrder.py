__author__ = 'Prateek'
from sympy import totient
from divisors import divisors
from coPrime import coPrime


def order(n, elt):
    if elt in coPrime(n):
        for i in sorted(divisors(totient(n))):
            if elt ** i % n == 1:
                return i
    else:
        return "Element not in set"


#if __author__ == 'Prateek':
#    n=10
#    print order(n,3)            #similar to n_order in sympy
