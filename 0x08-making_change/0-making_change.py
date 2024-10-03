#!/usr/bin/python3
"""
    Module implementing making_change function

"""


def makeChange(coins, total):
    """Computes minimum number of coins needed for the total"""
    # Edge case
    if total <= 0:
        return 0

    # Initialize dp array with a large value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0
    # Update dp array using the coins

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    # If dp[total] is still inf, return -1
    # as it's not possible to make the amount
    return dp[total] if dp[total] != float('inf') else -1
