import board

class GameStateTracker:
    def __init__(self, board) -> None:
        self.__board = board
        self.player_1_wins = 0
        self.player_2_wins = 0
        
        # Tracks whether it's player 1's turn or player 2's turn
        self.current_player_turn = 1
        
        
    def updateTurn(self):
        if self.current_player_turn == 1:
            self.current_player_turn += 1
        else:
            self.current_player_turn -= 1
    
    