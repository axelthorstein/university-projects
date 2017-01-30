def upper_lower(s):
    """ (str) -> bool
    
    Return True if and only if there is at least one alphabetic character in s and the alphabetic characters in s
    are either all uppercase or all lowercase.
    
    >>> upper_lower('abc')
    True
    >>> upper_lower('abcXYZ')
    False
    >>> upper_lower('XYZ')
    True
    """
    
    for ch in s:
        if s.islower():
            return True
        if s.isupper():
            return True
        else:
            return False
