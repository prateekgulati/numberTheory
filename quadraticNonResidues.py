__author__ = 'Prateek'
from quadraticResidues import quadraticResidues
from sympy import isprime


def quadraticNonResidues(n):
    nonResidues = set()
    residues = quadraticResidues(n);
    for elt in range(1, n):
        if elt not in residues:
            nonResidues.add(elt)
    return nonResidues


if __author__ == 'Prateek':
    n = 13
    if isprime(n):
        print quadraticNonResidues(n)
    else:
        print "N is not prime"
