__author__ = 'Prateek'

import sympy

n = 3
x = sympy.symbols('a0:%d' % n)
A = sympy.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
B = sympy.Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

# a0.A + a1.A^2 + a2.A^3

for i in range(3):
    B += A ** (i + 1) * x[i]
print B
