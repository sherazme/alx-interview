#!/usr/bin/python3
"""
Minimum Operations's
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations 
    needed to result in exactly n H characters in the file.
    """

    if n <= 1:
        return 0
    i, div, num = n, 2, 0

    while i > 1:
        if i % div == 0:
            i = i / div
            num = num + div
        else:
            div += 1
    return num
