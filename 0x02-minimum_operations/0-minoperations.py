#!/usr/bin/python3
'''module for Minimum Operations'''


def minOperations(n):
    '''method that calculates the fewest number of
    operations needed to result in exactly'''
    if n <= 1:
        return 0

    # Initialize the number of operations needed for each position
    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
