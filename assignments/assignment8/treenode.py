# CMPT 145: Binary trees
# Defines the tree node ADT
#
# A treenode is a simple container with three pieces of information
#   data: the contained information
#   left:  a reference to another treenode or None
#   right: a reference to another treenode or None


# Implementation notes:
#   This implementation uses a Python dictionary as a record.


def create(data, left=None, right=None):
    """
    Create a new treenode for the given data.
    Pre-conditions:
        data:  Any data value to be stored in the treenode
        left:  Another treenode (or None, by default)
    Post-condition:
        none
    Return:
        the treenode created
    """
    return {'data':data, 'left':left, 'right':right}


def get_data(treenode):
    """
    Retrieve the contents of the data field.
    Pre-conditions:
        node: a node created by create()
    Post-conditions:
        none
    Return
        the data value stored previously in the node
    """
    return treenode['data']


def get_left(tnode):
    """
    Retrieve the contents of the left field.
    Pre-conditions:
        tnode: a treenode created by create()
    Post-conditions:
        none
    Return
        the value stored in left field
    """
    return tnode['left']


def get_right(tnode):
    """
    Retrieve the contents of the right field.
    Pre-conditions:
        tnode: a treenode created by create()
    Post-conditions:
        none
    Return
        the value stored in right field
    """
    return tnode['right']


def set_data(tnode, val):
    """
    Set the contents of the data field to val.
    Pre-conditions:
        tnode: a node created by create()
        val:  a data value to be stored
    Post-conditions:
        stores the new data value, replacing the existing value
    Return
        none
    """
    tnode['data'] = val


def set_left(tnode, val):
    """
    Set the contents of left field to val.
    Pre-conditions:
        tnode: a treenode created by create()
        val:   a treenode, or the value None
    Post-conditions:
        stores the val in left field, replacing the existing value
    Return
        none
    """
    tnode['left'] = val

def set_right(tnode, val):
    """
    Set the contents of right field to val.
    Pre-conditions:
        tnode: a treenode created by create()
        val:   a treenode, or the value None
    Post-conditions:
        stores the val in right field, replacing the existing value
    Return
        none
    """
    tnode['right'] = val

