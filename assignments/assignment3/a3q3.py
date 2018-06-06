#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

#Assignment 3 Question 3

def create():
    suits = ['H', 'D', 'S', 'C']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10' 'J', 'Q', 'K']

    deck = []

    for suit in suits:
        for number in numbers:
            deck.append(number + suit)

    return deck
