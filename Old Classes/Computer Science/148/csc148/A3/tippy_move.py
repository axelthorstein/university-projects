from move import Move


class TippyMove(Move):
    ''' A move in the game of Tippy.

    move: str -- is a capital X or O
    '''

    def __init__(self, move):
        ''' (TippyMove, int) -> NoneType

        Initialize a new TippyMove for inputting a str into a Tippy game grid.

        Assume: move is a capital X or O, or an int.
        '''
        self.move = move

    def __repr__(self):
        ''' (TippyMove) -> str

        Return a string representation of this TippyMove.
        >>> t1 = TippyMove(4)
        >>> t1
        TippyMove(4)
        '''
        return 'TippyMove({})'.format(str(self.move))

    def __str__(self):
        ''' (TippyMove) -> str

        Return a string representation of this TippyMove
        that is suitable for users to read.

        >>> t1 = TippyMove(4)
        >>> print(t1)
        4
        '''

        return '{}'.format(str(self.move))

    def __eq__(self, other):
        ''' (TippyMove, TippyMove) -> bool

        Return True iff this TippyMove is the same as other.

        >>> t1 = TippyMove('1')
        >>> t2 = TippyMove('2')
        >>> print(t1 == t2)
        False
        '''
        return (isinstance(other, TippyMove) and 
                self.move == other.move)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
