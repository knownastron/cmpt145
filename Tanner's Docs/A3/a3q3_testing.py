# CMPT 145
# Assignment 3: ADTs and Testing

import a3q3 as Counter

#####################################################################
# test Counter.create()
# create() has no parameters, so we only need one test case
# but we can test several things about the statistics data structure

test_create = [
    {'inputs' : [],  
     'outputs':[0, 0],  # [size, total]
     'reason' : 'Checking initial values'},
]

for t in test_create:
    args_in = t['inputs']       # pointless, but keeps the pattern consistent
    expected = t['outputs']

    # create the Counter data structure
    thing = Counter.create()

    # we'll open the data structure in these tests
    # check the initial size
    if thing['size'] != expected[0]:
        print('Test: Create: Error in create(): expected size', expected[0],
              ' but found ', thing['size'], '--', t['reason'])

    # check the initial total
    if thing['total'] != expected[1]:
        print('Test: Create: Error in create(): expected total', expected[1],
              ' but found ', thing['total'], '--', t['reason'])



#####################################################################
# test Counter.see()
# these are integration tests

test_see = [
    {'inputs' : [0],    # single value to be recorded
     'outputs':[1, 1], # [size, total]
     'reason' : 'Single number'},

    {'inputs' : ['a'],    # single value to be recorded
     'outputs':[1, 1], # [size, total]
     'reason' : 'Single letter'},

    {'inputs' : ['word'],    # single value to be recorded
     'outputs':[1, 1], # [size, total]
     'reason' : 'Single word'},

    {'inputs' : [7.5],    # single value to be recorded
     'outputs':[1, 1], # [size, total]
     'reason' : 'Single floating point'},
]

for t in test_see:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Counter data structure
    thing = Counter.create()

    # now call see()
    Counter.see(thing, args_in[0])

    # now call seen()
    result = Counter.seen(thing, args_in[0])

    # we'll open the data structure in these tests
    # check the count
    if thing['size'] != expected[0]:
        print('Test see Error in see(): expected size', expected[0],
              ' but found ', thing['size'], '--', t['reason'])

    # check the ave
    if thing['total'] != expected[1]:
        print('Test see Error in see(): expected total', expected[1],
              ' but found ', thing['total'], '--', t['reason'])

    # check the item is in the dictionary
    adict = thing['counting']
    if args_in[0] not in adict:
        print('Test see Error in see(): expected to find', args_in[0],
              ' but it was missing --', t['reason'])

    # check the count from the dictionary
    counted = adict[args_in[0]]
    if args_in[0] in adict and counted != 1:
        print('Test see Error in see(): expected to count', args_in[0],
              ' exactly once, but found', counted, '--', t['reason'])

    # check the count from return value
    if args_in[0] in adict and result != 1:
        print('Test see Error in see(): expected to count', args_in[0],
              ' exactly once, but found', result, '--', t['reason'])

#####################################################################
# Integration tests for Counter

test_count = [
    {'inputs' : [[0,0,0,0,0], [0,1]],   # [record, seen]
     'outputs': [1, 5, [5,0], [0]],    #[size, total, seen, unique]
     'reason' : 'All the same'},

    {'inputs' : [[1,0,1,0,1,1], [0,1]],   # [record, seen]
     'outputs': [2, 6, [2,4], [0,1]],    #[size, total, seen, unique]
     'reason' : 'Just two integers'},

    {'inputs' : [['a', 'b', 'c'], ['a','1']],   # [record, seen]
     'outputs': [3, 3, [1,0], ['a', 'b', 'c']],    #[size, total, seen, unique]
     'reason' : 'All different'},


]



for t in test_count:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Counter data structure
    thing = Counter.create()
    # add the give values to the
    for val in args_in[0]:
        Counter.see(thing, val)

    # now call size()
    size = Counter.size(thing)

    if size != expected[0]:
        print('Test count Error in size(): expected size', expected[0],
              ' but found ', size, '--', t['reason'])

    # now call total()
    total = Counter.total(thing)

    if total != expected[1]:
        print('Test count Error in total(): expected total', expected[1],
              ' but found ', total, '--', t['reason'])

    for i in range(len(args_in[1])):
        # check seen
        val = args_in[1][i]
        count = expected[2][i]
        result = Counter.seen(thing, val)
        if result != count:
            print('Test count Error in seen(): expected to see', val,
                  'exactly', count, 
                  'times, but found ', result, '--', t['reason'])

    # check the result of unique()
    uni = Counter.unique(thing)
    uni.sort()
    exp = expected[3]
    exp.sort()
    if uni != exp:
        print('Test count Error in unique(): expected ', exp,
              ' but found ', uni, '--', t['reason'])



print('*** Test script completed ***')
