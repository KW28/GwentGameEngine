import player
import board

class Game:
    def __init__(self) -> None:
        self.current_round = 0
        self.board = board.Board()
        self.player_1, self.player_2 = player.Player(), player.Player()
        
    def start_of_round_draw(self):
        assert(0 < self.current_round < 4 and type(self.current_round) == int, 
               f"did not pass assert and current round is {self.current_round}")
        
        if self.current_round == 1:
            self.player_1.draw_cards(10)
            self.player_2.draw_cards(10)
            
        elif self.current_round == 2:
            self.player_1.draw_cards(2)
            self.player_2.draw_cards(2)
            
        elif self.current_round == 3:
            self.player_1.draw_cards(1)
            self.player_2.draw_cards(1)
        
        else:
            raise SyntaxError(f"next_round function could not detect a round and passed assertion check. current round is {self.current_round}")
        
        
    def next_round(self):
        assert(0 < self.current_round < 4 and type(self.current_round) == int, 
               f"did not pass assert and current round is {self.current_round}")
        self.current_round += 1
        
    def round_loop(self):
        player_1_pass, player_2_pass = False, False
        
        while player_1_pass == False and player_2_pass == False:
            self.player_1.take_action()
            self.player_2.take_action()
        
        
        