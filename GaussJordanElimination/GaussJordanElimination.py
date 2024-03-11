def gauss_jordan(A, b):
    """
    Gauss-Jordan Elimination Method for solving a system of linear equations

    Parameters:
    A (list of lists): Coefficient matrix of the system of equations
    b (list): Constant vector on the right-hand side

    Returns:
    x (list): Solution vector
    """

    n = len(A)
    augmented_matrix = [row + [bi] for row, bi in zip(A, b)]

    for i in range(n):
        pivot_row = max(range(i, n), key=lambda k: abs(augmented_matrix[k][i]))
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]

        pivot_value = augmented_matrix[i][i]
        for j in range(i, n + 1):
            augmented_matrix[i][j] /= pivot_value

        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(i, n + 1):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    x = [row[-1] for row in augmented_matrix]

    return x


def main():
    A = [[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
    b = [7.85, -19.3, 71.4]

    solution = gauss_jordan(A, b)
    for i, xi in enumerate(solution):
        print(f"x{i+1} = {round(xi, 4)}")


if __name__ == "__main__":
    main()
