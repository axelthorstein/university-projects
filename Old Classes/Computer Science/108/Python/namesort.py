def earlier_name(name1, name2):
    """ (str, str) -> str
    
    return name, name 1 or name2, that comes first alphabetically
    
    >>> earlier_name('Jen', 'Paul')
    'Jen'
    """
    
    if (name1.islower)[0] > (name2.islower)[0]:
        return name1
    else:
        return name2
        