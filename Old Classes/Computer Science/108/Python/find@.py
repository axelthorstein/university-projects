def find_at(s):
    """(str) -> list of int
    
    Find @
    
    >>>find_at('When@ will I find the in this??')
    4
    """
    
    result = []
    i = 0
    while i < len(s):
        if s[i] in '@':
            result.append(i)
        i = i + 1
    return result