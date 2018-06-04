# CMPT 145: Assignment 5 Question 3
# test script


# try to import the student's solutions
imported = False
try:
    import a5q3 as student_a5q3
    imported = True
except:
    print('a5q3 not found')

# if a5q3 isn't there, try A5Q3
if not imported:
    try:
        import A5Q3 as student_a5q3
        print('found A5Q3')
        imported = True
    except:
        print('No A5Q3 either')

# if A5Q3 isn't there, try A5q3
if not imported:
    try:
        import A5q3 as student_a5q3
        print('found A5q3')
        imported = True
    except:
        print('No A5q3 either')

# if A5q3 isn't there, try a5Q3
if not imported:
    try:
        import a5Q3 as student_a5q3
        print('found A5q3')
        imported = True
    except:
        print('No a5Q3 either')

if not imported:
    # made a reasonable attempt, bail!
    print('Not continuing')
    exit(1)

def to_string_correct(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty
    Post_conditions:
        None
    Return: A string representation of the nodes.
    """
    # special case: empty node chain
    if node_chain is None:
        result = 'EMPTY'
    else:
        # walk along the chain
        walker = node_chain
        value = node.get_data(walker)
        # print the data
        result = '[ ' + str(value) + ' |'
        while node.get_next(walker) is not None:
            walker = node.get_next(walker)
            value = node.get_data(walker)
            # represent the next with an arrow-like figure
            result += ' *-]-->[ '+str(value)+' |'

        # at the end of the chain, use '/'
        result += ' / ]'

    return result


import node as node

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

def createCounter(reason, lim=0, quiet=True):
    """
    Create a counter to counter tests.  The counter will
    collect statistics based on calls to function expecting().
    :param reason: a string to describe what's being tested.
    :param lim: how many errors to detect before halting the tests
    :return: None
    """
    return {'successes': 0, 'tests': 0, 'reason': reason, 'limit': lim, 'silent' : quiet}


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
    if not counter['silent']:
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
    print(counter['reason']+'\t', counter['successes'], 'of', counter['tests'], 'tests passed')


# end of the counter ADT
###############################################################################################


split_counter = createCounter('A5Q3 split()\t')
test_split_chain = [
    {'inputs' : None,
     'outputs': ["EMPTY","EMPTY"],
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': ["EMPTY", "[ 1 | / ]"],
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': ["[ 1 | / ]","[ two | / ]"],
     'reason' : 'node chain with two nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': ["[ 1 | / ]", "[ two | *-]-->[ 3 | / ]"],
     'reason' : 'node chain with three nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3,node.create('four')))),
     'outputs': ["[ 1 | *-]-->[ two | / ]","[ 3 | *-]-->[ four | / ]"],
     'reason' : 'node chain with four nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3,node.create('four', node.create(5))))),
     'outputs': ["[ 1 | *-]-->[ two | / ]", "[ 3 | *-]-->[ four | *-]-->[ 5 | / ]"],
     'reason' : 'node chain with five nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3,node.create('four', node.create(5, node.create('six')))))),
     'outputs': ["[ 1 | *-]-->[ two | *-]-->[ 3 | / ]", "[ four | *-]-->[ 5 | *-]-->[ six | / ]"],
     'reason' : 'node chain with six nodes'},
]


for t in test_split_chain:
    args_in = t['inputs']
    expected = t['outputs']
    first, second = student_a5q3.split_chain(args_in)

    str_result = to_string_correct(second)
    str_args_in = to_string_correct(first)
    expecting(split_counter, str_result == expected[1] and str_args_in == expected[0],
        'split_chain(): got '
        +str_result+' and '+str_args_in+' -- ' +t['reason'])

final_report(split_counter)

insert_counter = createCounter('A5Q3 insert_at()   ')

test_insert_at = [

    {'inputs' :  [None, 1, 0],
     'outputs': "[ 1 | / ]",
     'reason' : 'empty node chain'},

    {'inputs' :  [node.create('a'), 1, 0],
     'outputs': "[ 1 | *-]-->[ a | / ]",
     'reason' : 'node chain with one node, insert at front'},

    {'inputs' :  [node.create('a'), 1, 1],
     'outputs': "[ a | *-]-->[ 1 | / ]",
     'reason' : 'node chain with one node, insert at back'},

    {'inputs' :  [node.create('a', node.create('b')), 1, 0],
     'outputs': "[ 1 | *-]-->[ a | *-]-->[ b | / ]",
     'reason' : 'node chain with two nodes, insert at front'},

    {'inputs' :  [node.create('a', node.create('b')), 1, 2],
     'outputs': "[ a | *-]-->[ b | *-]-->[ 1 | / ]",
     'reason' : 'node chain with two nodes, insert at back'},

    {'inputs' :  [node.create('a', node.create('b')), 1, 1],
     'outputs': "[ a | *-]-->[ 1 | *-]-->[ b | / ]",
     'reason' : 'node chain with two nodes, insert at mid'},

    {'inputs' :  [node.create('a', node.create('b', node.create('c', node.create('d')))), 1, 2],
     'outputs': "[ a | *-]-->[ b | *-]-->[ 1 | *-]-->[ c | *-]-->[ d | / ]",
     'reason' : 'node chain with 4 nodes, insert at mid'},

    {'inputs' :  [node.create('a', node.create('b', node.create('c', node.create('d')))), 1, 4],
     'outputs': "[ a | *-]-->[ b | *-]-->[ c | *-]-->[ d | *-]-->[ 1 | / ]",
     'reason' : 'node chain with 4 nodes, insert at back'},

]

for t in test_insert_at:
    args_in = t['inputs']
    expected = t['outputs']
    result = student_a5q3.insert_at(args_in[0], args_in[1], args_in[2])

    str_result = to_string_correct(result)
    expecting(insert_counter, str_result == expected, 'insert_at(): got "'
        +str_result+'" expected "'+expected+'" -- ' +t['reason'])

final_report(insert_counter)

remove_counter = createCounter('A5Q3 remove_chain()')

test_remove_chain = [
    {'inputs' : [None, 1],
     'outputs': "EMPTY",
     'reason' : 'Empty node chain'},

    {'inputs' : [node.create(1), 1],
     'outputs': "EMPTY",
     'reason' : 'node chain with one node, val in'},

    {'inputs' : [node.create(1), 2],
     'outputs': "[ 1 | / ]",
     'reason' : 'node chain with one node, val not in'},

    {'inputs' : [node.create(1, node.create('two')), 'two'],
     'outputs': "[ 1 | / ]",
     'reason' : 'node chain with two nodes, val last'},

    {'inputs' : [node.create(1, node.create('two')), 1],
     'outputs': "[ two | / ]",
     'reason' : 'node chain with two nodes, val first'},

    {'inputs' : [node.create(1, node.create('two')), 3],
     'outputs': "[ 1 | *-]-->[ two | / ]",
     'reason' : 'node chain with two nodes, val not in'},

    {'inputs' : [node.create(1, node.create('two', node.create(3))), 'two'],
     'outputs': "[ 1 | *-]-->[ 3 | / ]",
     'reason' : 'node chain with three nodes, val in middle'},

    {'inputs' : [node.create(1, node.create('two', node.create(1, node.create('four')))), 1],
     'outputs': "[ two | *-]-->[ 1 | *-]-->[ four | / ]",
     'reason' : 'node chain with four nodes, val at front and middle'},

    {'inputs' : [node.create(1, node.create(1, node.create(1, node.create('four')))), 1],
     'outputs': "[ 1 | *-]-->[ 1 | *-]-->[ four | / ]",
     'reason' : 'node chain with four nodes, val repeated at front'},

    {'inputs' : [node.create(2, node.create(1, node.create(1, node.create('four')))), 1],
     'outputs': "[ 2 | *-]-->[ 1 | *-]-->[ four | / ]",
     'reason' : 'node chain with four nodes, val repeated in mid'},

    {'inputs' : [node.create(2, node.create(1, node.create('four', node.create('four')))), 'four'],
     'outputs': "[ 2 | *-]-->[ 1 | *-]-->[ four | / ]",
     'reason' : 'node chain with four nodes, val repeated at end'},

]

for t in test_remove_chain:
    args_in = t['inputs']
    expected = t['outputs']
    result = student_a5q3.remove_chain(args_in[0], args_in[1])

    str_result = to_string_correct(result)
    expecting(remove_counter, str_result == expected, 'remove_all_chain(): got "'
        +str_result+'" expected "'+expected+'" -- ' +t['reason'])

final_report(remove_counter)
print('*** testing complete ***')
