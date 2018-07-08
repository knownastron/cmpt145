# CMPT 145: Node-Based Data Structures
# Defines the Linked List ADT
#
# Here we re-invent Python's built-in lists.  We will provide a subset of
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
    llist['head'] = None  # the node chain starts here; initially empty
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

    if alist['size'] == 0:
        return True
    else:
        return False


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


    if size(alist) == 0:
        new_node = node.create(val, None)
        alist['head'] = new_node
        alist['tail'] = new_node
        alist['size'] += 1
    else:
        new_node = node.create(val, alist['head'])
        alist['head'] = new_node
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


    if size(alist) == 0:
        new_node = node.create(val, None)
        alist['head'] = new_node
        alist['tail'] = new_node
        alist['size'] += 1
    else:
        cur_last_node = alist['tail']
        new_node = node.create(val, None)
        node.set_next(cur_last_node, new_node)
        alist['tail'] = new_node
        alist['size'] += 1


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
    """

    cur_node = alist['head']

    while cur_node is not None:
        if node.get_data(cur_node) == val:
            return True
        cur_node = node.get_next(cur_node)

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
        :return the tuple (True, idx) if the val appears in alist
        :return the tuple (False, None) if the vale does not appear in alist
    """

    cur_index = 0
    cur_node = alist['head']

    while cur_node is not None:
        if node.get_data(cur_node) == val:
            return True, cur_index
        cur_node = node.get_next(cur_node)
        cur_index += 1

    return False, None


# TODO: complete  retrieve_data_at_index(alist, idx)   --- when done, delete this line
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

    if alist['size'] - idx < 1:
        return False, None
    else:
        count = 0
        cur_node = alist['head']

        while cur_node is not None:
            if count == idx:
                return True, node.get_data(cur_node)
            else:
                count += 1
                cur_node = node.get_next(cur_node)



# TODO: complete set_data_at_index(alist, idx, val)   --- when done, delete this line
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
    return False


# TODO: complete remove_from_front(alist)   --- when done, delete this line
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
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """
    return False, None

# TODO: complete remove_from_back(alist)   --- when done, delete this line
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
        :return The tuple (True, value) if alist is not empty
        :return The tuple (False, None) if alist is empty
    """
    return False, None


# TODO: complete insert_value_at_index(alist, val, idx)   --- when done, delete this line
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
    return False

# TODO: complete delete_item_at_index(alist, idx)   --- when done, delete this line
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
    return False
