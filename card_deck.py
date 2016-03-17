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
# loops through the suite and pulls first element
    x=0
    # sets counter for index at 0 for each new suite
    for name in names:
#loops through the suite and pulls every element until the list is done
        card = Card(suite, name, values[x])
        deck.append(card)
        x+=1
        # adds 1 to the counter so pulls the correct value from the value
# then it swaps to the second suite and loops through all the values
print(deck)



class Hand:
    def __init__(self):
        self.hand_list = []
    def __repr__(self):
        return "You have the following cards in your hand " + self.hand
    def draw(self):
        drawn_card = deck[random.randint(0, len(deck)-1)]
        self.hand_list.append(drawn_card)
        deck.remove(drawn_card)


hand_1 = Hand()
#creates an instance
hand_1.draw()
#runs the draw method on this instance
print(hand_1.hand_list)


#create hand specific draw functions
#makes sure that the deck list track cards in all hands
#recreate for x number of players
# create game
