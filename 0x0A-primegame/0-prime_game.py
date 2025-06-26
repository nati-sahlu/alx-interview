#!/usr/bin/python3
"""Module defining isWinner function."""


def sieve_of_eratosthenes(limit):
    """Return a list of number of primes up to each i <= limit."""
    primes = [True] * (limit + 1)
    primes[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i*i, limit + 1, i):
                primes[multiple] = False

    prime_counts = [0] * (limit + 1)
    count = 0
    for i in range(len(primes)):
        if primes[i]:
            count += 1
        prime_counts[i] = count
    return prime_counts


def isWinner(x, nums):
    """Determine who the winner of the game is after x rounds."""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    prime_counts = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

