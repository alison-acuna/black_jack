import random

import random

suites = ["heart", "club", "diamond", "spades"]
names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
values = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 10, 10]
values_dict = {
            'A': 10,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10
            }
class Card:
    def __init__(self, suite, name):
        self.suite = suite
        self.name = name
    def __repr__(self):
        return self.name + " of " + self.suite 

deck = []

for suite in suites:
# loops through the suite and pulls first element
    for name in names:
#loops through the suite and pulls every element until the list is done
        card = Card(suite, name)
        deck.append(card)
# then it swaps to the second suite and loops through all the values
print(deck)
