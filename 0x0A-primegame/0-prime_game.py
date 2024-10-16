#!/usr/bin/python3
"""
Module implementing the Prime Game
"""


def isWinner(x, nums):
    """Funtion that determines game winner"""
    def is_prime(num):
        """function dtermines if a number is prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    # Precompute prime numbers up to the maximum possible n in nums
    max_n = max(nums)
    primes = [False, False] + [True] * (max_n - 1)
    for i in range(2, int(max_n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_n + 1, i):
                primes[j] = False

    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        # Count the number of primes up to n
        prime_count = sum(1 for i in range(2, n + 1) if primes[i])

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
