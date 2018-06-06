#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03


# Assignment 3: ADTs and Testing

# This script is a starter file for testing the Statistics ADT

import Statistics as Stat

#####################################################################
# test Statistics.create()
# create() has no parameters, so we only need one test case
# but we can test several things about the statistics data structure

test_create = [
    {'inputs' : [],
     'outputs':[0, 0, None, None], #[count, avg, min, max]
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

    # q2 test: check initial the min and max values
    if thing['min'] != expected[2]:
        print('Error in create(): expected min', expected[2],
              ' but found ', thing['min'], '--', t['reason'])

    if thing['max'] != expected[2]:
        print('Error in create(): expected max', expected[3],
              ' but found ', thing['max'], '--', t['reason'])


#####################################################################
# test Statistics.add()
# these are integration tests

test_add = [
    {'inputs' : [0],    # single value to be added
     'outputs':[1, 0, 0, 0], # [count, avg, min, max]
     'reason' : 'No change to avg'},
    # q1 test cases:
    {'inputs' : [5],    # single value to be added
     'outputs':[1, 5, 5, 5], # [count, avg, min, max]
     'reason' : 'Positive integer change to avg'},
    {'inputs' : [-5],    # single value to be added
     'outputs':[1, -5, -5, -5], # [count, avg, min, max]
     'reason' : 'Negative integer change to avg'},
    {'inputs' : [5.55],    # single value to be added
     'outputs':[1, 5.55, 5.55, 5.55], # [count, avg, min, max]
     'reason' : 'Positive float change to avg'},
    {'inputs' : [-5.55],    # single value to be added
     'outputs':[1, -5.55, -5.55, -5.55], # [count, avg, min, max]
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

    #q2 tests: check the min and max values
    if abs(thing['min'] - expected[2]) > 0.00001:
        print('Error in add(): expected min', expected[2],
              ' but found ', thing['min'], '--', t['reason'])

    if abs(thing['max'] - expected[3]) > 0.00001:
        print('Error in add(): expected max', expected[2],
              ' but found ', thing['max'], '--', t['reason'])


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
     'outputs':[0],          #[count]
     'reason' : 'no values added'},
    {'inputs' : [10],    # data values to be added
     'outputs':[1],          #[count]
     'reason' : 'One value added'},
    {'inputs' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],    # data values to be added
     'outputs':[10],          #[count]
     'reason' : '10 integer values added - ascending order'},
    {'inputs' : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],    # data values to be added
     'outputs':[10],          #[count]
     'reason' : '10 integer values added - descending order'},
    {'inputs' : [1, 8, 9, 4, 5, 2, 3, 10, 6, 7],    # data values to be added
     'outputs':[10],          #[count]
     'reason' : '10 integer values added - mixed order'},
    {'inputs' : [1.0, 2.6, 3.42, 4.84, 5.1, 6.555, 7.0, 8.0, 9.8484, 10.5],    # data values to be added
     'outputs':[10],          #[count]
     'reason' : '10 float values added - ascending order'},
    {'inputs' : [10.5, 9.8484, 8.0, 7.0, 6.555, 5.1, 4.84, 3.42, 2.6, 1],    # data values to be added
     'outputs':[10],          #[count]
     'reason' : '10 float values added - descending order'},
    {'inputs' : [1.0, 8, 9.8484, 4.84, 5.1, 2.6, 3.42, 10.5, 6.555, 7],    # data values to be added
     'outputs':[10],          #[count]
     'reason' : '10 float values added - mixed order'},
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

#####################################################################
# test Statistics.minimum() and Statistic.maximum()

test_min_max = [
    {'inputs' : [],    # data values to be added
     'outputs':[None, None],          #[min, max]
     'reason' : 'no values added'},
    {'inputs' : [10],    # data values to be added
     'outputs': [10, 10],          #[min, max]
     'reason' : 'One value added'},
    {'inputs' : [1, 8, 9, 4, 5, 2, 3, 10, 6, 7],    # data values to be added
     'outputs': [1, 10],          #[min, max]
     'reason' : '10 positive integer values added - mixed order'},
    {'inputs' : [-1, -8, -9, -4, -5, -2, -3, -10, -6, -7],    # data values to be added
     'outputs': [-10, -1],          #[min, max]
     'reason' : '10 negative integer values added - mixed order'},
    {'inputs' : [1, -8, 9, -4, 5, -2, 3, -10, 6, -7],    # data values to be added
     'outputs': [-10, 9],          #[min, max]
     'reason' : '10 positive and negative integer values added - mixed order'},
    {'inputs' : [1.0, 8, 9.8484, 4.84, 5.1, 2.6, 3.42, 10.5, 6.555, 7],    # data values to be added
     'outputs': [1.0, 10.5],          #[min, max]
     'reason' : '10 positive float values added - mixed order'},
    {'inputs' : [-1.0, -8, -9.8484, -4.84, -5.1, -2.6, -3.42, -10.5, -6.555, -7],    # data values to be added
     'outputs': [-10.5, -1.0],          #[min, max]
     'reason' : '10 positive float values added - mixed order'},
    {'inputs' : [1.0, -8, 9.8484, -4.84, 5.1, -2.6, 3.42, -10.5, 6.555, -7],    # data values to be added
     'outputs': [-10.5, 9.8484],          #[min, max]
     'reason' : '10 positive and negative float values added - mixed order'},
]

for t in test_min_max:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call min() and max()
    min_result = Stat.minimum(thing)
    max_result = Stat.maximum(thing)

    # we'll open the data structure in these tests
    # check the min
    if min_result == None:
        if min_result != expected[0]:
            print('Error in minimum(): expected minimum', expected[0],
                  ' but found ', min_result, '--', t['reason'])
    elif abs(min_result - expected[0]) > 0.00001:
        print('Error in minimum(): expected minimum', expected[0],
              ' but found ', min_result, '--', t['reason'])

    # check the max
    if max_result == None:
        if max_result != expected[1]:
            print('Error in maximum(): expected maximum', expected[1],
                  ' but found ', max_result, '--', t['reason'])
    elif abs(max_result - expected[1]) > 0.00001:
        print('Error in maximum(): expected maximum', expected[1],
              ' but found ', max_result, '--', t['reason'])


print('*** Test script completed ***')
