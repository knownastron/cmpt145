# CMPT 145: Scope Laboratory

# run the test below.  Add more tests.

import scope as scope

test_dups = [
    {'inputs'  : [],
     'outputs' : [],
     'reason'  : 'Empty list'},
    {'inputs'  : [1],
     'outputs' : [],
     'reason'  : 'Singleton list'},
    {'inputs'  : [1,1],
     'outputs' : [1],
     'reason'  : 'Simplest list with duplicate'},
    {'inputs'  : [1,2,3],
     'outputs' : [],
     'reason'  : 'Longer list with no duplicate'},
    {'inputs'  : [4,3,2,1],
     'outputs' : [],
     'reason'  : 'Longer list with no duplicate'},
]

for t in test_dups:
    args_in  = t['inputs']
    expected = t['outputs']

    result = scope.find_duplicates(args_in)
    if result != expected:
        print('Error in find_duplicates: expected', expected,
              'but obtained', result, '--', t['reason'])

print('*** Test script finished ***')
