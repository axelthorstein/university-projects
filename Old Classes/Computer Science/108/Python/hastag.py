def contains_hash_symbol(tweet):
    """(str) -> bool	
    
    Return True if and only if the tweet contains a hash symbol.

    >>> contains_hash_symbol('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + '# knowledge. - Grace Hopper')
    True
    >>> contains_hash_symbol('The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand. - Donald Knuth')
    False
    """
    if '#' in (tweet):
        return True
    else:
        return False