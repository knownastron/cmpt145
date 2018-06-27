# CMPT 145: Assignment 5 Question 3
# test script

import a5q1 as a5q1
import a5q3 as a5q3
import node as node


test_contains_duplicates = [
    {'inputs' : None,
     'outputs': False,
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': False,
     'reason' : 'node chain with one node'},

    {'inputs' : node.create('two', node.create('two')),
     'outputs': True,
     'reason' : 'node chain with two nodes that are duplicates'},

    {'inputs' : node.create(1, node.create('two', node.create(1))),
     'outputs': True,
     'reason' : 'node chain with three nodes, duplicates are separated'},

    {'inputs' : node.create(1, node.create('two', node.create(3,node.create('four')))),
     'outputs': False,
     'reason' : 'node chain with four nodes, no duplicates'}
]


for t in test_contains_duplicates:
    args_in = t['inputs']
    expected = t['outputs']
    result = a5q3.contains_duplicates(args_in)
    assert result == expected, \
        'contains_duplicates(): got '\
        +str(result)+' expecting '+str(expected)+' -- ' +t['reason']
print('Done test_contains_duplicates')

test_reverse_chain = [
    {'inputs' : None,
     'outputs': "EMPTY",
     'reason' : 'Empty node chain, nothing to reverse'},

    {'inputs' : node.create(1),
     'outputs': "[ 1 | / ]",
     'reason' : 'node chain with one node, nothing to reverse'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': "[ two | *-]-->[ 1 | / ]",
     'reason' : 'node chain with two nodes, should be reversed'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': "[ 3 | *-]-->[ two | *-]-->[ 1 | / ]",
     'reason' : 'node chain with three nodes, should be reversed'},

    {'inputs' : node.create(1, node.create('two', node.create(3, node.create('four')))),
     'outputs': "[ four | *-]-->[ 3 | *-]-->[ two | *-]-->[ 1 | / ]",
     'reason' : 'node chain with four nodes, should be reversed'}
]

for t in test_reverse_chain:
    args_in = t['inputs']
    expected = t['outputs']
    result = a5q3.reverse_chain(args_in)

    str_result = a5q1.to_string(result)
    assert str_result == expected, 'reverse_chain(): got "'\
        +str_result+'" expected "'+expected+'" -- ' +t['reason']
print('Done reverse_chain')


test_insert_value_sorted = [

    {'inputs' :  [None, 1],
     'outputs': "[ 1 | / ]",
     'reason' : 'empty node chain, insert 1'},

    {'inputs' :  [node.create(2), 1],
     'outputs': "[ 1 | *-]-->[ 2 | / ]",
     'reason' : 'node chain with one node, insert at front'},

    {'inputs' :  [node.create(0), 1],
     'outputs': "[ 0 | *-]-->[ 1 | / ]",
     'reason' : 'node chain with one node, insert at back'},

    {'inputs' :  [node.create(2, node.create(3)), 1],
     'outputs': "[ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]",
     'reason' : 'node chain with two nodes, insert at front'},

    {'inputs' :  [node.create(-1, node.create(0)), 1],
     'outputs': "[ -1 | *-]-->[ 0 | *-]-->[ 1 | / ]",
     'reason' : 'node chain with two nodes, insert at back'},

    {'inputs' :  [node.create(0, node.create(2)), 1],
     'outputs': "[ 0 | *-]-->[ 1 | *-]-->[ 2 | / ]",
     'reason' : 'node chain with two nodes, insert at mid'},

    {'inputs' :  [node.create(1, node.create(2, node.create(3, node.create(4)))), 3],
     'outputs': "[ 1 | *-]-->[ 2 | *-]-->[ 3 | *-]-->[ 3 | *-]-->[ 4 | / ]",
     'reason' : 'node chain with 4 nodes, insert at mid'},

    {'inputs' :  [node.create(1, node.create(2, node.create(3, node.create(4)))), 5],
     'outputs': "[ 1 | *-]-->[ 2 | *-]-->[ 3 | *-]-->[ 4 | *-]-->[ 5 | / ]",
     'reason' : 'node chain with 4 nodes, insert at back'},

]

for t in test_insert_value_sorted:
    args_in = t['inputs']
    expected = t['outputs']
    result = a5q3.insert_value_sorted(args_in[0], args_in[1])

    str_result = a5q1.to_string(result)
    assert str_result == expected, 'insert_value_sorted(): got "'\
        +str_result+'" expected "'+expected+'" -- ' +t['reason']


print('*** testing complete ***')
