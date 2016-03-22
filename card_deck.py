import random

suites = ["heart", "club", "diamond", "spades"]
names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
values = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 10, 10]

class Card:
    def __init__(self, suite, name, value):
        self.suite = suite
        self.name = name
        self.value = value
    def __repr__(self):
        return self.name + " of " + self.suite

deck = []

for suite in suites:
    x=0
    # sets counter for index at 0 for each new suite
    for name in names:
        card = Card(suite, name, values[x])
        deck.append(card)
        x+=1
        # adds 1 to the counter so pulls the correct value from the value
        # then it swaps to the second suite and loops through all the values

class Hand:
    def __init__(self):
        self.hand_list = []
    def __repr__(self):
        return "{} {}".format("You have the following cards in your hand ", self.hand_list)
    def draw(self):
        drawn_card = deck[random.randint(0, len(deck)-1)]
        self.hand_list.append(drawn_card)
        deck.remove(drawn_card)
    def hand_value(self):
        total_value = 0
        for card in self.hand_list:
            total_value += card.value
        return total_value

# BREAK this is where the black jack class files should start
