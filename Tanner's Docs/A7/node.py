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
        :param: data:  Any data value to be stored in the node
        :param: next:  A reference to another node (or None, by default)
    Post-condition:
        none
    Return:
        the node created
    """
    return {'data':data, 'next':next}


def get_data(node):
    """
    Retrieve the data value stored in the node.
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
    Retrieve the node reference stored in the node.
    Pre-conditions:
        node: a node created by create()
    Post-conditions:
        none
    Return
        the reference value stored previously in the node
    """
    return node['next']


def set_data(node, val):
    """
    Set the data value stored in the node to val.
    Pre-conditions:
        node: a node created by create()
        val:  a data value to be stored
    Post-conditions:
        replaces the existing data value, and stores the new value
    Return
        none
    """
    node['data'] = val

def set_next(node, val):
    """
    Set the reference value stored in the node to val.
    Pre-conditions:
        node: a node created by create()
        val:  a reference to another node, to be stored
    Post-conditions:
        replaces the existing reference value, and stores the new value
    Return
        none
    """
    node['next'] = val

