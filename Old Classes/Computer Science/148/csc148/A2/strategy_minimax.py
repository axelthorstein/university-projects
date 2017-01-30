from strategy import Strategy
from game_state import GameState
from subtract_square_state import SubtractSquareState


class StrategyMinimax(Strategy):
    '''Interface to suggest moves for a Minimax Strategy.

    '''

    def __init__(self, interactive=False):
        '''(StrategyMinimax, bool) -> NoneType

        Create new Strategy (self), prompt user if interactive.
        '''
        self.scores = []
        self.game_state_score = 0
        self.max_move = -1
        
    def minimax(self, state):
        '''(Strategy, GameState) -> float

        Return whether a player wins, looses, or ties, and the likelihood 
        for each move. 
        >>> s = SubtractSquareState('p1', current_total=5)
        >>> sm = StrategyMinimax()
        >>> sm.minimax(s)
        -1.0
        '''    
        if state.over:
            return state.outcome()
        else:
            for move in state.possible_next_moves():
                new_game_state = state.apply_move(move)
                self.game_state_score = (self.minimax(new_game_state))
                self.game_state_score = (self.game_state_score * -1)
                if self.max_move < self.game_state_score:
                    self.max_move = self.game_state_score
            return self.max_move
            
    def suggest_move(self, state):
        '''(Strategy, GameState) -> Move

        Suggest a next move for state.
        >>> s = SubtractSquareState('p1', current_total=16)
        >>> sm = StrategyMinimax()
        >>> sm.suggest_move(s)
        SubtractSquareMove(16)
        '''
        new_game_states = []
        new_scores = []
        for move in state.possible_next_moves():
            new_game_states.append(state.apply_move(move))
        for game_state in new_game_states:
            self.scores.append(self.minimax(game_state))
        for score in self.scores:
            new_scores.append(score * -1)
        best_score = new_scores.index(max(new_scores))
        return state.possible_next_moves()[best_score]