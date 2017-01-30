def count_collatz_steps(n):
    """ (int) -> int
    
    pre condition: n > 0
    
    >>> count_collatz_steps(6)
    8
    """
    
    result = 0

    while n > 1:
        if n % 2 == 0:
            n = (n // 2)
        else:
            n = (n * 3) + 1
        result = result + 1
            
    return result