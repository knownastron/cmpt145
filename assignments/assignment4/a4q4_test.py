#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import TQueue as Queue

###############################################################################
# test Queue.create() using Queue.is_empty() and Queue.size()
# Integration testing

test_create = [
    {'inputs' : [],
     'outputs':[True, 0],
     'reason' : 'Checking initial values'},
]

for t in test_create:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Queue data structure
    thing = Queue.create()

    # check that Queue is empty
    if Queue.is_empty(thing) != expected[0]:
        print('Error in create(): expected,', expected[0], 'when checking empty',
              Queue.is_empty(thing), '--', t['reason'])

    # check the initial size of the Queue
    if Queue.size(thing) != expected[1]:
        print('Error in create(): expected size', expected[1],
              'but found', Queue.size(thing), '--', t['reason'])


###############################################################################
# test is_empty, test size(), test enqueue(), test dequeue, test peek()
# Integration testing
# In this test, A queue is created, all inputs are enqueued, then values for
# is_empty(), size(), and peek() are checked. 5 items are dequeued and the three
# values are checked again

#outputs: [is_empty after enqueue, size after enqueue, peek after enqueue,
#           is_empty after dequeue, size after dequeue, peek after dequeue]
test_queue = [
    {'inputs' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     'outputs': [False, 10, 1, False, 5, 6],
     'reason' : 'integers ascending - False on both empty check'},
    {'inputs' : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
     'outputs': [False, 10, 10, False, 5, 5],
     'reason' : 'integers descending - False on both empty check'},
    {'inputs' : [1.1, 2.6, 3.6, 4.9, 5.1],
     'outputs': [False, 5, 1.1, True, 0, None],
     'reason' : 'Floats ascending - True on second empty check'},
    {'inputs' : [10.1, 9.2, 8.5, 7.7, 6.9],
     'outputs': [False, 5, 10.15, True, 0, None],
     'reason' : 'Floats decending - True on second empty check'},
    # {'inputs' : [],
    #  'outputs': [True, 0, None],
    #  'reason' : ''},

]

for t in test_queue:
    args_in = t['inputs']
    expected = t['outputs']

    # create the Queue data structure
    thing = Queue.create()

    #enqueue all items in args_in
    for i in args_in:
        Queue.enqueue(thing, i)

    # check that Queue is empty
    if Queue.is_empty(thing) != expected[0]:
        print('Error in is_empty(): expected,', expected[0], 'when checking empty',
              Queue.is_empty(thing), '--', t['reason'])

    # check the size of the Queue
    if Queue.size(thing) != expected[1]:
        print('Error in size(): expected size', expected[1],
              'but found', Queue.size(thing), '--', t['reason'])

    #check the peek value of the Queue only if size != 0
    if Queue.size(thing) != 0:
        if Queue.peek(thing) != expected[2]:
            print('Error in peek(): expected', expected[2],
                'but found', Queue.peek(thing), '--', t['reason'])

    #dequeue 5 items from Queue
    for i in range(5):
        Queue.dequeue(thing)

    # check that Queue is empty
    if Queue.is_empty(thing) != expected[3]:
        print('Error in is_empty(): expected,', expected[3], 'when checking empty',
              Queue.is_empty(thing), '--', t['reason'])

    # check the size of the Queue
    if Queue.size(thing) != expected[4]:
        print('Error in size(): expected size', expected[4],
              'but found', Queue.size(thing), '--', t['reason'])

    #check the peek value of the Queue only if size != 0
    if Queue.size(thing) != 0:
        if Queue.peek(thing) != expected[5]:
            print('Error in peek(): expected', expected[5],
                'but found', Queue.peek(thing), '--', t['reason'])


print('*** Test script completed ***')
