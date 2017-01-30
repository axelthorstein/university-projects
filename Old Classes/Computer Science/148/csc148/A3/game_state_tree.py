from subtract_square_state import SubtractSquareState


class GameStateNode:
    '''
    A tree of possible states for a two-player, sequential move, zero-sum,
    perfect-information game.

    value: GameState -- the game state at the root of this tree
    children: list -- all possible game states that can be reached from this
    game state via one legal move in the game.  children is None until grow
    is called.
    '''

    def __init__(self, game_state):
        ''' (GameStateNode, GameState) -> NoneType

        Initialize a new game state tree consisting of a single root node 
        that contains game_state.
        '''
        self.value = game_state
        self.children = []

    def __eq__(self, other):
        ''' (GameStateNode, object) -> bool

        Return whether this GameStateNode is equivalent to other, i.e., they
        contain equivalent GameStates, and equivalent children.  The order of
        their children does not matter.

        >>> s1 = SubtractSquareState('p1', current_total = 6)
        >>> s2 = SubtractSquareState('p2', current_total = 5)
        >>> s3 = SubtractSquareState('p1', current_total = 2)
        >>> leaf1 = GameStateNode(s1)
        >>> leaf2 = GameStateNode(s2)
        >>> leaf3 = GameStateNode(s3)
        >>> leaf1.__eq__(leaf2)
        False
        >>> root1 = GameStateNode(s1)
        >>> root1.children = [s2, s3]
        >>> root2 = GameStateNode(s1)
        >>> root1.__eq__(root2)
        False
        >>> root2.children = [s2, s3]
        >>> root1.__eq__(root2)
        True
        '''
        # Checking that the children lists have the same contents requires
        # checking that every element of one list is in the other, and vice
        # versa. Since checking "in" causes calls to the __eq__ method, we
        # end up recursing.
        return (type(self) == type(other) and
                self.value == other.value and        
                same_contents(self.children, other.children))

    def __str__(self, indent=0):
        ''' (Tree, int) -> str

        Return a string representation of a tree

        '''
        root_str = indent * ' ' + str(self.value)
        return '\n'.join([root_str] +
                         [c.__str__(indent + 3) for c in self.children])   

    def grow(self):
        ''' (GameStateNode) -> NoneType

        Grow the tree of all possible game state nodes that can be reached
        starting from this one.

        Assume that the game is finite (and so the tree will be finite).
        
        >>> a0 = SubtractSquareState('p1', current_total = 0)
        >>> b1 = SubtractSquareState('p2', current_total = 1)
        >>> a2 = SubtractSquareState('p1', current_total = 2)
        >>> b3 = SubtractSquareState('p2', current_total = 3)
        >>> a4 = SubtractSquareState('p1', current_total = 4)
        >>> b0 = SubtractSquareState('p2', current_total = 0)
        >>> a0_node = GameStateNode(a0)
        >>> b1_node = GameStateNode(b1)
        >>> b1_node.children = [a0_node]
        >>> a2_node = GameStateNode(a2)
        >>> a2_node.children = [b1_node]
        >>> b3_node = GameStateNode(b3)
        >>> b3_node.children = [a2_node]
        >>> b0_node = GameStateNode(b0)
        >>> a4_node = GameStateNode(a4)
        >>> a4_node.children = [b0_node, b3_node]
        >>> root = GameStateNode(SubtractSquareState('p1', current_total = 4))
        >>> root.grow()
        >>> root.__eq__(a4_node)
        True
        '''
        if not self.children:
            if self.value.possible_next_moves():
                for move in self.value.possible_next_moves():
                    game_state = self.value.apply_move(move)
                    node = GameStateNode(game_state)
                    self.children.append(node)
        if self.children:
            for child in self.children:
                child.grow()


def same_contents(L1, L2):
    ''' (list, list) -> bool
    
    Return True iff L1 and L2 have the same contents, although not necessarily
    in the same order.
    
    >>> same_contents([1, 4, 5, 2], [5, 2, 4, 1])
    True
    >>> same_contents([1, 2], [2, 1, 1])
    False
    '''
    return (len(L1) == len(L2) and 
            all([x in L2 for x in L1]) and 
            all([x in L1 for x in L2]))


def node_count(root):
    ''' (GameStateNode) -> int
    
    Return the number of nodes in the tree rooted at root.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> node_count(root)
    13
    '''
    if not root:
        return 0
    if root.children:
        return sum([node_count(child) for child in root.children]) + 1
    else:
        return 1


def leaf_count(root):
    '''(GameStateNode) -> int
    
    Return the number of leaves in the tree rooted at root.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> leaf_count(root)
    4
    '''
    if not root:
        return 0
    if not root.children:
        return 1
    if root.children:
        return sum([leaf_count(child) for child in root.children])


def _node_collector(root):
    ''' (GameStateNode) -> set
    
    Return a set of nodes in the tree rooted at root.
    
    >>> s = SubtractSquareState('p1', current_total = 4)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> nodes = _node_collector(root)
    >>> list_nodes = list(nodes)
    >>> list_nodes.sort()
    >>> list_nodes
    ['Current total: 0; next player: p1', 'Current total: 0; next player: p2',\
 'Current total: 1; next player: p2', 'Current total: 2; next player: p1',\
 'Current total: 3; next player: p2', 'Current total: 4; next player: p1']
    '''
    node_set = set()
    if not root:
        return set()
    if root.children:
        for child in root.children:
            node_set = node_set.union(_node_collector(child))
    node_set.add(str(root.value))
    return node_set


def distinct_node_count(root):
    '''(GameStateNode) -> int
    
    Return the number of nodes representing distinct game states in the
    tree rooted at root.  Two game states are distinct if they are not __eq__.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> distinct_node_count(root)
    10
    '''
    return len(_node_collector(root))

            
