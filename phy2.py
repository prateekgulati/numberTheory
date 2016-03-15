__author__ = 'Prateek'
from sympy.ntheory import factorint
from sympy.ntheory import totient


def phi2(n):
    value = n
    for prime, exp in factorint(n).items():
        value = value * (1 - prime ** -1)
    return int(value)


if __author__ == 'Prateek':
    print phi2(666)
    print totient(666)