#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

# CMPT 145: Assignment 5 Question 2

import node as node



def count_chain(node_chain):
    """
    Purpose:
        Counts the number of nodes in the node chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Return:
        :return: The number of nodes in the node chain.
    """

    count = 0
    cur_node = node_chain

    while cur_node is not None:
        count += 1
        cur_node = node.get_next(cur_node)

    return count


def delete_front_nodes(node_chain, n):
    """
    Purpose:
        Deletes the first n nodes from the front of the node chain.
    Pre-Conditions:
        :param node_chain: a node-chain, possibly empty
        :param n: integer, how many nodes that should be removed off the front of the node chain
    Post-conditions:
        The node-chain is changed, by removing the first n nodes. If n>length of node_chain, node_chain is set to be empty (None)
    Return:
        :return: The resulting node chain, which may now be empty (None)
    """
    cur_node = node_chain
    count = 0

    while True:
        count += 1
        if cur_node == None:
            node_chain = None
            break
        elif count == n:
            node_chain = node.get_next(cur_node)
        cur_node = node.get_next(cur_node)

    return node_chain



def replace_last(node_chain, target_val, replacement_val):
    """
    Purpose:
        Replaces the last occurrence of target data value with the new_value. The chain should at most have 1 data value changed.
    Pre-conditions:
        :param node_chain: a node chain, possibly None
        :param target_val: the target data value we are searching to replace the last instance of
        :param replacement_val: the data value to replace the target_val that we found
    Post-conditions:
        The node-chain is changed, by replacing the last occurrence of target_val. If target_val is not present, then the node_chain returns unaltered.
    Return:
        :return: The altered node chain where any data occurrences of target_val has been replaced with replacement_val.
    """

    cur_node = node_chain
    target_node = None

    while cur_node != None:
        cur_value = node.get_data(cur_node)
        if cur_value == target_val:
            target_node = cur_node
        cur_node = node.get_next(cur_node)

    #if there is a target node, change its data value
    if target_node != None:
        node.set_data(target_node, replacement_val)

    return node_chain
