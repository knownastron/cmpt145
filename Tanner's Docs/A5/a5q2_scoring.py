# CMPT 145: Assignment 5 Question 2
# test script


# try to import the student's solutions
imported = False
try:
    import a5q2 as student_a5q2
    imported = True
except:
    print('a5q2 not found')

# if a5q1 isn't there, try A5Q2
if not imported:
    try:
        import A5Q2 as student_a5q2
        print('found A5Q2')
        imported = True
    except:
        print('No A5Q2 either')

# if A5Q2 isn't there, try A5q2
if not imported:
    try:
        import A5q2 as student_a5q2
        print('found A5q2')
        imported = True
    except:
        print('No A5q2 either')

# if A5q2 isn't there, try a5Q2
if not imported:
    try:
        import a5Q2 as student_a5q2
        print('found A5q2')
        imported = True
    except:
        print('No a5Q2 either')

if not imported:
    # made a reasonable attempt, bail!
    print('Not continuing')
    exit(1)


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


test_count_chain = [
    {'inputs' : None,
     'outputs': 0,
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': 1,
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': 2,
     'reason' : 'node chain with two nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': 3,
     'reason' : 'node chain with three nodes'},
]

count_chain_counter = createCounter('A5Q2 count_chain()')

for t in test_count_chain:
    args_in = t['inputs']
    expected = t['outputs']
    result = student_a5q2.count_chain(args_in)
    expecting(count_chain_counter, result == expected, 'count_chain(): got '\
        +str(result)+' expected '+str(expected)+' -- ' +t['reason'])

test_copy_chain = [
    {'inputs' : None,
     'outputs': None,
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': None,
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': None,
     'reason' : 'node chain with two nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': None,
     'reason' : 'node chain with three nodes'},
]

final_report(count_chain_counter)

copy_chain_counter = createCounter('A5Q2 copy_chain()')

for t in test_copy_chain:
    args_in = t['inputs']
    result = student_a5q2.copy_chain(args_in)

    expecting(copy_chain_counter, (args_in is None and result is None)
           or (args_in is not result),
        'copy_chain(): original chain returned -- '+t['reason'])

    expecting(copy_chain_counter, args_in == result, 'copy_chain(): chains not equal -- '+t['reason'])

final_report(copy_chain_counter)

replace_counter = createCounter('A5Q2 replace()\t')

test_replace = [
    {'inputs' : [None, 1, 1],
     'outputs': "EMPTY",
     'reason' : 'Empty node chain'},

    {'inputs' : [node.create(1), 1, 2],
     'outputs': "[ 2 | / ]",
     'reason' : 'node chain with one node, target in'},

    {'inputs' : [node.create(1), 5, 2],
     'outputs': "[ 1 | / ]",
     'reason' : 'node chain with one node, target not in'},

    {'inputs' : [node.create(1, node.create('two')),
                 1, 'one'],
     'outputs': "[ one | *-]-->[ two | / ]",
     'reason' : 'node chain with two nodes, target first'},

    {'inputs' : [node.create(1, node.create('two')),
                 5, 'five'],
     'outputs': "[ 1 | *-]-->[ two | / ]",
     'reason' : 'node chain with two nodes, target not in'},
    {'inputs' : [node.create(1, node.create('two')),
                 'two', 2],
     'outputs': "[ 1 | *-]-->[ 2 | / ]",
     'reason' : 'node chain with two nodes, target last'},

    {'inputs' : [node.create(1, node.create('two', node.create(3))),
                 'two', 2],
     'outputs': "[ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]",
     'reason' : 'node chain with three nodes, target middle'},

    {'inputs' : [node.create(1, node.create(3, node.create(3))),
                 3, 2],
     'outputs': "[ 1 | *-]-->[ 2 | *-]-->[ 2 | / ]",
     'reason' : 'node chain with three nodes, target repeated middle last'},

    {'inputs' : [node.create(3, node.create(1, node.create(3))),
                 3, 2],
     'outputs': "[ 2 | *-]-->[ 1 | *-]-->[ 2 | / ]",
     'reason' : 'node chain with three nodes, target repeated first last'},

    {'inputs' : [node.create(1, node.create(1, node.create(3))),
                 1, 2],
     'outputs': "[ 2 | *-]-->[ 2 | *-]-->[ 3 | / ]",
     'reason' : 'node chain with three nodes, target repeated first middle'},

]

for t in test_replace:
    args_in = t['inputs']
    expected = t['outputs']
    student_a5q2.replace(args_in[0], args_in[1], args_in[2])
    result = to_string_correct(args_in[0])
    expecting(replace_counter, result == expected,
        'replace(): got "'+result+'" expected "'+expected+'" -- '+t['reason'])

final_report(replace_counter)

print('*** testing complete ***')
