#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """
    How many of this type of coin can I get with my money? Okay,
        I'll take that many. Now, how much money do I have left?
        And how many coins do I have in my pocket?
    """
    if total < 1:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        num = total // coin
        total -= num * coin
        count += num
    return count if total == 0 else -1
