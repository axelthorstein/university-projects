def can_pay_with_two_coins(denoms, amount):
    """ (list of int, int) -> bool
    
    return true if it is possible to form the given amount using two coin of any denomination in this list of denoms
    
    >>> can_pay_with_two_coins([1, 5, 10, 25], 35)
    True
    """
    
    
    i = 0
    while i < len(denoms):
        if denoms[i] + 1 or 5 or 10 or 25 == amount:
            return True
        else:
            False
        i += i
