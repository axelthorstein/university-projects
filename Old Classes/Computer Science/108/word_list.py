def triple(x):
    print('Tripling', x)
    return x * 3
def subtract(y, z):
    print('Subtracting', y, z)
    return y - z


    
#if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    
    # Size: 
    #   for lists/tuple/dict: empty, 1 item, 
    #   smallest interesting case, several items
    
    # Dichotomies: 
    #   (e.g., vowels/non-vowels, even/odd, 
    #                positive/negative, etc.)
    
    # Boundaries:
    #   If a function behaves differently for a 
    #   value near a particular threshold (i.e. 
    #   an if statement checking when a value is 
    #   3; 3 is a threshold), test at the that 
    #   threshold and around it.
    
    # Order:
    #    If a function behaves differently when 
    #    the values are in a different order,
    #    identify and test each of those orders.