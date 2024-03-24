#!/usr/bin/python3
"""Minimum operation challenge in python"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to achieve n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed.

    Raises:
        ValueError: If n is less than or equal to 1.

    """
    if n <= 1:
        raise ValueError("n must be greater than 1")
    
    # Initialize a list to store the minimum operations
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        # Initialize with the maximum number value
        dp[i] = i
        
        # Try all possible divisors of i
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
