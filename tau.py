__author__ = 'Prateek'
from divisors import divisors


def tau(n):
    return divisors(n).__len__()


if __author__ == 'Prateek':
    print tau(10)
