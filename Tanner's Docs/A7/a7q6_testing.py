import a7q6 as a7q6
import node as node

def to_string(node_chain):
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
        return 'EMPTY'

    value = node.get_data(node_chain)
    # print the data
    result = '[ ' + str(value) + ' |'

    if node.get_next(node_chain) is None:
        # at the end of the chain, use '/'
        result += ' / ]'
    else:
        result += ' *-]-->'
        result += to_string(node.get_next(node_chain))
    return result


def display(node):
    """
    Purpose:
        Display a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty
    Post_conditions:
        Displays a string to the console
    Return:
        None
    """
    print(to_string(node))







test_subst = [
    {'inputs' : [None,
                 3, 5],
     'outputs' : None,
     'reason': 'empty chain'},

    {'inputs' : [node.create('one', None),
                 1, 2],
     'outputs' : node.create('one', None),
     'reason': 'short chain no target'},

    {'inputs' : [node.create('one', None),
                 'one', 'two'],
     'outputs' : node.create('two', None),
     'reason': 'short chain with target'},

    {'inputs' : [ node.create('a',node.create('b',node.create('c', node.create(1)))),
                 'one', 'two'],
     'outputs' : node.create('a',node.create('b',node.create('c', node.create(1)))),
     'reason': 'longer chain no target'},

    {'inputs' : [ node.create('a',node.create('b',node.create('c', node.create(1)))),
                 'c', 'si'],
     'outputs' : node.create('a',node.create('b',node.create('si', node.create(1)))),
     'reason': 'longer chain with target'},

    {'inputs' : [ node.create('a',node.create('b',node.create('c', node.create(1)))),
                 'a', 'eh'],
     'outputs' : node.create('eh',node.create('b',node.create('c', node.create(1)))),
     'reason': 'longer chain with target first'},

    {'inputs' : [ node.create('a',node.create('b',node.create('c', node.create(1)))),
                 1, 2],
     'outputs' : node.create('a',node.create('b',node.create('c', node.create(2)))),
     'reason': 'longer chain with target last'},

    {'inputs' : [ node.create('a',node.create('b',node.create('a', node.create(1)))),
                 'a', 'eh'],
     'outputs' : node.create('eh',node.create('b',node.create('eh', node.create(1)))),
     'reason': 'longer chain with multiple targets'},
]

for t in test_subst:
    args_in = t['inputs']
    chain = args_in[0]
    target = args_in[1]
    replace = args_in[2]
    a7q6.subst(chain, target, replace)
    expected = t['outputs']
    str_result = to_string(chain)
    str_expected = to_string(expected)
    if str_result != str_expected:
        print('Error in subst(): expected ', str_expected, 'obtained', str_result, '---', t['reason'])


test_reverse = [
    {'inputs' : None,
     'outputs' : None,
     'reason': 'empty chain'},

    {'inputs' :  node.create('one', None),
     'outputs' : node.create('one', None),
     'reason': 'short chain'},

    {'inputs' :  node.create('a',node.create('b',node.create('c', node.create(1)))),
     'outputs' : node.create('1',node.create('c',node.create('b', node.create('a')))),
     'reason': 'longer chain'},
]

for t in test_reverse:
    chain = t['inputs']
    result = a7q6.reverse_c(chain)
    expected = t['outputs']
    str_result = to_string(result)
    str_expected = to_string(expected)
    if str_result != str_expected:
        print('Error in reverse(): expected ', str_expected, 'obtained', str_result, '---', t['reason'])

test_copy = [
    {'inputs' : None,
     'outputs' : None,
     'reason': 'empty chain'},

    {'inputs' :  node.create('one', None),
     'outputs' : None,
     'reason': 'short chain'},

    {'inputs' :  node.create('a',node.create('b',node.create('c', node.create(1)))),
     'outputs' : None,
     'reason': 'longer chain'},
]

for t in test_copy:
    chain = t['inputs']
    result = a7q6.copy(chain)
    if chain is None and result is not None:
        print('Error in copy(): expected ', None, 'obtained', None, '---', t['reason'])
    elif chain is not None:
        if chain != result:
            print('Error in copy(): expected equal chains', '---', t['reason'])
        if chain is result:
            print('Error in copy(): expected distinct chains', '---', t['reason'])


print('*** testing complete ***')