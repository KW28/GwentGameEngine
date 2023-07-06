import csv

class CardFinder:
    def __init__(self) -> None:
        self.csv_size = 0
        self.setup()
    
    def setup(self):
        with open("cards.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.csv_size += 1
    
    def findCard(self, target_id):
        cards_generator = self.cardSearchGenerator()
    
    def recursiveBinarySearch(self, target_id, generator_object, search_min, search_max):
        pass
        

    def cardSearchGenerator(self):
        with open("cards.csv", "r") as file:
            reader = csv.reader(file)
            for item in reader:
                yield item