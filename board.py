
import game_state
import row_classes
import csv
import card_classes


class Board:
    def __init__(self, interface) -> None:
        self.card_array = self.createCardArray()
        self.interface = interface
        self.game_state = game_state.GameStateTracker(self)
        self.player_1_boards, self.player_2_boards = self.createBoards()
        
    def createCardArray(self):
        final_array = ()
        with open("cards.csv", "r", newline="") as file:
            reader = csv.reader(file)
            final_array = tuple(reader)
        return final_array
            
    def createBoards(self):
        player_1_melee = row_classes.Row()
        player_1_ranged = row_classes.Row()
        player_1_siege = row_classes.Row()
        
        player_2_melee = row_classes.Row()
        player_2_ranged = row_classes.Row()
        player_2_siege = row_classes.Row()
        return (player_1_melee, player_1_ranged, player_1_siege), (player_2_melee, player_2_ranged, player_2_siege)
    
    def getBoard(self):
        return self.player_1_boards, self.player_2_boards
    
    def searchCsv(self, target_card_id): 
        return self.binarySearch(self.card_array, target_card_id)
            
    def binarySearch(self, given_list, target_card_id): # Remember to change once you add ID's to the cards
        middle = given_list[len(given_list) // 2]
        if middle[0] == target_card_id:
            return middle
        if target_card_id < middle[0]:
            return self.binarySearch(given_list[:middle])
        else:
            return self.binarySearch(given_list[middle + 1:])
    
    def requestCard(self, current_player_turn): # seperate into smaller functions. TODO
        played_card = self.readCard(current_player_turn)
        played_card(played_card, current_player_turn)
        played_card.placed(current_player_turn)
        
    def placeCard(self, card, current_player_turn):
        position_dict = {"Melee": 0, "Ranged": 1, "Siege": 2}
        if current_player_turn == 1:
            self.player_1_boards[position_dict.get(card.type)].addCard(card)
        else:
            self.player_2_boards[position_dict.get(card.type)].addCard(card)
        
    def readCard(self, current_player_turn):
        input_id = self.interface.requestCard(current_player_turn)
        if input_id == "pass": #condition may change in the future
            return "pass"
        return card_classes.Card(self.searchCsv(input_id))