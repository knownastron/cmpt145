#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import a2q1


#UNIT TESTING
########################################################################################################################

#testing a2q1.get_confession()


test_get_confession = [
    {
        #ensure the file confession.txt is in the directory!
        'inputs': ['confession.txt'],
        'outputs': ['M', 'B', 'R'],
        'reason': 'Testing that function output grid matches expected letters - beginning, middle, end'
    },
]

for t in test_get_confession:
    args_in = t['inputs']
    expected = t['outputs']
    reason = t['reason']

    result = a2q1.get_confession(args_in[0])

    #check if first element, last element and middle element are the same as expected
    if (result[0][0] != expected[0]):
        print('Error: First letter of get_confession(), result', result[0][0],
              'does not match expected', expected[0])
    elif (result[6][6] != expected[1]):
        print('Error: Middle letter of get_confession(), result', result[6][6],
              'does not match expected', expected[1])
    elif (result[14][14] != expected[2]):
        print('Error: Last letter of get_confession(), result', result[14][14],
              'does not match expected', expected[2])



#testing a2q1.find_word()


#Set up 15x15 lists of lists for testing:
confession1 = [
['M', 'L', 'G', 'Y', 'J', 'U', 'G', 'D', 'T', 'W', 'W', 'I', 'S', 'F', 'P'],
['G', 'Y', 'O', 'H', 'I', 'K', 'O', 'P', 'V', 'F', 'J', 'B', 'J', 'J', 'H'],
['N', 'B', 'I', 'M', 'T', 'M', 'Y', 'W', 'R', 'D', 'J', 'E', 'C', 'A', 'I'],
['I', 'Y', 'M', 'X', 'C', 'U', 'E', 'U', 'Z', 'G', 'U', 'I', 'J', 'Y', 'C'],
['K', 'D', 'P', 'S', 'L', 'R', 'W', 'J', 'I', 'N', 'C', 'N', 'S', 'W', 'T'],
['O', 'P', 'S', 'D', 'I', 'D', 'A', 'B', 'Z', 'I', 'D', 'G', 'D', 'A', 'B'],
['M', 'X', 'D', 'H', 'K', 'E', 'B', 'H', 'U', 'G', 'T', 'S', 'I', 'L', 'G'],
['S', 'G', 'D', 'U', 'Y', 'R', 'V', 'D', 'G', 'N', 'D', 'M', 'L', 'K', 'M'],
['S', 'P', 'X', 'K', 'T', 'W', 'E', 'F', 'P', 'I', 'G', 'E', 'J', 'I', 'T'],
['B', 'U', 'L', 'B', 'C', 'M', 'K', 'I', 'F', 'S', 'I', 'L', 'F', 'N', 'W'],
['Z', 'Q', 'L', 'X', 'H', 'G', 'C', 'J', 'N', 'D', 'I', 'L', 'B', 'G', 'C'],
['M', 'T', 'B', 'W', 'Z', 'L', 'A', 'D', 'A', 'A', 'X', 'Y', 'O', 'K', 'X'],
['A', 'E', 'C', 'Z', 'K', 'F', 'Y', 'V', 'F', 'B', 'U', 'V', 'G', 'A', 'W'],
['Y', 'G', 'O', 'Z', 'E', 'A', 'W', 'J', 'R', 'N', 'S', 'Q', 'J', 'E', 'A'],
['L', 'O', 'I', 'T', 'E', 'R', 'I', 'N', 'G', 'H', 'F', 'I', 'P', 'G', 'R']
]


test_find_word = [
    {
        'inputs': ["OPVF", "LADAAX"],
        'outputs': True,
        'reason': 'Testing strings that appear horizontally going forward (right) - All True'
     },
    {
        'inputs': ['GUJY', 'HBEKH'],
        'outputs': True,
        'reason': 'Testing strings that appear horizontally going backward (left) - All True'
     },
    {
        'inputs': ['EYOG', 'DCUJJW'],
        'outputs': True,
        'reason': "Testing strings that appear vertically going backward (up) - All True"
     },
    {
         'inputs': ['MXSDH', 'RZIZUGP'],
         'outputs': True,
         'reason': "Testing strings that appear vertically going forward (down) - All True"
     },
    {
        'inputs': ['HANDKERCHIEF', 'ABNEGATION'],
        'outputs': False,
        'reason': "Strings that do not appear in the confession - All False"
    }
]


#test confession1
for t in test_find_word:
    args_in = t['inputs']
    expected = t['outputs']


    for arg in args_in:
        result = a2q1.find_word(confession1, arg)
        if result != expected:
            print('Error: Returned', result, 'on input', arg, t['reason'])





#INTEGRATION TESTING
########################################################################################################################


#testing get_confession() and find_word() together

test_get_confession_and_find_word = [
    {
        #ensure file confession.txt is in the directory!
        'inputs': ['confession.txt', 'WEFP'],
        'outputs': True,
        'reason': 'String is in confession.txt - True'
    },
    {
        #ensure file confession.txt is in the directory!
        'inputs': ['confession.txt', 'DJOISDJFO'],
        'outputs': False,
        'reason': 'String is not in confession.txt - False'
    }
]

for t in test_get_confession_and_find_word:
    args_in = t['inputs']
    expected = t['outputs']
    reason = t['reason']

    grid = a2q1.get_confession(args_in[0])
    guilty = a2q1.find_word(grid, args_in[1])

    if guilty != expected:
        print('Error: get_confession and find_word. Expected', expected, 'but got result', guilty, '--', reason)


#VERIFICATION
#######################################################################################################################

# assignment2 $ python3.6 a2q1.py confession.txt JAYWALKING
# Gentleman GoGo IS GUILTY OF JAYWALKING

# assignment2 $ python3.6 a2q1.py confession.txt BURGLARY
# BURGLARY was NOT found

# assignment2 $ python3.6 a2q1.py confession.txt LAUNDERING
# LAUNDERING was NOT found

# assignment2 $ python3.6 a2q1.py confession.txt BADSINGING
# Gentleman GoGo IS GUILTY OF BADSINGING

# assignment2 $ python3.6 a2q1.py confession.txt REDRUM
# Gentleman GoGo IS GUILTY OF REDRUM

# assignment2 $ python3.6 a2q1.py confession.txt SMOKING
# Gentleman GoGo IS GUILTY OF SMOKING

# assignment2 $ python3.6 a2q1.py confession.txt BEINGSMELLY
# Gentleman GoGo IS GUILTY OF BEINGSMELLY

# assignment2 $ python3.6 a2q1.py confession.txt CONNING
# CONNING was NOT found

# assignment2 $ python3.6 a2q1.py confession.txt SCAMS
# SCAMS was NOT found

# assignment2 $ python3.6 a2q1.py confession.txt LOITERING
# Gentleman GoGo IS GUILTY OF LOITERING
