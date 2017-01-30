def check_password(passwd):
    """ (str) -> bool

    A strong password has a length greater than or equal to 6, contains at
    least one lowercase letter, at least one uppercase letter, and at least
    one digit.  Return True iff passwd is considered strong.

    >>> check_password('I<3csc108')
    True
    """
    if len(passwd) < 6:
        return False 
    #contains at least one lowercase letter    
    i = 0
    while i < len(passwd) and not passwd[i].islower():    
        i = i + 1
    if i == len(passwd):
        return False    
    #at least one uppercase letter
    i = 0
    while i < len(passwd) and not passwd[i].isupper():    
        i = i + 1
    if i == len(passwd):
        return False       
    #and at least one digit    
    i = 0
    while i < len(passwd) and not passwd[i].isdigit():    
        i = i + 1
    if i == len(passwd):
        return False      
    return True


if __name__ == '__main__':
    print(check_password('dE6ghi'))
    
    