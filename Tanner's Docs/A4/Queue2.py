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
    return {'enqueue': Stack.create(), 'dequeue': Stack.create()}


def is_empty(queue):
    """
    Purpose
        checks if the given queue has no data in it
    Pre-conditions:
        queue is a queue created by create()
    Return:
        True if the queue has no data, or false otherwise
    """
    return size(queue) == 0


def size(queue):
    """
    Purpose
        returns the number of data values in the given queue
    Pre-conditions:
        queue: a queue created by create()
    Return:
        The number of data values in the queue
    """
    return Stack.size(queue['enqueue']) + Stack.size(queue['dequeue'])


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
    for i in range(Stack.size(queue['dequeue'])):
        v = Stack.pop(queue['dequeue'])
        Stack.push(queue['enqueue'], v)
    Stack.push(queue['enqueue'], value)



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
    if size(queue) == 0:
        return None
    for i in range(Stack.size(queue['enqueue'])):
        v = Stack.pop(queue['enqueue'])
        Stack.push(queue['dequeue'], v)
    return Stack.pop(queue['dequeue'])


def peek(queue):
    """
    Purpose
        returns the first data value from the given queue
        without removing it
    Pre-conditions:
        queue: a queue created by create()
    Post-condition:
        None
    Return:
        the first value in the queue
    """
    if size(queue) == 0:
        return None
    for i in range(Stack.size(queue['enqueue'])):
        v = Stack.pop(queue['enqueue'])
        Stack.push(queue['dequeue'], v)
    return Stack.peek(queue['dequeue'])