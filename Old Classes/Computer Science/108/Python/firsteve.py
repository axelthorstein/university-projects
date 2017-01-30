def first_even(items):
2	    """ (list of int) -> int
3	    
4	    Return the first even number from items. Return -1 if items contains no even numbers.
5	
6	    >>> first_even([5, 8, 3, 2])
7	    8
8	    >>> first_even([7, 1])
9	    -1
10	    """
11	    
12	    result = []
13	    i = 0
14	    while not result[0] % 2 == 0:
15	        if not int(items[i]) % 2 == 0:
16	            i = i + 1
17	        else:
18	            result.append(items[i])
19	    return result
20	    
21	first_even([5, 8, 3, 2])



#if __name__ == "__main__"

#first_even([5, 8, 3, 2])