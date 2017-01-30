def is_correct(file, word):
    """ (file open for reading, str) -> bool
    
    return true iff word in file.
    
    >>> dict_file = open('dictionary.txt')
    >>> is_correct(dict_file, 'Zyrtec')
    True
    """
    
    for line in file:
        #if line == word:
        if word == line.strip():
            return True
    return False