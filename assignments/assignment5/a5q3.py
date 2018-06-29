# CMPT 145: Assignment 5 Question 3

import node as node
import a5q2 as a5q2


def contains_duplicates(node_chain):
    """
    Purpose:
        Returns whether or not the given node_chain contains one or more duplicate data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
    Return:
        :return: True if duplicate data value(s) were found, False otherwise
    """

    cur_node = node_chain
    word_list = []

    while cur_node is not None:
        cur_word = node.get_data(cur_node)
        if cur_word in word_list:
            return False
        word_list.append(cur_word)

    return True




def reverse_chain(node_chain):
    """
    Purpose:
        Completely reverses the order of the given node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Post-conditions:
        The front of the node_chain is altered to be the back, with all nodes now pointing next the opposite direction.
    Return:
        :return: The resulting node chain that has had its order reversed
    """
    return None





def insert_value_sorted(node_chain, number_value):
    """
    Purpose:
        Insert the given number_value into the node-chain so that it appears after a previous value that is <= value. If the node_chain was empty, new value is simply placed at the front.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing only numbers
        :param number_value: a numerical value to be inserted
        Assumption:  node_chain only contains numbers (which can be compared to the given number_value)
    Post-condition:
        The node-chain is modified to include a new node with number_value as its data after a previous node's data value is <= number_value.
    Return
        :return: the node-chain with the new value in it
    """
    return None
