#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import TQueue as Queue

###############################################################################
#test Queue.create() using Queue.is_empty() and Queue.size()
#Integration testing

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
        print('Error in create(): expected,' expected[0], 'when checking empty',
              Queue.is_empty(thing), '--', t['reason'])

    # check the initial size of the Queue
    if Queue.size(thing) != expected[1]:
        print('Error in create(): expected size', expected[1],
              'but found', Queue.size(thing), '--', t['reason'])


###############################################################################
# #test is_empty

#test size()

#test enqueue()

#test dequeue()

#test peek()


print('*** Test script completed ***')
