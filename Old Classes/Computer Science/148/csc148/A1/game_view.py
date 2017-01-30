from generic_game_state import *
from player import *


class GameView:
    """ A class for representing the game view """
    
    def __init__(self):
        """ (GameView) -> NoneType
        
        Initialtize a list of game options to be later chosen between, where
        the game options are a list of game classes. 
        >>> g = GameView()
        >>> g.game_options
        0
        """
        
        self.game_options = [SubtractSquaresGame()]
        
    def __str__(self):
        """ (GameView) -> str
        
        Return a string representation of the game class
        >>> g = GameView()
        >>> print(s)
        Subtract a Square
        """
        return '{}'.format(self.game)
    
    def __eq__(self, other):
        """ (GameView) -> NoneType
        
        We are never required to compare the gameview class to anything,
        I also don't have any arguments in my __init__ that I could 
        compare, any intasntiated variables, or other classes to compare.
        I can't think of any way to implement it without it being 
        redundant 
        """    
         
        raise NotImplementedError
    
    def __repr__(self):
        """ (GameView) -> NoneType
        
        Return a string of the class that can be evaluated.
        """    
        
        return '{}'.format(repr(self.game))
        
    def game_menu(self):
        """ (GameView) -> str
        
        Return an interactive menu of all avaliable games. Each game
        associated with a corresponding number.
        
        >>> game_menu()
        ======================================================
        Enter the number of the game you would like to play?
        1: Subtract a Square
        """
        
        print('======================================================')
        print('Enter the number of the game you would like to play?')
        
        i = 0
        menu_options = []
        while i < len(self.game_options):
            print('{}: {}'.format((i + 1), self.game_options[i]))
            i += 1
            menu_options.append(i)

        # Check if input is a game in the menu
        selected_game = int(input())
        while selected_game not in menu_options:
            print('Game not in menu, please enter valid game number')
            selected_game = int(input())
        self.game = self.game_options[selected_game - 1]
        
    def run_game(self):
        """ (GameView) -> NoneType
        
        Run the selected game until it ends, calling all appropriate functions
        from the game state, keeping track of score, and declaring the winner. 
        """
        
        self.game.setup()
        while not self.game.is_over():
            self.game.current_move()
            self.game.next_move()
            
            
if __name__ == "__main__":
    
    game = GameView()
    game.game_menu()
    game.run_game()
    
    