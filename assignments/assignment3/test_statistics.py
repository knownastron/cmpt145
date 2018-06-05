# Assignment 3: ADTs and Testing

# This script is a starter file for testing the Statistics ADT

import Statistics as Stat

#####################################################################
# test Statistics.create()
# create() has no parameters, so we only need one test case
# but we can test several things about the statistics data structure

test_create = [
    {'inputs' : [],
     'outputs':[0, 0],
     'reason' : 'Checking initial values'},
]

for t in test_create:
    args_in = t['inputs']       # pointless, but keeps the pattern consistent
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # we'll open the data structure in these tests
    # check the initial count
    if thing['count'] != expected[0]:
        print('Error in create(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the initial ave
    if thing['avg'] != expected[1]:
        print('Error in create(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.add()
# these are integration tests

test_add = [
    {'inputs' : [0],    # single value to be added
     'outputs':[1, 0], # [count, avg]
     'reason' : 'No change to avg'},
    # TODO Add more test cases
    {'inputs' : [5],    # single value to be added
     'outputs':[1, 5], # [count, avg]
     'reason' : 'Positive integer change to avg'},
    {'inputs' : [-5],    # single value to be added
     'outputs':[1, -5], # [count, avg]
     'reason' : 'Negative integer change to avg'},
    {'inputs' : [5.55],    # single value to be added
     'outputs':[1, 5.55], # [count, avg]
     'reason' : 'Positive float change to avg'},
    {'inputs' : [-5.55],    # single value to be added
     'outputs':[1, -5.55], # [count, avg]
     'reason' : 'Negative float change to avg'},
]

for t in test_add:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()

    # now call add()
    Stat.add(thing, args_in[0])

    # we'll open the data structure in these tests
    # check the count
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    # changed the if statment to an abs difference calculation
    if abs(thing['avg'] - expected[1]) > 0.00001:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.mean()

test_mean = [
    {'inputs' : [0,0,0,0,0],    # data values to be added
     'outputs':[5, 0],          #[count, avg]
     'reason' : 'All zeroes'},
    # TODO Add more test cases
    {'inputs' : [10,5,8,2,8],    # data values to be added
     'outputs':[5, 6.6],          #[count, avg]
     'reason' : 'All positive integers'},
    {'inputs' : [-10,-5,-8,-2,-8],    # data values to be added
     'outputs':[5, -6.6],          #[count, avg]
     'reason' : 'All negative integers'},
    {'inputs' : [10.01, 5.55, 8.222, 2.90, 8.8],    # data values to be added
     'outputs':[5, 7.096399],          #[count, avg]
     'reason' : 'All positive floats'},
    {'inputs' : [-10.01, -5.55, -8.222, -2.90, -8.8],    # data values to be added
     'outputs':[5, -7.096399],          #[count, avg]
     'reason' : 'All negative floats'},
    {'inputs' : [-10.01, 5, -8.222, 2.90, -8],    # data values to be added
     'outputs':[5, -3.6664],          #[count, avg]
     'reason' : 'Mixed positive and negative, floats and integers'},
]

for t in test_mean:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call mean()
    result = Stat.mean(thing)

    # we'll open the data structure in these tests
    # check the count
    if thing['count'] != expected[0]:
        print('Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    # changed the if statment to an abs difference calculation
    if abs(thing['avg'] - expected[1]) > 0.00001:
        print('Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])

    # check the result of mean()
    # changed the if statment to an abs difference calculation
    if abs(result - expected[1]) > 0.00001:
        print('Error in mean(): expected avg', expected[1],
              ' but found ', result, '--', t['reason'])

#####################################################################
# test Statistics.count()

test_count = [
    {'inputs' : [],    # data values to be added
     'outputs':[0, 0],          #[count, avg]
     'reason' : 'no values added'},
    {'inputs' : [10],    # data values to be added
     'outputs':[1, 10],          #[count, avg]
     'reason' : 'One value added'},
    {'inputs' : [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],    # data values to be added
     'outputs':[10, 5],          #[count, avg]
     'reason' : '10 values added'},
]

for t in test_count:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call count()
    result = Stat.count(thing)

    # we'll open the data structure in these tests
    # check the count
    if result != expected[0]:
        print('Error in count(): expected count', expected[0],
              ' but found ', result, '--', t['reason'])



print('*** Test script completed ***')
