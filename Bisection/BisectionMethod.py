# Write a program to find the roots of a non linear equation using Bisection method

def bisect(function : str, a : int, b : int, Epsilon : float) -> float :
    if function(a) * function(b) >= 0:
        return None
    c = None 
    while ((b-a) >= Epsilon):
        c = (a + b) / 2
        if function(c) == 0.0:
            break
        if function(c) * function(a) < 0:
            b = c
        else:
            a = c
    return c


def main():
    function = input("Enter the function in terms of x: ")
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    Epsilon = float(input("Enter the value of ε: "))
    func = lambda x: eval(function)
    root = bisect(func, a, b, Epsilon)
    if root is not None:
        print("The value of root is : ", "%.4f"%root)
    else:
        print("Can't find root in given interval")
        
if __name__ == "__main__":
    main()