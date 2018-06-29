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
        cur_val = node.get_data(cur_node)
        #check if cur_val is in the word_list
        if cur_val in word_list:
            return True
        #add the cur_val to word_list
        word_list.append(cur_val)
        cur_node = node.get_next(cur_node)

    return False




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

    #if node_chain is empty, immediately return the node_chain
    if a5q2.count_chain(node_chain) > 0:
        cur_node = node_chain
        prev_node = None
        next_node = node.get_next(node_chain)

        while True:
            node.set_next(cur_node, prev_node)
            prev_node = cur_node
            cur_node = next_node

            #If next is None break, otherwise, move next to next node
            if next_node is None:
                break
            else:
                next_node = node.get_next(next_node)

        node_chain = prev_node

    return node_chain






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

    #if the node chain is empty, add the new node
    if a5q2.count_chain(node_chain) < 1:
        node_chain = node.create(number_value, None)
    else:
        cur_node = node_chain
        prev_node = None
        next_node = node.get_next(node_chain)

        while True:
            cur_val = node.get_data(cur_node)

            #check if the value should be placed in front of current node
            if cur_val == number_value + 1:
                if prev_node == None:
                    node_chain = node.create(number_value, cur_node)
                else:
                    new_node = node.create(number_value, cur_node)
                    node.set_next(prev_node, new_node)
                break

            #check if the value should be placed behind the current node
            if cur_val == number_value - 1:
                if next_node == None:
                    new_node = node.create(number_value, None)
                    node.set_next(cur_node, new_node)
                else:
                    new_node = node.create(number_value, next_node)
                    node.set_next(cur_node, new_node)
                break

            #break if at the end of the node chain
            if next_node == None:
                break
            #move to next node if not at the end
            else:
                prev_node = cur_node
                cur_node = next_node
                next_node = node.get_next(next_node)

    return node_chain
