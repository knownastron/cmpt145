# File: magic_testing.py
# Author: CMPT 145
# Version: 1.0

# NOTE
# To run this test script, it might be better to comment out the
# main script of a1q1.

import a1q1 as magic


##########################################################
test_get_square = [ {'inputs' : [],
                     'outputs': 3,
                     'reason' : ' minimal testing for I/O'}
                  ]

# testing loop
for test in test_get_square:
    result = magic.get_square()
    if len(result) != test['outputs']:
        print ('Testing fault: get_square returned list of length', result, '('+str(test['reason'])+')')
    if len(result[0]) != test['outputs']:
        print ('Testing fault: get_square returned list of length', result, '('+str(test['reason'])+')')


##########################################################
test_check_diagonals = [
	    {'inputs' : [[1,2,3],[4,5,6],[7,8,9]],
             'outputs': True,
             'reason' : 'both diagonals sum to 15'}
	  , {'inputs' : [[1,1,1],[1,5,1],[1,1,9]],
             'outputs': False,
             'reason' : 'only down diagonal sums to 15'}
	  , {'inputs' : [[1,1,1],[1,5,1],[9,1,1]],
             'outputs': False,
             'reason' : 'only up diagonal sums to 15'}
	  , {'inputs' : [[1,1,1],[1,1,1],[1,1,1]],
             'outputs': False,
             'reason' : 'no diagonal sums to 15'}
          ]

# testing loop
for test in test_check_diagonals:
    inputs = test['inputs']
    result = magic.check_diagonals(inputs)
    if result != test['outputs']:
        print ('Testing fault: check_diagonals returned', result,
		'on input', test['inputs'], '('+str(test['reason'])+')')

##########################################################
test_check_rows = [
	    {'inputs' : [[1,2,3],[4,5,6],[7,8,9]],
             'outputs': False,
             'reason' : 'only middle row sums to 15'}
	  , {'inputs' : [[1,1,1],[1,1,1],[1,1,9]],
             'outputs': False,
             'reason' : 'no rows sum to 15'}
	  , {'inputs' : [[5,5,5],[1,5,1],[9,1,1]],
             'outputs': False,
             'reason' : 'only first row sums to 15'}
	  , {'inputs' : [[1,1,1],[1,1,1],[5,5,5]],
             'outputs': False,
             'reason' : 'only last row sums to 15'}
	  , {'inputs' : [[5,5,5],[5,5,5],[5,5,5]],
             'outputs': True,
             'reason' : 'all rows sum to 15'}
          ]

# testing loop
for test in test_check_rows:
    inputs = test['inputs']
    result = magic.check_rows(inputs)
    if result != test['outputs']:
        print ('Testing fault: check_rows returned', result,
		'on input', test['inputs'], '('+str(test['reason'])+')')


##########################################################
test_check_columns = [
	    {'inputs' : [[1,2,3],[4,5,6],[7,8,9]],
             'outputs': False,
             'reason' : 'only middle column sums to 15'}
	  , {'inputs' : [[1,1,1],[1,1,1],[1,1,9]],
             'outputs': False,
             'reason' : 'no columns sum to 15'}
	  , {'inputs' : [[5,5,5],[1,5,1],[9,1,1]],
             'outputs': False,
             'reason' : 'only first column sums to 15'}
	  , {'inputs' : [[1,1,5],[1,1,5],[5,5,5]],
             'outputs': False,
             'reason' : 'only last row sums to 15'}
	  , {'inputs' : [[5,5,5],[5,5,5],[5,5,5]],
             'outputs': True,
             'reason' : 'all rows sum to 15'}
          ]

# testing loop
for test in test_check_columns:
    inputs = test['inputs']
    result = magic.check_columns(inputs)
    if result != test['outputs']:
        print ('Testing fault: check_columns returned', result,
		'on input', test['inputs'], '('+str(test['reason'])+')')



##########################################################
test_check_range = [
	    {'inputs' : [[1,2,3],[4,5,6],[7,8,9]],
             'outputs': True,
             'reason' : 'all 1 .. 9 are here'}
	  , {'inputs' : [[1,1,1],[1,1,1],[1,1,1]],
             'outputs': False,
             'reason' : 'only one number appears'}
	  , {'inputs' : [[1,2,3],[4,5,6],[7,8,0]],
             'outputs': False,
             'reason' : 'one number out of range'}
	  , {'inputs' : [[1,2,3],[4,5,6],[7,8,1]],
             'outputs': False,
             'reason' : 'one number repeated'}
          ]

# testing loop
for test in test_check_range:
    inputs = test['inputs']
    result = magic.check_range(inputs)
    if result != test['outputs']:
        print ('Testing fault: check_range returned', result,
		'on input', test['inputs'], '('+str(test['reason'])+')')

##########################################################
test_check_square = [
	    {'inputs' : [[1,2,3],[4,5,6],[7,8,9]],
             'outputs': False,
             'reason' : 'all the numbers, but not magic.'}
	  , {'inputs' : [[1,1,1],[1,1,1],[1,1,1]],
             'outputs': False,
             'reason' : 'not all the numbers'}
	  , {'inputs' : [[8,1,6],[3,5,7],[4,9,2]],
             'outputs': True,
             'reason' : 'Magic!'}
          ]

# testing loop
for test in test_check_square:
    inputs = test['inputs']
    result = magic.check_square(inputs)
    if result != test['outputs']:
        print ('Testing fault: check_square returned', result,
		'on input', test['inputs'], '('+str(test['reason'])+')')

