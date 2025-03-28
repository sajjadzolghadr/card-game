import random
suits = ('Hearts' , 'Diamonds' , 'Spades' , 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven' , 'Eight' , 'Nine' , 'Ten' ,'Jack' , 'Queen' , 'King' ,'Ace')
values = {'Two':2 , 'Three':3 , 'Four':4 , 'Five':5 , 'Six':6 , 'Seven':7 , 'Eight':8 , 'Nine':9 , 'Ten':10 ,'Jack':10 , 'Queen':10 , 'King':10 ,'Ace':11}
playing = True


class Card():
    def __init__(self , suit ,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank+' of '+self.suit

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit , rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has:" +deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self , card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21  and self.aces > 0  :
            self.value -= 10
            self.aces -= 1

    
class Chips():
    def __init__(self , total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

 
def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry Please provide an integer")   
        else:
            if chips.bet > chips.total:
                print("Sorry you do not have enough chips! You have:{}".format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing 
    while True:
        x = input('Hit or Stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck,hand)
            return True
        elif x[0].lower() == 's':
            print('Player Stands')
            playing = False
            return False
        else:
            print('Sorry , I did no understand that. please enter h or s only! ')
            continue

def show_some(player,dealer):
    #show only one of the dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])
    #show 2 cards of player's cards
    print("\n Player's Hand: " ,*player.cards,sep ='\n')

def show_all(player,dealer):
    #show all the dealer's cards
    print("\n Dealer's Hand: " ,*dealer.cards,sep ='\n')
    print(f"Value of Dealer's hand is :{dealer.value}")
    #show all the player's cards
    print("\n Player's Hand: " ,*player.cards,sep ='\n')
    print(f"Value of Player's hand is :{player.value}")


def player_busts(player,dealer,chips):
    print('Bust Player!')
    chips.lose_bet()
    

def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Bust Dealer!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()

def push(player,dealer):
    print('Dealer and Player tie! Push')

while True:
    print("Welcome to BlackJack")
    #Create deck
    deck = Deck()
    deck.shuffle()
    #Create and give card to player and dealer
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #Set up player's chips
    player_chips = Chips()

    #prompt the player for their bet
    take_bet(player_chips)

    # show some card player and dealer
    show_some(player_hand,dealer_hand)
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand , dealer_hand,player_chips)
            continue

        break

    if player_hand.value<=21:
    
        while dealer_hand.value<player_hand.value:
            hit(deck,dealer_hand)
        
        show_all(player_hand , dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand, player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand, player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand, player_chips)
        else:
            push(player_hand,dealer_hand)
    
    print(f"\n player total chips are at:{player_chips.total}")

    # ask do you want play again?
    new_game = input('do you want play again y/n : ')
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        break

        








    