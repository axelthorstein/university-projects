def stack_list(L):
    """ (list) -> NoneType
    
    Adds each element of the list to the stack
    
    >>> L = ['Hello', 'world', 'read', 'this', 'string', 'end']
    >>> stack_list(L)
    end
    """
    stack = []
    
    for item in L:
        stack.append(item)
    while stack:
        stack_top = stack.pop()
        if not isinstance(stack_top, list):
            print(stack_top)
        else:
            return stack_list(stack_top)
            



if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    #stack = []
    #while 'end' not in stack:
        #stack.append(input('Type a string:'))

    #for item in range(len(stack)):
        #print(stack.pop())