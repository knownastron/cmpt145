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

print('Running', games, 'games with', players, 'players drawing', cards,
'cards each')

#score_board keeps track of wins per player
score_board = {}
for i in range(players):
    score_board[str(i+1)] = 0
