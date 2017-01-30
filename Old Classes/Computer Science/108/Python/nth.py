def every_nth_character(s, n):
    """ (str, int) -> str
    >>> every_nth_character('Computer Science', 'u')
    'CpeSee'
    """
    
    """    result = ''
    i = 0
    while s[i] != n:
        result = result + s[i]
        i = i + 1
    return result
    """
    
    result = ''
    i = 0
    while i < len(s):
        result = result + s[i]
        i = i + n
    return result