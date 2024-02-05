# Write a program to find the root of a given function using Newton-Raphson method.

from sympy import symbols, diff
from math import sin, cos, exp, log, tan, pi, e

def newton_raphson(function, derivative, x0, Epsilon, itmax):
    i = 0
    while i < itmax:
        x1 = x0 - function(x0) / derivative(x0)
        if abs(x1 - x0) < Epsilon:
            print(f"Iteration {i+1}; x{i+1} = {x1:.6f}, f(x{i+1}) = {function(x1):.6f}")
            return x1
        print(f"Iteration {i+1}; x{i+1} = {x1:.6f}, f(x{i+1}) = {function(x1):.6f}")
        x0 = x1
        i += 1
    print("Exceeded maximum iterations. No solution found.")
    return None

def get_decimals(Epsilon : float) -> int:
    s = str(Epsilon)
    if 'e' in s:
        return int(s.split('e-')[1])
    else:
        return len(s) - s.index('.') - 1

def round_to_n(x, n):
    return round(x, n - len(str(int(x))) - 1)

def main():
    x = symbols('x')
    function_expression = input("Enter the function in terms of x : ")
    func = lambda x: eval(function_expression)
    derivative_expression = str(diff(function_expression, x))
    derivative_func = lambda x: eval(derivative_expression)
    x0 = float(input("Enter the initial guess (x0) : "))
    Epsilon = float(input("Enter the value of ε : "))
    itmax = int(input("Enter the maximum number of iterations : "))
    root = newton_raphson(func, derivative_func, x0, Epsilon, itmax)
    if root is not None:
        print(f"The value of root is :  {round(root, get_decimals(Epsilon)):.{get_decimals(Epsilon)}f}")
    else:
        print("Can't find root in given interval")

if __name__ == "__main__":
    main()