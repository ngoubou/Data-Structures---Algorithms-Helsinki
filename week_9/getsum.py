def count(n, k, x):
    # Create a 2D table to store the subproblem solutions
    dp = [[0] * (x + 1) for _ in range(k + 1)]

    # Base case: If k is 0 and x is 0, there is only one way (selecting none)
    dp[0][0] = 1

    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for j in range(k, 0, -1):
            for s in range(x, i - 1, -1):
                dp[j][s] += dp[j - 1][s - i]

    # Return the count of ways to choose k numbers with sum x
    return dp[k][x]

if __name__ == "__main__":
    print(count(1, 1, 1))   # Expected output: 1
    print(count(5, 2, 6))   # Expected output: 2
    print(count(8, 3, 12))  # Expected output: 6
    print(count(10, 4, 20)) # Expected output: 16
