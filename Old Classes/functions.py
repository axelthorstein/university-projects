#def game_lengths(root):
    #''' (GameStateNode) -> {int: int}
    
    #Return a dict that represents the distribution of game lengths in the
    #tree rooted at root. Each key is a length of game >= 1, and its value is
    #the number of games that are that long. The length of a game is the
    #number of moves in the game.
    
    #>>> s = SubtractSquareState('p1', current_total = 6)
    #>>> root = GameStateNode(s)
    #>>> root.grow()
    #>>> print(root)
    #>>> game_lengths(root)
    #>>> game_lengths(root) == {6: 1, 3: 3}
    #True
    #'''
    #if root.children:
        #return max([game_lengths(c) for c in root.children]) + 1
    #else:
        #return 1
    #game_lengths = {}
    
    #if not root:
        #return {}
    #if root.children:
        #for child in root.children:
            #game = game_lengths(child)
        
    #if not root.children:
        #pass
        ##from each leaf, come back up and count how long the game lasted

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
    ['p1:6 -> p2:2 -> p1:1 -> p2:0 = p1 wins!', 'p1:6 -> p2:5 -> p1:1 -> p2:0 = p1 wins!', 'p1:6 -> p2:5 -> p1:4 -> p2:0 = p1 wins!', 'p1:6 -> p2:5 -> p1:4 -> p2:3 -> p1:2 -> p2:1 -> p1:0 = p2 wins!']
    '''
    game_descriptions_list = []
    game_description = ''

    if not root:
        return []
    if root.children:
        for child in root.children:
            game_state = game_descriptions(child)
            game_description += game_state
            game_descriptions_list.append(game_description)
    if not root.children:
        game_description += '{} = {} wins!'.format(abbreviated(root.value), root.value.opponent()[-2:])
        return game_description
    else:
        game_description += abbreviated(root.value) + ' -> '
        return game_description    

    return game_descriptions_list