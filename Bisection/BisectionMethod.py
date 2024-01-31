# Write a program to find the roots of a non linear equation using Bisection method

__import__("os").system('cls' if __import__("os").name == 'nt' else 'clear')

def bisect(function : str, a : int, b : int, Epsilon : float) -> float :
    if function(a) * function(b) >= 0:
        return None
    c = None
    i : int = 0
    dec : int = get_decimals(Epsilon)
    while ((b-a) >= Epsilon):
        c = (a + b) / 2
        if function(c) == 0.0:
            break
        if function(c) * function(a) < 0:
            b = c
        else:
            a = c
        i = i + 1
        print(f"Iteration {i}; a = ", trim_float(f"{a:.{dec}f}"), "b = ", trim_float(f"{b:.{dec}f}"), "c = ", trim_float(f"{c:.{dec}f}"), "f(c) = ", trim_float(f"{function(c):.{dec}f}"))
    return c

def get_decimals(Epsilon : float) -> int:
    s = str(Epsilon)
    if 'e' in s:
        return int(s.split('e-')[1])
    else:
        return len(s) - s.index('.') - 1
    
def trim_float(number : float) -> float:
    return str(number).rstrip('0').rstrip('.') if '.' in str(number) else number

def main():
    function = input("Enter the function in terms of x: ")
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    Epsilon = float(input("Enter the value of ε: "))
    func = lambda x: eval(function)
    root = bisect(func, a, b, Epsilon)
    if root is not None:
        print(f"The value of root is :  {root:.{get_decimals(Epsilon)}f}")
    else:
        print("Can't find root in given interval")
        
if __name__ == "__main__":
    main()