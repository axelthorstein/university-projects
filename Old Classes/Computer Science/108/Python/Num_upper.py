def count_uppercase(s):
    """ (str) -> int
    
    Return the number of uppercase letters in s.
    
    >>> count_uppercase('Computer Science')
    
    """
    
    num_upper = 0
    
    for ch in s:
        if ch.isupper():
            num_upper = num_upper + 1
    return num_upper
        