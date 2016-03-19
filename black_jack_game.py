import card_deck

# BREAK this is where the black jack class files should start

class BlackJackHand(Hand):
    def draw_print(self):
        self.draw()
        print(self.__repr__())
    def decision(self):
        hit_or = "hit"
        while hit_or == "hit":
            hit_or = input("Would you like to hit or stay? ").lower()
            if hit_or == "hit":
#this is my problem child- how do you call a method within a method
                self.draw_print()
            else:
                print("Next Player!")
            # call function that starts the next player
# CLASS black jack dealer hand class
class DealerHand(Hand):
    def initial_dealer_hand(self):
        return "{} {}".format("The dealers hand is one hidden card and ", self.hand_list[1:])
    def show_dealer_hand(self):
        return "{} {}".format("The dealers hand was ", self.hand_list)

# BREAK:  This is where the play file should start


black_jack_start = print("Welcome to Black Jack")
#INPUT ask for number of players
player_numbers = [input("How many player are playing today? ")]

for item in player_numbers:
    player_numbers[] = BlackJackHand()

#create a new player
hand_1 = BlackJackHand()

hand_1.draw_print()
hand_1.decision()

#hit and print


# INIT create number of hands for number of players
# INIT Deal to the dealer one up, one down
#Method for dealer hand - deal to 17
# METHOD from Hand Class: deal card to hand 1
# PRINT METHOD from black jack hand reveal card to the table
# INPUT Ask if the player would like to hit or stay
# if hit -
    # METOD from Hand Class:  Deal card to hand
    # Ask if the player would like to hit or stay
# if stay -
    #stay and cycle to the next player
# Select winner
    # reveal final dealer card
    # compare dealer value to each player
