def count_startswith(L, ch):
    """ (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1

    Return the number of strings in L that begin with ch.

    >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
    2
    """
    

    count = 0

    for item in L:
        if item.startswith(ch):
            count = count + 1

    return count
        

if __name__ == "__main__":
    
    count_startswith(['rumba', 'salsa', 'samba'], 's')