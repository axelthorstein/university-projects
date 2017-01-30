def is_mentioned(tweet, username):
    """(str, str) -> bool
    
    Return True if and only if the tweet mentions that username preceded by @.
    
    >>> is_mentioned('To me programming is more than an important ' \
        + 'practical art. It is also a gigantic undertaking in the ' \
        + 'foundations of @gracehopper', 'gracehopper')
    True
    >>> is_mentioned('The best programs are written so that computing ' \
        + 'machines can perform them quickly and so that human beings can ' \
        + 'understand.', 'Donald Knuth')
    False
    """
    if '@' + username in tweet:
        return True
    else:
        return False 