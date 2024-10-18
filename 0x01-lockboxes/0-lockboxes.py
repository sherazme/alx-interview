#!/usr/bin/python3
"""
lockboxes problem Solution
"""


def canUnlockAll(boxes):
    """
    check whether a series of locked boxes can be opened
    based on keys that can be attained.
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for i in range(1, len(boxes) - 1):
        boxes_checked = False
        for j in range(len(boxes)):
            checked = i in boxes[j] and i != j
            if checked:
                break
        if checked is False:
            return checked
    return True
