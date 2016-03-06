__author__ = 'Prateek'
from math import sqrt


def divisors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))

# if __author__=='Prateek':
#    print divisors(666)
