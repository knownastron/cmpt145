# CMPT 145 Assignment 2 Question 1
# Sudoku Square checking

# test script

import a2q1 as Checker

test_check = [
    {'inputs'  : [1,2,3,4,5,6,7,8,9],
     'outputs' : [True],
     'reason'  : 'Simplest basic case of a legal group'},

    {'inputs'  : [1,1,1,1,1,1,1,1,1],
     'outputs' : [False],
     'reason'  : 'Simple case of an illegal group'},

    {'inputs'  : [1,3,5,7,9,2,4,6,8],
     'outputs' : [True],
     'reason'  : 'Simple shuffle of legal group'},

    {'inputs'  : [1,9,2,8,3,7,4,6,5],
     'outputs' : [True],
     'reason'  : 'Simple shuffle of legal group'},

    {'inputs'  : [0,2,3,4,5,6,7,8,9],
     'outputs' : [False],
     'reason'  : 'Value out of range'},

    {'inputs'  : [1,2,3,4,5,6,1,8,9],
     'outputs' : [False],
     'reason'  : 'Repeated first number'},

    {'inputs'  : [1,2,3,4,5,6,9,8,9],
     'outputs' : [False],
     'reason'  : 'Repeated last number'},

    {'inputs'  : [-1,2,3,4,5,6,7,8,9],
     'outputs' : [False],
     'reason'  : 'Value out of range: negative'},

    {'inputs'  : [10,2,3,4,5,6,7,8,9],
     'outputs' : [False],
     'reason'  : 'Value out of range: positive'},

    {'inputs'  : [1,3,5,7,19,2,4,6,8],
     'outputs' : [False],
     'reason'  : 'Value out of range: positive'},

    {'inputs'  : [1,9,2,8,3,7,4,-6,5],
     'outputs' : [False],
     'reason'  : 'Value out of range: negative'},
]


for t in test_check:
    group = t['inputs']
    expected = t['outputs']

    result = Checker.check(group)
    if result != expected[0]:
        print('Error in check(): expected ', expected[0],
              ' but got ', result, '--', t['reason'])



#######################################################################
# set up some sudoku squares to test check_all()

egstr_1 = ['4 6 7 5 8 1 2 3 9',
           '5 3 2 7 9 4 8 1 6',
           '1 8 9 3 2 6 5 7 4',
           '6 1 8 2 3 9 7 4 5',
           '7 2 3 1 4 5 9 6 8',
           '9 4 5 6 7 8 1 2 3',
           '3 5 1 9 6 7 4 8 2',
           '2 9 4 8 1 3 6 5 7',
           '8 7 6 4 5 2 3 9 1']

egstr_2 = ['6 1 9 3 2 8 7 4 5',
           '3 8 7 4 5 6 9 2 1',
           '2 4 5 7 9 1 8 6 3',
           '8 2 1 9 6 4 3 5 7',
           '5 3 6 2 1 7 4 8 9',
           '9 7 4 5 8 3 6 1 2',
           '4 5 2 6 3 9 1 7 8',
           '1 6 3 8 7 2 5 9 4',
           '7 9 8 1 4 5 2 3 6']

bad_egstr_1 = ['8 3 5 2 6 7 9 1 4',
               '6 1 4 8 5 9 7 3 2',
               '2 7 9 4 3 1 5 8 6',
               '7 4 2 6 9 3 8 5 1',
               '9 6 1 5 4 4 2 7 3',
               '5 8 3 1 7 2 6 4 9',
               '3 2 6 7 1 8 4 9 5',
               '1 5 7 9 4 6 3 2 8',
               '4 9 8 3 2 5 1 6 7']

bad_egstr_2 = ['8 2 6 1 5 3 4 7 9',
               '1 4 7 9 8 6 2 3 5',
               '5 9 3 7 2 4 6 8 1',
               '3 8 1 2 7 9 5 6 4',
               '9 5 2 6 4 8 3 1 7',
               '6 7 4 5 3 1 9 2 8',
               '4 6 5 8 1 2 7 9 3',
               '2 3 8 4 9 7 1 0 6',
               '7 1 9 3 6 5 8 4 2']

test_checkall = [
    {'inputs' : [egstr_1],
     'outputs': [True],
     'reason' : 'A true sudoku example'},
    {'inputs' : [egstr_2],
     'outputs': [True],
     'reason' : 'A true sudoku example'},
    {'inputs' : [bad_egstr_1],
     'outputs': [False],
     'reason' : 'A non sudoku example'},
    {'inputs' : [bad_egstr_2],
     'outputs': [False],
     'reason' : 'A non sudoku example'},]

for t in test_checkall:
    args_in = t['inputs']
    expected = t['outputs']
    square = []
    squarestr = args_in[0]
    for s in squarestr:
        square.append([int(x) for x in s.split()])
    result = Checker.check_all(square)
    if result != expected[0]:
        print('Error in checkall(): expected ', expected[0],
              ' but got ', result, '--', t['reason'])