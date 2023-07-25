
#This is a test file and everything in here does not effect how the rest of the engine functions.
import board
import card_classes

def test1():
    test_dict = {"one": 1, "two": 2, "three": 3}
    test_list = ["one", "two", "three"]
    for item in test_list:
        if item in test_dict:
            print(item, test_dict.get(item))
        else:
            print("not here")
    
def test2(card_stats):
    card = card_classes.Card(card_stats, None)
    print(card.name, card.type, card.current_power, card.attributes, card.is_gold)
    
def test3(card_stats):
    card = card_classes.Card(card_stats, None)
    print(card.name, card.type, card.current_power, card.attributes, card.is_gold)
    card.placed()