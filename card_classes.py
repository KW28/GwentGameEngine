
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
        effects_dict = {"Agile": self.agile, "Medic": self.medic, "Moral Boost": self.moralBoost, 
                        "Muster": self.muster, "Spy": self.spy, "Tight Bond": self.tightBond}
        for item in self.attributes:
            if item in effects_dict:
                effects_dict.get(item, lambda: "invalid")()
            else:
                print(f"{item} not found")
        
    def not_found(self):
        print("not found")
    
    def agile(self):
        pass
    
    def medic(self):
        print("healing!")
    
    def moralBoost(self):
        pass
    
    def muster(self):
        pass
    
    def spy(self):
        pass
    
    def tightBond(self):
        pass
    