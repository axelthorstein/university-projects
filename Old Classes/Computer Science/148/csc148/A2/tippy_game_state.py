from game_state import GameState
from game_view import GameView
from tippy_move import TippyMove


class TippyGameState(GameState):
    ''' The state of a Tippy game

    grid: list of list   --- a grid to keep track of player moves
    '''

    def __init__(self, p, grid=None, interactive=False):
        '''(TippyGameState, int, str) -> NoneType

        Initialize TippyGameState self starting with an empty grid.

        Assume: -- p in {'p1', 'p2'}
        Assume: -- p1 == 'X', p2 == 'O'
        '''
        GameState.__init__(self, p)
        self.p1, self.p2, self.p = 'X', 'O', p
        if interactive:
            grid = self.create_board()
        self.grid = grid
        self.next_player, self.over = p, self.winner(p)
        self.instructions = ('---------------------------------------\n\
Choose a tile on the board where you would like\
 to place an X.\nTry to place Xs in the shape of a tetronimo \
 to win. Good luck!')
        
    def __repr__(self):
        ''' (TippyGameState) -> str

        Return a string representation of TippyGameState self
        that evaluates to an equivalent TippyGameState

        >>> t = TippyGameState('p1', interactive=True)
        >>> t
        TippyGameState('p1', 17)
        '''
        player = self.next_player
        return 'TippyGameState({}, {})'.format(repr(player), repr(self.grid))
    
    def __str__(self):
        """ (TippyGameState) -> str

        Return a string representation of the Tippy game board

        >>> t = TippyGameState('p1', interactive=True)
        >>> 3
        >>> print(t)
         ------------
        | 1 | 2 | 3 |
         ------------
        | 4 | 5 | 6 |
         ------------
        | 7 | 8 | 9 |
         ------------
        """
        # A somewhat elaborate way to represent the grid so it scales well
        # Can scale up to 10x10 board before it can't scale
        grid_line_length = (' ' + ('-' * len(self.grid) * 4) + '\n')
        grid_string = ''
        i = 0
        grid_string += grid_line_length
        for row in self.grid:
            grid_string += '| '
            for item in row:
                if len(str(item)) == 1:
                    grid_string += (str(item) + ' | ')
                else:
                    grid_string += (str(item) + '| ')
            grid_string += '\n'
            grid_string += grid_line_length
        return(grid_string)
    
    def __eq__(self, other):
        ''' (TippyGameState, TippyGameState) -> bool

        Return True iff this TippyGameState is the equivalent to other.

        >>> t1 = TippyGameState('p1', interactive=True)
        >>> 3
        >>> t2 = TippyGameState('p1', interactive=True)
        >>> 3
        >>> t1 == t2
        True
        '''
        return (isinstance(other, TippyGameState) and
                self.grid == other.grid and
                self.next_player == other.next_player)

    def create_board(self):
        ''' (TippyGameState) -> list of list

        Create a user specified sized grid for Tippy game to be played

        >>> t = TippyGameState('p1', interactive=True)
        >>> 3
        >>> print(str(t))
         ------------
        | 1 | 2 | 3 |
         ------------
        | 4 | 5 | 6 |
         ------------
        | 7 | 8 | 9 |
         ------------
        '''
        board_size = input('Enter a number 3 or greater for the board size: ')
        board_range = range(int(board_size))
        grid = [[0 for j in board_range] for i in board_range]

        count = 1
        for row in board_range:
            for item in board_range:
                grid[row][item] = count
                count += 1
        return grid

    def apply_move(self, move):
        ''' (TippyGameState, TippyeMove) -> TippyGameState

        Return the new TippyGameState reached by applying move to self.

        >>> t = TippyGameState('p1', interactive=True)
        >>> 3
        >>> t2 = t.apply_move(TippyMove(5))
        >>> print(t)
         ------------
        | 1 | 2 | 3 |
         ------------
        | 4 | X | 6 |
         ------------
        | 7 | 8 | 9 |
         ------------
        '''
        row_length = range(len(self.grid))
        if move in self.possible_next_moves():
            for row in row_length:
                for item in row_length:
                    if TippyMove(self.grid[row][item]) == move:
                        if self.p == 'p1':
                            self.grid[row][item] = self.p1
                            return TippyGameState('p2', grid=self.grid)
                        if self.p == 'p2':
                            self.grid[row][item] = self.p2
                            return TippyGameState('p1', grid=self.grid)
        else:
            return None

    def rough_outcome(self):
        '''(TippyGameState) -> float

        Return an estimate in interval [LOSE, WIN] of best outcome next_player
        can guarantee from state self.

        >>> t = TippyGameState('p1', interactive=True)
        >>> t.grid = [[1, 'O', 'O', 'X'], [5, 6, 'X', 'X'], \
        [9, 'X', 'O', 12], [13, 14, 'O', 'X']]
        >>> t.rough_outcome()
        -1.0
        '''
        move_count_list = []
        for move in [self.p1, self.p2]:
            count = 0
            for row in t.grid:
                for item in range(len(row))[:-1]:
                    if row[item] == move:
                        if row[item + 1] == move:
                            count += 1
            move_count_list.append(count)
        if move_count_list[0] < move_count_list[1]:
            return TippyGameState.LOSE
        elif move_count_list[0] > move_count_list[1]:
            return TippyGameState.WIN
        else:
            return TippyGameState.DRAW

    def get_move(self):
        '''(TippyGameState) -> TippyMove

        Prompt user and return move.
        '''
        return TippyMove(int(input("Input the number of the tile you \
would like to make your move: ")))

    def winner(self, player):
        ''' (TippyGameState, str) -> bool

        Return True iff the game is over and player has won.

        >>> t = TippyGameState('p1', interactive=True)
        >>> t.grid = [[1, 'O', 'O', 'X'], [5, 6, 'X', 'X'], \
        [9, 'X', 'X', 12], [13, 14, 'X', 'X']]
        >>> t.winner('p1')
        True

        Preconditions: player is either 'p1' or 'p2'
        '''
        # Check for one shape and manipulate the board to check for the others.
        list_s = [[row[i] for row in self.grid] for i in range(len(self.grid))]
        list_s_backwards = [row[::-1] for row in list_s]
        list_z_backwards = [row[::-1] for row in self.grid]
        
        for grid in [self.grid, list_s, list_s_backwards, list_z_backwards]:
            for move in [self.p1, self.p2]:
                row_num = 0
                for row in grid[:-1]:
                    row_num += 1
                    tile_num = 0
                    for tile in row[:-2]:
                        tile_num += 1
                        if tile == move:
                            if row[tile_num] == move:
                                if grid[row_num][tile_num] == move:
                                    tile_num += 1
                                    if grid[row_num][tile_num] == move:
                                        if move == self.p1:
                                            if player == 'p1':
                                                return True
                                        else:
                                            if player == 'p2':
                                                return True
        return False
        
    def possible_next_moves(self):
        ''' (TippyGameState) -> list of TippyGameState

        Return a (possibly empty) list of moves that are legal
        from the present state.

        >>> t = TippyGameState('p1', interactive=True)
        >>> t.possible_next_moves()
        [TippyMove(0), TippyMove(1), TippyMove(2), TippyMove(3), \
        TippyMove(4), TippyMove(5), TippyMove(6), TippyMove(7), \
        TippyMove(8), TippyMove(9)]
        '''
        possible_moves = []
        for row in self.grid:
            for item in row:
                if isinstance(item, int):
                    possible_moves.append(item)
        return [TippyMove(i) for i in possible_moves if isinstance(i, int)]

#if __name__ == '__main__':
    #import doctest
    #doctest.testmod()