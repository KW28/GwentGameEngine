# This is the interface that the game engine will connect to.
# The scanner and potentially different interfaces will have their own interfaces that will connect to this one.

import board

class GameEngineInterface:
    def __init__(self, connecting_interface) -> None:
        self.interface = connecting_interface
        self.__board = board.Board()
        
    def getBoard(self): 
        return self.__board.getBoard()
    
    def requestCard(self, current_player): 
        return self.interface.requestCard(current_player)
    
    def requestAgility(self): 
        return self.interface.requestAgility()
    
    def requestMedic(self, current_player):
        self.interface.requestMedic(current_player)
    