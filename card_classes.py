
class Card:
    def __init__(self, card_statistics, board_class) -> None:
        self.__parent_board = board_class
        self.name = card_statistics[0]
        self.type = card_statistics[1]
        self.__original_power = card_statistics[2]
        self.attributes = card_statistics[3]
        self.is_gold = bool(int(card_statistics[4]))
        self.current_power = self.__original_power
        
    def placed(self):
        effects_dict = {"Agile": self.placedAgile, "Medic": self.placedMedic, "Moral Boost": self.placedMoralBoost, 
                        "Muster": self.placedMuster, "Spy": self.placedSpy, "Tight Bond": self.placedTightBond}
        for item in self.attributes:
            if item in effects_dict:
                effects_dict.get(item)()
                
    def placedAgile(self):
        pass
        
    def placedMedic(self):
        print("healing!")
    
    def placedMoralBoost(self):
        pass
    
    def placedMuster(self):
        pass
    
    def placedSpy(self):
        pass
    
    def placedTightBond(self):
        pass
                
    def setOriginalPower(self):
        self.current_power = self.__original_power
    
    def setWeatherActive(self):
        self.current_power = 1
    
    def moralBoost(self):
        pass
    
    def tighBond(self, card_name):
        if self.name == card_name:
            self.current_power *= 2
    