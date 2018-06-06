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
     'outputs':['AH', 'KC' , '4S', 'JC', '8D', 'yas'], #[first, last, random, random, random]
     'reason' : 'Check first & last value and 3 arbitrarily chosen values'},
]

for t in test_create:
    args_in = t['inputs']
    expected = t['outputs']

#create the Card data structure
thing = Card.create()

for output in expected:
    if output not in thing:
        print('Error in create(): expected card', expected[2],
              'did not appear in deck', '--', t['reason'])

print('*** Test script completed ***')
