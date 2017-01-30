def find_letter_n_times(s, letter, n):
    """ str, str, int) -> str
    
    >>> find_letter_n_times('Computer Science', 'e', 2)
    'Computer Scie'
    """
    
    i = 0
    count = 0
    while count < n:
        if s[i] == letter:
            count = count + 1
        i = i + 1
    return s[:i]