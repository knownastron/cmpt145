# CMPT 145: Assignment 5 Question 3

import node as node
import a5q2 as a5q2


def split_chain(node_chain):
    """
    Purpose:
        Splits the given node chain in half, returning the second half.
        If the given chain has an odd length, the extra node is part of
        the second half of the chain.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Post-conditions:
        the original node chain is cut in half!
    Return:
        :return: A tuple (nc1, nc2) where nc1 and nc2 are node-chains
         each containing about half of the nodes in node-chain
    """
    # calculate size
    n = a5q2.count_chain(node_chain)

    # special case: empty chain
    if n == 0:
        return None, None
    # special case: chain with one node
    if n == 1:
        return None, node_chain

    # calculate halfway
    mid = n // 2

    # walk along the chain until half-way
    walker = node_chain
    prev = None
    counter = 0
    while counter < mid:
        prev = walker
        walker = node.get_next(walker)
        counter += 1

    # terminate the first half with a well-placed None
    node.set_next(prev, None)

    # return the two new chains
    return node_chain, walker




def remove_chain(node_chain, val):
    """
    Purpose:
        Remove the first occurrence of val from node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
        :param val: a value to be removed
    Post-conditions:
        The first occurrence of the value is removed from the chain.
        If val does not appear, the node-chain is unmodified.
    Return:
        :return: The resulting node chain with val removed
    """
    # special case: empty node chain
    if node_chain is None:
        return None

    # special case: node to be removed is first
    if node.get_data(node_chain) == val:
        return node.get_next(node_chain)

    # walk along the chain
    walker = node.get_next(node_chain)
    prev = node_chain
    while walker is not None and node.get_data(walker) != val:
        prev = walker
        walker = node.get_next(walker)

    # found first occurrence of val?
    if walker is not None:
        node.set_next(prev, node.get_next(walker))

    return node_chain





def insert_at(node_chain, value, index):
    """
    Purpose:
        Insert the given value into the node-chain so that
        it appears at the the given index.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
        :param value: a value to be inserted
        :param index: the index where the new value should appear
        Assumption:  0 <= index <= n
                     where n is the number of nodes in the chain
    Post-condition:
        The node-chain is modified to include a new node at the
        given index with the given value as data.
    Return
        :return: the node-chain with the new value in it
    """

    # special case: insert at index 0
    if index == 0:
        return node.create(value, node_chain)

    # walk along the chain until the indicated index
    walker = node_chain
    counter = 0
    prev = None
    while walker is not None and counter < index:
        prev = walker
        walker = node.get_next(walker)
        counter += 1

    # If there is a node at the index
    if counter == index:
        # insert a new node
        node.set_next(prev, node.create(value, walker))
    else:
        # insert at the very end
        node.set_next(prev, node.create(value, None))

    return node_chain

