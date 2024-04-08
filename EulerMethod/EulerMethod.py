# Write a program to approximate the solutions of ordinary differential equations using Euler's method.

# No external libraries are needed for this program.

from math import (
    sin,
    cos,
    exp,
    log,
    sqrt,
    log10,
    tan,
    atan,
    asin,
    acos,
    sinh,
    cosh,
    tanh,
    asinh,
    acosh,
    atanh,
)


def euler_method(f, x0, y0, h, n):
    """
    Approximate the solution of the ordinary differential equation y' = f(x, y) using Euler's method.

    :param f: The function f(x, y) in the ordinary differential equation y' = f(x, y).
    :param x0: The initial value of x.
    :param y0: The initial value of y at x0.
    :param h: The step size.
    :param n: The number of steps to take.
    :return: A list of n + 1 tuples (x, y) representing the approximated solution.
    """
    x = x0
    y = y0
    result = [(x, y)]
    for i in range(n):
        y += h * f(x, y)
        x += h
        result.append((x, y))
    return result


def main():
    x0 = float(input("Enter the initial value of x: "))
    y0 = float(input("Enter the initial value of y at x0: "))
    h = float(input("Enter the step size h: "))
    n = int(input("Enter the number of steps n: "))
    func_str = input("Enter the function f(x, y): ")

    def f(x, y):
        return eval(func_str, {"x": x, "y": y})

    result = euler_method(f, x0, y0, h, n)
    print("The approximated solution is:")
    for x, y in result:
        print(f"x = {x}, y = {y}")
    return


if __name__ == "__main__":
    main()
