# CMPT 145: Node-Based Data Structures
#   Linked List ADT scoring script
#
#   The script runs two kinds of tests:
#      - unit tests: test one function at a time
#      - integration tests: test how functions work together
#   The script counts the number of tests attempted and passed.

import LList as List


###############################################################################################
# A little tool to help with the reporting of errors and counting, etc.
# It's an ADT defined within this file, with the following operations:
#   - createCounter(reason, lim)
#     create a counter data structure labelled with a reason (string) and an error limit (lim)
#   - expecting(counter, flag, errstring)
#     counts and reports, based on the outcome of a test (flag)
#   - set_limit(counter, lim)
#     cause the counter to stop the script after a given number of errors (lim)
#   - final_report(counter)
#     displays the final results

def createCounter(reason, lim=0):
    """
    Create a counter to counter tests.  The counter will
    collect statistics based on calls to function expecting().
    :param reason: a string to describe what's being tested.
    :param lim: how many errors to detect before halting the tests
    :return: None
    """
    return {'successes': 0, 'tests': 0, 'reason': reason, 'limit': lim}


def expecting(counter, flag, errstring='null'):
    """
    Do the work of counting and reporting.
    If flag is true, the condition being tested is true, meaning no error.
    Report the progress at all times, but give more detail when flag is False.
    The value of this for debugging depends on useful errstring!

    :param counter: the counter to use
    :param flag: A Boolean, the result of a test for an expected correct result
    :param errstring: a string that describes what should have happened
    :return: None
    """
    counter['tests'] += 1
    if flag:
        counter['successes'] += 1
    print("***", counter['successes'], 'of', counter['tests'], 'tests passed', end=' ')
    if not flag:
        print('**FAILURE**', counter['reason'] + errstring)
    else:
        print()
    assert counter['limit'] == 0 or counter['tests'] - counter['successes'] < counter[
        'limit'], "Halting because of too many errors"


def set_limit(counter, errors):
    """
    Set the counter to terminate testing after a number of errors.
    If errors is 0, there is no limit.
    :param counter: a counter
    :param errors: an integer
    :return: None
    """
    counter['limit'] = errors


def final_report(counter):
    """
    Display the final count for the number of successful tests.
    :param counter: a counter.
    :return: None
    """
    print('Final Count for', counter['reason'], counter['successes'], 'of', counter['tests'], 'tests passed')


# end of the counter ADT
###############################################################################################

test_counter = createCounter('Linked List ADT:')
# SUGGESTION: 
#   -set limit to 10 errors as you are working; keeps output focussed
#   -set limit to 0 (default, meaning "attempt all tests") 
#    when you're close to done
# set_limit(test_counter, 10)

###############################################################################################
reason = 'create() unit test'
print('---Test phase:', reason, '---')
allist = List.create()

try:
    expecting(test_counter, allist['size'] == 0, reason + ": size not zero ")
except:  # yah, I know, this is "too broad"
         # the use of try/except here allows us to keep counting
         # if any runtime errors occur
         # it's not a normal use of Python's Exception handling
    expecting(test_counter, 'size' in allist, reason + ': could not find size')

try:
    expecting(test_counter, allist['head'] is None, reason + ": head not None")
except:
    expecting(test_counter, 'head' in allist, reason + ': could not find head')

try:
    expecting(test_counter, allist['tail'] is None, reason + ": tail not None")
except:
    expecting(test_counter, 'tail' in allist, reason + ': could not find tail')

###############################################################################################
reason = 'size()/is_empty() test'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
expecting(test_counter, List.is_empty(thellist), reason + ': is_empty returned False')
expecting(test_counter, List.size(thellist) == 0, reason + ': size not zero')

thenode = {'data': 'not the target', 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}
expecting(test_counter, not List.is_empty(thellist), reason + ': returned True on singleton list')
expecting(test_counter, List.size(thellist) == 1, reason + ': size should be 1')

###############################################################################################
reason = 'add_to_front() test first insertion'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
target = 'one'
List.add_to_front(thellist, target)

expecting(test_counter, thellist['size'] == 1, reason + ': size not set correctly')

expecting(test_counter, thellist['head'] == thellist['tail'], reason + ' head tail refs different')

