def stretch_string(s, stretch_factors):
    """ (str, list of int) -> str
    
    >>> stretch_string('hello', [2, 0, 3, 1, 1])
    """
    
    result = ''
    i = 0
    while len(result) < sum(stretch_factors):
        if stretch_factors[i] > 0:
            result += str(s[i] * stretch_factors[i])
        else:
            result += ''
        i = i + 1
    return result