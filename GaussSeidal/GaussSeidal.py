def gauss_seidel(A, b, max_iter=100, tol=1e-4):
    """
    Gauss-Seidel Method for solving a system of linear equations

    Parameters:
    A (list of lists): Coefficient matrix of the system of equations
    b (list): Constant vector on the right-hand side
    max_iter (int): Maximum number of iterations
    tol (float): Tolerance for convergence

    Returns:
    x (list): Solution vector
    """

    n = len(A)
    x = [0] * n
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            sigma = 0
            for j in range(n):
                if i != j:
                    sigma += A[i][j] * x_new[j]
            x_new[i] = (b[i] - sigma) / A[i][i]

        # Check for convergence
        diff = [abs(x_new[i] - x[i]) for i in range(n)]
        if max(diff) < tol:
            return x_new, k + 1

        x = x_new

    print(
        "Warning: Gauss-Seidel method did not converge within the specified number of iterations."
    )
    return x, max_iter


def main():
    A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    b = [7.85, -19.3, 71.4]

    solution, iterations = gauss_seidel(A, b)
    print(f"Solution after {iterations} iterations:")
    for i in range(len(solution)):
        print(f"x{i+1} = {round(solution[i], 4)}")


if __name__ == "__main__":
    main()
