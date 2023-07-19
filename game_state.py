
class GameStateTracker:
    def __init__(self) -> None:
        self.player_1_wins = 0
        self.player_2_wins = 0
        
    def incrementWins(self, winning_player):
        if winning_player == 1:
            self.player_1_wins += 1
        else:
            self.player_2_wins += 1
    
    