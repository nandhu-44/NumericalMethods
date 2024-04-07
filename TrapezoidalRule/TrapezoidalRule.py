# Write a program to find the approximate value of the integral of a function using Trapezoidal rule.

from math import e, log10, log2, sin, cos, tan, pi, sqrt, exp, log


def f(x, func):
    return eval(func)


def trapezoidal_rule(a, b, n, func):
    h = (b - a) / n
    x = a
    sum = f(x, func)

    for i in range(1, n):
        x += h
        sum += 2 * f(x, func)

    sum += f(b, func)
    integral = (h / 2) * sum

    return integral


def main():
    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))
    n = int(input("Enter the number of subintervals: "))
    func = input("Enter the function to integrate: ")

    approx_integral = trapezoidal_rule(a, b, n, func)
    print(
        f"The approximate value of the integral of {func} from {a} to {b} is {approx_integral:.6f}"
    )


if __name__ == "__main__":
    main()
