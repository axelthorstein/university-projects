class LLNode:
    '''Node to be used in linked list

    nxt: LLNode -- next node
                   None iff we're at end of list
    value: object --- data for current node
    '''

    def __init__(self, value, nxt=None):
        ''' (LLNode, object, LLNode) -> NoneType

        Create LLNode (self) with data value and successor nxt.
        '''
        self.value, self.nxt = value, nxt

    def __repr__(self):
        ''' (LLNode) -> str

        Return a string representation of LLNode (self) that can yields
        an equivalent LLNode if evaluated in Python.

        >>> n = LLNode(5, LLNode(7))
        >>> n.nxt
        LLNode(7)
        >>> n
        LLNode(5, LLNode(7))
        '''
        if self.nxt is None:
            return 'LLNode({})'.format(repr(self.value))
        else:
            return 'LLNode({}, {})'.format(repr(self.value), repr(self.nxt))

    def __str__(self):
        ''' (LLNode) -> str

        Return a user-friendly representation of this LLNode.

        >>> n = LLNode(5, LLNode(7))
        >>> print(n)
        5 -> 7 ->|
        '''
        if self.nxt is None:
            return '{} ->|'.format(str(self.value))
        else:
            return '{} -> {}'.format(str(self.value), str(self.nxt))

    def __eq__(self, other):
        ''' (LLNode, object) -> bool

        Return whether LLNode (self) is equivalent to other.

        >>> LLNode(5).__eq__(5)
        False
        >>> n = LLNode(5, LLNode(7))
        >>> n2 = LLNode(5, LLNode(7, None))
        >>> n.__eq__(n2)
        True
        '''
        return (type(self) == type(other) and
                (self.value, self.nxt) == (other.value, other.nxt))


class LinkedList:
    '''Collection of LLNodes organized into a linked list.

    front: LLNode -- front of list
    back:  LLNode -- back of list'''

    def __init__(self):
        ''' (LinkedList) -> NoneType

        Create an empty linked list.
        '''
        self.front, self.back = None, None
        self.size = 0

    def __str__(self):
        ''' (LinkedList) -> str

        Return a human-friendly string representation of
        LinkedList (self)

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->|
        '''
        return str(self.front)

    def __eq__(self, other):
        ''' (LinkedList, object) -> bool

        Return whether LinkedList (self) is equivalent to
        other.

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        '''
        return (type(self) == type(other) and
                (self.size, self.front) == (other.size, other.front))

    def append(lnk, value):
        ''' (LinkedList, object) -> NoneType

        Insert a new node with value at back of lnk.

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        '''
        new_node = LLNode(value)
        if lnk.back:
            lnk.back.nxt = new_node
            lnk.back = new_node
        else:
            lnk.back = lnk.front = new_node
        lnk.size += 1

    def prepend(self, value):
        ''' (LinkedList, object) -> Nonetype

        Insert value at front of LLNode (self).

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        '''
        self.front = LLNode(value, self.front)
        if self.back is None:
            self.back = self.front
        self.size += 1

    #def delete_front(self):
        #''' (LinkedList) -> NoneType

        #Delete front node from LinkedList (self).

        #self.front must not be None

        #>>> lnk = LinkedList()
        #>>> lnk.prepend(0)
        #>>> lnk.prepend(1)
        #>>> lnk.prepend(2)
        #>>> lnk.delete_front()
        #>>> str(lnk.front)
        #'1 -> 0 ->|'
        #>>> lnk.size
        #2
        #'''

    def __getitem__(self, index):
        ''' (LinkedList, int|slice) -> object

        Return the value at position index.
        # don't fuss about slices yet.

        >>> lnk = LinkedList()
        >>> lnk.prepend(1)
        >>> lnk.prepend(0)
        >>> lnk.__getitem__(1)
        1
        '''
        if index > self.size - 1:
            raise Exception('out of range')
        else:
            current_node = self.front
            for i in range(0, index):
                current_node = current_node.nxt
            return current_node.value


    def __setitem__(self, index, value):
        ''' (LinkedList, int|slice, object) -> NoneType

        Set the value at index to value, if index is in range, otherwise
        raise an IndexError.  Indexs are counted from 0. Note that negative
        integers can be adjusted by adding self.size, to get a index in
        range.

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(7)
        >>> lnk.__setitem__(1, 9)
        >>> print(lnk.front)
        7 -> 9 ->|
        >>> lnk[0] = 3
        >>> print(lnk.front)
        3 -> 9 ->|
        >>> lnk[-1] = 8
        >>> print(lnk.front)
        3 -> 8 ->|
        '''
        if index > self.size - 1:
            raise Exception('out of range')
        else:
            current_node = self.front
            for i in range(0, self.size):
                if i == index:
                    current_node.value = value
                current_node = current_node.nxt

    def __contains__(self, value):
        ''' (LinkedList, object) -> bool

        Return whether LinkedList (self) contains value.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.__contains__(1)
        True
        >>> lnk.__contains__(3)
        False
        '''
        current_node = self.front
        while current_node:
            if value == current_node.value:
                return True
            current_node = current_node.nxt
        return False

    #def __add__(self, other):
        #''' (LinkedList, LinkedList) -> LinkedList

        #Concatenate LinkedList (self) to LinkedList (other) and
        #return a new list, leaving self and other unchanged.

        #>>> lnk1 = LinkedList()
        #>>> lnk1.prepend(5)
        #>>> lnk2 = LinkedList()
        #>>> lnk2.prepend(7)
        #>>> lnk3 = lnk1.__add__(lnk2)
        #>>> print(lnk3.front)
        #5 -> 7 ->|
        #>>> print(lnk1.front)
        #5 ->|
        #>>> print(lnk2.front)
        #7 ->|
        #'''


