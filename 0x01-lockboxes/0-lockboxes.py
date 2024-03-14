#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """

    unlocked = set([0])
    keys = [0]
    while keys:
        current_keys = boxes[keys.pop()]
        for key in current_keys:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)
    return len(unlocked) == len(boxes)
