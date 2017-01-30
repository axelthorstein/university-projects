from game_view import *
from player import *
import random


class GameState:
    """ A class establishing current game state """
    
    def __init__(self):
        """ (GameState) -> NoneType
        
        Initialize a class that controls which state the game currently is in.
        Also instantiate a current player variable that can be used to 
        determine what player is currently making a move.
        
        >>> g = GameState()
        >>> g.current_player
        0
        """
        
        self.current_player = 0
        
    def __str__(self):
        """ (GameState) -> str
        
        Return a string representation of the game class
        >>> s = GameState()
        >>> print(s)
        GameState
        """
        return 'GameState'
    
    def __eq__(self, L):
        """ (GameState, list of players) -> NoneType
        
        Return if two generated players are the same. 
        
        >>> g = GameState()
        >>> s.generate_players()
        >>> s.__eq__(s.generate_players())
        False
        """    
        return L[0] == L[1]
    
    def __repr__(self):
        """ (GameState) -> NoneType
        
        Initialize the GameState class and take the values from the
        GameState
        
        >>> s = GameState()
        >>> s.current_player
        0
        """     
        return 'GameState'
    
    def generate_players(self):
        """ (GameState) -> list of Players
        
        Generate two players, one for the user to interact with the game, and
        one to hold the computers strategy. Store in a list. 
        >>> g = GameState()
        >>> g.generate_players()
        [Player, Player]
        """        
        user = Player()
        computer = Player()
        return [user, computer]
        
    def next_move(self):
        """ (GameState) -> NoneType
        
        Switch turns. If the current player refers to 0, change to 1, and 
        vice versa. 
        >>> g = GameState()
        >>> g.next_move()
        >>> g.current_player
        1
        """
        self.current_player = abs(self.current_player - 1)
        
    def current_move(self):
        """ (GameState) -> NoneType
        
        Run the appropriate function on a players turn in order to take input
        form either the computer or user.
        """
        self.player = self.player_list[self.current_player]
        number = self.player.make_move()
        self.move(number)

    def is_over(self):
        """ (GameState) -> NoneType
        
        Check if the game is over and iff True, return True. redefined in child
        class
        """
        raise NotImplementedError


class SubtractSquaresGame(GameState):
    """ A class to handle the Subtract Squares game states """
    
    current_value = 100
    
    def __init__(self):
        """ (SubtractSquaresGame) -> NoneType
        
        Initialize the SubtractSquaresGame class and take the values from the
        GameState
        
        >>> s = SubtractSquaresGame()
        >>> s.current_player
        0
        """
        GameState.__init__(self)
        
    def __str__(self):
        """ (SubtractSquaresGame) -> str
        
        Return a string representation of the game class
        >>> s = SubtractSquaresGame()
        >>> print(s)
        Subtract a Square
        """
        return 'Subtract a Square'
        
    def generate_players(self):
        """ (SubtractSquaresGame) -> list of Players
        
        Generate two players, one for the user to interact with the game, and
        one to hold the computers strategy. Store in a list and overwrite the
        parent to be Subtract a Square game specific. 
        
        >>> s = SubtractSquaresGame()
        >>> s.generate_players()
        [Player, Player]
        """
        user = SubtractSquaresPlayer(SubtractSquaresGame())
        computer = SubtractSquaresComputer(SubtractSquaresGame())
        return [user, computer]    
    
    def setup(self):
        """ (SubtractSquaresGame) -> str
        
        Print a brief introduction of the game, as well as the aim of the game
        and any important information necessary to start the game. Only call
        when the game begins. Also generate the player list. 
        
        >>> s = SubtractSquaresGame()
        >>> s.setup()
        >>> s.player_list
        [Player, Player]
        """
        
        self.player_list = self.generate_players()
        print("""======================================================
        Welcome to Subtract a Square!
          The current number is 100 
Each player subtracts a square from the current number 
and the last player to make a subtraction losses!
                     ***                              """)

    def move(self, number):
        """ (SubtractSquaresGame) -> NoneType
        
        Initialize the SubtractSquaresGame class and take the values from the
        GameState
        
        >>> s = SubtractSquaresGame()
        >>> s.current_player
        0
        """
        
        new_value = self.subtract_from_current_score(number)
        
        SubtractSquaresGame.current_value = new_value

    def subtract_from_current_score(self, number):
        """ (SubtractSquaresGame) -> NoneType
        
        Subtract the inputed integer form the current score if it is a legal move.
        
        >>> s = SubtractSquaresGame()
        >>> s.subtract_from_current_score(4)
        84
        """
        while not self.legal_player_moves(number):
            number = self.player.make_move()
            
        square = int(number)
        if self.is_valid_number(square):
            return SubtractSquaresGame.current_value - (square * square)
        
    def legal_player_moves(self, number):
        """ (SubtractSquaresGame, int) -> Bool 
        
        Check whether the players input is valid and if not raise an error
        and ask for valid input. Check for anything that isn't a number.
        
        >>> s = SubtractSquaresGame()
        >>> s.legal_player_moves(20)
        Please enter a valid square less than the current value
                                ---                  
        False
        """
        if isinstance(number, int):
            return self.is_valid_number(number)
        
        while not number or not number.isnumeric():
            print('Error! Please enter a valid number')    
            number = self.player.make_move()
        return self.is_valid_number(number)
        
    def is_valid_number(self, number):
        """ (SubtractSquaresGame, int) -> bool
        
        Check if the number is valid input
        >>> s = SubtractSquaresGame()
        >>> s.is_valid_number(1)
        True
        """
        square = int(number)
        if not isinstance(square, int):
            print('Error! Please enter a valid square')
            return False
        elif square * square > SubtractSquaresGame.current_value:
            print("""Please enter a valid square less than the current value
                                ---                  """)
            return False
        else:
            return True   
        
    def is_over(self):
        """ (SubtractSquaresGame, int) -> bool 
        
        Check if the game is over and iff True, return True and print game over 
        information.
        
        >>> s = SubtractSquaresGame()
        >>> s.is_over()
        False
        """
        
        if SubtractSquaresGame.current_value == 0:
            print('Game over! {} loses!'.format(self.player.__str__()))
            return True
        else:
            return False

