#!/usr/bin/python3
''' module to open the boxes'''


def canUnlockAll(boxes):
    ''' function to open the boxes'''
    open = set([0])
    closed = set(boxes[0]).difference(open)

    while len(closed) > 0:
        key = closed.pop()

        if key is not in open:
            open.add(key)
            closed = closed.union(boxes[key]).difference(open)
    return len(open) == len(boxes)