try:
    expecting(test_counter, thellist['head']['data'] == target, reason + ': data not set correctly')
except:
    expecting(test_counter, thellist['head'] is not None, reason + ': head not set correctly')
try:
    expecting(test_counter, thellist['tail']['data'] == target, reason + ': data not set correctly')
except:
    expecting(test_counter, thellist['tail'] is not None, reason + ': tail not set correctly')
try:
    expecting(test_counter, thellist['head']['next'] is None, reason + ': chain should end at one node')
except:
    expecting(test_counter, thellist['head'] is not None, reason + ': head not set correctly')

expecting(test_counter, not List.is_empty(thellist), reason + ': is_empty returned True')

expecting(test_counter, List.size(thellist) == 1, reason + ': size not set correctly')

###############################################################################################
reason = 'add_to_front() test second insertion'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
List.add_to_front(thellist, 'not the target')
target = 'two'
List.add_to_front(thellist, target)

try:
    expecting(test_counter, thellist['size'] == 2, reason + ': size not set correctly')
except:
    expecting(test_counter, 'size' in thellist, reason + ': could not find size')

try:
    expecting(test_counter, thellist['head'] != thellist['tail'], reason + ' head tail refs equal')
    expecting(test_counter, thellist['head']['data'] == target, reason + ': data not set correctly in head')
    expecting(test_counter, thellist['head']['next'] is not None, reason + ': chain should not end at one node')
except:
    expecting(test_counter, thellist['head'] is not None, reason + ': head not set correctly')
try:
    expecting(test_counter, thellist['tail']['data'] != target, reason + ': data not set correctly in tail')
except:
    expecting(test_counter, thellist['tail'] is not None, reason + ': tail not set correctly')

expecting(test_counter, not List.is_empty(thellist), reason + ': is_empty() returned True')

expecting(test_counter, List.size(thellist) == 2, reason + ': size() not returning correct value')

###############################################################################################
reason = 'add_to_back() test first insertion'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
target = 'three'
List.add_to_back(thellist, target)

expecting(test_counter, thellist['size'] == 1, reason + ': size not set correctly')
expecting(test_counter, thellist['head'] == thellist['tail'], reason + ' head tail refs different')

try:
    expecting(test_counter, thellist['head']['data'] == target, reason + ': data not set correctly in head')
except:
    expecting(test_counter, thellist['head'] is not None, reason + ': head not set correctly')
try:
    expecting(test_counter, thellist['tail']['data'] == target, reason + ': data not set correctly in tail')
except:
    expecting(test_counter, thellist['tail'] is not None, reason + ': head not set correctly')
try:
    expecting(test_counter, thellist['head']['next'] is None, reason + ': chain should end at one node')
except:
    expecting(test_counter, thellist['head'] is not None, reason + ': head not set correctly')

expecting(test_counter, not List.is_empty(thellist), reason + ': is_empty() returned True')

expecting(test_counter, List.size(thellist) == 1, reason + ': size() not returning correct value')

###############################################################################################
reason = 'add_to_back() test second insertion'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
List.add_to_back(thellist, 'not the target')
target = 'four'
List.add_to_back(thellist, target)

expecting(test_counter, thellist['size'] == 2, reason + ': size not set correctly')

expecting(test_counter, thellist['head'] != thellist['tail'], reason + ' head tail refs equal')

try:
    expecting(test_counter, thellist['tail']['data'] == target, reason + ': data not set correctly in tail')
except:
    expecting(test_counter, thellist['tail'] is not None, reason + ': tail not set correctly')
try:
    expecting(test_counter, thellist['head']['data'] != target, reason + ': data not set correctly in head')
except:
    expecting(test_counter, thellist['head'] is not None, reason + ': head not set correctly')
try:
    expecting(test_counter, thellist['head']['next'] is not None, reason + ': chain should not end at one node')
except:
    expecting(test_counter, thellist['head'] is not None, reason + ': head not set correctly')

expecting(test_counter, not List.is_empty(thellist), reason + ': is_empty() returned True')

expecting(test_counter, List.size(thellist) == 2, reason + ': size() not returning correct value')

###############################################################################################
reason = 'value_is_in() test'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
target = 5

