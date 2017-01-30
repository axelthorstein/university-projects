def every_nth_character(s, n):
    """ (str, int) -> str
    >>> every_nth_character('Computer Science', 3)
    'CpeSee'
    """
    
    result = ''
    i = 0
    while i != n:
        result = result + s[i]
        i = i + n
    return result
