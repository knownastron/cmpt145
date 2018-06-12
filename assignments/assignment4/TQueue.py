# CMPT 145: Linear ADTs
# Implements the Queue ADT
#
# A queue (also called a FIFO queue) is a compound data 
# structure in which the data values are ordered according to 
# the FIFO (first-in first-out) protocol.
#
# Implementation notes:
# This implementation was designed to point out when ADT operations are
# used incorrectly.




def create():
    """
    Purpose
        creates an empty queue
    Return
        an empty queue
    """
    return '__Queue__',list()


def is_empty(queue):
    """
    Purpose
        checks if the given queue has no data in it
    Pre-conditions:
        queue is a queue created by create()
    Return:
        True if the queue has no data, or false otherwise
    """
    if type(queue) is tuple:
        t,q = queue
        assert t == '__Queue__', 'Type Error: Expected __Queue__ but received '+t
        return len(q) == 0
    else:
        assert False, 'Type Error: Expected __Queue__ but received '+str(type(queue))


def size(queue):
    """
    Purpose
        returns the number of data values in the given queue
    Pre-conditions:
        queue: a queue created by create()
    Return:
        The number of data values in the queue
    """
    if type(queue) is tuple:
        t,q = queue
        assert t == '__Queue__', 'Type Error: Expected __Queue__ but received '+t
        return len(q)
    else:
        assert False, 'Type Error: Expected __Queue__ but received '+str(type(queue))



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
    if type(queue) is tuple:
        t,q = queue
        assert t == '__Queue__', 'Type Error: Expected __Queue__ but received '+t
        q.append(value)
    else:
        assert False, 'Type Error: Expected __Queue__ but received '+str(type(queue))


def dequeue(queue):
    """
    Purpose
        removes and returns a data value from the given queue
    Pre-conditions:
        queue: a queue created by create()
    Post-condition:
        the first value is removed from the queue
    Return:
        the first value in the queue
    """
    if type(queue) is tuple:
        t,q = queue
        assert t == '__Queue__', 'Type Error: Expected __Queue__ but received '+t
        return q.pop(0)
    else:
        assert False, 'Type Error: Expected __Queue__ but received '+str(type(queue))


def peek(queue):
    """
    Purpose
        returns the value from the front of given queue without removing it
    Pre-conditions:
        queue: a queue created by create()
    Post-condition:
        None
    Return:
        the value at the front of the queue
    """
    if type(queue) is tuple:
        t,q = queue
        assert t == '__Queue__', 'Type Error: Expected __Queue__ but received '+t
        return q[0]
    else:
        assert False, 'Type Error: Expected __Queue__ but received '+str(type(queue))