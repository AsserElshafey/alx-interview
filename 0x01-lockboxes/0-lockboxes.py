#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    # Initialize a set to keep track of unlocked boxes
    unlocked = set([0])
    # Initialize a list to process boxes that can be unlocked
    keys = [0]
    while keys:
        # Get the current box's keys
        current_keys = boxes[keys.pop()]
        for key in current_keys:
            # If the key corresponds to a box we haven't unlocked yet
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)
    # If the number of unlocked boxes equals the total number of boxes, return True
    return len(unlocked) == len(boxes)
