def contains_no_lowercase_vowels(phrase):
    """ (str) -> bool

    Return True iff (if and only if) phrase does not contain any lowercase vowels.

    >>> contains_no_lowercase_vowels('syzygy')
    True
    >>> contains_no_lowercase_vowels('e')
    False
    >>> contains_no_lowercase_vowels('abce')
    False
    """
    
    for ch in phrase:
        if ch not in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            return False
    else:
        return True
        
    
        