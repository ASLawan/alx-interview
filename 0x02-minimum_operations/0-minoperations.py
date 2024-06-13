#!/usr/bin/python3
"""
    Module implementing a function that returns minimum number of
    operations required to arrive at a solution

"""


def minOperations(n: int) -> int:
    """Returns minimum number of operations"""
    if n <= 1:
        return 0

    count = 0
    prime_factor = 2

    while n > 1:
        while n % prime_factor == 0:
            count += prime_factor
            n //= prime_factor
        prime_factor += 1

    return count
