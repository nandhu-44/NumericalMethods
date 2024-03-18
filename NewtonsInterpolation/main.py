from NewtonsForwardInterpolation import newton_forward_interpolation
from NewtonsBackwardInterpolation import newton_backward_interpolation


def main():
    x = [float(i) for i in input("Enter the values of x: ").split()]
    y = [float(i) for i in input("Enter the values of y: ").split()]
    x0 = float(input("Enter the value of x0: "))

    median = len(x) // 2
    if x0 < x[median] or x0 > x[-1]:
        result = newton_forward_interpolation(x, y, x0)
        print(f"The value of y at x = {x0} using Forward Interpolation is {result}")
    else:
        result = newton_backward_interpolation(x, y, x0)
        print(f"The value of y at x = {x0} using Backward Interpolation is {result}")


if __name__ == "__main__":
    main()
