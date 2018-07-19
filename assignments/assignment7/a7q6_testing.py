#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import node as node
import a7q6 as a7q6
#####################################################################
# Nodes for testing

empty_node = None
single_node = node.create(1)
several_node = node.create(0)

for i in range(1,5):
    several_node = node.create(i, several_node)


#####################################################################
# test a7q6.average()
# Unit testing



test_average = [
    {'inputs' : [empty_node],
     'outputs': [0],
     'reason' : 'empty node'
     },
    {'inputs' : [single_node],
     'outputs': [1],
     'reason' : 'single node'
     },
    {'inputs' : [several_node],
     'outputs': [2],
     'reason' : 'several node'
     },

]

for t in test_average:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from average()
    result = a7q6.average(args_in[0])

    if result != expected[0]:
        print('Error in average(): expected', expected[0],
            'but returned', result, '--', t['reason'])


#####################################################################
# test a7q6.reverse_chain()
# Unit testing



test_reverse = [
    {'inputs' : [empty_node],
     'outputs': [None],
     'reason' : 'empty node'
     },
    {'inputs' : [single_node],
     'outputs': [1],
     'reason' : 'single node'
     },
    {'inputs' : [several_node],
     'outputs': [0,1,2,3,4],
     'reason' : 'several node'
     },

]

for t in test_reverse:
    args_in = t['inputs']
    expected = t['outputs']

    #get the data from the node in order and append to list
    result = []
    anode = a7q6.reverse_chain(args_in[0])
    while anode is not None:
        result.append(node.get_data(anode))
        anode = node.get_next(anode)

    #corner case if the result is empty due to an empty chain
    if result == []:
        if expected[0] != None:
            print('Error in average(): expected', expected[0],
                'but returned', result, '--', t['reason'])
    elif result != expected:
        print('Error in average(): expected', expected[0],
            'but returned', result, '--', t['reason'])

#####################################################################
# test a7q6.copy()
# Unit testing



test_copy = [
    {'inputs' : [empty_node],
     'outputs': [0],
     'reason' : 'empty node'
     },
    {'inputs' : [single_node],
     'outputs': [1],
     'reason' : 'single node'
     },
    {'inputs' : [several_node],
     'outputs': [2],
     'reason' : 'several node'
     },

]

for t in test_copy:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from average()
    result = a7q6.average(args_in[0])

    if result != expected[0]:
        print('Error in average(): expected', expected[0],
            'but returned', result, '--', t['reason'])


print('*** Test script completed ***')
