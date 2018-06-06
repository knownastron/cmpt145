#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

#Assignment 3 Question 3

import random as rand

def create():
    """
    Purpose:
        Create a deck of cards
    Pre-conditions:
        (none)
    Post-conditions:
        a new deck is allocated
    Return:
        A reference to deck of cards
    """
    suits = ['H', 'D', 'S', 'C']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    deck = []

    for suit in suits:
        for number in numbers:
            deck.append(number + suit)

    return deck


def deal(num_cards, num_players, deck):
    cards_dealt = []

    for player in range(num_players):
        cur_player_hand = []
        for i in range(num_cards):
            #if there are no more cards in the deck
            if (len(deck) == 0):
                #add the current hand to the dealt cards and return the cards
                cards_dealt.append(cur_player_hand)
                return cards_dealt

            card_index = rand.randint(0, len(deck)-1) #choose random index
            cur_card = deck[card_index] #select card at index
            deck.remove(cur_card) #remove selected card from deck
            cur_player_hand.append(cur_card) #add to the current hand

        #add the hand of this player to the output list
        cards_dealt.append(cur_player_hand)

    return cards_dealt

my_deck = create()
deal_hands = deal(5, 8, my_deck)
for i in deal_hands:
    print(i)

print(my_deck)
