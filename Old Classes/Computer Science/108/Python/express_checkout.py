def express_checkout(product_to_quantity):
    """ (dict of {str:int}) -> bool
    
    >>> express_checkout({'banana' : 3, 'soy milk' : 1, 'peanut butter': 1})
    True
    
    """
    
    
    count = 0
    for item in product_to_quantity:
        count = count + product_to_quantity[item]
    return count < 8