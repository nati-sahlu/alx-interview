#!/usr/bin/python3
"""Module for Prime Game."""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str or None: Winner ("Maria" or "Ben") or None if it's a tie.
    """
    if not nums or x < 1 or x != len(nums):
        return None

    n = max(nums)
    sieve = [True for _ in range(max(n + 1, 2))]
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    prime_counts = [0] * (n + 1)
    count = 0
    for i in range(len(sieve)):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria = 0
    for num in nums:
        if prime_counts[num] % 2 == 1:
            maria += 1

    if maria * 2 == x:
        return None
    return "Maria" if maria * 2 > x else "Ben"

