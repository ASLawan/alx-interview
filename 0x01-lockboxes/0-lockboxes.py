#!/usr/bin/python3
"""
    Module with a function that implements lockboxes algorithm
    checks if a given list of boxes can all be unlocked or not
"""


def canUnlockAll(boxes):
    """Checks if all the boxes can be unlocked or not"""
    n = len(boxes)

    unlocked = [False] * n

    unlocked[0] = True

    keys = [0]

    while keys:

        current_key = keys.pop()

        for key in boxes[current_key]:

            if key < n and not unlocked[key]:

                unlocked[key] = True

                keys.append(key)

    return all(unlocked)
