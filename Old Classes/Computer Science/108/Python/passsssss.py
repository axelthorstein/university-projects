def check_password(passwd):
    """ (str) -> bool

    A strong password has a length greater than or equal to 6, contains at
    least one lowercase letter, at least one uppercase letter, and at least
    one digit.  Return True iff passwd is considered strong.

    >>> check_password('I<3csc108')
    True
    """
    
    for ch in passwd:
        if len(passwd) >= 6:
            return True
        if ch in 'abcdefghijklmnopqrstuvwxyz':
            return True
        if ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return True
        if ch in '0123456789':
            return True
        if ch in '`~!@#$%^&*()-_=+<>?/.,':
            return True        
        else:
            return False
    