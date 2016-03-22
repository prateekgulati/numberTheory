__author__ = 'Prateek'
from isQuadraticResidue import isQuadraticResidue

def legendre(p, a):
    if isQuadraticResidue(p,a):
        return 1
    else:
        return -1

#if __author__ == 'Prateek':
#    n = 7
#    a = 3
#    print legendre(n,a)

