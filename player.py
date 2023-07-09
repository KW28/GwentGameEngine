import scanner

class Player:
    def __init__(self, starting) -> None:
        self.melee_creatures = []
        self.ranged_creatures = []
        self.seige_creatures = []
        
    # waiting for a card scan from scanner and then returns False for pass and True for a card played
    def takeAction(self, card_array):
        if scanner.scanner() == 0:
            return False
        
    # recursive binary search to find the card info
    def cardLocator(self, card_array, target_id):
        middle = len(card_array)//2
        if middle == target_id:
            return card_array[middle]
        if middle < target_id:
            return self.cardLocator(card_array[middle:], target_id)
        else:
            return self.cardLocator(card_array[:middle], target_id)
        