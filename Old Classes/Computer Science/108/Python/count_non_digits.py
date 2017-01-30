def count_non_digits(s):
    """ (str) -> int

    Return the number of non-digits in s.

    >>> count_non_digits('abc12d')
    4
    >>> count_non_digits('135')
    0
    >>> count_non_digits('A.4')
    2
    """
    result = 0
    for ch in s:
        if ch not in '0123456789':
            result = result + 1
    return result