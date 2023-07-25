import card_classes
import row_classes


class Board:
    def __init__(self) -> None:
        self.player_1_boards, self.player_2_boards = self.createBoards()
    
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
    
    #This function will be changed once arduino code is set up.
    def readCard(self):
        read_card = input("Type in a card name:\n")
        if read_card == "pass":
            return "pass"
        else:
            return read_card