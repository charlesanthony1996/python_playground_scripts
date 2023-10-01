import numpy as np

def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1
    dp = [[float("inf")] * n for _ in range(n)]

    # initialize diagonal elements to 0 since multiplying a single matrix has no cost
    for i in range(n):
        dp[i][i] = 0


    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            for k in range(i, j):
                # compute the number of multiplications for the current parenthesization
                cost = dp[i][k] + dp [k+ 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j+ 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

                
    def parenthesize(i, j):
        if i == j:
            return f"M{i + 1}"
        else:
            for k in range(i, j):
                if dp[i][j] == dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k+ 1] * dimensions[j + 1]:
                    left = parenthesize(i, k)
                    right = parenthesize(k + 1, j)
                    return f"({left} * {right})"

                
    optimal_parenthesization = parenthesize(0, n - 1)
    min_multiplications = dp[0][n- 1]

    return optimal_parenthesization, min_multiplications


# example usage
matrix_dimensions = [10, 3, 5, 60]
optimal_order, min_multiplications = matrix_chain_multiplication(matrix_dimensions)

print("optimal order: ", optimal_order)
print("minimum multiplications: ", min_multiplications)