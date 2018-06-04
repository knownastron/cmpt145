# CMPT 145: Abstract Data Types
# Defines the Registry ADT

#  A registry records a Boolean value for a range of integers.
#  It can be used to record observations or events.

# Implementation:
#  - a simple list of Boolean values
#  - set() and reset() are standard names for Boolean operations.


def create(size, value):
    """
    Purpose:
        Create a registry of a give size filled with the given value
    Pre-conditions:
        size: number of elements in the registry
        value: the default initial value for all elements
    Post-conditions:
        (none)
    Return:
        the newly created registry
    """
    return [value for i in range(size)]


def set(reg, i):
    """
    Purpose:
        Set the registry element at i to True
    Pre-conditions:
        reg: the registry
        i: an index, in the correct range for reg
    Post-conditions:
        the registry value at i is set to True
    Return:
        (none)
    """
    reg[i] = True

def reset(reg,i):
    """
    Purpose:
        Set the registry element at i to False
    Pre-conditions:
        reg: the registry
        i: an index, in the correct range for reg
    Post-conditions:
        the registry value at i is set to False
    Return:
        (none)
    """
    reg[i] = False

def is_registered(reg, i):
    """
    Purpose:
        Returns the value stored at registry element i
    Pre-conditions:
        reg: the registry
        i: an index, in the correct range for reg
    Post-conditions:
        (none)
    Return:
        the value stored at element i
    """
    return reg[i]
