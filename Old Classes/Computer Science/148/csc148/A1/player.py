from game_view import *
from generic_game_state import *
import random
import math
import time


class Player:
    """ """
    def __init__(self):
        """ (Player) -> NoneType
        
        Initialize a blank player to be overwritten once a game has been
        started, unless the game 
        >>> p = Player()
        >>> p
        'Player'
        """
        
    def __str__(self):
        """ (Player) -> str
        
        Return a str representation of a player.
        
        >>> p = Player()
        >>> p.__str__()
        'Player'
        """
        return 'Player'
        
    def __eq__(self, other):
        """ (GameState, list of players) -> NoneType
        
        Return if two generated players are the same. 
        
        >>> p1 = Player()
        >>> p2 = Player()
        >>> p1.__eq__(p2)
        False
        """    
        return self == other    
        
    def __repr__(self):
        """ (Player) -> str
        
        Return a str representation of a player that can be used.
        """
        return 'Player'
    
    
class SubtractSquaresPlayer(Player):
    """ """
    def __init__(self, game):
        """ (SubtractSquaresPlayer) -> NoneType
        
        Initialize a player and store their name for a subtract squares game. 
        >>> p = SubtractSquaresPlayer(SubtractSquaresGame)
        What is your name?
        >>> p.player_name
        'Axel'
        """
        print('What is your name?')
        self.player_name = input()
        self.game = game    
    
    def __str__(self):
        """ (SubtractSquaresPlayer) -> str
        
        Return the name of the player as a str.
        
        >>> p = SubtractSquaresPlayer(SubtractSquaresGame)
        What is your name?
        >>> p.player_name
        'Axel'
        """
        return '{}'.format(self.player_name)
    
    def make_move(self):
        """ (SubtractSquaresPlayer) -> int
        
        Ask the player for an input the satisfies the legal moves.
        
        >>> self.game.make_move()
        The current number is 100
        Please choose a square less than the current number
        (user input)
        """
        print('The current number is {}'.format(self.game.current_value))
        print('Please choose a square less than the current number')
        self.player_move = input()
        return self.player_move
    

class SubtractSquaresComputer(Player):
    """ """  
    
    def __init__(self, game):
        """ (SubtractSquaresComputer) -> NoneType
        
        Initialize a computer player to play against the user.
        >>> p = SubtractSquaresComputer(SubtractSquaresGame)
        >>> p
        
        """
        self.game = game
        
    def __str__(self):
        """ (SubtractSquaresComputer) -> str
        
        Return a str representation of a player.
        
        >>> p = Player()
        >>> p.__str__()
        'Player'
        """
        return 'Computer'
        
    def make_move(self):
        """ (SubtractSquaresComputer) -> int
        
        Have the computer choose a random int between 0 and the current value.
        Place a 2 second delay for a real time effect. 
        >>> SubtractSquaresComputer.make_move()
        It is the computers turn
        ...
        The computer entered (computers random int)
        """ 
        print("""It is the computers turn
        ...""")

        time.sleep(2)
        self.computer_move = random.randint(1, int(math.sqrt(self.game.current_value)))
        print("""The computer entered {}
        """.format(self.computer_move))        
        return self.computer_move
