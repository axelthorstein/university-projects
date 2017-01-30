def num_same(s1, s2):
    """ (str, str) -> list of int

    Return a two-item list with the first item representing the number of characters
    that are the same at corresponding positions of s1 and s2, and the second item
    representing the number of characters that are different at those positions.

    >>> num_same('hello', 'jello')
    [4, 1]
    >>> num_same('him', 'this')
    [0, 3]
    """

    same_count = 0
    different_count = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            same_count = same_count + 1
        else:
            different_count = different_count + 1

    return [same_count, different_count]