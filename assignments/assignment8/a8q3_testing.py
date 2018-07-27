#Name: Jason Tran
#NSID: jat687
#Student Number: 1101081
#Course: CMPT 145-01
#Lab: L03


import treenode as tn
import a8q3 as a8q3

#####################################################################
# test a8q3.cmplt

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




test_cmplt = [
    {'inputs' : [empty_tree],
     'outputs': [True],
     'reason' : 'empty tree'
     },
    {'inputs' : [single_tree],
     'outputs': [True],
     'reason' : 'single tree'
     },
    {'inputs' : [example_tree],
     'outputs': [False],
     'reason' : 'example tree'
     },
     {'inputs' : [fibona_tree],
     'outputs': [False],
     'reason' : 'fibonachi tree'
     },
     {'inputs' : [only_zeros_tree],
     'outputs': [True],
     'reason' : 'Only zeros tree'
     },
    {'inputs': [expr_tree],
     'outputs': [True],
     'reason': 'expr_tree from example trees'
     },
]

for t in test_cmplt:
    args_in = t['inputs']
    expected = t['outputs']

    #get result from cmplt()
    result = a8q3.cmplt(args_in[0])


    if result != expected[0]:
        print('Error in cmplt(): expected', expected[0],
                'but returned,', result, '--', t['reason'])


print('*** Test script completed ***')