expecting(test_counter, List.value_is_in(thellist, target) is False, reason + ': returned True for empty list')

thenode = {'data': 'not the target', 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}
target = 'six'

expecting(test_counter, List.value_is_in(thellist, target) is False,
          reason + ': returned True for singleton list (not in)')

target = '7'
thenode = {'data': target, 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}

expecting(test_counter, List.value_is_in(thellist, target) is True, reason + ': returned False for singleton list (in)')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

expecting(test_counter, List.value_is_in(thellist, target) is False,
          reason + ': returned True for list size 2 (not in)')

thetail = {'data': target, 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

expecting(test_counter, List.value_is_in(thellist, target) is True,
          reason + ': returned False for list size 2 (in tail)')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': target, 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

expecting(test_counter, List.value_is_in(thellist, target) is True,
          reason + ': returned False for list size 2 (in head)')

###############################################################################################
reason = 'get_index_of_value() test'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
target = 9

flag, idx = List.get_index_of_value(thellist, target)
expecting(test_counter, flag is False, reason + ': returned True for empty list')
expecting(test_counter, idx is None, reason + ': returned non-None index for empty list')

thenode = {'data': 'not the target', 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}
target = 'six'

flag, idx = List.get_index_of_value(thellist, target)
expecting(test_counter, flag is False, reason + ': returned True for singleton list (not in)')
expecting(test_counter, idx is None, reason + ': returned non-None index for singleton list (not in)')

target = '10'
thenode = {'data': target, 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}

flag, idx = List.get_index_of_value(thellist, target)
expecting(test_counter, flag is True, reason + ': returned False for singleton list (in)')
expecting(test_counter, idx == 0, reason + ': returned non-zero index for singleton list (in)')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

flag, idx = List.get_index_of_value(thellist, target)
expecting(test_counter, flag is False, reason + ': returned True for list size 2 (not in)')
expecting(test_counter, idx is None, reason + ': returned non-None index for list size 2 (not in)')

thetail = {'data': target, 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

flag, idx = List.get_index_of_value(thellist, target)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (in tail)')
expecting(test_counter, idx == 1, reason + ': returned incorrect index for singleton list (in)')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': target, 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

flag, idx = List.get_index_of_value(thellist, target)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (in head)')
expecting(test_counter, idx == 0, reason + ': returned non-zero index for singleton list (in)')

###############################################################################################
reason = 'retrieve_data_at_index() test'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
idx = 0

flag, val = List.retrieve_data_at_index(thellist, idx)
expecting(test_counter, flag is False, reason + ': returned True for empty list')
expecting(test_counter, val is None, reason + ': returned non-None value for empty list')

target = 12
thenode = {'data': target, 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}
idx = 0

flag, val = List.retrieve_data_at_index(thellist, idx)
expecting(test_counter, flag is True, reason + ': returned True for singleton list (not in)')
expecting(test_counter, val == target, reason + ': returned non-None index for singleton list (not in)')

thetail = {'data': 16, 'next': None}
thehead = {'data': 18, 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

idx = 0
flag, val = List.retrieve_data_at_index(thellist, idx)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (valid index)')
expecting(test_counter, val == 18, reason + ': returned non-None index for list size 2 (not in)')

idx = 1
flag, val = List.retrieve_data_at_index(thellist, idx)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (valid index)')
expecting(test_counter, val == 16, reason + ': returned non-None index for list size 2 (not in)')

idx = 2
flag, val = List.retrieve_data_at_index(thellist, idx)
expecting(test_counter, flag is False, reason + ': returned True for invalid index')
expecting(test_counter, val is None, reason + ': returned non-None value for invalid index')

###############################################################################################
reason = 'set_data_at_index() test'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
idx = 0

flag = List.set_data_at_index(thellist, idx, val)
expecting(test_counter, flag is False, reason + ': returned True for empty list')

target = 23
thenode = {'data': 'not the target', 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}
idx = 0

flag = List.set_data_at_index(thellist, idx, target)
expecting(test_counter, flag is True, reason + ': returned False for singleton list (valid index)')
expecting(test_counter, thellist['head']['data'] == target,
          reason + ': value not set correctly for singleton list (valid index)')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

idx = 0
flag = List.set_data_at_index(thellist, idx, target)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (valid index)')
expecting(test_counter, thellist['head']['data'] == target,
          reason + ': value not set correctly for list size 2 (valid index)')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

idx = 1
flag = List.set_data_at_index(thellist, idx, target)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (valid index)')
expecting(test_counter, thellist['tail']['data'] == target,
          reason + ': value not set correctly for list size 2 (valid index)')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

idx = 2
flag = List.set_data_at_index(thellist, idx, val)
expecting(test_counter, flag is False, reason + ': returned True for list size 2 (invalid index)')
expecting(test_counter, thellist['head']['data'] == 'not the target',
          reason + ': value changed incorrectly for list size 2 (invalid index)')
expecting(test_counter, thellist['tail']['data'] == 'not the target',
          reason + ': value changed incorrectly for list size 2 (invalid index)')

###############################################################################################
reason = 'remove_from_front() test'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}

flag, val = List.remove_from_front(thellist)
expecting(test_counter, flag is False, reason + ': returned True for empty list')
expecting(test_counter, val is None, reason + ': returned non-None value for empty list')

target = 25
thenode = {'data': target, 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}

flag, val = List.remove_from_front(thellist)
expecting(test_counter, flag is True, reason + ': returned False for singleton list')
expecting(test_counter, val == target, reason + ': returned incorrect value for singleton list')
expecting(test_counter, thellist['size'] == 0, reason + ': set incorrect size for singleton list')

thetail = {'data': 29, 'next': None}
thehead = {'data': 33, 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

target = 33
flag, val = List.remove_from_front(thellist)
expecting(test_counter, flag is True, reason + ': returned False for list size 2')
expecting(test_counter, val == target, reason + ': returned incorrect value for list size 2')
expecting(test_counter, thellist['size'] == 1, reason + ': set incorrect size for list size 2')

###############################################################################################
reason = 'remove_from_back() test'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}

flag, val = List.remove_from_back(thellist)
expecting(test_counter, flag is False, reason + ': returned True for empty list')
expecting(test_counter, val is None, reason + ': returned non-None value for empty list')

target = 25
thenode = {'data': target, 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}

flag, val = List.remove_from_back(thellist)
expecting(test_counter, flag is True, reason + ': returned False for singleton list')
expecting(test_counter, val == target, reason + ': returned incorrect value for singleton list')
expecting(test_counter, thellist['size'] == 0, reason + ': set incorrect size for singleton list')

thetail = {'data': 29, 'next': None}
thehead = {'data': 33, 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

target = 29
flag, val = List.remove_from_back(thellist)
expecting(test_counter, flag is True, reason + ': returned False for list size 2')
expecting(test_counter, val == target, reason + ': returned incorrect value for list size 2')
expecting(test_counter, thellist['size'] == 1, reason + ': set incorrect size for list size 2')

###############################################################################################
reason = 'insert_value_at_index() test'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
idx = 0
target = 'one'

flag = List.insert_value_at_index(thellist, target, idx)
expecting(test_counter, flag is True, reason + ': returned False for empty list')
expecting(test_counter, thellist['size'] == 1, reason + ': set incorrect size for empty list')
expecting(test_counter, thellist['head'] == thellist['tail'], reason + ' head tail refs different')

try:
    expecting(test_counter, thellist['head']['data'] == target, reason + ': data not set correctly')
    expecting(test_counter, thellist['head']['next'] is None, reason + ': chain should end at one node')
except:
    expecting(test_counter, 'head' in allist, reason + ': could not find head')

try:
    expecting(test_counter, thellist['tail']['data'] == target, reason + ': data not set correctly')
except:
    expecting(test_counter, 'tail' in allist, reason + ': could not find head')

target = 'two'
thenode = {'data': 'not the target', 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}

idx = 0
flag = List.insert_value_at_index(thellist, target, idx)
expecting(test_counter, flag is True, reason + ': returned False for singleton list (valid index)')
expecting(test_counter, thellist['head']['data'] == target,
          reason + ': value not inserted correctly for singleton list (index = 0)')
expecting(test_counter, thellist['head']['next'] is not None, reason + ': chain should have 2 nodes now')
expecting(test_counter, thellist['size'] == 2, reason + ': set incorrect size for singleton list')
expecting(test_counter, thellist['head'] != thellist['tail'], reason + ' head tail refs are equal')
expecting(test_counter, thellist['tail']['next'] is None, reason + ': tail should have next == None')

target = 'three'
thenode = {'data': 'not the target', 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}

idx = 1
flag = List.insert_value_at_index(thellist, target, idx)
expecting(test_counter, flag is True, reason + ': returned False for singleton list (valid index)')
expecting(test_counter, thellist['head']['data'] != target,
          reason + ': head value set incorrectly for singleton list (index = 1)')
expecting(test_counter, thellist['tail']['data'] == target,
          reason + ': value not inserted correctly for singleton list (index = 1)')
expecting(test_counter, thellist['head']['next'] is not None, reason + ': chain should have 2 nodes now!')
expecting(test_counter, thellist['size'] == 2, reason + ': set incorrect size for singleton list')
expecting(test_counter, thellist['head'] != thellist['tail'], reason + ' head tail refs are equal')
expecting(test_counter, thellist['tail']['next'] is None, reason + ': tail should have next == None')

target = 'four'
thenode = {'data': 'not the target', 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}

idx = 2
flag = List.insert_value_at_index(thellist, target, idx)
expecting(test_counter, flag is False, reason + ': returned True for singleton list but invlaid index')
expecting(test_counter, thellist['size'] == 1, reason + ': changed size for for singleton list but invlaid index')
expecting(test_counter, thellist['head'] == thellist['tail'], reason + ' head tail refs changed on invalid index')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

target = 'five'
idx = 0
flag = List.insert_value_at_index(thellist, target, idx)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (valid index)')
expecting(test_counter, thellist['head']['data'] == target,
          reason + ': value not inserted correctly for list size 2 (index = 0)')
expecting(test_counter, thellist['size'] == 3, reason + ': set incorrect size for list size 2')
expecting(test_counter, thellist['tail']['next'] is None, reason + ': list size 2, tail should have next == None')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

target = 'six'
idx = 1
flag = List.insert_value_at_index(thellist, target, idx)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (valid index)')
expecting(test_counter, thellist['head']['data'] != target,
          reason + ': value not inserted correctly for list size 2 (index = 1)')
expecting(test_counter, thellist['head']['next']['data'] == target,
          reason + ': value not inserted correctly for list size 2 (index = 1)')
expecting(test_counter, thellist['size'] == 3, reason + ': set incorrect size for list size 2')
expecting(test_counter, thellist['tail']['next'] is None, reason + ': list size 2, tail should have next == None')

thetail = {'data': 'not the target', 'next': None}
thehead = {'data': 'not the target', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

target = 'nine'
idx = 2
flag = List.insert_value_at_index(thellist, target, idx)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (valid index)')
expecting(test_counter, thellist['head']['data'] != target,
          reason + ': value not inserted correctly for list size 2 (index = 2)')
expecting(test_counter, thellist['head']['next']['data'] != target,
          reason + ': value not inserted correctly for list size 2 (index = 2)')
expecting(test_counter, thellist['tail']['data'] == target,
          reason + ': value not inserted correctly for list size 2 (index = 2)')
expecting(test_counter, thellist['size'] == 3, reason + ': set incorrect size for list size 2')
expecting(test_counter, thellist['tail']['next'] is None, reason + ': list size 2, tail should have next == None')

###############################################################################################
reason = 'delete_item_at_index() test'
print('---Test phase:', reason, '---')

thellist = {'size': 0, 'tail': None, 'head': None}
idx = 0

flag = List.delete_item_at_index(thellist, idx)
expecting(test_counter, flag is False, reason + ': returned True for empty list')
expecting(test_counter, thellist['size'] == 0, reason + ': set incorrect size for empty list')
expecting(test_counter, thellist['head'] == thellist['tail'], reason + ' head tail refs different')

thenode = {'data': 'not the target', 'next': None}
thellist = {'size': 1, 'tail': thenode, 'head': thenode}

idx = 0
flag = List.delete_item_at_index(thellist, idx)
expecting(test_counter, flag is True, reason + ': returned False for singleton list (valid index)')
expecting(test_counter, thellist['head'] is None,
          reason + ': value not deleted correctly for singleton list (index = 0)')
expecting(test_counter, thellist['size'] == 0, reason + ': set incorrect size for singleton list')
expecting(test_counter, thellist['tail'] is None, reason + ': tail should be None')

thetail = {'data': 'ten', 'next': None}
thehead = {'data': 'twelve', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

idx = 0
flag = List.delete_item_at_index(thellist, idx)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (index = 0)')
expecting(test_counter, thellist['head']['data'] == 'ten',
          reason + ': value not deleted correctly for list size 2 (index = 0)')
expecting(test_counter, thellist['size'] == 1, reason + ': set incorrect size for list size 2')
expecting(test_counter, thellist['head'] == thellist['tail'], reason + ': head tail should be equal')

thetail = {'data': 'ten', 'next': None}
thehead = {'data': 'twelve', 'next': thetail}
thellist = {'size': 2, 'tail': thetail, 'head': thehead}

idx = 1
flag = List.delete_item_at_index(thellist, idx)
expecting(test_counter, flag is True, reason + ': returned False for list size 2 (index = 1)')
expecting(test_counter, thellist['head']['data'] == 'twelve',
          reason + ': value not deleted correctly for list size 2 (index = 1)')
expecting(test_counter, thellist['size'] == 1, reason + ': set incorrect size for list size 2')
expecting(test_counter, thellist['head'] == thellist['tail'], reason + ': head tail should be equal')

###############################################################################################
reason = 'integration: building a short list with add_to_back()'
print('---Test phase:', reason, '---')

thellist = List.create()
stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
for word in stuff:
    List.add_to_back(thellist, word)

expecting(test_counter, List.is_empty(thellist) is False, reason + ": should not be empty")
expecting(test_counter, List.size(thellist) == 7, reason + ": should have size 7")
expecting(test_counter, List.value_is_in(thellist, "HEY") is True, reason + ": should have found HEY first")
expecting(test_counter, List.value_is_in(thellist, "STOPSIGN") is True, reason + ": should have found STOPSIGN")
expecting(test_counter, List.value_is_in(thellist, "TURTLE") is True, reason + ": should have found TURTLE last")
expecting(test_counter, List.value_is_in(thellist, "not in the list") is False, reason + ": should have returned False")
expecting(test_counter, List.get_index_of_value(thellist, "HEY") == (True, 0), reason + ": HEY is at index zero")
expecting(test_counter, List.get_index_of_value(thellist, "TURTLE") == (True, 6), reason + ": TURTLE is at index 6")
expecting(test_counter, List.get_index_of_value(thellist, "DOING-DOING") == (True, 4),
          reason + ": DOING-DOING is at index 4")
expecting(test_counter, List.get_index_of_value(thellist, "GLOBE") == (False, None), reason + ": GLOBE Not in llist")
expecting(test_counter, List.retrieve_data_at_index(thellist, 6) == (True, "TURTLE"), reason + ": TURTLE is at index 6")
expecting(test_counter, List.retrieve_data_at_index(thellist, 0) == (True, "HEY"), reason + ": HEY is at index 0")
expecting(test_counter, List.retrieve_data_at_index(thellist, 2) == (True, "THANK-YOU"),
          reason + ": THANK-YOU is at index 3")
expecting(test_counter, List.retrieve_data_at_index(thellist, 7) == (False, None), reason + ": index not valid")

###############################################################################################
reason = 'integration: building a short list with add_to_front()'
print('---Test phase:', reason, '---')

thellist = List.create()
stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
for word in stuff:
    List.add_to_front(thellist, word)

expecting(test_counter, List.is_empty(thellist) is False, reason + ": should not be empty")
expecting(test_counter, List.size(thellist) == 7, reason + ": should have size 7")
expecting(test_counter, List.value_is_in(thellist, "HEY") is True, reason + ": should have found HEY last")
expecting(test_counter, List.value_is_in(thellist, "STOPSIGN") is True, reason + ": should have found STOPSIGN")
expecting(test_counter, List.value_is_in(thellist, "TURTLE") is True, reason + ": should have found TURTLE first")
expecting(test_counter, List.value_is_in(thellist, "not in the list") is False, reason + ": should have returned False")
expecting(test_counter, List.get_index_of_value(thellist, "HEY") == (True, 6), reason + ": HEY is at index 6")
expecting(test_counter, List.get_index_of_value(thellist, "TURTLE") == (True, 0), reason + ": TURTLE is at index 0")
expecting(test_counter, List.get_index_of_value(thellist, "DOING-DOING") == (True, 2),
          reason + ": DOING-DOING is at index 2")
expecting(test_counter, List.get_index_of_value(thellist, "GLOBE") == (False, None), reason + ": GLOBE Not in llist")
expecting(test_counter, List.retrieve_data_at_index(thellist, 0) == (True, "TURTLE"), reason + ": TURTLE is at index 0")
expecting(test_counter, List.retrieve_data_at_index(thellist, 6) == (True, "HEY"), reason + ": HEY is at index 6")
expecting(test_counter, List.retrieve_data_at_index(thellist, 3) == (True, "TURN-AROUND"),
          reason + ": TURN-AROUND is at index 3")
expecting(test_counter, List.retrieve_data_at_index(thellist, 7) == (False, None), reason + ": index not valid")

###############################################################################################
reason = 'integration: changing data in a short list'
print('---Test phase:', reason, '---')

thellist = List.create()
stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
for word in stuff:
    List.add_to_back(thellist, word)

expecting(test_counter, List.set_data_at_index(thellist, 0, "now") == True, reason + ": index valid")
expecting(test_counter, List.get_index_of_value(thellist, "HEY") == (False, None), reason + ": HEY should be gone")
expecting(test_counter, List.get_index_of_value(thellist, "now") == (True, 0), reason + ": now is at index 0")
expecting(test_counter, List.size(thellist) == 7, reason + ": should have size 7")

expecting(test_counter, List.set_data_at_index(thellist, 6, "SIGN") == True, reason + ": index valid")
expecting(test_counter, List.get_index_of_value(thellist, "TURTLE") == (False, None),
          reason + ": TURTLE should be gone")
expecting(test_counter, List.get_index_of_value(thellist, "SIGN") == (True, 6), reason + ": SIGN is at index 0")
expecting(test_counter, List.size(thellist) == 7, reason + ": should have size 7")

expecting(test_counter, List.set_data_at_index(thellist, 3, "FOLLOWER") == True, reason + ": index valid")
expecting(test_counter, List.get_index_of_value(thellist, "TURN-AROUND") == (False, None),
          reason + ": TURN-AROUND should be gone")
expecting(test_counter, List.get_index_of_value(thellist, "FOLLOWER") == (True, 3), reason + ": FOLLOWER is at index 3")
expecting(test_counter, List.size(thellist) == 7, reason + ": should have size 7")

###############################################################################################
reason = 'integration: inserting data in a short list'
print('---Test phase:', reason, '---')

thellist = List.create()
stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
for word in stuff:
    List.add_to_back(thellist, word)

expecting(test_counter, List.insert_value_at_index(thellist, "LEFT", 0) == True, reason + ": index valid")
expecting(test_counter, List.get_index_of_value(thellist, "LEFT") == (True, 0), reason + ": LEFT is first")
expecting(test_counter, List.get_index_of_value(thellist, "DOING-DOING") == (True, 5),
          reason + ": DOING-DOING is at index 5")
expecting(test_counter, List.size(thellist) == 8, reason + ": should have size 8")

expecting(test_counter, List.insert_value_at_index(thellist, "RIGHT", 8) == True, reason + ": index valid")
expecting(test_counter, List.get_index_of_value(thellist, "RIGHT") == (True, 8), reason + ": RIGHT is last")
expecting(test_counter, List.get_index_of_value(thellist, "TURTLE") == (True, 7), reason + ": TURTLE is at index 7")
expecting(test_counter, List.size(thellist) == 9, reason + ": should have size 9")

expecting(test_counter, List.insert_value_at_index(thellist, "MIDDLE", 5) == True, reason + ": index valid")
expecting(test_counter, List.get_index_of_value(thellist, "MIDDLE") == (True, 5), reason + ": MIDDLE is at index 5")
expecting(test_counter, List.get_index_of_value(thellist, "TURTLE") == (True, 8), reason + ": TURTLE is at index 8")
expecting(test_counter, List.size(thellist) == 10, reason + ": should have size 10")

###############################################################################################
reason = 'integration: deleting data from a short list'
print('---Test phase:', reason, '---')

thellist = List.create()
stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
for word in stuff:
    List.add_to_back(thellist, word)

expecting(test_counter, List.delete_item_at_index(thellist, 0) == True, reason + ": index valid")
expecting(test_counter, List.get_index_of_value(thellist, "HEY") == (False, None), reason + ": HEY should be gone")
expecting(test_counter, List.value_is_in(thellist, "HEY") is False, reason + ": HEY should be gone")
expecting(test_counter, List.size(thellist) == 6, reason + ": should have size 6")
expecting(test_counter, List.get_index_of_value(thellist, "STOPSIGN") == (True, 0),
          reason + ": STOPSIGN should be at index 0")

expecting(test_counter, List.delete_item_at_index(thellist, 5) == True, reason + ": index valid")
expecting(test_counter, List.get_index_of_value(thellist, "TURTLE") == (False, None),
          reason + ": TURTLE should be gone")
expecting(test_counter, List.value_is_in(thellist, "TURTLE") is False, reason + ": TURTLE should be gone")
expecting(test_counter, List.size(thellist) == 5, reason + ": should have size 5")
expecting(test_counter, List.get_index_of_value(thellist, "HORSESHOE") == (True, 4),
          reason + ": HORSESHOE should be at index 4")

expecting(test_counter, List.delete_item_at_index(thellist, 2) == True, reason + ": index valid")
expecting(test_counter, List.get_index_of_value(thellist, "TURN-AROUND") == (False, None),
          reason + ": TURN-AROUND should be gone")
expecting(test_counter, List.value_is_in(thellist, "TURN-AROUND") is False, reason + ": TURN-AROUND should be gone")
expecting(test_counter, List.size(thellist) == 4, reason + ": should have size 4")
expecting(test_counter, List.get_index_of_value(thellist, "DOING-DOING") == (True, 2),
          reason + ": DOING-DOING should be at index 2")

###############################################################################################
reason = 'integration: removing from back'
print('---Test phase:', reason, '---')

thellist = List.create()
stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
for word in stuff:
    List.add_to_back(thellist, word)
expecting(test_counter, List.size(thellist) == 7, reason + ": should have size 7")
for i in range(4):
    List.remove_from_back(thellist)
expecting(test_counter, List.size(thellist) == 3, reason + ": should have size 3")
expecting(test_counter, List.get_index_of_value(thellist, "TURN-AROUND") == (False, None),
          reason + ": TURN-AROUND should be gone")
expecting(test_counter, List.get_index_of_value(thellist, "THANK-YOU") == (True, 2),
          reason + ": THANK-YOU should be at index 2")
expecting(test_counter, List.retrieve_data_at_index(thellist, 2) == (True, "THANK-YOU"),
          reason + ": THANK-YOU is at index 2")

###############################################################################################
reason = 'integration: removing from front'
print('---Test phase:', reason, '---')

thellist = List.create()
stuff = 'HEY STOPSIGN THANK-YOU TURN-AROUND DOING-DOING HORSESHOE TURTLE'.split()
for word in stuff:
    List.add_to_front(thellist, word)
expecting(test_counter, List.size(thellist) == 7, reason + ": should have size 7")
for i in range(4):
    List.remove_from_front(thellist)
expecting(test_counter, List.size(thellist) == 3, reason + ": should have size 3")
expecting(test_counter, List.get_index_of_value(thellist, "TURN-AROUND") == (False, None),
          reason + ": TURN-AROUND should be gone")
expecting(test_counter, List.get_index_of_value(thellist, "THANK-YOU") == (True, 0),
          reason + ": THANK-YOU should be at index 0")
expecting(test_counter, List.retrieve_data_at_index(thellist, 0) == (True, "THANK-YOU"),
          reason + ": THANK-YOU is at index 0")

final_report(test_counter)
