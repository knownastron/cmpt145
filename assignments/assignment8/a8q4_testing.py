#Name: Jason Tran
#NSID: jat687
#Student Number: 1101081
#Course: CMPT 145-01
#Lab: L03


import treenode as tn
import a8q4 as a8q4

#####################################################################
# test a8q4.ordered

# Trees for testing
empty_tree = None
single_tree = tn.create(1776)
xtree = tn.create(5,
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

ordered_tree = tn.create(100,
                    tn.create(50,
                        tn.create(-20,
                            tn.create(-100),
                            tn.create(0)),
                        tn.create(80,
                            tn.create(70),
                            tn.create(95))),
                    tn.create(150,
                        tn.create(110,
                            tn.create(101),
                            tn.create(123)),
                        tn.create(1000,
                            tn.create(800),
                            tn.create(1500))))






test_ordered = [
    {'inputs' : [empty_tree],
     'outputs': [True],
     'reason' : 'empty tree'
     },
    {'inputs' : [single_tree],
     'outputs': [True],
     'reason' : 'single tree'
     },
    {'inputs' : [xtree],
     'outputs': [False],
     'reason' : 'example tree'
     },
     {'inputs' : [fibona_tree],
     'outputs': [False],
     'reason' : 'fibonachi tree'
     },
     {'inputs' : [only_zeros_tree],
     'outputs': [False],
     'reason' : 'Only zeros tree'
     },
    {'inputs': [ordered_tree],
     'outputs': [True],
     'reason': 'Ordered tree'
     },
]

for t in test_ordered:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from ordered()
    result = a8q4.ordered(args_in[0])


    if result != expected[0]:
        print('Error in ordered(): expected', expected[0],
                'but returned,', result, '--', t['reason'])


print('*** Test script completed ***')