#def insert_before(lnk, v1, v2):
    #''' (LinkedList, object) -> NoneType

    #Insert a new node with value v1 before the first occurrence
    #of a node with value v2.  Do nothing if no node has value
    #v2.

    #>>> lnk = LinkedList()
    #>>> lnk.prepend(5)
    #>>> insert_before(lnk, 4, 5)
    #>>> print(lnk.front)
    #4 -> 5 ->|
    #>>> insert_before(lnk, 3, 5)
    #>>> print(lnk.front)
    #4 -> 3 -> 5 ->|
    #>>> insert_before(lnk, 3, 7)
    #>>> print(lnk)
    #4 -> 3 -> 5 ->|
    #'''


#def delete_after(lnk, value):
    #''' (LinkedList, object) -> NoneType

    #Insert a new node with value after the first occurrence of a
    #node containing value, if possible.

    #>>> lnk = LinkedList()
    #>>> lnk.append(3)
    #>>> lnk.append(5)
    #>>> lnk.append(7)
    #>>> lnk.append(9)
    #>>> delete_after(lnk, 3)
    #>>> print(lnk)
    #3 -> 7 -> 9 ->|
    #>>> delete_after(lnk, 7)
    #>>> print(lnk)
    #3 -> 7 ->|
    #>>> delete_after(lnk, 15)
    #>>> print(lnk)
    #3 -> 7 ->|
    #'''


def delete_back(lnk):
    ''' (LinkedList) -> NoneType

    Delete back node of lnk, if it exists, otherwise
    do nothing.

    >>> lnk = LinkedList()
    >>> lnk.prepend(5)
    >>> lnk.prepend(7)
    >>> print(lnk.front)
    7 -> 5 ->|
    >>> delete_back(lnk)
    >>> lnk.size
    1
    >>> print(lnk.front)
    7 ->|
    >>> delete_back(lnk)
    >>> lnk.size
    0
    >>> print(lnk.front)
    None
    '''
    if lnk.size > 0:
        prev_node, cur_node = None, lnk.front
        # walk along until cur_node is lnk.back
        while not cur_node.nxt is None:
            prev_node = cur_node
            cur_node = cur_node.nxt
        lnk.back = prev_node
        if lnk.back is None:
            lnk.front = None
        else:
            lnk.back.nxt = None
        lnk.size -= 1


#def odd_nodes(lnk):
    #''' (LinkedList) -> LinkedList

    #Return a new linked list with values of odd-indexed nodes of lnk.

    #>>> lnk = LinkedList()
    #>>> lnk.append(3)
    #>>> lnk.append(5)
    #>>> lnk.append(7)
    #>>> lnk.append(9)
    #>>> lnk2 = odd_nodes(lnk)
    #>>> print(lnk2)
    #5 -> 9 ->|
    #'''


#def filter_nodes(lnk, f):
    #''' (LinkedList, function) -> LinkedList

    #Return a new linked list with values of lnk for
    #nodes that satisfy boolean-valued function f.

    #>>> lnk = LinkedList()
    #>>> lnk.append(3)
    #>>> lnk.append(4)
    #>>> lnk.append(5)
    #>>> lnk.append(6)
    #>>> def f(node): return node.value % 2 == 0
    #>>> lnk2 = filter_nodes(lnk, f)
    #>>> print(lnk2)
    #4 -> 6 ->|
    #'''
    new_list, cur_node = LinkedList(), lnk.front


if __name__ == '__main__':
    import doctest
    doctest.testmod()