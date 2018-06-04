# CMPT 145: Chapter 07
# Testing

# This script tests the Registry ADT

import Registry as Reg

# UNIT TESTING
# testing Reg.create()
# in ADT testing you can look inside the ADT!

# These test cases for create are [size, initial]
#   - size: the sizer of the Registry to create()
#   - initial: the initial value to use in create()

test_create = [
    {'inputs' : [1, True],
     'outputs':[1, True],
     'reason' : 'Smallest example, all True'},
]


for t in test_create:
    # grab information from the test
    args_in  = t['inputs']
    expected = t['outputs']

    # call the operation
    thing = Reg.create(args_in[0], args_in[1])

    # we know a Registry is just a list, so we can test things about that list
    if len(thing) != expected[0]:
        print('Error in create(): expected registry of size', expected[0],
              ' but found length ', len(thing), '--', t['reason'])

    # check all the elements are initialized correctly
    for i in range(len(thing)):
        if thing[i] != expected[1]:
            print('Error in create(): expected value', expected[1], 'at index ', i,
                  ' but found ', thing[i], '--', t['reason'])



# These test cases for set are [size, initial, index]
#   - size: the sizer of the Registry to create()
#   - initial: the initial value to use in create()
#   - the index to set() and check

test_set = [
    {'inputs': [123, True, 0],
     'outputs':[True],
     'reason': 'Check first index in registry initially True'},
]

for t in test_set:
    # grab information from the test
    args_in = t['inputs']
    index = args_in[2]
    expected = t['outputs']

    # create a registry to test
    thing = Reg.create(args_in[0], args_in[1])

    # check the operation
    Reg.set(thing, index)
    if thing[index] != expected[0]:
        print('Error in set(): expected value', expected[0], 'at index ', index,
              ' but found ', thing[index], '--', t['reason'])


# These test cases for reset are [size, initial, index]
#   - size: the sizer of the Registry to create()
#   - initial: the initial value to use in create()
#   - the index to set() and check

test_reset = [
    {'inputs': [123, True, 0],
     'outputs':[False],
     'reason': 'Check first index in registry initially True'},
]

for t in test_reset:
    # grab information from the test
    args_in = t['inputs']
    index = args_in[2]
    expected = t['outputs']

    # create a registry to test
    thing = Reg.create(args_in[0], args_in[1])

    # use the operation
    Reg.reset(thing, index)

    # check first that the value at index is as expected
    if thing[index] != expected[0]:
        print('Error in reset(): expected value', expected[0], 'at index ', index,
              ' but found ', thing[index], '--', t['reason'])

    # now check that nothing else changed!
    for i in range(args_in[0]):
        if i != index and thing[i] != args_in[1]:
            print('Error in reset(): expected initial value', args_in[1], 'at index ', i,
                  ' but found ', thing[i], '--', t['reason'])


# These test cases for isregistered are [size, initial, index, value]
#   - size: the sizer of the Registry to create()
#   - initial: the initial value to use in create()
#   - the index to set and check
#   - the value to put in the registery at index

test_isregistered = [
    {'inputs': [123, True, 0, True],
     'outputs':[True],
     'reason': 'Check first index in registry initially True'},
]


for t in test_isregistered:
    # grab information from the test
    args_in = t['inputs']
    index = args_in[2]
    expected = t['outputs']

    # create a registry to test
    thing = Reg.create(args_in[0], args_in[1])

    # manually set the value at the specified index
    thing[index] = args_in[3]

    # call the operation
    result = Reg.is_registered(thing, index)

    # check first that the value at index is as expected
    if result != expected[0]:
        print('Error in is_registered(): expected value', expected[0], 'at index ',
              index, ' but found ', result, '--', t['reason'])

    # now check that nothing else changed!
    for i in range(args_in[0]):
        if i != index and thing[i] != args_in[1]:
            print('Error in is_registered(): expected initial value', args_in[1], 'at index ', i,
                  ' but found ', thing[i], '--', t['reason'])




# INTEGRATION TESTING

# These test cases use [size, initial, index]
#   - size: the sizer of the Registry to create()
#   - initial: the initial value to use in create()
#   - the index to set and check
#
#  Here we don't look inside the ADT, and just use the operations
# in a coordinated manner.

test_integration = [
    {'inputs': [123, True, 0],
     'outputs': None,
     'reason': 'Check first index in registry initially True'},

]

for t in test_integration:
    # grab information from the test
    args_in = t['inputs']
    index = args_in[2]

    # create a registry
    reg = Reg.create(args_in[0], args_in[1])

    # check the initial value
    check = Reg.is_registered(reg, index)
    if check != True:
        print('Error after set(), is_registered(): expected value', True, 'at index ', index,
              ' but found ', check, '--', t['reason'])

    # use operation set()
    Reg.set(reg, index)

    check = Reg.is_registered(reg, index)
    if check != True:
        print('Error after set(), is_registered(): expected value', True, 'at index ', index,
              ' but found ', check, '--', t['reason'])

    # use the operation reset()
    Reg.reset(reg, index)

    check = Reg.is_registered(reg, index)
    if check != False:
        print('Error after set(), is_registered(): expected value', False, 'at index ', index,
              ' but found ', check, '--', t['reason'])

