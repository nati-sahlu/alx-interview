#!/usr/bin/python3
"""
Checks if all boxes can be opened
"""


def canUnlockAll(boxes):
    if not boxes:
        return False

    opened = set([0])
    keys = boxes[0].copy()

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == len(boxes)
