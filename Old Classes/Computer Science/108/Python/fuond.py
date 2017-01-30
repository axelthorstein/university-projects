def contains(value, lst):
    """ (object, list of list of object) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    """

    found = False  # We have not yet found value in the list.

    for item in lst:
        if value == item:
            value = True

    return found