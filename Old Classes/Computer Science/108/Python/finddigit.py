def index_first_digit(s):
    """ (str) -> int
    
    Return the index of the first digit in a string
    
    >>> index_first_digit('Found the first 1!')
    16
    
    """
    
    i = 0
    
    while i < len(s) and s[i] not in '0123456789':
        i = i + 1
    return i