#!/usr/bin/python3
"""
This module provides an alternative implementation of the isWinner function.
"""


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_n = max(nums)
    sieve = [0] * (max_n + 1)

    for i in range(2, max_n + 1):
        if sieve[i] == 0:
            for j in range(i, max_n + 1, i):
                sieve[j] += 1

    # Count primes up to each index
    prime_counts = [0] * (max_n + 1)
    primes = 0
    for i in range(2, max_n + 1):
        if sieve[i] == 1:
            primes += 1
        prime_counts[i] = primes

    maria_score = 0
    ben_score = 0

    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    return None
