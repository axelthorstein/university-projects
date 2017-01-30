def format_name(last, first):
    """ (str, str) -> str
    
    Print first and last name given.
    >>> format_name('steingrimsson', 'axel')
    'steingrimsson, axel'
    """
    return last + ', ' + first


def to_listing(last, first, phone): 
    """ (str, str, str) -> str
    return a string contains a listing
    >>>to_listing('Steingrimsson', 'Axel', '4165714525')
    'Steingrimsson, Axel: 4165714525'
    """
    return to_listing(last, first) + ': ' + phone
    #return last + ', ' + first + ': ' + phone
