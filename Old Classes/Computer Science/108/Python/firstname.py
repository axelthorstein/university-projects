def same_first_name(name1, name2):
    """ (list of str, list of str) -> bool
    
    Return whether the first element of name1 and name2 are the same.
    
    >>> same_first_name(['John', 'Smith'], ['John', 'Harkness'])
    True
    >>> same_first_name(['John', 'Smith'], ['Matt', 'Smith'])
    False
    """
    
    if name1[:1] == name2[:1]:
        return True
    else:
        return False
        