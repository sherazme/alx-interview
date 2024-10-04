#!/usr/bin/env python3
from typing import List


def pascal_triangle(n: int) -> List[list]:
    '''
    Pascal’s triangle of n representation
    '''
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    Pascal_try = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]
        for j in range(0, len(Pascal_try[-1])-1):

            temp.insert(-1, Pascal_try[-1][j] + Pascal_try[-1][j+1])
        Pascal_try.append(temp)

    return Pascal_try
