
class Card:
    def __init__(self, card_statistics, board_class) -> None:
        self.__parent_board = board_class
        self.name = card_statistics[0]
        self.type = card_statistics[1]
        self.__original_power = card_statistics[2]
        self.attributes = card_statistics[3]
        self.is_gold = bool(int(card_statistics[4]))
        self.current_power = self.__original_power
        
    def placed(self, current_player_turn):
        effects_dict = {"Agile": self.placedAgile, "Medic": self.placedMedic, "Moral Boost": self.placedMoralBoost, 
                        "Muster": self.placedMuster, "Spy": self.placedSpy, "Tight Bond": self.placedTightBond}
        for item in self.attributes:
            if item in effects_dict:
                effects_dict.get(item)(current_player_turn)
                
    def placedAgile(self, *args):
        pass
        
    def placedMedic(self, current_player_turn):
        print("healing!")
    
    def placedMoralBoost(self, *args):
        pass
    
    def placedMuster(self, *args):
        pass
    
    def placedSpy(self, current_player_turn):
        pass
    
    def placedTightBond(self, *args):
        pass
                
    def setOriginalPower(self):
        self.current_power = self.__original_power
    
    def setWeatherActive(self):
        self.current_power = 1
    
    def moralBoost(self, given_card):
        if self != given_card:
            self.current_power += 1
    
    def tighBond(self, given_card):
        if self.name == given_card.name:
            self.current_power *= 2
    
    def horn(self, given_card):
        if self.is_gold is True:
            return
        if self != given_card:
            self.current_power *= 2