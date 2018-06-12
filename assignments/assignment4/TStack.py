# CMPT 145: Linear ADTs
# Defines the Stack ADT
#
# A stack (also called a pushdown or LIFO stack) is a compound 
# data structure in which the data values are ordered according 
# to the LIFO (last-in first-out) protocol.
#
# Implementation:
# This implementation was designed to point out when ADT operations are
# used incorrectly.


def create():
    """
    Purpose
        creates an empty stack
    Return
        an empty stack
    """
    return '__Stack__',list()


def is_empty(stack):
    """
    Purpose
        checks if the given stack has no data in it
    Pre-conditions:
        stack is a stack created by create()
    Return:
        True if the stack has no data, or false otherwise
    """
    if type(stack) is tuple:
        t,s = stack
        assert t == '__Stack__', 'Type Error : Expected __Stack__ but received '+t
        return len(s) == 0
    else:
        assert False, 'Type Error: Expected __Stack__ but received '+str(type(stack))



def size(stack):
    """
    Purpose
        returns the number of data values in the given stack
    Pre-conditions:
        stack: a stack created by create()
    Return:
        The number of data values in the queue
    """
    if type(stack) is tuple:
        t,s = stack
        assert t == '__Stack__', 'Type Error: Expected __Stack__ but received '+t
        return len(s)
    else:
        assert False, 'Type Error: Expected __Stack__ but received '+str(type(stack))


def push(stack, value):
    """
    Purpose
        adds the given data value to the given stack
    Pre-conditions:
        queue: a stack created by create()
        value: data to be added
    Post-condition:
        the value is added to the stack
    Return:
        (none)
    """
    if type(stack) is tuple:
        t,s = stack
        assert t == '__Stack__', 'Type Error: Expected __Stack__ but received '+t
        s.append(value)
    else:
        assert False, 'Type Error: Expected __Stack__ but received '+str(type(stack))


def pop(stack):
    """
    Purpose
        removes and returns a data value from the given stack
    Pre-conditions:
        stack: a stack created by create()
    Post-condition:
        the top value is removed from the stack
    Return:
        returns the value at the top of the stack
    """
    if type(stack) is tuple:
        t,s = stack
        assert t == '__Stack__', 'Type Error: Expected __Stack__ but received '+t
        return s.pop()
    else:
        assert False, 'Type Error: Expected __Stack__ but received '+str(type(stack))

def peek(stack):
    """
    Purpose
        returns the value from the front of given stack without removing it
    Pre-conditions:
        stack: a stack created by create()
    Post-condition:
        None
    Return:
        the value at the front of the stack
    """
    if type(stack) is tuple:
        t,s = stack
        assert t == '__Stack__', 'Type Error: Expected __Stack__ but received '+t
        return s[-1]
    else:
        assert False, 'Type Error: Expected __Stack__ but received '+str(type(stack))
