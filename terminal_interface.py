import game_engine_interface

class TerminalInterface:
    def __init__(self) -> None:
        self.game_interface = game_engine_interface.GameEngineInterface(self)
    
    def requestCard(self, current_player): 
        return int(input(f"Player {current_player}, type in a card ID: "))
    
    def requestAgility(self): 
        answer = input("This card has Agility, type in whether you want the row to be Melee or Ranged: ").lower()
        assert(answer in ["melee", "ranged"], "Please type melee or ranged.")
        return answer
    
    def getBoard(self): 
        print(self.game_interface.getBoard())
        
    def requestMedic(self, current_player_turn):
        return int(input(f"Player {current_player_turn}, revive a card from your discard pile and submit ID: "))
    