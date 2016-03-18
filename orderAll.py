__author__ = 'Prateek'
from coPrime import coPrime
from elementOrder import order


def orderAll(n):
    for elt in coPrime(n):
        print "Order of ", elt, "is", order(n, elt)

if __author__ == 'Prateek':
    n=9
    orderAll(n)
