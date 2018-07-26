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
empty_tree = None
single_tree = tn.create(1776)
example_tree = tn.create(5,
              tn.create(1,None,
                        tn.create(4,
                                  tn.create(3,tn.create(2,None,None),None),
                                  None)),
              tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                          tn.create(1,tn.create(3,None,None),tn.create(3,None,None))))
fibona_tree = tn.create(5,tn.create(2,tn.create(1,None,None),
                                     tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None))),
                         tn.create(3,tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None)),
                                     tn.create(2,tn.create(1,None,None),
                                                 tn.create(1,tn.create(0,None,None),
                                                             tn.create(1,None,None)))))
expr_tree = tn.create('*',
                  tn.create('+',
                            tn.create('+',
                                      tn.create(2.0, None, None),
                                      tn.create(3.0, None, None)),
                            tn.create(3.0, None, None)),
                  tn.create('+',
                            tn.create(4.0, None, None),
                            tn.create('/',
                                      tn.create(2.0, None, None),
                                      tn.create('+',
                                                tn.create(89.0, None, None),
                                                tn.create(3.0, None, None)))))
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
empty_tree = None
single_tree = tn.create(1776)
example_tree = tn.create(5,
              tn.create(1,None,
                        tn.create(4,
                                  tn.create(3,tn.create(2,None,None),None),
                                  None)),
              tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                          tn.create(1,tn.create(3,None,None),tn.create(3,None,None))))
fibona_tree = tn.create(5,tn.create(2,tn.create(1,None,None),
                                     tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None))),
                         tn.create(3,tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None)),
                                     tn.create(2,tn.create(1,None,None),
                                                 tn.create(1,tn.create(0,None,None),
                                                             tn.create(1,None,None)))))
expr_tree = tn.create('*',
                  tn.create('+',
                            tn.create('+',
                                      tn.create(2.0, None, None),
                                      tn.create(3.0, None, None)),
                            tn.create(3.0, None, None)),
                  tn.create('+',
                            tn.create(4.0, None, None),
                            tn.create('/',
                                      tn.create(2.0, None, None),
                                      tn.create('+',
                                                tn.create(89.0, None, None),
                                                tn.create(3.0, None, None)))))
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
     'outputs': [],
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

    #test if original and copy are the same value
    if result != args_in[0] :
        print('Error in copy(): expected trees to the same value but returned',
                'the different values --', t['reason'])

    # change first node on original tree
    # then test if original and copy are different
    if args_in[0] is None:
        args_in[0] = tn.create(100)

    tn.set_data(args_in[0], 100)


    if result == args_in[0] :
        print('Error in copy(): expected trees to be different but returned',
                'the same --', t['reason'])

#####################################################################
# test a8q1.collect_data_inorder
# Unit testing

# Trees for testing
empty_tree = None
single_tree = tn.create(1776)
example_tree = tn.create(5,
              tn.create(1,None,
                        tn.create(4,
                                  tn.create(3,tn.create(2,None,None),None),
                                  None)),
              tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                          tn.create(1,tn.create(3,None,None),tn.create(3,None,None))))
fibona_tree = tn.create(5,tn.create(2,tn.create(1,None,None),
                                     tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None))),
                         tn.create(3,tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None)),
                                     tn.create(2,tn.create(1,None,None),
                                                 tn.create(1,tn.create(0,None,None),
                                                             tn.create(1,None,None)))))
expr_tree = tn.create('*',
                  tn.create('+',
                            tn.create('+',
                                      tn.create(2.0, None, None),
                                      tn.create(3.0, None, None)),
                            tn.create(3.0, None, None)),
                  tn.create('+',
                            tn.create(4.0, None, None),
                            tn.create('/',
                                      tn.create(2.0, None, None),
                                      tn.create('+',
                                                tn.create(89.0, None, None),
                                                tn.create(3.0, None, None)))))
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




test_collect_data_inorder = [
    {'inputs' : [empty_tree],
     'outputs': [[]],
     'reason' : 'empty tree'
     },
    {'inputs' : [single_tree],
     'outputs': [[1776]],
     'reason' : 'single tree'
     },
    {'inputs' : [example_tree],
     'outputs': [[1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 1, 3]],
     'reason' : 'example tree'
     },
     {'inputs' : [fibona_tree],
     'outputs': [[1, 2, 0, 1, 1, 5, 0, 1 ,1, 3, 1 ,2 ,0 , 1, 1]],
     'reason' : 'fibonachi tree'
     },
     {'inputs' : [only_zeros_tree],
     'outputs': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
     'reason' : 'Only zeros tree'
     },
     {'inputs' : [expr_tree],
     'outputs': [[2.0, '+', 3.0, '+', 3.0, '*', 4.0, '+', 2.0, '/', 89.0, '+', 3.0]],
     'reason' : 'expr tree'
     }
]

for t in test_collect_data_inorder:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from collect_data_inorder()
    result = a8q1.collect_data_inorder(args_in[0])


    if result != expected[0]:
        print('Error in collect_data_inorder(): expected', expected[0],
                'but returned,', result, '--', t['reason'])

#####################################################################
# test a8q1.alter_subtrees
# Unit testing

# Trees for testing
empty_tree = None
single_tree = tn.create(1776)
example_tree = tn.create(5,
              tn.create(1,None,
                        tn.create(4,
                                  tn.create(3,tn.create(2,None,None),None),
                                  None)),
              tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                          tn.create(1,tn.create(3,None,None),tn.create(3,None,None))))
fibona_tree = tn.create(5,tn.create(2,tn.create(1,None,None),
                                     tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None))),
                         tn.create(3,tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None)),
                                     tn.create(2,tn.create(1,None,None),
                                                 tn.create(1,tn.create(0,None,None),
                                                             tn.create(1,None,None)))))
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




test_alter_subtrees = [
    {'inputs' : [empty_tree],
     'outputs': [[]],
     'reason' : 'empty tree'
     },
    {'inputs' : [single_tree],
     'outputs': [[1776]],
     'reason' : 'single tree'
     },
    {'inputs' : [example_tree],
     'outputs': [[1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 1, 3]],
     'reason' : 'example tree'
     },
     {'inputs' : [fibona_tree],
     'outputs': [[1, 2, 0, 1, 1, 5, 0, 1 ,1, 3, 1 ,2 ,0 , 1, 1]],
     'reason' : 'fibonachi tree'
     },
     {'inputs' : [only_zeros_tree],
     'outputs': [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
     'reason' : 'Only zeros tree'
     },
]

for t in test_alter_subtrees:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from alter_subtrees()
    result = a8q1.alter_subtrees(args_in[0])


    if result != expected[0]:
        print('Error in alter_subtrees(): expected', expected[0],
                'but returned,', result, '--', t['reason'])

print('*** Test script completed ***')
