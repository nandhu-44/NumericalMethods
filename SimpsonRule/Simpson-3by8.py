# Write a program to find the approximate value of the integral of a function using Simpson's 1/3 rule.

from math import e, log10, log2, sin, cos, tan, pi, sqrt, exp, log


def f(x, func):
    return eval(func)


def simpsons_3by8(a, b, n, func):
    if n % 3 != 0:
        print("The number of subintervals must be a multiple of 3.")
        exit()
    h = (b - a) / n
    x = a
    sum = f(x, func)

    for i in range(1, n):
        x += h
        if i % 3 == 0:
            sum += 2 * f(x, func)
        else:
            sum += 3 * f(x, func)

    sum += f(b, func)
    integral = (3 * h / 8) * sum

    return integral


def main():
    a = float(input("Enter the lower limit of integration: "))
    b = float(input("Enter the upper limit of integration: "))
    n = int(input("Enter the number of subintervals: "))
    func = input("Enter the function to integrate: ")

    approx_integral = simpsons_3by8(a, b, n, func)
    print(
        f"The approximate value of the integral of {func} from {a} to {b} is {approx_integral:.6f}"
    )


if __name__ == "__main__":
    main()
