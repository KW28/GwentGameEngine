
#This is a test file and everything in here does not effect how the rest of the engine functions.
import board
import card_classes
import csv
import row_classes

def test1():
    row = row_classes.Row()
    heap = row_classes.PriorityQueue(row)
    heap.addEffect(("Horn", 3))
    heap.addEffect(("Weather", 1))
    heap.addEffect(("Moral Boost", 4))
    heap.addEffect(("Tight Bond", 2))
    heap.addEffect(("Horn", 3))
    heap.addEffect(("Moral Boost", 4))
    heap.addEffect(("Tight Bond", 2))
    heap.deleteEffect(("Weather", 1))
    #print(heap.getHeap())
    heap.applyEffects()
    
    
def test2(card_stats):
    card = card_classes.Card(card_stats, None)
    print(card.name, card.type, card.current_power, card.attributes, card.is_gold)
    
def test3(card_stats):
    card = card_classes.Card(card_stats, None)
    print(card.name, card.type, card.current_power, card.attributes, card.is_gold)
    card.placed()
    
def test4():
    with open("cards.csv", "r", newline='') as file:
        reader = csv.reader(file)
        card_list = tuple(reader)
        print(len(reader))
    
