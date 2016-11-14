#!/usr/bin/env python3
def find_max_min(l):
    """
    Returns list containing [min, max]
    If elements are equal return [list length]
    """
    l.sort()
    if l[0] != l[-1]:
        return [l[0], l[-1]]
    elif l[0] == l[-1]:
        return [len(l)]
