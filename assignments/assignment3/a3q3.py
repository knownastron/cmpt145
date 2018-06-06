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
    """
    Purpose:
        Deal num_cards cards to num_player players from deck
    Pre-conditions:
        :param num_cards: an integer for the number of cards per player
        :param num_players: an integer for each player to be dealt cards
        :param deck: A deck of cards to be dealt from
    Post-conditions:
        deck has all cards that are dealt removed
    Return:
        A list of lists of cards that each player was dealt
    """

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

def value(card):
    """
    Purpose:
        get the value of a card
    Pre-conditions:
        :param card: a card
    Post-conditions:
        (none)
    Return:
        An integer value representing the value of the card
    """

    letters = ['A', 'J', 'Q', 'K']
    first_char = card[0]


    if first_char in letters: #check that first char is A, J, Q, or K
        if first_char == letters[0]:
            return 1
        elif first_char == letters[1]:
            return 11
        elif first_char == letters[2]:
            return 12
        elif first_char == letters[3]:
            return 13
    elif len(card) == 3: #if len(card) is 3 then the card is a 10
        return 10
    else: #return the value of the first character
        return int(first_char)


def maximum(list_of_cards):
    """
    Purpose:
        get the card with the highest value
    Pre-conditions:
        :param card: a list of cards
    Post-conditions:
        (none)
    Return:
        the card with the highest value
    """

    cur_max = list_of_cards[0]

    for card in list_of_cards[1:]:
        if value(card) > value(cur_max):
            cur_max = card

    return cur_max

def maximum(list_of_cards):
    """
    Purpose:
        get the card with the lowest value
    Pre-conditions:
        :param card: a list of cards
    Post-conditions:
        (none)
    Return:
        the card with the lowest value
    """

    cur_min = list_of_cards[0]

    for card in list_of_cards[1:]:
        if value(card) < value(cur_min):
            cur_min = card

    return cur_min

#
# my_deck = create()
# deck1 = []
# deck2 = []
# deck3 = []
# deck4 = []
# for k in range(13):
#     deck1.append(my_deck[k])
# for k in range(13,26):
#     deck2.append(my_deck[k])
# for k in range(26, 39):
#     deck3.append(my_deck[k])
# for k in range(39,52):
#     deck4.append(my_deck[k])
# print(deck1)
# print(deck2)
# print(deck3)
# print(deck4)
# deal_hands = deal(11, 5, my_deck)
# for i in deal_hands:
#     print(i)
#
# print(my_deck)
