import card_classes
import row_classes
import game_state

class Board:
    def __init__(self) -> None:
        self.game_tracker = game_state.GameStateTracker()
        
    def startRound(self):
        player_1_boards, player_2_boards = self.createBoards()
        player_1_pass = False
        player_2_pass = False
        
        while player_1_pass == False or player_2_pass == False:
            player_1_turn = self.readCard()
            if player_1_turn == "pass":
                player_1_pass = True
            else:
                card = card_classes.Card(self.searchCsv(player_1_turn))
                if card.row_type == "melee":
                    player_1_boards[0].addCard(card)
                elif card.rowtype == "range":
                    player_1_boards[1].addCard(card)
                else:
                    player_1_boards[2].addCard(card)
            
            player_2_turn = self.readCard()
            if player_2_turn == "pass":
                player_2_pass = True
            else:
                card = card_classes(self.searchCsv(player_2_turn))
                if card.row_type == "melee":
                    player_2_boards[0].addCard(card)
                elif card.rowtype == "range":
                    player_2_boards[1].addCard(card)
                else:
                    player_2_boards[2].addCard(card)
        
    
    def createBoards(self):
        player_1_melee = row_classes.Row()
        player_1_ranged = row_classes.Row()
        player_1_siege = row_classes.Row()
        
        player_2_melee = row_classes.Row()
        player_2_ranged = row_classes.Row()
        player_2_siege = row_classes.Row()
        return (player_1_melee, player_1_ranged, player_1_siege), (player_2_melee, player_2_ranged, player_2_siege)
    
    def searchCsv(self, given_card):
        pass
    
    def readCard(self):
        read_card = input("Type in a card name:\n")
        if read_card == "pass":
            return "pass"
        else:
            return read_card