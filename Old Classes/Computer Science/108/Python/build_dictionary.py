def build_placements(shoes):
    """ (list of str) -> dict of {str: list of int}
    
    >>> build_placements(['Saucony', 'Asics', 'Asics', 'NB', 'Saucony', 'Nike', 'Asics', 'Adidas', 'Saucony', 'Asics'])
    {'Saucony': [1, 5, 9], 'NB': [4], 'Adidas': [8], 'Asics': [2, 3, 7, 10], 'Nike': [6]}

    
    """
    
    result = {}
    i = 1
    for shoe in shoes:
        if shoe not in result:
            result[shoe] = [i]
        elif shoe in result:
            result[shoe].append(i)
        i += 1
    return result


