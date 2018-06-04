# CMPT 145: Node-based Queues
# Implements the Queue ADT
#
# A queue (also called a FIFO queue) is a compound data 
# structure in which the data values are ordered according to 
# the FIFO (first-in first-out) protocol.
#
# Implementation notes:
# This implementation uses the linked node structure.


import node as node

def create():
    """
    Purpose
        creates an empty queue
    Return
        an empty queue
    """
    queue = {}
    queue['size'] = 0        # how many elements in the queue
    queue['front'] = None    # the node chain starts here
    queue['back'] = None     # the node chain ends here
    return queue


def size(queue):
    """
    Purpose
        returns the number of data values in the given queue
    Pre-conditions:
        queue: a queue created by create()
    Return:
        The number of data values in the queue
    """
    return queue['size']


def is_empty(queue):
    """
    Purpose
        checks if the given queue has no data in it
    Pre-conditions:
        queue is a queue created by create()
    Return:
        True if the queue has no data, or false otherwise
    """
    return queue['size'] == 0


def enqueue(queue, value):
    """
    Purpose
        adds the given data value to the given queue
    Pre-conditions:
        queue: a queue created by create()
        value: data to be added
    Post-condition:
        the value is added to the queue
    Return:
        (none)
    """
    new_node = node.create(value, None)

    if is_empty(queue):
        queue['front'] = new_node
        queue['back'] = new_node
    else:
        prev_last_node = queue['back']
        node.set_next(prev_last_node, new_node)
        queue['back'] = new_node

    queue['size'] += 1



def dequeue(queue):
    """
    Purpose
        removes and returns a data value from the given queue
    Pre-conditions:
        queue: a queue created by create()
    Post-condition:
        the first value is removed from the queue
    Return:
        the first value in the queue, or None
    """
    assert not is_empty(queue), 'dequeued an empty queue'

    prev_first_node = queue['front']
    result = node.get_data(prev_first_node)
    queue['front'] = node.get_next(prev_first_node)
    queue['size'] -= 1
    if queue['size'] == 0:
        queue['back'] = None
    return result


def peek(queue):
    """
    Purpose
        returns the value from the front of given stack
        without removing it
    Pre-conditions:
        queue: a non-empty queue created by create()
    Post-condition:
        None
    Return:
        the value at the front of the queue
    """
    assert not is_empty(queue), 'peeked into an empty queue'

    first_node = queue['front']
    result = node.get_data(first_node)
    return result
