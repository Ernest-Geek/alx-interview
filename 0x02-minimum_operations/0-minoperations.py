#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return []
    # initialize a list to store the minimum operation
    dp = [0] * (n+1)
    for i in range(2, n+1):
        # initialize with the maximum number value
        dp[i] = i
        # try all possible divisors of i
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)


    return dp[n]
