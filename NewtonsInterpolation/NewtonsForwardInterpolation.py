# Write a program to estimate the x0 of a function for any intermediate x0 of the independent variable using Newton's forward interpolation formula.

from utils import *


def newton_forward_interpolation(x: list, y: list, x0: float) -> float:
    n = len(x)
    h = x[1] - x[0]
    p = (x0 - x[0]) / h
    y_new = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        y_new[i][0] = y[i]

    for i in range(1, n):
        for j in range(n - i):
            y_new[j][i] = y_new[j + 1][i - 1] - y_new[j][i - 1]

    y0 = y_new[0][0]
    for i in range(1, n):
        y0 += (p_terms(p, i) * y_new[0][i]) / fact(i)
    return y0
