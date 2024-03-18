# Write a program to estimate the value of a function for any intermediate value of the independent variable using Lagrange's Interpolation formula.

def lagrange_interpolation(x, y, x0):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term = term * (x0 - x[j]) / (x[i] - x[j])
        result += term
    return result


def main():
    x = [float(i) for i in input("Enter the values of x: ").split()]
    y = [float(i) for i in input("Enter the values of y: ").split()]
    x0 = float(input("Enter the value of x0: "))

    result = lagrange_interpolation(x, y, x0)
    print(f"The value of y at x = {x0} using Lagrange Interpolation is {result}")
    

if __name__ == "__main__":
    main()
