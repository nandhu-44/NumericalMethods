def fact(n):
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f


def p_terms(p: float, n: int, type="fwd") -> float:
    p_term = 1
    for i in range(n):
        p_term *= p - i if type == "fwd" else p + i
    return p_term
