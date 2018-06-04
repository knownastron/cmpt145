# CMPT 145: Node-based Queues
# Defines the Node ADT
#
# A node is a simple container with two pieces of information
#   data: the contained information
#   next: a reference to another node
# We can create node-chains of any size.

# Implementation notes:
#   This implementation uses a Python dictionary as a record.


def create(data, next=None):
    """
    Create a new node for the given data.
    Pre-conditions:
        data:  Any data value to be stored in the node
        next:  Another node (or None, by default)
    Post-condition:
        none
    Return:
        the node created
    """
    return {'data':data, 'next':next}


def get_data(node):
    """
    Retrieve the contents of the data field.
    Pre-conditions:
        node: a node created by create()
    Post-conditions:
        none
    Return
        the data value stored previously in the node
    """
    return node['data']


def get_next(node):
    """
    Retrieve the contents of the next field.
    Pre-conditions:
        node: a node created by create()
    Post-conditions:
        none
    Return
        the value stored previously in the next field
    """
    return node['next']


def set_data(node, val):
    """
    Set the contents of the data field to val.
    Pre-conditions:
        node: a node created by create()
        val:  a data value to be stored
    Post-conditions:
        stores the new data value, replacing the existing value
    Return
        none
    """
    node['data'] = val

def set_next(node, val):
    """
    Set the contents of the next field to val.
    Pre-conditions:
        node: a node created by create()
        val:  a node, or the value None
    Post-conditions:
        stores the new next value, replacing the existing value
    Return
        none
    """
    node['next'] = val

