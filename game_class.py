import player
import csv

class Game:
    def __init__(self) -> None:
        self.current_round = 0
        self.player_1, self.player_2 = player.Player(True), player.Player(False)
        
    #counts athe rounds and does an assertion check
    def nextRound(self):
        assert(0 < self.current_round < 4 and type(self.current_round) == int, 
               f"did not pass assert and current round is {self.current_round}")
        self.current_round += 1
        
    # game engine loop, stops when both players pass
    def roundLoop(self):
        player_1_pass, player_2_pass = False, False
        
        while player_1_pass == False and player_2_pass == False:
            if self.player_1.takeAction() == False:
                player_1_pass = True
            if self.player_2.takeAction() == False:
                player_2_pass = True
            
    #loads csv for the rest of the program to work
    def loadCsv(self):
        final_array = []
        with open("cards.csv", "r") as file:
            reader = csv.reader(file)
            for item in reader:
                final_array.append(tuple(item))
                
        return tuple(final_array)
                
        
        
        