#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

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
    return None


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
    return None

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

    cur_idx = 0
    cur_node = alist['head']

    while cur_node is not None:
        if node.get_data(cur_node) == val:
            return True, cur_idx
        cur_node = node.get_next(cur_node)
        cur_idx += 1

    return False, None


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

    #check if target index is within scope of alist
    if alist['size'] - idx < 1:
        return False, None
    else:
        cur_idx = 0
        cur_node = alist['head']

        while cur_node is not None:
            if cur_idx == idx:
                return True, node.get_data(cur_node)
            else:
                cur_idx += 1
                cur_node = node.get_next(cur_node)



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

    cur_node = alist['head']
    cur_idx = 0

    #check if target index is within scope of alist
    if alist['size'] - idx < 1:
        return False
    else:
        while cur_node is not None:
            if cur_idx == idx:
                node.set_data(cur_node, val)
                return True
            else:
                cur_idx += 1
                cur_node = node.get_next(cur_node)


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

    #check if linked list is already EMPTY
    if is_empty(alist):
        return False, None

    #check if linked list is a singleton
    elif size(alist) == 1:
        node_to_remove = alist['head']
        removed_data = node.get_data(node_to_remove) #data to be removed and returned
        alist['head'] = None
        alist['tail'] = None
        alist['size'] = 0
        return True, removed_data

    else:
        node_to_remove = alist['head']
        removed_data = node.get_data(node_to_remove) #data to be removed and returned
        new_head = node.get_next(node_to_remove)
        alist['head'] = new_head
        alist['size'] -= 1

        return True, removed_data


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
    #check if linked list is already EMPTY
    if is_empty(alist):
        return False, None

    #check if linked list is a singleton
    elif size(alist) == 1:
        node_to_remove = alist['head']
        removed_data = node.get_data(node_to_remove) #data to be removed and returned
        alist['head'] = None
        alist['tail'] = None
        alist['size'] = 0
        return True, removed_data

    else:
        prev_node = alist['head']
        next_node = node.get_next(prev_node)

        while next_node is not None:
            #if next_node is the same as tail, then previous node (prev_node) becomes the new tail
            if next_node == alist['tail']:
                removed_data = node.get_data(next_node) #data to be removed and returned
                node.set_next(prev_node, None)
                alist['tail'] = prev_node
                alist['size'] -= 1
                return True, removed_data
            else:
                prev_node = next_node
                next_node = node.get_next(next_node)



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

    #check if idx beyond alist['size'] + 1 or idx is negative, return False
    if alist['size'] - idx < 0 or idx < 0:
        return False

    #if index is the first index or is empty, add new val at the front
    if idx == 0 or is_empty(alist):
        add_to_front(alist, val)
        return True

    #if index is immediately after the last index of alist, add new val to back
    elif idx == alist['size']:
        add_to_back(alist, val)
        return True

    #general case
    else:
        cur_node = alist['head']
        next_node = node.get_next(cur_node)
        next_idx = 1 #index of next_node

        while next_node is not None:
            if next_idx == idx:
                new_node = node.create(val, next_node)
                node.set_next(cur_node, new_node)
                alist['size'] += 1
                return True
            else:
                cur_node = next_node
                next_node = node.get_next(next_node)
                next_idx += 1


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

    #check if idx is within scope of alist or check if alist is empty
    if alist['size'] - idx < 1 or is_empty(alist):
        return False

    #check if list is a singleton
    elif alist['size'] == 1:
        remove_from_front(alist)
        return True

    #check if idx is the first index
    elif idx == 0:
        remove_from_front(alist)
        return True

    #check if idx is the last index
    elif alist['size'] - idx == 1:
        remove_from_back(alist)
        return True

    #general case
    else:
        cur_node = alist['head']
        next_node = node.get_next(cur_node)
        next_idx = 1

        while next_node is not None:
            if next_idx == idx:
                after_next = node.get_next(next_node)
                node.set_next(cur_node, after_next)
                alist['size'] -= 1
                return True
            else:
                cur_node = next_node
                next_node = node.get_next(next_node)
                next_idx += 1

###############################################################################
#No credit functions
###############################################################################

def clear(alist):
    alist['head'] = None
    alist['tail'] = None
    alist['size'] = 0

def extend(alist, blist):
    atail = alist['tail']
    node.set_next(atail, blist['head'])
    alist['tail'] = blist['tail']
    alist['size'] += blist['size']

    return alist

def slice(alist, start, end, step):

    cur_idx = 0
    target_idx = start
    cur_node = alist['head']
    data_list = []

    while cur_idx < end:
        if cur_idx == target_idx:
            data_list.append(node.get_data(cur_node))
            target_idx += step
        cur_node = node.get_next(cur_node)
        cur_idx += 1

    new_llist = create()
    while len(data_list) > 0:
        add_to_back(new_llist, data_list.pop(0))

    return new_llist

def sorted(alist):

    if is_empty(alist) or size(alist) == 1:
        return alist

    prev_node = None
    cur_node = alist['head']
    next_node = node.get_next(cur_node)
    n = size(alist)
    i = 0
    count = 1

    while i != n-1 or next_node is not None:

        cur_value = node.get_data(cur_node)
        next_value = node.get_data(next_node)

        if next_value is None:
            break

        elif cur_value > next_value:
            if prev_node is None:
                node.set_next(cur_node, node.get_next(next_node))
                node.set_next(next_node, cur_node)
                alist['head'] = next_node
                i = 0

                #if last node changed, change 'tail'
                if node.get_next(cur_node) is None:
                    alist['tail'] = cur_node

            else:
                node.set_next(prev_node, next_node)
                node.set_next(cur_node, node.get_next(next_node))
                node.set_next(next_node, cur_node)
                i = 0

                #if last node changed, change 'tail'
                if node.get_next(cur_node) is None:
                    alist['tail'] = cur_node

            #reset node to beginning of list
            prev_node = None
            cur_node = alist['head']
            next_node = node.get_next(cur_node)

        #move to next node if cur is not greater than next
        else:
            prev_node = cur_node
            cur_node = next_node
            next_node = node.get_next(next_node)
            i += 1

    return alist
