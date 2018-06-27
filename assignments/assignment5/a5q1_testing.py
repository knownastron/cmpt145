# CMPT 145: Assignment 5 Question 1
# test script

import a5q1 as a5q1
import node as node

test_to_string = [
    {'inputs' : None,
     'outputs': 'EMPTY',
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': '[ 1 | / ]',
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': '[ 1 | *-]-->[ two | / ]',
     'reason' : 'node chain with two nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': '[ 1 | *-]-->[ two | *-]-->[ 3 | / ]',
     'reason' : 'node chain with three nodes'},
]

for t in test_to_string:
    args_in = t['inputs']
    expected = t['outputs']
    result = a5q1.to_string(args_in)
    assert result == expected, \
        'to_string(): got "'+str(result)+'" expected "'+str(expected)+'" -- ' +t['reason']

print('*** testing complete ***')
