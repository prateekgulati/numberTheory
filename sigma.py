__author__ = 'Prateek'
from divisors import divisors


def sigma(n):
    sum = 0
    for i in divisors(n):
        sum = sum + i
    return sum

# if __author__=='Prateek':
#    print sigma(9)
