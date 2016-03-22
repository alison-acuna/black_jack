import random
import card_deck

class BlackJackHand(card_deck.Hand):
    def __init__(self, name):
         #Hand.__init__(self)
        self.name = name
    def __repr__(self):
        print("{} {} {}".format(self.name, ", you have the following cards in your hand ", self.hand_list))
    def start_round(self):
        self.draw()
        self.draw()
    def decision(self):
        # missing a self positional argument
        hit_or = "hit"
        while hit_or == "hit":
            hit_or = input("Would you like to hit or stay? ").lower()
            if hit_or == "hit":
                self.draw()
                self.__repr__()
                if self.hand_value() > 21:
                    print("You bust!")
                    return None

# CLASS black jack dealer hand class

# player1 = BlackJackHand("A")
#
# player1.decision()

class DealerHand(card_deck.Hand):
    def initial_dealer_hand(self):
        print("{} {}".format("The dealers hand is one hidden card and ", self.hand_list[1:]))
    def show_dealer_hand(self):
        print("{} {}".format("The dealers hand was ", self.hand_list))
