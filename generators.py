__author__ = 'Prateek'
from coPrime import coPrime
from sympy import totient
from elementOrder import order


def generators(n):
    list = []
    for elt in coPrime(n):
        if order(n, elt) == totient(n):
            list.append(elt)
    return list


if __author__ == 'Prateek':
    n = 13
    print "Number of generators for",13," are",totient(totient(n))
    print generators(n)

