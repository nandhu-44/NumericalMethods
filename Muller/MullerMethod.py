# Write a program to find the root of a given function using Mullers Method.

from math import sqrt, sin, cos, tan, log, pi

def muller_method(f : str, x0 : float, x1 : float, x2 : float, tol : float = 1e-6, max_iter : int = 100) -> float | str :
    h1 = x1 - x0
    h2 = x2 - x1
    delta1 = (f(x1) - f(x0)) / h1
    delta2 = (f(x2) - f(x1)) / h2
    d = (delta2 - delta1) / (h2 + h1)
    
    i = 3
    while i <= max_iter:
        b = delta2 + h2 * d
        D = sqrt(b**2 - 4 * f(x2) * d)
        
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        
        h = -2 * f(x2) / E
        p = x2 + h
        
        if abs(h) < tol:
            return p
        
        x0 = x1
        x1 = x2
        x2 = p
        
        h1 = x1 - x0
        h2 = x2 - x1
        delta1 = (f(x1) - f(x0)) / h1
        delta2 = (f(x2) - f(x1)) / h2
        d = (delta2 - delta1) / (h2 + h1)
        
        i += 1
    
    return p

def get_decimals(Epsilon: float)-> int:
    return len(str(Epsilon).split(".")[1])

def decimal_rounded(x: float, decimals : int) -> str:
    dec_in_x = get_decimals(x)
    if dec_in_x < decimals :
        return str(x)
    else :
        rounded_str = str(round(x, decimals))
        for i in rounded_str.split(".")[1] :
            if i != 0 :
                return rounded_str
        return rounded_str.split(".")[0]

def main():
    function = input("Enter the function in terms of x : ")
    x0 = float(input("Enter the value of x0 : "))
    x1 = float(input("Enter the value of x1 : "))
    x2 = float(input("Enter the value of x2 : "))
    Epsilon = float(input("Enter the value of epsilon : "))
    max_iter = int(input("Enter the maximum no of iterations : "))
    func = lambda x : eval(function)
    root = muller_method(func, x0, x1, x2, Epsilon, max_iter )
    if root is None :
        print("Unable to find the roots in the given interval.")
    else:
        print(f"Root : {decimal_rounded(root, get_decimals(Epsilon))}")
    
if __name__ == "__main__":
    main()
    