def _leaf_collector(root):
    ''' (GameStateNode) -> set
    
    Return a set of leaf nodes in the tree rooted at root.
    
    >>> s = SubtractSquareState('p1', current_total = 4)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> nodes = _leaf_collector(root)
    >>> list_nodes = list(nodes)
    >>> list_nodes.sort()
    >>> list_nodes
    ['Current total: 0; next player: p1', 'Current total: 0; next player: p2']
    '''
    node_set = set()
    if not root:
        return set()
    if root.children:
        for child in root.children:
            node_set = node_set.union(_leaf_collector(child))
    if not root.children:
        node_set.add(str(root.value))
    return node_set


def distinct_leaf_count(root):
    '''
    (GameStateNode) -> int
    
    Return the number of leaves representing distinct game states in the
    tree rooted at root.
       
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> distinct_leaf_count(root)
    2
    '''
    return len(_leaf_collector(root))


def branching_stats(root):
    ''' (GameStateNode) -> {int: int}
    
    Return a dict that represents the distribution of branching factors in
    the tree rooted at root. Each key is a branching factor >= 0, and its
    value is the number of nodes with that branching factor.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> branching_stats(root) == {0: 4, 1: 6, 2: 3}
    True
    '''
    node_dict = {}
    if not root:
        return {}
    if root.children:
        for child in root.children:
            child_dict = branching_stats(child)
            for key in child_dict.keys():
                if key in node_dict.keys():
                    node_dict[key] += child_dict[key]
                else:
                    node_dict[key] = child_dict[key]
    if len(root.children) in node_dict.keys():
        node_dict[len(root.children)] += 1
    else:
        node_dict[len(root.children)] = 1
    return node_dict


def outcome_counts(root):
    ''' (GameStateNode) -> [int, int, int]
    
    Return a list containing the number of leaf nodes containing a state in
    which player 'p1' is the winner, the number in which player 'p2' is, and
    the number in which the outcome of the game is a tie.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> outcome_counts(root)
    [3, 1, 0]
    '''
    winner_list = [0, 0, 0]
    if not root:
        return winner_list
    if root.children:
        for child in root.children:
            outcome = outcome_counts(child)
            winner_list[0] += outcome[0]
            winner_list[1] += outcome[1]
            winner_list[2] += outcome[2]
    if not root.children:
        player = root.value.opponent()
        if player == 'p1':
            if not root.value.outcome == 1.0:
                winner_list[0] += 1
        if player == 'p2':
            if not root.value.outcome == 1.0:
                winner_list[1] += 1
        else:
            if root.value.outcome == 0.0:
                winner_list[2] += 1
    return winner_list


def _leaf_length_list(root):
    ''' (GameStateNode) -> list of int
    
    Return a list of the possible game lengths.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> _leaf_length_list(root)
    [3, 3, 3, 6]
    '''    
    if not root:
        return root
    if not root.children:
        return [0]
    else:
        children_leaf_lengths = []
        for child in root.children:
            children_leaf_lengths += _leaf_length_list(child)
        for i in range(len(children_leaf_lengths)):
            children_leaf_lengths[i] += 1
        return children_leaf_lengths


def game_lengths(root):
    ''' (GameStateNode) -> {int: int}
    
    Return a dict that represents the distribution of game lengths in the
    tree rooted at root. Each key is a length of game >= 1, and its value is
    the number of games that are that long. The length of a game is the
    number of moves in the game.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> game_lengths(root) == {6: 1, 3: 3}
    True
    '''
    game_lengths_list = _leaf_length_list(root)
    game_lengths_dict = {}
    
    for game_length in game_lengths_list:
        if game_length in game_lengths_dict:
            game_lengths_dict[game_length] += 1
        else:
            game_lengths_dict[game_length] = 1
    return game_lengths_dict


def game_descriptions(root):
    ''' (GameStateNode) -> list of str
    
    Return a list containing a str describing each complete game that is
    possible from the game stored at root.
    
    Assume root is the root of a game state tree specifically for the game
    Subtract Square.
    
    >>> s = SubtractSquareState('p1', current_total = 6)
    >>> root = GameStateNode(s)
    >>> root.grow()
    >>> game_descriptions(root)
    ['p1:6 -> p2:2 -> p1:1 -> p2:0 = p1 wins!', \
'p1:6 -> p2:5 -> p1:1 -> p2:0 = p1 wins!', \
'p1:6 -> p2:5 -> p1:4 -> p2:0 = p1 wins!', \
'p1:6 -> p2:5 -> p1:4 -> p2:3 -> p1:2 -> p2:1 -> p1:0 = p2 wins!']
    '''
    game_description = ''
    if not root:
            return root
    if not root.children:
        return ['', ('{} = {} wins!'.format(
            abbreviated(root.value), root.value.opponent()[-2:]))]
    else:
        game_descriptions_list = []
        for child in root.children:
            game_descriptions_list += game_descriptions(child)
        for i in range(len(game_descriptions_list)):
            game_descriptions_list[i] = abbreviated(root.value) + ' -> ' +\
                game_descriptions_list[i]
        # To remove any duplicates that don't have the last conclusion string
        for item in game_descriptions_list:
            if 'win' not in item:
                game_descriptions_list.remove(item)
        return game_descriptions_list


def abbreviated(s):
    '''(SubtractSquareState) -> str
    
    Return an abbreviated str representation of SubtractSquareState s.
    '''
    return "{}:{}".format(s.next_player, s.current_total)

if __name__ == '__main__':
    import doctest
    doctest.testmod()