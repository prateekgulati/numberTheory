__author__ = 'Prateek'
from sympy import primerange

def phi(n):
    value = n
    for i in primerange(1, n):
        if n % i == 0:
            value = value * (1 - i ** -1)
    return int(value)


if __author__ == 'Prateek':
    print phi(666)