def first_even(items):
    """ (list of int) -> int
    
    Return the first even number from items. Return -1 if items contains no even numbers.

    >>> first_even([5, 8, 3, 2])
    8
    >>> first_even([7, 1])
    -1
    """
    result = -1
    i = 0
    while result <= 0 and i < len(items):
        if items[i] % 2 == 0:
            result = result + items[i] + 1
        i = i + 1
        
    return result
        