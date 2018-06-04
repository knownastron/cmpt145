# CMPT 145
# Assignment 3: ADTs and Testing

import a3q2 as Stat

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
        print('Test: Create: Error in create(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the initial ave
    if thing['avg'] != expected[1]:
        print('Test: Create: Error in create(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.add()
# these are integration tests

test_add = [
    {'inputs' : [0],    # single value to be added
     'outputs':[1, 0], # [count, avg]
     'reason' : 'No change to avg'},

    {'inputs' : [1],    # single value to be added
     'outputs':[1, 1], # [count, avg]
     'reason' : 'Positive value'},

    {'inputs' : [-3],    # single value to be added
     'outputs':[1, -3], # [count, avg]
     'reason' : 'Negative value'},

    {'inputs' : [7.5],    # single value to be added
     'outputs':[1, 7.5], # [count, avg]
     'reason' : 'Floating point positive value'},

    {'inputs' : [-18.5],    # single value to be added
     'outputs':[1, -18.5], # [count, avg]
     'reason' : 'Floating point negative value'},
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
        print('Test add: Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    if thing['avg'] != expected[1]:
        print('Test add: Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])



#####################################################################
# test Statistics.mean()

test_mean = [
    {'inputs' : [0,0,0,0,0],    # data values to be added
     'outputs':[5, 0],          #[count, avg]
     'reason' : 'All zeroes'},

    {'inputs' : [1,2,3,4,5],    # data values to be added
     'outputs':[5, 3],          #[count, avg]
     'reason' : 'All positive integers'},

    {'inputs' : [-8, -3, -4],    # data values to be added
     'outputs':[3, -5],          #[count, avg]
     'reason' : 'All negative integers'},

    {'inputs' : [1.1,2.2,3.3,4.4],    # data values to be added
     'outputs':[4, 2.75],          #[count, avg]
     'reason' : 'All positive floats'},

    {'inputs' : [-8.1, -3.1, -4.4],    # data values to be added
     'outputs':[3, -5.2],          #[count, avg]
     'reason' : 'All negative floats'},

    {'inputs' : [1.1,2.2,3.3,4.4,5.5],    # data values to be added
     'outputs':[5, 3.3],          #[count, avg]
     'reason' : 'Mixed floats'},

    {'inputs' : [-1,-2,-3,4,5],    # data values to be added
     'outputs':[5, 0.6],          #[count, avg]
     'reason' : 'Mixed integers'},

    {'inputs' : [-1,-2.2,0,4,5.7],    # data values to be added
     'outputs':[5, 1.3],          #[count, avg]
     'reason' : 'Mixed integers and floats'},
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
        print('Test mean: Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the ave
    if abs(thing['avg'] - expected[1]) > 0.0001:
        print('Test mean: Error in add(): expected avg', expected[1],
              ' but found ', thing['avg'], '--', t['reason'])

    # check the result of mean()
    if abs(result - expected[1]) > 0.0001:
        print('Test mean: Error in mean(): expected avg', expected[1],
              ' but found ', result, '--', t['reason'])



#####################################################################
# test Statistics.count()

test_count = [
    {'inputs' : [0,0,0,0,0],    # data values to be added
     'outputs':[5],          #[count]
     'reason' : 'Odd count'},

    {'inputs' : [-8, -3, -4],    # data values to be added
     'outputs':[3],          #[count]
     'reason' : 'Odd count'},

    {'inputs' : [1.1,2.2,3.3,4.4],    # data values to be added
     'outputs':[4],          #[count]
     'reason' : 'Even count'},

    {'inputs' : [],    # data values to be added
     'outputs':[0],          #[count, avg]
     'reason' : 'No values added'},
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
    if thing['count'] != expected[0]:
        print('Test count Error in add(): expected count', expected[0],
              ' but found ', thing['count'], '--', t['reason'])

    # check the result of count()
    if result != expected[0]:
        print('Test count: Error in count(): expected avg', expected[0],
              ' but found ', result, '--', t['reason'])



#####################################################################
# test Statistics.maximum()

test_maximum = [
    {'inputs' : [0,0,0,0,0],    # data values to be added
     'outputs':[0],          #[maximum]
     'reason' : 'All equalt to maximum'},

    {'inputs' : [1,2,3,4,5],    # data values to be added
     'outputs':[5],          #[maximum]
     'reason' : 'All positive integers'},

    {'inputs' : [-8, -3, -4],    # data values to be added
     'outputs':[-3],          #[maximum]
     'reason' : 'All negative integers'},

    {'inputs' : [1.1,2.2,3.3,4.4],    # data values to be added
     'outputs':[4.4],          #[maximum]
     'reason' : 'All positive floats'},

    {'inputs' : [-8.1, -3.1, -4.4],    # data values to be added
     'outputs':[-3.1],          #[maximum]
     'reason' : 'All negative floats'},

    {'inputs' : [1.1,-2.2,3.3,4.4,5.5],    # data values to be added
     'outputs':[5.5, 3.3],          #[maximum]
     'reason' : 'Mixed floats'},

    {'inputs' : [-1,-2,-3,4,5],    # data values to be added
     'outputs':[5],          #[maximum]
     'reason' : 'Mixed integers'},

    {'inputs' : [-1,-2.2,0,4,5.7],    # data values to be added
     'outputs':[5.7],          #[maximum]
     'reason' : 'Mixed integers and floats'},

    {'inputs' : [100,-2.2,0,4,5.7],    # data values to be added
     'outputs':[100],          #[maximum]
     'reason' : 'Max first'},

    {'inputs' : [100,-2.2,2345,4,5.7],    # data values to be added
     'outputs':[2345],          #[maximum]
     'reason' : 'Max between'},

    {'inputs' : [],    # data values to be added
     'outputs':[None],          #[maximum]
     'reason' : 'No values added'},
]

for t in test_maximum:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call count()
    result = Stat.maximum(thing)

    # we'll open the data structure in these tests
    # check the count
    if thing['max'] != expected[0]:
        print('Test count Error in maximum(): expected count', expected[0],
              ' but found ', thing['max'], '--', t['reason'])

    # check the result of count()
    if result != expected[0]:
        print('Test count: Error in maximum(): expected avg', expected[0],
              ' but found ', result, '--', t['reason'])



#####################################################################
# test Statistics.maximum()

test_minimum = [
    {'inputs' : [0,0,0,0,0],    # data values to be added
     'outputs':[0],          #[minimum]
     'reason' : 'All equalt to minimum'},

    {'inputs' : [1,2,3,4,5],    # data values to be added
     'outputs':[1],          #[minimum]
     'reason' : 'All positive integers'},

    {'inputs' : [-8, -3, -4],    # data values to be added
     'outputs':[-8],          #[minimum]
     'reason' : 'All negative integers'},

    {'inputs' : [1.1,2.2,3.3,4.4],    # data values to be added
     'outputs':[1.1],          #[minimum]
     'reason' : 'All positive floats'},

    {'inputs' : [-8.1, -3.1, -4.4],    # data values to be added
     'outputs':[-8.1],          #[minimum]
     'reason' : 'All negative floats'},

    {'inputs' : [1.1,-2.2,3.3,4.4,5.5],    # data values to be added
     'outputs':[-2.2],          #[minimum]
     'reason' : 'Mixed floats'},

    {'inputs' : [-1,-2,-3,4,5],    # data values to be added
     'outputs':[-3],          #[minimum]
     'reason' : 'Mixed integers'},

    {'inputs' : [-1,-2.2,0,4,5.7],    # data values to be added
     'outputs':[-2.2],          #[minimum]
     'reason' : 'Mixed integers and floats'},

    {'inputs' : [-100,-2.2,0,4,5.7],    # data values to be added
     'outputs':[-100],          #[minimum]
     'reason' : 'Min first'},

    {'inputs' : [-100,-2.2,-2345,4,5.7],    # data values to be added
     'outputs':[-2345],          #[minimum]
     'reason' : 'Min between'},

    {'inputs' : [],    # data values to be added
     'outputs':[None],          #[minimum]
     'reason' : 'No values added'},
]

for t in test_minimum:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Statistics data structure
    thing = Stat.create()
    # add the give values to the
    for val in args_in:
        Stat.add(thing, val)

    # now call count()
    result = Stat.minimum(thing)

    # we'll open the data structure in these tests
    # check the count
    if thing['min'] != expected[0]:
        print('Test count Error in minimum(): expected count', expected[0],
              ' but found ', thing['min'], '--', t['reason'])

    # check the result of count()
    if result != expected[0]:
        print('Test count: Error in minimum(): expected avg', expected[0],
              ' but found ', result, '--', t['reason'])





print('*** Test script completed ***')
