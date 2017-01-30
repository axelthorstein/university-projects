def distance(x, y):
    """ (number, number) -> float
    
    This function determines the distances and returns that value from coordinate (x,y) to the origin. 

    >>> distance(3, 4)
    5
    >>> distance(-5, 12)
    13
    """
    
    return ( x ** 2 + y ** 2 ) ** (1/2)
