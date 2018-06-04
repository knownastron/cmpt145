# CMPT 145: Assignment 5 Question 1
# test script

# try to import the student's solutions
imported = False
try:
    import a5q1 as student_a5q1
    imported = True
except:
    print('a5q1 not found')

# if a5q1 isn't there, try A5Q1
if not imported:
    try:
        import A5Q1 as student_a5q1
        print('found A5Q1')
        imported = True
    except:
        print('No A5Q1 either')

# if A5Q1 isn't there, try A5q1
if not imported:
    try:
        import A5q1 as student_a5q1
        print('found A5q1')
        imported = True
    except:
        print('No A5q1 either')

# if A5q1 isn't there, try a5Q1
if not imported:
    try:
        import a5Q1 as student_a5q1
        print('found A5q1')
        imported = True
    except:
        print('No a5Q1 either')

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


test_to_string = [
    {'inputs' : None,
     'outputs': 'EMPTY',
     'reason' : 'Empty node chain'},

    {'inputs' : node.create(1),
     'outputs': '[ 1 | / ]',
     'reason' : 'node chain with one node'},

    {'inputs' : node.create(1, node.create('two')),
     'outputs': '[ 1 | *-]-->[ two | / ]',
     'reason' : 'node chain with two nodes'},

    {'inputs' : node.create(1, node.create('two', node.create(3))),
     'outputs': '[ 1 | *-]-->[ two | *-]-->[ 3 | / ]',
     'reason' : 'node chain with three nodes'},
]

to_string_counter = createCounter('A5Q1 to_string()')

for t in test_to_string:
    args_in = t['inputs']
    expected = t['outputs']
    result = student_a5q1.to_string(args_in)
    try:
        expecting(to_string_counter, result == expected,
            'to_string(): got "'+result+'" expected "'+expected+'" -- ' +t['reason'])
    except:
        expecting(to_string_counter, False, "testing exception! "+t['reason'])


final_report(to_string_counter)
print('*** testing complete ***')
