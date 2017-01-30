def all_fluffy(s):
    """ (str) -> bool
    
    return True iff every letter in s is fluffy
    
    >>> all_fluffy('flu')
    True
    """
    
    for ch in s:
        if ch not in 'fluffy':
            return False
    return True