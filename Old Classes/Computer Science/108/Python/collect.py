def collect_under_performers(nums, threshold):
    """ (list of number, int) -> list of number
    
    >>> collect_under_performers([1, 2, 3, 4], 3)
    [1, 2]
    
    """
    
    collect = []
    i = 0
    while i < len(nums):
        if nums[i] < threshold:
            collect.append(nums[i])
        i = i + 1
    return collect

#for item in nums:
#    if nums[i] < threshold
#        collect.append(nums[i])


