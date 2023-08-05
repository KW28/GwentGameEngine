
#This class holds a subgle row used in the board class. Most methods are self explanitory.
class Row:
    def __init__(self) -> None:
        self.__cards = []
        self.active_affects = []
        self.priority_queue = PriorityQueue(self)
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
    # Change Weather to a normal card effect --TODO
    def activeWeather(self, *args):
        """if self.weather == True:
            return
        for item in self._cards:
            item.setWeatherActive()"""
        print("weather")
    
    def clearWeather(self, *args):
        if self.weather == False:
            return
        for item in self._cards:
            item.current_power = item.setOriginalPower()
            self.applyBuffs()
            
    def resetCardBuffs(self):
        pass
            
    def addBuff(self, buff):
        self.priority_queue.addEffect(buff)
            
    def updateBuffs(self): # Finish --TODO
        self.priority_queue.applyEffects()
    
    def removeBuff(self, buff):
        self.priority_queue.deleteEffect(buff)
    
    def moralBoost(self, *args):
        print("moral boost")
    
    def tightBond(self, *args):
        print("tight bond")
            
    def horn(self, *args):
        print("horn")
            
            
class PriorityQueue:
    def __init__(self, parent_row) -> None:
        self.row = parent_row
        self.__effects_heap = []
        self.effect_dict = {"Weather": 1, "Tight Bond": 2, "Horn": 3, "Moral Boost": 4}
        
    def addEffect(self, given_effect):
        self.__effects_heap.append(given_effect)
        if len(self.__effects_heap) == 1:
            return
        self.minHeapify()
        
    def deleteEffect(self, target):
        for i in range(len(self.__effects_heap)):
            if self.__effects_heap[i] == target:
                if i == len(self.__effects_heap):
                    self.__effects_heap.pop()
                    return
                last_node_value = self.__effects_heap[-1]
                self.__effects_heap[-1] = self.__effects_heap[i]
                self.__effects_heap[i] = last_node_value
                self.__effects_heap.pop()
                self.minHeapify()
                return
        
    def minHeapify(self):
        # The range is written wierdly, but it goes from (the number of elements) // 2 - 1 to 0, with a -1 step.
        # The reason we start from (n // 2 - 1) is because thats the first non leaf node in the heap.
        for index in range((len(self.__effects_heap) // 2) - 1, -1, -1):
            self.heapify(self.__effects_heap, index)
        
    def heapify(self, given_list, current_index):
        smallest = current_index
        left_child_index, right_child_index = (2 * current_index) + 1, (2 * current_index) + 2
        try:
            left_child_value = given_list[left_child_index][0]
        except IndexError:
            return given_list
        try:
            right_child_value =  given_list[right_child_index][0]
        except IndexError:
            right_child_value = None
            
        if self.effect_dict.get(left_child_value) < self.effect_dict.get(given_list[smallest][0]):
            smallest = left_child_index
            
        if right_child_value != None:
            if self.effect_dict.get(right_child_value) < self.effect_dict.get(given_list[smallest][0]):
                smallest = right_child_index
        
        if smallest == current_index:
            return given_list
        smallest_value = given_list[smallest]
        given_list[smallest] = given_list[current_index]
        given_list[current_index] = smallest_value
        return self.heapify(given_list, smallest)
        
    def applyEffects(self):
        apply_list = []
        apply_list.extend(self.__effects_heap)
        row_functions = {"Weather": self.row.activeWeather, "Tight Bond": self.row.tightBond, "Horn": self.row.horn, 
                        "Moral Boost": self.row.moralBoost}
          
        for index in range(len(apply_list) -1, -1, -1):
            smallest = apply_list[0]
            apply_list[0] = apply_list[-1]
            apply_list.pop()
            row_functions.get(smallest[0])(smallest)
            if len(apply_list) == 0:
                return 
            for index in range((len(apply_list) // 2) - 1, -1, -1):
                apply_list = self.heapify(apply_list, index)
                    
    def getHeap(self):
        return self.__effects_heap