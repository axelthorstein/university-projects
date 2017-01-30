def greatest_difference(nums1, nums2):
    """ (list of numbers, list of numbers) -> number
    
    >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    """
    
    result = []
    i = 0
    while i < len(nums1):
        result.append(abs(nums1[i] - nums2[i]))
        i = i + 1
    return max(result)

__name__ == "__main__"

print(greatest_difference([1, 2, 3], [6, 8, 10]))
