# CMPT 145: Assignment 5 Question 2
# test script


import a5q1 as a5q1
import a5q2 as a5q2
import node as node

test_count_chain = [
    {'inputs' : None,
     'outputs': 0,
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': 1,
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': 2,
     'reason' : 'node chain with two nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': 3,
     'reason' : 'node chain with three nodes'},
]

for t in test_count_chain:
    args_in = t['inputs']
    expected = t['outputs']
    result = a5q2.count_chain(args_in)
    assert result == expected, 'count_chain(): got '\
        +str(result)+' expected '+str(expected)+' -- ' +t['reason']




test_delete_front_nodes = [
    {'inputs' : [None, 0],  # Inputs are node_chain, and number of nodes to delete
     'outputs': 'EMPTY',
     'reason' : 'Empty node chain, nothing to remove'},

    {'inputs' : [node.create(1), 1],
     'outputs': 'EMPTY',
     'reason' : 'Node chain with single nodes to remove '},

    {'inputs' : [node.create(1, node.create('two')), 1],
     'outputs': '[ two | / ]',
     'reason' : 'Node chain with multiple nodes, front should be removed'},

    {'inputs' : [node.create(1, node.create('two', node.create(3))), 2],
     'outputs': '[ 3 | / ]',
     'reason' : 'node chain with multiple nodes, all but one should be removed'},

    {'inputs': [node.create(1, node.create('two', node.create(3))), 6],
     'outputs': 'EMPTY',
     'reason': 'node chain with multiple nodes, remove all of them'},
]

for t in test_delete_front_nodes:
    args_in = t['inputs']
    expected = t['outputs']
    altered_chain = a5q2.delete_front_nodes(args_in[0], args_in[1])
    # Use count_chain to see how many nodes should be remaining
    result = a5q1.to_string(altered_chain)
    assert (result == result), \
        'delete_front_nodes(): got "'+result+'" expected "'+expected+'" -- '+t['reason']



test_replace_last = [
    {'inputs' : [None, 1, 1],
     'outputs': "EMPTY",
     'reason' : 'Empty node chain'},

    {'inputs' : [node.create(1), 1, 2],
     'outputs': "[ 2 | / ]",
     'reason' : 'node chain with one node, target in'},

    {'inputs' : [node.create(1), 5, 2],
     'outputs': "[ 1 | / ]",
     'reason' : 'node chain with one node, target not in'},

    {'inputs' : [node.create(1, node.create('two')),
                 1, 'one'],
     'outputs': "[ one | *-]-->[ two | / ]",
     'reason' : 'node chain with two nodes, target first'},

    {'inputs' : [node.create(1, node.create('two')),
                 5, 'five'],
     'outputs': "[ 1 | *-]-->[ two | / ]",
     'reason' : 'node chain with two nodes, target not in'},
    {'inputs' : [node.create(1, node.create('two')),
                 'two', 2],
     'outputs': "[ 1 | *-]-->[ 2 | / ]",
     'reason' : 'node chain with two nodes, target last'},

    {'inputs' : [node.create(1, node.create('two', node.create('two'))),
                 'two', 3],
     'outputs': "[ 1 | *-]-->[ two | *-]-->[ 3 | / ]",
     'reason' : 'node chain with multiple copies of value, target last'},
]

for t in test_replace_last:
    args_in = t['inputs']
    expected = t['outputs']
    a5q2.replace_last(args_in[0], args_in[1], args_in[2])
    result = a5q1.to_string(args_in[0])
    assert result == expected, \
        'replace(): got "'+result+'" expected "'+expected+'" -- '+t['reason']

print('*** testing complete ***')
