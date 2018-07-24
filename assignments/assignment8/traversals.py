# CMPT 145: Binary trees
# Defines simple traversals for treenode (primitive) trees.
#
# These traversals print the data values stored in a primitive tree.

import treenode as tn
import queue as Queue

def in_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        in_order(tn.get_left(tnode))
        print(tn.get_data(tnode), end=" ")
        in_order(tn.get_right(tnode))


def pre_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        print(tn.get_data(tnode), end=" ")
        pre_order(tn.get_left(tnode))
        pre_order(tn.get_right(tnode))


def post_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        post_order(tn.get_left(tnode))
        post_order(tn.get_right(tnode))
        print(tn.get_data(tnode), end=" ")



def breadth_first_order(tnode):
    """
    Display the nodes of a tree in breadth-first-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    nodes = Queue.create()
    Queue.enqueue(nodes, tnode)
    order = Queue.create()
    #
    while Queue.size(nodes) > 0:
        current = Queue.dequeue(nodes)
        if current is not None:
            Queue.enqueue(order, tn.get_data(current))
            Queue.enqueue(nodes, tn.get_left(current))
            Queue.enqueue(nodes, tn.get_right(current))

    while not Queue.is_empty(order):
        n = Queue.dequeue(order)
        print(n, end=" ")

