# CMPT 145: Linear ADTs
# Defines the Queue ADT
#
# A queue (also called a FIFO queue) is a compound data structure
# in which the data values are ordered according to the FIFO
# (first-in first-out) protocol.
#
# Implementation notes:
# This implementation uses two stacks.


import TStack as Stack


def create():
    """
    Purpose
        creates an empty queue
    Return
        an empty queue
    """
    q2 = {}
    q2['e-stack'] = Stack.create()
    q2['d-stack'] = Stack.create()
    return q2


def is_empty(queue):
    """
    Purpose
        checks if the given queue has no data in it
    Pre-conditions:
        queue is a queue created by create()
    Return:
        True if the queue has no data, or false otherwise
    """

    return Stack.is_empty(queue['e-stack']) and Stack.is_empty(queue['d-stack'])


def size(queue):
    """
    Purpose
        returns the number of data values in the given queue
    Pre-conditions:
        queue: a queue created by create()
    Return:
        The number of data values in the queue
    """

    return Stack.size(queue['e-stack']) + Stack.size(queue['d-stack'])


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

    if Stack.is_empty(queue['d-stack']):
        Stack.push(queue['e-stack'], value)
    else:
        for i in range(Stack.size(queue['d-stack'])):
            cur_item = Stack.pop(queue['d-stack'])
            Stack.push(queue['e-stack'], cur_item)
        Stack.push(queue['e-stack'], value)

def dequeue(queue):
    """
    Purpose
        removes and returns a data value from the given queue
    Pre-conditions:
        queue: a queue created by create()
    Post-condition:
        the first value is r emoved from the queue
    Return:
        the first value in the queue
        """

    if Stack.is_empty(queue['e-stack']):
        return Stack.pop(queue['d-stack'])
    else:
        for i in range(Stack.size(queue['e-stack'])):
            cur_item = Stack.pop(queue['e-stack'])
            Stack.push(queue['d-stack'], cur_item)
        return Stack.pop(queue['d-stack'])



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

    if Stack.is_empty(queue['e-stack']):
        t, s = queue['d-stack']
        return s[-1]
    else:
        t, s = queue['e-stack']
        return s[0]
