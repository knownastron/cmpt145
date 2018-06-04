# CMPT 145: Linear ADTs
# Test the Queue ADT

# The script does not look directly at the queue data structure.
# instead, it probes the effects of different operations, and 
# matches the results of the probing against the expectations.

import Queue2 as Queue

# test consistency for new queue with size() and is_empty()
test_create = [
    {'inputs' : None,
     'outputs': None,
     'reason' : 'create, size, is_empty all consistent'}
]

for t in test_create:
    the_queue = Queue.create()
    res1 = Queue.is_empty(the_queue)
    if not res1:
        print("Error: is_empty returned", res1, 'expected', True, '--', t['reason'])
    res2 = Queue.size(the_queue)
    if  res2 != 0:
        print("Error: size returned", res2, 'expected', 0, '--', t['reason'])

# test consistency of size, is_empty, peek after a few enqueue
test_enqueue = [
    {'inputs' : [7],
     'outputs': [False, 1, 7],
     'reason' : 'size, is_empty, peek all consistent after one enqueue'},
    {'inputs' : ['a'],
     'outputs': [False, 1, 'a'],
     'reason' : 'size, is_empty, peek all consistent after one enqueue'},
    {'inputs' : [7, 'a'],
     'outputs': [False, 2, 7],
     'reason' : 'size, is_empty, peek all consistent after two enqueue'},
    {'inputs' : [4, 7, 3, 'a', 'g'],
     'outputs': [False, 5, 4],
     'reason' : 'size, is_empty, peek all consistent after several enqueue'},
]


for t in test_enqueue:
    args_in = t['inputs']
    expected = t['outputs']
    the_queue = Queue.create()

    for v in args_in:
        Queue.enqueue(the_queue, v)

    res1 = Queue.is_empty(the_queue)
    if res1 != expected[0]:
        print("Error: is_empty returned", res1, 'expected', expected[0], '--', t['reason'])

    res2 = Queue.size(the_queue)
    if  res2 != expected[1]:
        print("Error: size returned", res2, 'expected', expected[1], '--', t['reason'])

    res3 = Queue.peek(the_queue)
    if  res3 != expected[2]:
        print("Error: peek returned", res3, 'expected', expected[2], '--', t['reason'])



# test consistency dequeue size, is_empty peek, after a few enqueue
test_dequeue = [
    {'inputs' : [7],
     'outputs': [7, 0, True, None],
     'reason' : 'dequeue consistent after one enqueue'},
    {'inputs' : ['a'],
     'outputs': ['a', 0, True, None],
     'reason' : 'dequeue consistent after one enqueue'},
    {'inputs' : [7, 'a'],
     'outputs': [7, 1, False, 'a'],
     'reason' : 'dequeue consistent after two enqueue'},
    {'inputs' : [4, 7, 3, 'a', 'g'],
     'outputs': [4, 4, False, 7],
     'reason' : 'dequeue consistent after several enqueue'},
]


for t in test_dequeue:
    args_in = t['inputs']
    expected = t['outputs']
    the_queue = Queue.create()

    for v in args_in:
        Queue.enqueue(the_queue, v)

    res0 = Queue.dequeue(the_queue)
    if res0 != expected[0]:
        print("Error: dequeue returned", res0, 'expected', expected[0], '--', t['reason'])

    res1 = Queue.size(the_queue)
    if  res1 != expected[1]:
        print("Error: size returned", res1, 'expected', expected[1], '--', t['reason'])

    res2 = Queue.is_empty(the_queue)
    if res2 != expected[2]:
        print("Error: is_empty returned", res2, 'expected', expected[2], '--', t['reason'])

    if res1 ==  expected[1] and res1 > 0:
        res3 = Queue.peek(the_queue)
        if res3 != expected[3]:
            print("Error: peek returned", res3, 'expected', expected[3], '--', t['reason'])


# test consistency dequeue size, is_empty peek, after a few enqueue
test_integration = [
    {'inputs' : [[7],  # enqueue these
                 1,    # dequeue this many --> check size, isempty, peek
                 [],   # enqueue these
                 0],   # dequeue this many --> check size, isempty, peek
     'outputs': [[7],  # what got dequeued
                 0,    # how many left?
                 True, # is_empty?
                 None, # peek
                 [],   # dequeued
                 0,    # how many left?
                 True, # is_empty?
                 None],# peek
     'reason' : 'one dequeue consistent after one enqueue'},

    {'inputs' : [['a', 'b'], 1, [], 0],
     'outputs': [['a'], 1, False, 'b', [], 1, False, 'b'],
     'reason' : 'one dequeue consistent after two enqueue'},

    {'inputs' : [[1,3,2,4], 2, [], 0],
     'outputs': [[1,3], 2, False, 2, [], 2, False, 2],
     'reason' : 'two dequeue consistent after four enqueue'},

    {'inputs' : [[1,3,2,4], 2, [5,7], 3],
     'outputs': [[1,3], 2, False, 2, [2,4,5], 1, False, 7],
     'reason' : 'some dequeues after multipe enqueues'},

    {'inputs' : [[1,3,2,4], 0, [5,7], 3],
     'outputs': [[], 4, False, 1, [1,3,2], 3, False, 4],
     'reason' : 'some dequeues after multipe enqueues'},

    {'inputs' : [[1,3,2,4], 4, [5,7], 2],
     'outputs': [[1,3,2,4], 0, True, None, [5,7], 0, True, None],
     'reason' : 'some dequeues after multipe enqueues'},

    {'inputs' : [[1,3,2,4], 1, [5,7], 1],
     'outputs': [[1], 3, False, 3, [3], 4, False, 2],
     'reason' : 'some dequeues after multipe enqueues'},
]

for t in test_integration:
    args_in = t['inputs']
    expected = t['outputs']
    the_queue = Queue.create()

    for v in args_in[0]:
        Queue.enqueue(the_queue, v)

    for times in range(args_in[1]):
        res0 = Queue.dequeue(the_queue)
        if res0 != expected[0][times]:
            print("Error: is_empty returned", res0, 'expected', expected[0][times], '--', t['reason'])

    res1 = Queue.size(the_queue)
    if  res1 != expected[1]:
        print("Error: size returned", res1, 'expected', expected[1], '--', t['reason'])

    res2 = Queue.is_empty(the_queue)
    if res2 != expected[2]:
        print("Error: is_empty returned", res2, 'expected', expected[2], '--', t['reason'])

    if res1 ==  expected[1] and res1 > 0:
        res3 = Queue.peek(the_queue)
        if res3 != expected[3]:
            print("Error: peek returned", res3, 'expected', expected[3], '--', t['reason'])


    for v in args_in[2]:
        Queue.enqueue(the_queue, v)

    for times in range(args_in[3]):
        res0 = Queue.dequeue(the_queue)
        if res0 != expected[4][times]:
            print("Error: dequeue returned", res0, 'expected', expected[4][times], '--', t['reason'])

    res1 = Queue.size(the_queue)
    if  res1 != expected[5]:
        print("Error: size returned", res1, 'expected', expected[5], '--', t['reason'])

    res2 = Queue.is_empty(the_queue)
    if res2 != expected[6]:
        print("Error: is_empty returned", res2, 'expected', expected[6], '--', t['reason'])

    if res1 ==  expected[5] and res1 > 0:
        res3 = Queue.peek(the_queue)
        if res3 != expected[7]:
            print("Error: peek returned", res3, 'expected', expected[7], '--', t['reason'])



# that's enough!!
