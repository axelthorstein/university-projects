class SpecialList:
    """A list that can hold a limited number of items."""

    def __init__(self, size):
        """ (SpecialList, int)

        >>> L = SpecialList(10)
        >>> L.size
        10
        >>> L.value_list
        []
        """
        self.size = size
        self.value_list = []


    def push_value(self, new_value):
        """ (SpecialList, object) -> NoneType

        Append new_value to this list, if there is enough space in the list according to its maximum size.  
        If there is insufficient space, new_value should not be added to the list.

        >>> L = SpecialList(10)
        >>> L.push_value(3)
        >>> L.value_list
        [3]
        """
        if len(self.value_list) < self.size:
            self.value_list.append(new_value)

    def pop_most_recent_value(self):
        """ (SpecialList) -> object

        Precondition: len(self.value_list) != 0

        Return the value added most recently to value_list and remove it from the list.

        >>> L = SpecialList(10)
        >>> L.push_value(3)
        >>> L.push_value(4)
        >>> L.value_list
        [3, 4]
        >>> L.pop_most_recent_value()
        4
        """
        result = self.value_list[-1]
        self.value_list.remove(self.value_list[-1])
        return result
        
    
    def compare(self, other):
        """ (SpecialList, SpecialList) -> int

        Return 0 if both SpecialList objects have lists of the same size.
        Return 1 if self's list contains more items than other's list.
        Return -1 if self's list contains fewer items than other's list.
        """
        for self.value_list in SpecialList:
            if len(self.value_list) == len(other.value_list):
                return 0
            elif:
                len(self.value_list) > len(other.value_list):
                return 1
            else:
                return -1
                

if __name__ == "__main__":
    import doctest
    doctest.testmod()
