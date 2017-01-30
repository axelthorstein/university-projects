def digital_sum(nums_list):
    '''
    >>> digital_sum(['12', '3'])
    
    '''
    result = 0
    for item in nums_list:
        for ch in item:
            result += int(ch)
            
    return result