def count_uppercase(s):
    """ (str) -> int
    
    return the number of uppercase letters
    
    >>> count_uppercase(Apple Computer)
    2
    >>> count_uppercase(Apple COMputer)
    4
    
    """
  
    num_uppercase = 0
    for ch in s:
        if ch.isupper():
            num_uppercase = num_uppercase + 1
    return num_uppercase