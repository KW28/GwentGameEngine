
class Row:
    def __init__(self) -> None:
        self._cards = []
        self.weather = False
        
    def addCard(self, card):
        self._cards.append(card)
    
    def removeCard(self, card_name):
        for i in range(len(self._cards)):
            if self._cards[i].name == card_name:
                self._cards[i].pop
    
    def getCard(self, card_name):
        for i in range(len(self._cards)):
            if self._cards[i].name == card_name:
                return self._cards[i]
    
    def activeWeather(self):
        if self.weather == False:
            return
        for item in self._cards:
            item.power = 1
            self.weather = True
            

    def clearWeather(self):
        if self.weather == True:
            return
        for item in self._cards:
            item.power = item.original_power
            
    def getCardList(self):
        return self._cards
    
