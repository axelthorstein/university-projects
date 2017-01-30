def make_absolute(nums):
    """ (list of number) -> Nonetype
    Replace each item in nums with its absolute value.
    >>> nums = [1, -4.5, 0.2, -6]
    >>> make_absolute(nums)
    >>> nums
    [1, 4.5, 0.2, 6]
    """
    
    result = []
    i = 0
    while i < range(len(nums)):
        result.append(abs(nums[i]))
        i = i + 1
    
    
    
    #for i in range(len(nums)):
     #   nums[i] = abs(nums[i])
