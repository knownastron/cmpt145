#Name: Jason Tran
#NSID: jat687
#Student Number: 1101081
#Course: CMPT 145-01
#Lab: L03

import exampletrees as exampletrees
import treenode as tn
import a8q1 as a8q1

#####################################################################
# test a8q1.count_node_types
# Unit testing

# Trees for testing
empty_tree = exampletrees.mtree
single_tree = exampletrees.ctree
example_tree = exampletrees.xtree
fibona_tree = exampletrees.fibonatree
expr_tree = exampletrees.expr_tree
only_zeros_tree = tn.create(0,
                    tn.create(0,
                        tn.create(0,
                            tn.create(0),
                            tn.create(0)),
                        tn.create(0,
                            tn.create(0),
                            tn.create(0))),
                    tn.create(0,
                        tn.create(0,
                            tn.create(0),
                            tn.create(0)),
                        tn.create(0,
                            tn.create(0),
                            tn.create(0))))



test_count_node_types = [
    {'inputs' : [empty_tree],
     'outputs': [(0,0)],
     'reason' : 'empty tree'
     },
    {'inputs' : [single_tree],
     'outputs': [(1,0)], #leaf (no children), non-leaf (has children)
     'reason' : 'single tree'
     },
    {'inputs' : [example_tree],
     'outputs': [(4,8)],
     'reason' : 'example tree'
     },
     {'inputs' : [fibona_tree],
     'outputs': [(8,7)],
     'reason' : 'fibonachi tree'
     },
     {'inputs' : [only_zeros_tree],
     'outputs': [(8,7)],
     'reason' : 'Only zeros tree'
     },
     {'inputs' : [expr_tree],
     'outputs': [(7,6)],
     'reason' : 'expr tree'
     }
]

for t in test_count_node_types:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from count_node_types()
    result = a8q1.count_node_types(args_in[0])

    if result != expected[0]:
        print('Error in count_node_types(): expected', expected[0],
            'but returned', result, '--', t['reason'])


#####################################################################
# test a8q1.copy
# Unit testing

# Trees for testing
empty_tree = exampletrees.mtree
single_tree = exampletrees.ctree
example_tree = exampletrees.xtree
fibona_tree = exampletrees.fibonatree
expr_tree = exampletrees.expr_tree
only_zeros_tree = tn.create(0,
                    tn.create(0,
                        tn.create(0,
                            tn.create(0),
                            tn.create(0)),
                        tn.create(0,
                            tn.create(0),
                            tn.create(0))),
                    tn.create(0,
                        tn.create(0,
                            tn.create(0),
                            tn.create(0)),
                        tn.create(0,
                            tn.create(0),
                            tn.create(0))))



test_copy = [
    {'inputs' : [empty_tree],
     'outputs': [],
     'reason' : 'empty tree'
     },
    {'inputs' : [single_tree],
     'outputs': [], #leaf (no children), non-leaf (has children)
     'reason' : 'single tree'
     },
    {'inputs' : [example_tree],
     'outputs': [],
     'reason' : 'example tree'
     },
     {'inputs' : [fibona_tree],
     'outputs': [],
     'reason' : 'fibonachi tree'
     },
     {'inputs' : [only_zeros_tree],
     'outputs': [],
     'reason' : 'Only zeros tree'
     },
     {'inputs' : [expr_tree],
     'outputs': [],
     'reason' : 'expr tree'
     }
]

for t in test_copy:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from copy()
    result = a8q1.copy(args_in[0])

    #test if original and copy are the same
    if result != args_in[0] :
        print('Error in copy(): expected trees to the same different but returned',
                'the same --', t['reason'])

    # change first node on original tree
    # then test if original and copy are different 
    if args_in[0] is None:
        args_in[0] = tn.create(100)

    tn.set_data(args_in[0], 100)


    if result == args_in[0] :
        print('Error in copy(): expected trees to be different but returned',
                'the same --', t['reason'])


print('*** Test script completed ***')
