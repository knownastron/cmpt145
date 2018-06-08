#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

#Assignment 3 Question 4

import sys as sys
import a3q3 as Card

#take in console input
games = int(sys.argv[1])
players = int(sys.argv[2])
cards = int(sys.argv[3])

def play_game(games, players, cards):
    """
    Purpose:
        Plays a card game a number of times with the desired number of
        players and cards. Prints out the result
    Pre-conditions:
        :param games: integer for desired number of games to play
        :param players: integer for desired number of players
        :param cards: integer for desired number of cards per player
    Post-conditions:
        (none)
    Return:
        (none)
    """
    #score_board keeps track of wins per player
    score_board = {}
    for i in range(players):
        score_board[str(i+1)] = 0

    #main loop that runs the games desired amount of times
    for game in range(games):
        deck = Card.create() #create the deck

        #if more cards than 52 cards are required, some players don't get cards
        dealt_deck = Card.deal(cards, players, deck)

        cur_max_card = None #tracks the winning card
        cur_max_val = 0 #tracks the value of the winning card
        cur_max_index = None #keeps track of the winning player

        #checks each hand for the maximum card, compares with current max card
        for index, hand in enumerate(dealt_deck):
            #in case of a tie, player who reveals card last wins
            if Card.value(Card.maximum(hand)) >= cur_max_val:
                cur_max_val = Card.value(Card.maximum(hand))
                cur_max_card = Card.maximum(hand)
                cur_max_index = index + 1

        #Prints who, what card, and what value won the current game
        print('Player', cur_max_index, 'won with a', cur_max_card,
              '(' + str(cur_max_val) + ')')

        #adds win to the scoreboard
        score_board[str(cur_max_index)] += 1

    #Prints out the final score
    print('---SCOREBOARD---')
    for key in score_board:
        print('Player', key, 'won a total of', score_board[key], 'games')

#check if more cards are required than necessary to play
if players * cards > 52:
    print('There are not enough cards for', players, 'players to be dealt',
           cards, 'cards each. Please retry with different number of' +
           ' players and/or cards.')
else:
    print('Running', games, 'games with', players, 'players drawing', cards,
    'cards each')
    play_game(games, players, cards)
