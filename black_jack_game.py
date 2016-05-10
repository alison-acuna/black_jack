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


class BlackJackHand(Hand):
    def __init__(self, name):
        Hand.__init__(self)
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

class DealerHand(Hand):
    def initial_dealer_hand(self):
        print("{} {}".format("The dealers hand is one hidden card and ", self.hand_list[1:]))
    def show_dealer_hand(self):
        print("{} {}".format("The dealers hand was ", self.hand_list))



# INPUT ask for number of players + create correct number of players
players = []

def set_table():
    number_of_players = int(input("How many players are playing today? "))
    for player in range(0 , number_of_players):
        name_1 = input("What is the {} player's name? ".format(str(player + 1)))
        print(name_1)
        players.append(BlackJackHand(name_1))
#    return players

def again():
    while True:
        try:
            play_again = input("Would you like to play again? y/n ").lower()
            if play_again == "y":
                main()
            else:
                print("Thank you for playing!")
                return None
        except:
            print("That is not a valid entry. Please try again.")
            return None

def dealer_game(dealer):
    dealer.draw()
    dealer.draw()
    dealer.initial_dealer_hand()
    if dealer.hand_value() < 17:
        dealer.draw()
        print("The dealer hits.")
        dealer.initial_dealer_hand()
        if dealer.hand_value() > 21:
            print("The dealerbust! The table wins!")

def players_game(players):
    for player in players:
        player.start_round()
        player.__repr__()
        player.decision()

def win_conditions(players, dealer):
    dealer.show_dealer_hand()
    for player in players:
        if player.hand_value() > 21:
            print("{} {}".format(player.name, "You already busted"))
        elif player.hand_value() > dealer.hand_value():
            print("{} {}".format(player.name, "You win!"))
        elif player.hand_value() < dealer.hand_value():
            print("{} {}".format(player.name, "The house wins."))
        elif player.hand_value() == dealer.hand_value():
            print("{} {}".format(player.name, "You tie."))
        else:
            print("Not sure what happened")

def main():
    print ("Welcome to Black Jack")
    set_table()
    dealer = DealerHand()
    dealer_game(dealer)
    players_game(players)
    win_conditions(players, dealer)
    again()

main()
