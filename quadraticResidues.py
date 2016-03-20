__author__ = 'Prateek'
from sympy import isprime


def quadraticResidues(n):
    residues = set()
    for i in range(1, n / 2 + 1):
        residues.add(i ** 2 % n)
    return residues

# if __author__ == 'Prateek':
#    n=11
#    if isprime(n):
#        print quadraticResidues(n)
#    else:
#        print "N is not prime"
