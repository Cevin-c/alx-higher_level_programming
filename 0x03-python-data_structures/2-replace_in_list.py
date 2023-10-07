#!/usr/bin/python3


def replace_in_list(my_list, idx, elements):
    """Replace an elements of a list at a specific position."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = elements
    return (my_list)
