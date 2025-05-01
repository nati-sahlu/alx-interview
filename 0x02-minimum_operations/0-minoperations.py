#!/usr/bin/python3
""" Minimum Operations
    """


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters using only Copy All and Paste operations.
    """

    if n < 2:
        return 0

    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n //= x
        x += 1
    return result
