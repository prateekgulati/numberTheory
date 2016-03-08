__author__ = 'Prateek'
from sigma import sigma


def perfectNumber(n):
    if sigma(n) == 2 * n:
        return True
    return False

#if __author__=='Prateek':
#    print perfectNumber(6)
