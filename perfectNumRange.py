__author__ = 'Prateek'
from perfectNumber import perfectNumber


def perfectNumRange(n):
    list = []
    for i in range(1, n + 1):
        if perfectNumber(i) == True:
            list.append(i)
    return list


if __author__ == 'Prateek':
    print perfectNumRange(1000)
