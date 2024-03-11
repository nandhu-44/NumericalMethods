def gauss_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    solution = [row[n] for row in matrix]

    return solution


if __name__ == "__main__":
    coefficient_matrix = [[4, 2, 3, 4], [2, 2, 1, 6], [1, 1, 1, 0]]

    solution = gauss_elimination(coefficient_matrix)
    print("Solution:")
    for i, value in enumerate(solution):
        print(f"x{i+1} = {round(value, 4)}")
