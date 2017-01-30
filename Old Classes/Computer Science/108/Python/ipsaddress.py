def is_ip_address(address):
    """ (str) -> bool
    
    Return True iff address contains only digits and periods
    
    >>> is_ip_address('128.100.31.52')
    True
    >>> is_ip_address('40 St.George St.')
    False
    """
    #ask about
    for ch in address:
        if ch not in '0123456789.':
            return False
    return True

#return address.replace('.', '2').isdigit    
#for ch in address:
#result = True
#    if ch not in '0123456789.':
#result False
#return result
    
#form for for
#for ch in a given_string:
#    execute statements - variable ch will refer to a character in a given string