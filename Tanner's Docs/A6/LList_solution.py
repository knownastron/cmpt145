# CMPT 145: Node-Based Data Structures
# Defines the List ADT
#
# Here we re-invent Python's built-in lists.  We will provide a small subset of
# the operations that a Python list provides.
#
# Implementation:
#   This implementation uses the linked node structure.


import node as node


def create():
    """
    Purpose
        creates an empty list
    Return
        :return an empty list
    """
    llist = {}
    llist['size'] = 0     # how many elements in the stack
    llist['head'] = None  # start of the chain; initially empty
    llist['tail'] = None
    return llist


def is_empty(alist):
    """
    Purpose
        Checks if the given list has no data in it
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return True if the list has no data, or False otherwise
    """
    return size(alist) == 0


def size(alist):
    """
    Purpose
        Returns the number of data values in the given list
    Pre-conditions:
        :param alist: a list created by create()
    Return:
        :return The number of data values in the list
    """
    return alist['size']


def add_to_front(alist, val):
    """
    Purpose
        Insert val into alist at the front of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is at index 0.
        The values previously in the list appear after the new value.
    Return:
        :return None
    """
    anode = node.create(val, alist['head'])
    if is_empty(alist):
        alist['tail'] = anode
    alist['head'] = anode
    alist['size'] += 1


def add_to_back(alist, val):
    """
    Purpose
        Insert val into alist at the end of the node chain
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        The list increases in size.
        The new value is last in the list.
    Return:
        :return None
    """
    anode = node.create(val)
    if is_empty(alist):
        alist['head'] = anode
    else:
        node.set_next(alist['tail'], anode)
    alist['tail'] = anode
    alist['size'] += 1


def retrieve_data_at_index(alist, idx):
    """
    Purpose
        Return the value stored in alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer
    Post-conditions:
        none
    Return:
        :return (True, val) if val is stored at index idx and idx is valid
        :return (False, None) if the idx is not valid for the list
    """
    if idx < 0 or idx >= size(alist):
        return False, None
    anode = alist['head']
    i = 0
    while anode is not None and i < idx:
        anode = node.get_next(anode)
        i += 1
    return True, node.get_data(anode)


def set_data_at_index(alist, idx, val):
    """
    Purpose
        Store val into alist at the index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a non-negative integer
    Post-conditions:
        The value stored at index idx changes to val
    Return:
        :return True if the index was valid, False otherwise
    """
    if idx < 0 or idx >= size(alist):
        return False
    anode = alist['head']
    i = 0
    while anode is not None and i < idx:
        anode = node.get_next(anode)
        i += 1
    node.set_data(anode, val)
    return True


def remove_from_front(alist):
    """
    Purpose
        Removes and returns the first value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The pair (True, value) if alist is not empty
        :return The pair (False, None) if alist is empty
    """
    if is_empty(alist):
        return False, None
    if size(alist) == 1:
        alist['tail'] = None
    anode = alist['head']
    alist['head'] = node.get_next(anode)
    alist['size'] -= 1
    return True, node.get_data(anode)


def remove_from_back(alist):
    """
    Purpose
        Removes and returns the last value in alist
    Preconditions:
        :param alist: a list created by create()
    Post-conditions:
        The list decreases in size.
        The returned value is no longer in in the list.
    Return:
        :return The pair True, value if alist is not empty
        :return The pair False, None if alist is empty
    """
    if is_empty(alist):
        return False, None

    if size(alist) == 1:
        anode = alist['head']
        alist['head'] = None
        alist['tail'] = None
        alist['size'] = 0
        return True, node.get_data(anode)

    # general case
    aprev = alist['head']
    anode = node.get_next(aprev)
    while node.get_next(anode) is not None:
        aprev = anode
        anode = node.get_next(anode)

    alist['tail'] = aprev
    node.set_next(aprev, None)
    alist['size'] -= 1
    return True, node.get_data(anode)


def insert_value_at_index(alist, val, idx):
    """
    Purpose
        Insert val into alist at index idx
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
        :param idx:   a valid index for the list
    Post-conditions:
        The list increases in size.
        The new value is at index idx.
        The values previously in the list at idx or later appear after the new value.
    Return:
        :return If the index is valid, insert_value_at_index returns True.
        :return If the index is not valid, insert_value_at_index returns False.
    """
    if idx < 0 or idx > size(alist):
        return False

    if idx == 0:
        add_to_front(alist, val)
        return True

    if idx == size(alist):
        add_to_back(alist, val)
        return True

    # general case
    anode = alist['head']
    i = 1
    while anode is not None and i < idx:
        anode = node.get_next(anode)
        i += 1
    new_node = node.create(val, node.get_next(anode))
    node.set_next(anode, new_node)
    alist['size'] += 1
    return True


def value_is_in(alist, val):
    """
    Purpose
        Check if the given value is in the given list
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return True if the value is in the list, False otherwise
        :return (False if the list is empty)
    """
    anode = alist['head']
    while anode is not None:
        if node.get_data(anode) == val:
            return True
        anode = node.get_next(anode)
    return False


def get_index_of_value(alist, val):
    """
    Purpose
        Return the smallest index of the given val in the given alist.
    Preconditions:
        :param alist: a list created by create()
        :param val:   a value of any kind
    Post-conditions:
        none
    Return:
        :return True, idx if the val appears in alist
        :return False, None if the vale does not appear in alist
    """
    anode = alist['head']
    i = 0
    while anode is not None:
        if node.get_data(anode) == val:
            return True, i
        anode = node.get_next(anode)
        i += 1
    return False, None


def delete_item_at_index(alist, idx):
    """
    Purpose
        Delete the value at index idx in alist.
    Preconditions:
        :param alist: a list created by create()
        :param idx:   a non-negative integer
    Post-conditions:
        The list decreases in size if the index is valid
        The value at idx is no longer in the list.
    Return:
        :return True if index was valid, False otherwise
    """
    if idx < 0 or idx >= size(alist):
        return False

    if idx == 0:
        remove_from_front(alist)
        return True

    if idx == size(alist) - 1:
        remove_from_back(alist)
        return True

    # general case
    anode = alist['head']
    aprev = None
    i = 0
    while anode is not None and i < idx:
        aprev = anode
        anode = node.get_next(anode)
        i += 1
    node.set_next(aprev, node.get_next(anode))
    alist['size'] -= 1
    return True

