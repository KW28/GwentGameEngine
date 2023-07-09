import game_class
import player

# This file is only for unit testing. Can be completely ignored.


def runTests():
    test1()
    test2()
    test3()

def test1():
    game = game_class.Game()
    print(game.loadCsv())
    print("Test 1 Done\n")
    
def test2():
    game = game_class.Game()
    player = game.player_1.cardLocator(game.loadCsv(), 2)
    if player == ('2', '2', '2', '2'):
        print("Test 2 Passed\n")
    else:
        print(f"Test 2 Failed {player}\n")
        
    
def test3():
    game = game_class.Game()
    player = game.player_1.cardLocator(game.loadCsv(), 0)
    if player == ('pass',):
        print("Test 2 Passed\n")
    else:
        print(f"Test 2 Failed {player}\n")