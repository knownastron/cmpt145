#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

#Assignment 3 Question 3 testing script

import a3q3 as Card

#####################################################################
# test Statistics.create()
#Unit testing

test_create = [
    {'inputs' : [],
     'outputs':['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H',
                'JH', 'QH', 'KH',
                'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D',
                'JD', 'QD', 'KD',
                'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S',
                'JS', 'QS', 'KS',
                'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C',
                'JC', 'QC', 'KC',],
     'reason' : 'comprehensive testing - every card should appear in deck'},
]

for t in test_create:
    args_in = t['inputs']
    expected = t['outputs']

#create the Card data structure
thing = Card.create()

for card in expected:
    if card not in thing:
        print('Error in create(): expected card', card,
              'did not appear in deck', '--', t['reason'])


#####################################################################
# test Card.deal()
# Integration testing


test_deal = [
    {'inputs' : [0, 0], #[num_cards, num_players]
     'outputs': [0, 0, 52], #[hands dealt, cards per hand, cards remaining in deck]
     'reason' : 'Zero num_cards and zero num_players - boundary testing'},
    {'inputs' : [1, 1], #[num_cards, num_players]
     'outputs': [1, 1, 51], #[hands dealt, cards per hand, cards remaining in deck]
     'reason' : '1 num_cards and 1 num_players - boundary testing'},
    {'inputs' : [6, 5], #[num_cards, num_players]
     'outputs': [5, 6, 22], #[hands dealt, cards per hand, cards remaining in deck]
     'reason' : '6 num_cards and 5 num_players - typical case'},
    {'inputs' : [13, 4], #[num_cards, num_players]
     'outputs': [4, 13, 0], #[hands dealt, cards per hand, cards remaining in deck]
     'reason' : 'entire deck is dealt_hand'},
    {'inputs' : [11, 5], #[num_cards, num_players]
     'outputs': [5, 8, 0], #[hands dealt, cards in *last* hand, cards remaining in deck]
     'reason' : 'deck runs out of cards before all players dealt all cards'},

]

for t in test_deal:
    args_in = t['inputs']
    expected = t['outputs']

    #create the Card data structure
    thing = Card.create()

    #call Card.deal()
    dealt_hand = Card.deal(args_in[0], args_in[1], thing)

    #check if deck runs out of cards before all players dealt all cards
    if args_in[0] * args_in[1] > 52:
        #check that the last hand has the correct number of cards
        last_hand = dealt_hand[len(dealt_hand)-1]
        if len(last_hand) != expected[1]:
            print('Error in deal(): expected', expected[1], 'in the last hand but',
                  'found', len(last_hand), 'cards in the last hand', '--', t['reason'])

        #check that deck has the correct number of cards remaining
        if len(thing) != expected[2]:
            print('Error in deal(): expected', expected[1],
                  'cards remaining in deck but found', len(thing),
                  'cards remaining in deck', '--', t['reason'])
    else:
        #check that the number of hands dealt is correct
        if len(dealt_hand) != expected[0]:
            print('Error in deal(): expected', expected[1], 'hands dealt but found',
                  len(dealt_hand), 'hands dealt', '--', t['reason'])

        #check that each hand has the correct number of cards
        for hand in dealt_hand:
            if len(hand) != expected[1]:
                print('Error in deal(): expected', expected[1],
                      'cards in hand but found', len(hand),
                      'cards in hand', '--', t['reason'])

        #check that deck has the correct number of cards remaining
        if len(thing) != expected[2]:
            print('Error in deal(): expected', expected[2],
                  'cards remaining in deck but found', len(thing),
                  'cards remaining in deck', '--', t['reason'])

#####################################################################
# test Card.value()
# Integration testing


test_value = [
    {'inputs' :[0],
     'outputs': [0], #[values to be returned]
     'reason' : '0 is sometimes passed to value() by minimum() or maximim()'},
    {'inputs' :['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H',
               'JH', 'QH', 'KH',
               'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D',
               'JD', 'QD', 'KD',
               'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S',
               'JS', 'QS', 'KS',
               'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C',
               'JC', 'QC', 'KC',],
     'outputs': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], #[values to be returned]
     'reason' : 'comprehensive testing, all cards in deck are tested'},
]

for t in test_value:
    args_in = t['inputs']
    expected = t['outputs']

    #check if the value of each card
    for index, card in enumerate(args_in):
        if Card.value(card) != expected[index % 13]:
            print('Error in Card.value(), expected', expected[index % 13],
            'but got', Card.value(card))


#####################################################################
# test Card.maximum() and Card.minimum()
# Integration testing


test_min_max = [
    {'inputs' :[], #a deck of cards
     'outputs': [0, 0], #[min value, max value]
     'reason' : 'Empty hand'},
    {'inputs' :['AH'], #a deck of cards
     'outputs': [1, 1], #[min value, max value]
     'reason' : 'Exactly one card'},
    {'inputs' :['AH', '2D', '5C', '9D', 'KS', 'KC'], #a deck of cards
     'outputs': [1, 13], #[min value, max value]
     'reason' : 'Decending deck with duplicate max value'},
    {'inputs' :['QD', 'JS', '7C', '4D', '3S', 'AS', 'AH'], #a deck of cards
     'outputs': [1, 12], #[min, max]
     'reason' : 'Ascending deck with duplicate min value'},
    {'inputs' :['9S', '10S', '2C', 'JH', '3D', '2H', '9H', '5D'], #a deck of cards
     'outputs': [2, 11], #[min value, max value]
     'reason' : 'Mixed order deck'},
]

for t in test_min_max:
    args_in = t['inputs']
    expected = t['outputs']

    #get the min and the max of each card
    min = Card.minimum(args_in)
    max = Card.maximum(args_in)

    #check if value of min card is equal expected value
    if Card.value(min) != expected[0]:
        print('Error in Card.minimum(), expected', expected[0],
              'but got', Card.value(min))

    #check if value of max card is equal expected value
    if Card.value(max) != expected[1]:
        print('Error in Card.value(), expected', expected[1],
              'but got', Card.value(max))


#####################################################################
# test Card.average()
# Integration testing


test_average = [
    {'inputs' :[], #a deck of cards
     'outputs': [0], #[average]
     'reason' : 'Empty list'},
    {'inputs' :['3D'], #a deck of cards
     'outputs': [3], #[average]
     'reason' : 'Single element list'},
    {'inputs' :['AH', '2D', '5C', '9D', 'KS', 'KC'], #a deck of cards
     'outputs': [7.166667], #[average]
     'reason' : 'Decending deck with duplicate max value'},
    {'inputs' :['QD', 'JS', '7C', '4D', '3S', 'AS', 'AH'], #a deck of cards
     'outputs': [5.571428], #[average]
     'reason' : 'Ascending deck with duplicate min value'},
    {'inputs' :['9S', '10S', '2C', 'JH', '3D', '2H', '9H', '5D'], #a deck of cards
     'outputs': [6.375], #[average]
     'reason' : 'Mixed order deck'},
]

for t in test_average:
    args_in = t['inputs']
    expected = t['outputs']

    #get average
    average = Card.average(args_in)


    if abs(average - expected[0]) > 0.00001:
        print('Error in Card.average(), expected', expected[0],
              'but got', average)

print('*** Test script completed ***')
