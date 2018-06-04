# CMPT 145: Node-Based Data Structures
# Implements the Stack ADT
#
# A stack (also called a pushdown or LIFO stack) is a compound 
# data structure in which the data values are ordered according 
# to the LIFO (last-in first-out) protocol.
#
# Implementation:
# This implementation uses the linked node structure.


import node as node

def create():
    """
    Purpose
        creates an empty stack
    Return
        an empty stack
    """
    stack = {}
    stack['size'] = 0        # how many elements in the stack
    stack['top'] = None      # the node chain starts here
    return stack


def size(stack):
    """
    Purpose
        returns the number of data values in the given queue
    Pre-conditions:
        queue: a queue created by create()
    Return:
        The number of data values in the queue
    """
    return stack['size']


def is_empty(stack):
    """
    Purpose
        checks if the given queue has no data in it
    Pre-conditions:
        queue is a queue created by create()
    Return:
        True if the queue has no data, or false otherwise
    """
    return stack['size'] == 0


def push(stack, value):
    """
    Purpose
        adds the given data value to the given stack
    Pre-conditions:
        stack: a stack created by create()
        value: data to be added
    Post-condition:
        the value is added to the stack
    Return:
        (none)
    """
    new_node = node.create(value, stack['top'])
    stack['top'] = new_node
    stack['size'] += 1




def pop(stack):
    """
    Purpose
        removes and returns a data value from the given stack
    Pre-conditions:
        stack: a stack created by create()
    Post-condition:
        the first value is removed from the stack
    Return:
        the first value in the stack, or None
    """
    assert not is_empty(stack), 'popped an empty stack'

    prev_first_node = stack['top']
    result = node.get_data(prev_first_node)
    stack['top'] = node.get_next(prev_first_node)
    stack['size'] -= 1
    return result


def peek(stack):
    """
    Purpose
        returns the value from the front of given stack
        without removing it
    Pre-conditions:
        stack: a stack created by create()
    Post-condition:
        None
    Return:
        the value at the front of the stack
    """
    assert not is_empty(stack), 'peeked into an empty stack'

    first_node = stack['top']
    result = node.get_data(first_node)
    return result