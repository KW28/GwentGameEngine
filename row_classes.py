
#This class holds a subgle row used in the board class. Most methods are self explanitory.
class Row:
    def __init__(self) -> None:
        self.__cards = []
        self.active_affects = []
        self.weather = False
        
    def addCard(self, card):
        self.__cards.append(card)
    
    def removeCard(self, card_name):
        for i in range(len(self.__cards)):
            if self.__cards[i].name == card_name:
                self.__cards[i].pop()
    
    def getCard(self, card_name):
        for i in range(len(self._cards)):
            if self._cards[i].name == card_name:
                return self._cards[i]
            
    def getCardList(self):
        return self._cards
    
    def getHighest(self):
        highest = []
        highest_number = 0
        for item in self._cards:
            if item.power == highest_number:
                highest.append(item)
            elif item.power > highest_number:
                highest = []
                highest.append(item)
                highest_number = item.power
        return (tuple(highest), highest_number)
    
    def activeWeather(self):
        if self.weather == False:
            return
        for item in self._cards:
            item.setWeatherActive()
    
    def clearWeather(self):
        if self.weather == True:
            return
        for item in self._cards:
            item.current_power = item.setOriginalPower()
            self.applyBuffs()
                    
    def applyBuffs(self):
        effect_dictionary = {"Moral Boost": self.moralBoost, "Tight Bond": self.tightBond}
        for item in self.active_affects:
            if item in effect_dictionary:
                effect_dictionary.get(item)()
    
    def moralBoost(self):
        pass
    
    def tightBond(self, card_name):
        for item in self.__cards:
            item.tightBond(card_name)
            
            
class PriorityQueue:
    def __init__(self, parent_row) -> None:
        self.__effects_heap = []
        self.effect_dict = {"Weather": 1, "Tight Bond": 2, "Horn": 3, "Moral Boost": 4}
        
    def addEffect(self, given_effect):
        pass
    
    def heapifyTop(self, current_node_index):
        current_parent = self.__effects_heap[current_node_index]
        left_child_index = (current_node_index * 2) + 1
        right_child_index = (current_node_index * 2) + 2
        
        
        