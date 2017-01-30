def only_evens(lst):
    """ (list of list of int) -> list of list of int

    Return a list of the lists in lst that contain only even integers. 
   
    >>> only_evens([[1, 2, 4], [4, 0, 6], [22, 4, 3], [2]])
    [[4, 0, 6], [2]]
    """
    
    
    
    
    even_lists = []
    for sublist in lst:
        result = True
        i = 0
        while i < len(sublist):
            if sublist[i] % 2 == 1:
                result = False
            i += 1 
        if result == True:
            even_lists.append(sublist)
            
    return even_lists


if __name__ == "__main__":

    only_evens([[1, 2, 4], [4, 0, 6], [22, 4, 3], [2]])